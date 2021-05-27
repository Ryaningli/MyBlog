import json
from django.utils.deprecation import MiddlewareMixin
from App.data_factory import DotDict


class RequestBytesToJson(MiddlewareMixin):
    @staticmethod
    def process_request(request):
        """
        将格式为bytes的json请求体（Content-Type: application/json）转换为可用点取值的json格式
        """
        try:
            if type(request.body) == bytes and request.META.get('CONTENT_TYPE') == 'application/json':
                request._body = DotDict(json.loads(request.body))
        except:
            pass
