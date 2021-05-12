# dictionary(hash) - key를 통해 value 를 가져온다.
# ex) 반복문을 통해 확인하지 않아도 됨- 키만 가지고 있으면 바로 value를 가져올수있다

dictionary={"아이돌":"매드몬스터", "데이트 상대":"이호창"}
print(dictionary["아이돌"]) # 아이돌 key에 대한 value 값 출력
print(dictionary["데이트 상대"]) # 데이트 상대 key에 대한 value 값 출력
print(dictionary) 
# dictionary[0] 은 불가능! 인덱스 번호처럼 사용할 수는 없음

# 하지만 key값이 정수인 경우에는 가능
dic={1:"hello", 2:"hi"}
print(dic[1])

dict={1:'One', 'Two':2, 5.0:3.3424, 'B':['최준',"방재호"]}
print(dict)