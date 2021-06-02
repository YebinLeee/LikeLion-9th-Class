# 잔돈 - 500 100 50 10 5 1
# 1000원 지폐 냈을 때, 받을 잔돈에 포함된 잔돈의 개수는?
# 예) 입력: 380 -> 거스름돈: 1000-380=620 : 500*1 + 100*1 + 10*2 => 답==총 4장
# change: 620%500 = 120 -> 120%100100 = 20 -> 20%10=0

userInput=int(input()) # 금액 입력 받음
change=int(1000-userInput) # 전체 거스름돈 액수
money=[500, 100, 50, 10, 5, 1]
cnt=0 # 잔돈의 개수 초깃값==0

for m in money:
    cnt+=change//m # change를 money리스트 안의 금액으로 나눈 몫을 누적하여 합산
    change%=m # money 요소로 나눈 나머지를 저장

print(cnt)