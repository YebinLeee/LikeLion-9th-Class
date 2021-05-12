a=[1,2,3,4,5]
print(a)
print(a[::-1])
print(a[0::-1])
print(a[:0:-1])

a[4]=7 # 4번 인덱스 5를 7로 변경
print(a)

a[0:3]=[3,2,1] # 0-2 인덱스(1,2,3)을 (3,2,1)러 뱐걍
print(a)

del a[0:3] # 0,1,2 인덱스 삭제
print(a)


list1=[]
list1.append('a')
list1.append(1)
print(list1)