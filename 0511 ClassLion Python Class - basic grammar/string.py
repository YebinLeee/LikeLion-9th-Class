# "문자형 자료형"
# 문자열에 대한 덧셈과 곱셈

# 인덱싱: 문자열을 구성하는 '하나'의 문자에 접근. 한 문자의 위치 정보
str1="멋쟁이사자처럼"
print(str1[0])
print(str1[-1])

# 슬라이싱 : 문자열을 구성하는 '여러개의' 문자에 범위로 접근 [ : ]
str2="hello"
print(str2[0:2]) # h부터 l의 이전 문자까지 출력



# 문자열(내장함수)

# 문자열 길이 : len(문자열 변수)
str="멋쟁이사자처럼 아기사자" #인덱스는 0~6, 길이는 7
print(len(str))

# 문자열 내에서 특정 문자의 등장 횟수 : 문자열.count('특정 문자')
print(str.count('사'))

# 문자열을 (특정 기준으로) 나누기 : 문자열.split() - 공백을 기준으로 리스트로 나눈다

print(str.split( ))
print(str.split('사'))

# 특정 문자 인덱스 찾기 : find('문자') , index('문자')

print(str.find('사'))
print(str.index('자'))