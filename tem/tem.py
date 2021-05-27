from schema import Schema, And, Use, Optional, Regex, SchemaError

data = {
    'username': 'tes',
    'password': '123456',
    'email': '1669971502@qq.com',
    'nick_name': '12121'
}


schema = {
    'username': And(And(str, error='用户名参数字符类型错误'), And(lambda x: 4 <= len(x) <= 16, error='用户名字符长度错误')),
    'password': And(And(str, error='密码参数字符类型错误'), And(lambda x: 4 <= len(x) <= 16, error='密码字符长度错误')),
    'email': And(And(str, error='邮箱参数字符类型错误'),
                 And(Regex(r'^\w+([-+.]\w+)*@\w+([-.]\w+)*\.\w+([-.]\w+)*$', error='邮箱正则匹配错误'))),
    Optional('nick_name'): And(And(str, error='昵称参数字符类型错误'), And(lambda x: len(x) <= 64, error='昵称字符长度错误'))
}


try:
    result = Schema(schema).validate(data)
    print(result)
except SchemaError as e:
    print(e.code)

