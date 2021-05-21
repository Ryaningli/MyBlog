class RequestParamError(Exception):
    pass


class RequestParamRequiredError(RequestParamError):
    def __init__(self, name=''):
        self.name = name
        self.msg = self.name + '请求参数不可为空'
        self.status = 40000


class RequestParamTypeError(RequestParamError):
    def __init__(self, name=''):
        self.name = name
        self.msg = self.name + '请求参数类型错误'
        self.status = 40000


class RequestParamLengthError(RequestParamError):
    def __init__(self, name=''):
        self.name = name
        self.msg = self.name + '请求参数字符长度错误'
        self.status = 40000


class RequestParamIncludeError(RequestParamError):
    def __init__(self):
        self.msg = '请求参数未包含指定字符'
        self.status = 40000


class RequestParamEqualError(RequestParamError):
    def __init__(self):
        self.msg = '请求参数不等于指定字符'
        self.status = 40000


class RequestParamRegexError(RequestParamError):
    def __init__(self, name=''):
        self.name = name
        self.msg = self.name + '请求参数正则匹配错误'
        self.status = 40000


if __name__ == '__main__':
    try:
        raise RequestParamLengthError('用户名')
    except RequestParamLengthError as e:
        print(e.msg)
        print(e.status)
        raise e
