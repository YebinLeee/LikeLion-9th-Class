a=['alpha', 'bravo', 'charlie', 'delta', 'echo', 'golf', 'foxtrot', 'golf','hotel', 'india']
b=[] # 빈 리스트 생성

# b = [i for i in a if len(i)==5]

for i in a: # a의 리스트 요소중에
   if len(i)==5: # 길이가 5라면
       b.append(i) # b 리스트 끝에 추가

print(b)
for i in b:
    print(i)
