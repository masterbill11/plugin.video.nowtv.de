__author__ = 'bromix'

import unittest
from resources.lib import nowtv


class TestClient(unittest.TestCase):
    def test_get_formats(self):
        channel_config = nowtv.Client.CHANNELS[0]
        client = nowtv.Client()
        formats = client.get_formats(channel_config)
        pass

    pass