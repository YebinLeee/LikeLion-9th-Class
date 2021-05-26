x=10

def ex():
    global x # 전역변수로 접근을 한다는 의미
    x=5 # 전역변수인 x의 원본 값 자체를 변경
    print(x)

ex()
print(x)