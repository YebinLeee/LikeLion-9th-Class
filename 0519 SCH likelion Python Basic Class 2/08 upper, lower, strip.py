# 리스트.upper() -> 소문자를 대문자로 변경
# 리스트.lower() -> 대문자를 소문자로 변경

s=' . . PyThon...'
print(s)
print("s.upper()", s.upper()) # s 문자열을 모두 대문자로 변경
print('원본:', s) # 원본은 변경되지 않음

s=s.lower() # s 문자열을 모두 소문자로 변경(원본 변경)
print("s=s.lower()", s)

# strip(), lstrip(), rstrip() -> 양쪽,왼쪽,오른쪽에 있는 연속된 모든 공백을 삭제
print("lstrip('.'):",s.lstrip('.')) # 왼쪽부터 스캔 - 공백부터 시작하므로 '.' 삭제 안됨
print("rstrip('.'):",s.rstrip('.')) # 오른쪽부터 스캔 - 연속된 '.' 3개 삭제
print("lstrip('.'):",s.strip('.')) # 왼쪽/오른쪽 모두 스캔 - 연속된 오른쪽의 '.' 3개만 삭제