__author__ = 'bromix'

import unittest
from resources.lib import nowtv


class TestClient(unittest.TestCase):
    def test_get_formats(self):
        channel_config = nowtv.Client.CHANNELS['rtl']
        client = nowtv.Client()
        formats = client.get_formats(channel_config)
        pass

    def test_get_format_tabs(self):
        channel_config = nowtv.Client.CHANNELS['rtl']
        client = nowtv.Client()
        format_tabs = client.get_format_tabs(channel_config, 'alarm-fuer-cobra-11')
        pass

    def test_get_videos(self):
        channel_config = nowtv.Client.CHANNELS['rtl']
        client = nowtv.Client()
        formats = client.get_videos(channel_config, 'betrugsfaelle')
        pass

    def test_get_video_streams(self):
        channel_config = nowtv.Client.CHANNELS['rtl']
        client = nowtv.Client()
        formats = client.get_video_streams(channel_config, 'rtl-aktuell/thema-ua-bahnstreik-beendet')
        pass

    pass