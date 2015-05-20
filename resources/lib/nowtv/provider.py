__author__ = 'bromix'

from resources.lib.kodion.utils import FunctionCache
from resources.lib import kodion
from resources.lib.kodion.items import DirectoryItem, VideoItem, UriItem
from resources.lib.kodion.utils import datetime_parser
from .client import Client, UnsupportedStreamException


class Provider(kodion.AbstractProvider):
    def __init__(self):
        kodion.AbstractProvider.__init__(self)
        self._client = None

        self._local_map.update({'now.library': 30500,
                                'now.newest': 30501,
                                'now.tips': 30502,
                                'now.top10': 30503,
                                'now.add_to_favs': 30101,
                                'now.watch_later': 30107,
                                'now.exception.drm_not_supported': 30504})
        pass

    def get_wizard_supported_views(self):
        return ['default', 'episodes', 'tvshows']

    def get_client(self, context):
        if not self._client:
            amount = context.get_settings().get_items_per_page()
            self._client = Client(Client.CONFIG_RTL_NOW, amount=amount)
            pass

        return self._client

    @kodion.RegisterProviderPath('^/play/$')
    def _on_play(self, context, re_match):
        video_id = context.get_param('video_id', '')
        if video_id:
            try:
                streams = self.get_client(context).get_film_streams(video_id)
            except UnsupportedStreamException, ex:
                context.get_ui().show_notification(context.localize(self._local_map['now.exception.drm_not_supported']))
                return False

            uri_item = UriItem(streams[0])
            return uri_item

        return False

    def on_root(self, context, re_match):
        result = []

        # favorites
        if len(context.get_favorite_list().list()) > 0:
            fav_item = kodion.items.FavoritesItem(context, fanart=self.get_fanart(context))
            result.append(fav_item)
            pass

        # watch later
        if len(context.get_watch_later_list().list()) > 0:
            watch_later_item = kodion.items.WatchLaterItem(context, fanart=self.get_fanart(context))
            result.append(watch_later_item)
            pass

        # list channels
        for channel_config in Client.CHANNELS:
            channel_id = channel_config['id']
            channel_title = channel_config['title']
            channel_item = DirectoryItem(channel_title, '')
            channel_item.set_fanart(context.create_resource_path('media', channel_id, 'background.jpg'))
            result.append(channel_item)
            pass

        return result

    def get_alternative_fanart(self, context):
        return self.get_fanart(context)

    def get_fanart(self, context):
        return context.create_resource_path('media', 'fanart.jpg')

    pass