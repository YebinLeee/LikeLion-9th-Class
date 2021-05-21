# replace('바꿀 문자열', '새 문자열')

a="Hello, Python. Hello!"

print(a.replace('Hello', 'Hi')) # 'Hello' 문자열 모두 'Hi'로 변경
print("원본 유지 : ",a) 

a=a.replace('Hello', 'Hi') # 원본 변경을 위해서는 다시 대입해줘야함
print("원본 변경 : ",a)