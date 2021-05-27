import functools
import json

from django.core.handlers.wsgi import WSGIRequest


def ak(*arg, **kw):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(request):
            request.body = json.loads(request.body)
            return func(request)
        return wrapper
    return decorator


def ak2(f):
    def wrapper(request):
        request._body = json.loads(request.body)
        return f(request)
    return wrapper


