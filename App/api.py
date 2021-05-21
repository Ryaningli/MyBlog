from django.contrib import auth
from django.db import IntegrityError
from django.forms import model_to_dict
from django.views.decorators.http import require_http_methods
from App.data_factory import response, req2dict
from App.error import RequestParamError
from App.models import User
from App.param_test import ParamCheck


# 注册接口
@require_http_methods(['GET', 'POST'])
def user_manage(request):
    if request.method == 'POST':
        data = req2dict(request)
        checker = ParamCheck(data)

        try:
            username = checker.check('username', '用户名', required=True, param_type=str, min_length=4, max_length=16)
            password = checker.check('password', '密码', required=True, param_type=str, min_length=4, max_length=16)
            email = checker.check('email', '电子邮箱', required=True, param_type=str,
                                  regex=r'^\w+([-+.]\w+)*@\w+([-.]\w+)*\.\w+([-.]\w+)*$')
            nick_name = checker.check('nick_name', '昵称', required=False)
        except RequestParamError:
            pass
        else:
            try:
                User.objects.create_user(username=username, password=password, email=email,
                                         nick_name=nick_name)
            except IntegrityError as e:
                if ('username' and 'Duplicate entry') in str(e):
                    checker.code = 3000
                    checker.msg = '用户已存在'
                    checker.result = False
        finally:
            code = checker.code
            msg = checker.msg
            result = checker.result
            return response(code=code, msg=msg, result=result)

    # 获取当前登录的用户信息
    if request.method == 'GET':
        if request.user.is_authenticated:
            response_data = model_to_dict(request.user, exclude=('password', ))
            return response(code=0, msg='处理成功', result=True, data=response_data)
        else:
            return response(code=1000, msg='用户未登录', result=False)


# 登录接口
@require_http_methods(['POST'])
def login(request):
    if request.method == 'POST':
        data = req2dict(request)
        checker = ParamCheck(data)
        response_data = None
        try:
            username = checker.check('username', '用户名', required=True, param_type=str)
            password = checker.check('password', '密码', required=True, param_type=str)
        except RequestParamError:
            pass
        else:
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)   # 设置session
                checker.code = 0
                checker.msg = '登录成功'
                checker.result = True
                response_data = model_to_dict(user, exclude=('password',))  # 返回用户信息
            else:
                checker.code = 5000
                checker.msg = '用户不存在或密码错误'
                checker.result = False
        finally:
            code = checker.code
            msg = checker.msg
            result = checker.result
            return response(code=code, msg=msg, result=result, data=response_data)
    else:
        return response(code=1000, msg='请求参数错误', result=False)


# 登出
@require_http_methods(['GET'])
def logout(request):
    if request.method == 'GET':
        result = auth.logout(request)
        print(result)
        return response()
