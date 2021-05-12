# 제어문 - 분기문(if문)
# if(조건):
#   참이라면 실행

# 85점 이상이면 pass or fail

score=int(input("점수를 입력하시오 : "))
if(score>=80):
    print("PASS")
else:
    print("FAIL")


# 동아리에 대해서

activity=input("너 동아리 뭐해? : ")
if(activity=="멋쟁이사자처럼"):
    print("어, 너도 멋사야? 나도.")
else:
    if(activity=="멋사"):
        print("어 나도.")
    else:
        print("나는 멋사에서 활동하고 있어.")


# else-if -> elif
if(activity=="멋쟁이사자처럼"):
    print("어, 너도 멋사야? 나도.")
elif(activity=="멋사"):
    print("어 나도.")
else:
    print("나는 멋사에서 활동하고 있어.")