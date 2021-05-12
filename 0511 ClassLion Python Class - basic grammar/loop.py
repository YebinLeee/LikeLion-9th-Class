# for 반복제어변수 in 반복대상(반복되길 바라는 대상)

# 우리반 학생 성적의 평균 (학생 성적을 반복해서 더해준 뒤 학생 수만큼 나눈다)

# range 함수: range(x,y) : x이상 y미만의 수를 리스트로 반환

sum=0
for number in range(1,11): # 1부터 10까지 총 10번 수행
    sum+=number
    print(sum)


# while (조건)
# 무한 루프 while(True)
# 반복문 종료 : if-break문

num=10
while(num>0):
    print("반복문 수행 중!")
    num-=1

