import json
from django.core.serializers.json import DjangoJSONEncoder
from django.http import JsonResponse


# 格式化json返回体
def response(code=0, msg='处理成功', result=True, data=None, **kw):
    d = {'code': code, 'msg': msg, 'result': result, 'data': data}
    for k, v in kw.items():
        d[k] = v
    return JR(d)


class DotDict(dict):
    """使用'点'访问字典属性"""

    # def __getattr__(self, name):
    #     try:
    #         return self[name]
    #     except:
    #         raise AttributeError('dict无"' + name + '"属性')
    __getattr__ = dict.get
    __setattr__ = dict.__setitem__
    __delattr__ = dict.__delitem__


# json返回体不使用ensure_ascii
class JR(JsonResponse):
    def __init__(self, data, encoder=DjangoJSONEncoder, safe=True, json_dumps_params=None, **kwargs):
        if json_dumps_params is None:
            json_dumps_params = {'ensure_ascii': False}
        super().__init__(data, encoder, safe, json_dumps_params, **kwargs)


if __name__ == '__main__':
    pass
