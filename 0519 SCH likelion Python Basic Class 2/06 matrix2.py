# [1,2,3,4,5] [6,7,8,..] ... 5x5 matrix 생성
# 두번째 방법 - 한 줄 생성후 전체 리스트에 추가

list=[] # 전체 리스트
num=0

for i in range(5):
    k=[] # 5개의 빈 리스트 생성
    for j in range(5): # 5개의 요소를
        k.append(num) # k의 빈 리스트에 추가
        num+=1
    list.append(k) # 5개의 요소에 대한 k 리스트를 list 리스트에 추가
    print(list) # 각 줄의 전체 요소 출력

print(list) # 5x5 전체 리스트 출력
for r in list: # 각 요소 출력해보기
    for c in r:
        print(c, ' ',end='')
    print()