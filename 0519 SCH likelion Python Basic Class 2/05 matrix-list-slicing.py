example=[
    ["동덕여대", "멋쟁이", "사자처럼", "7기"],
    ["단국대", "멋쟁이", "사자처럼", "8기"],
    ["선문대", "멋쟁이", "사자처럼", "9기"],
    ["순천향대", "멋쟁이", "사자처럼", "9기"]
]

# print(example) # 전체 출력 - 모두 한 줄에 한꺼번에

print(example[3][0]) # 순천향대 출력

for e in example: # 한 줄에 한 개 요소씩 출력
    print(e)

# 슬라이싱 기법
print(example[3][0:3]) # example[3] row의 (0~2)column 출력 : 순천향대 멋쟁이 사자처럼

# 행과 열까지 모두 고려하는 경우 : 반복문 이용
for e in example[1:]: # example[1] row 부터
    print(e[0:3]) # [e][0], [e][1], [e][2] 출력

# 각각의 요소를 개별적으로 출력
for e in example:
    for i in e:
        print(i,' ',end='')
    print()
