# 딕셔너리(해쉬) : '대응'이 되는 데이터를 표현해주는 자료형

# ex) 김연아-피겨스케이팅 / 박찬호 - 야구 / 마이클조던 - 농구 / 박지성-축구

# { Key1 : Value1, Value2, Value3...}
# key는 중복되어서는 안 됨

# 'key'를 통해 'value'를 얻는다 (2 X N 의 표)
# 딕셔너리 변수[Key1]==Value1
# ex) 운동선수 = {"김연아":"피겨스케이팅", "박지성": 축구" ...}
# ex) 운동선수['김연아']=='피겨스케이팅'



# 딕셔너리의 내장 함수

pairs={'잔나비':'뜨거운 여름밤은 가고 남은 건 볼품없지만', '소하':'산책', '홍크': '어쩌면'}

# 하나의 키-value 를 추가
# 딕셔너리형 변수[키]=value

print("pairs dictionary : ", pairs)
pairs['스탠딩 에그']='휴식'
print("1 add - pairs dictionary : ", pairs)

# 특정 키-value 삭제하는 함수 : del
# del 변수[키]

del pairs['잔나비']
print("1 delete - pairs dict : ", pairs)


# 키로 value 를 얻는 함수 : 변수.get(키)
print("get 스탠딩 에그 : ", pairs.get('스탠딩 에그'))
print("get 홍크 : ", pairs.get('홍크'))