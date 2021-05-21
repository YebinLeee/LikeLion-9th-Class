# 괄호의 짝이 맞는지 확인해보는 프로그램
# parenthesis, bracket, brace 추가 구현 해보기


quiz='(()(()(())(()()())()((()))()'
print(quiz)

while 1:
    tmp=quiz # tmp에 임시로 quiz 저장
    quiz=quiz.replace('()', '') # ()를 공백으로 바꾸기를 반복
    if quiz=='': # 반복하면서 quiz문자열 전체가 공백이 된다면
        print("잘 닫힌 괄호") # 괄호 짝이 모두 맞는 문자열임
        break
    if tmp==quiz: # tmp가 quiz랑 같다면(더이상 변화가 없다면)
        print(quiz) # 출력하고 끝내기
        print("괄호의 짝이 맞지 않음") 
        break
