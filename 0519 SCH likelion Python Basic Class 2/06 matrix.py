# 0으로 초기화된 2차원 배열 생성
list=[[0]*5 for _ in range(5)] 
print(list)
i=0

for k in range(5):
    for m in range(5):
        list.append(i)
        i+=1

print(list)
