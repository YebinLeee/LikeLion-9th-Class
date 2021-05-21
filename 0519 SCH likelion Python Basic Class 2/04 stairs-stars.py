# 입력받은 숫자의 층만큼 계단식으로 별을 찍는 프로그램

a=int(input())

for i in range(a): # (0~(i-1)) 반복
    for j in range(i+1):
         print('*', end='') # (0~i) 반복
    print() # 줄바꿈