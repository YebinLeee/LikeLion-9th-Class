# 문자열.split('구분자') -> 구분자로 나누어 문자열을 각 리스트 요소로 추출

path = '/Users/0519 SCH likelion Python Basic Class 2/1.py'
print('path : ',path)

x=path.split('/')
print('split(''/'') : ', x)

filename=x[-1] # 첫번째 요소의 앞에 있는 요소
print(filename)