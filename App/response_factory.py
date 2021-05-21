from django.core.serializers.json import DjangoJSONEncoder
from django.http import JsonResponse


# 格式化json返回体
def response(code=0, msg='处理成功', result=True, data=None, **kw):
    d = {'code': code, 'msg': msg, 'result': result, 'data': data}
    for k, v in kw.items():
        d[k] = v
    return JR(d)


# json返回体不使用ensure_ascii
class JR(JsonResponse):
    def __init__(self, data, encoder=DjangoJSONEncoder, safe=True, json_dumps_params=None, **kwargs):
        if json_dumps_params is None:
            json_dumps_params = {'ensure_ascii': False}
        super().__init__(data, encoder, safe, json_dumps_params, **kwargs)


# json格式返回体模板
class Response:
    code = 0
    msg = '处理成功'
    result = True
    data = None

    def get_response(self, **kw):
        d = {'code': self.code, 'msg': self.msg, 'result': self.result, 'data': self.data}
        for k, v in kw.items():
            d[k] = v
        return JR(d)

    @classmethod
    def success(cls, code=0, msg='处理成功', result=True, data=None, **kw):
        cls.code = code
        cls.msg = msg
        cls.result = result
        cls.data = data
        return cls().get_response(**kw)


if __name__ == '__main__':
    a = Response.success(code=400, msg='失败', result=False, data={'a': [1, 2]}, a=1, b=2, c={'a': 1})
    print(a)