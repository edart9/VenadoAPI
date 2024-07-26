from rest_framework import renderers
from urllib.parse import urlencode

class FormURLEncodedRenderer(renderers.BaseRenderer):
    media_type = 'application/x-www-form-urlencoded'
    format = 'urlencoded'

    def render(self, data, accepted_media_type=None, renderer_context=None):
        return urlencode(data)