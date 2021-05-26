def add(a,b):
    return a+b
def min(a,b):
    if a>b:
        return a-b
    else:
        return b-a
def mul(a,b):
    return a*b
def div(a,b):
    if a>b:
        return a/b
    else:
        return b/a

print("더하기 : ", add(2,4)) # f'더하기: {add(2,4)}'
print("빼기 : ", min(2,4))
print("곱하기 : ", mul(2,4))
print("나누기 : ", div(2,4))