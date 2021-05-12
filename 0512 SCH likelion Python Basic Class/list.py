# 인덱싱 []

a=[5,4,3,2,1]
print("a의  4번째 인덱스 값은", a[3])

# append 함수
print('a: ', a)
a.append(4)
print('a : ',a)

# 슬라이싱
print(a[0:3]) # 0, 1, 2번째 인덱스값들 리스트로 출력
print(a[0:5:2]) # 0부터 5번째 전까지 2씩 띄어서 출력

# 리스트 거꾸로 전부 출력하기
print(a[::-1]) # 처음부터 끝까지 -1 간격으로 간다는 뜻. 
print(a[0:]) #처음부터 끝까지 출력
print(a[:])

b=[1,2,3]
print(a+b)
print(a*3)
print(len(a), len(b))
