import functools
import json


class ParmaValidator:
    pass


def validator(rule):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(request):
            data = request.body
            print('-----------------')
            print(rule)
            print(data)
            return func(request)
        return wrapper
    return decorator


class Length:
    def __init__(self, *args):
        self._arg = args

    @property
    def args(self):
        return self._arg


if __name__ == '__main__':
    a = Length(1, 2)
    print(a.args)
