import re
from App.error import RequestParamRequiredError, RequestParamError, RequestParamLengthError, RequestParamRegexError, \
    RequestParamIncludeError


class ParamCheck:
    def __init__(self, dict_data):
        self.data = dict_data
        self.msg = '处理成功'
        self.code = 0
        self.result = True

    def check(self, name, zh_name='', required=True, param_type=None, min_length=None, max_length=None, include=None, included_in=None,
              equal=None, regex=None):
        # 获取参数值
        if name not in self.data:
            param = None
        else:
            param = self.data[name]

        # 校验是否为空
        if required:
            if not (name in self.data and self.data[name]):
                self.msg = (zh_name or name) + '不可为空'
                self.code = 40000
                self.result = False
                raise RequestParamRequiredError

        # 校验类型
        if param_type is not None:
            if type(param) is not param_type:
                self.msg = (zh_name or name) + '参数类型错误'
                self.code = 40000
                self.result = False
                raise RequestParamRequiredError

        # 校验最小长度
        if min_length is not None:
            if len(param or '') < min_length:
                self.msg = (zh_name or name) + '字符长度错误，应大于或等于{}位'.format(min_length)
                self.code = 40000
                self.result = False
                raise RequestParamLengthError

        # 校验最大长度
        if max_length is not None:
            if len(param or '') > max_length:
                self.msg = (zh_name or name) + '字符长度错误，应小于或等于{}位'.format(max_length)
                self.code = 40000
                self.result = False
                raise RequestParamLengthError

        # 校验包含
        if include is not None:
            if include not in (param or ''):
                self.msg = (zh_name or name) + '未包含' + include
                self.code = 40000
                self.result = False
                raise RequestParamIncludeError

        # 校验包含于
        if included_in is not None:
            if (param or '') not in included_in:
                self.msg = (zh_name or name) + '未包含于' + str(include)
                self.code = 40000
                self.result = False
                raise RequestParamIncludeError

        # 校验等于
        if equal is not None:
            if str(param or '0') != equal:
                self.msg = (zh_name or name) + '不等于' + str(param)
                self.code = 40000
                self.result = False
                raise RequestParamIncludeError

        # 校验正则
        if regex:
            if not re.match(regex, (param or '')):
                self.msg = (zh_name or name) + '正则匹配错误'
                self.code = 40000
                self.result = False
                raise RequestParamRegexError

        return param.strip()


if __name__ == '__main__':

    data = {
        'username': 'test001',
        'email': '1669971502@qq.com',
        'nick_nam': ''
    }

    checker = ParamCheck(data)
    try:
        username = checker.check('username', '用户名', required=True, min_length=4, max_length=16, include='test',
                                 included_in=['test001', 'test002'])
        email = checker.check('email', '电子邮箱', required=True, regex=r'^\w+([-+.]\w+)*@\w+([-.]\w+)*\.\w+([-.]\w+)*$')
        nick_name = checker.check('nick_name', '昵称', required=False)
    except RequestParamError as e:
        pass
    finally:
        print('msg: ' + checker.msg)
        print('code: ' + str(checker.code))
        print('result: ' + str(checker.result))
