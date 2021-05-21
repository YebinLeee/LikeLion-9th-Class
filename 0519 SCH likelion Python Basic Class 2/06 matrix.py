# [1,2,3,4,5] [6,7,8,..] ... 5x5 matrix 생성
# 첫번쨰 방법 - 0으로 초기화된 2차원 리스트의 틀을 미리 생성

list=[[0]*5 for _ in range(5)] # 5개의 요소 * 5 (Row) 생성
print('빈 리스트 생성: ', list) # 전체 출력

# 요소 한 줄씩 출력
for r in list:
    for c in r:
        print(c, end='')
    print()

num=0
for i in range(5):
    for j in range(5):
        list[i][j]=num # j+num
        num+=1 # num+=5
print(list)