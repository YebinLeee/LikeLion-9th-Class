# slicing problems

str="881120-1068234"
index=str.find('-')
print(str[0:index])
print(str[index:])

li=[1,3,5,4,2]
li.sort()
li.reverse()
print(li)

# 얕은 복사
a=b=[1,2,3]
a[1]=4
print(b)