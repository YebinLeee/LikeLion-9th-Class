# '구분자'.join(리스트) - 구분자 문자열과 문자열 리스트의 요소들 사이에 구분자를 삽입하여 새로운 문자열 생성
# 리스트.split('구분자') - 리스트의 요소들을 구분자로 나눈 새로운 문자열 생성
 
b='apple, pear, grape, pineapple, orange'

print(b)
# 쉼표로 문자열 분리
c=b.split(',')

# 문자열의 요소 모두 연결
print(''.join(c))

# 각 문자열 사이에 공백이 들어가도록 생성
print(' '.join(c))

# ' * ' 
print(' * '.join(c))


print(c)