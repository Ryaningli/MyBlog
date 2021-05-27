class A:
    pass


__all__ = [
    'B', 'test'
]

class B(A):
    pass


a = A()
b = B()

print(type(a))
print(type(b))

if type(b) in A:
    print('没错')