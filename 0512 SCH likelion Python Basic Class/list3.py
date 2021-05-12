# reverse, sort, index, insert(index, value) (append와의 차이)
# 내림차순 sort(reverse=True)

a=[1,3,4,5,2]
print(a)

a.reverse() # 오름차순
print("reverse a : ",a)

a.sort()
print("sort a : ", a)

print("2 index : ",a.index(2))


#insert(a,b) a번째에 b를 삽입 (append 는 가장 마지막에 삽입)

print(a)
print("a.insert(2,6)")
a.insert(2,6)
print(a)