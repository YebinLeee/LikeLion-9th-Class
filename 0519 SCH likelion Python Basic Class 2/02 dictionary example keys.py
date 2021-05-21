example={'최민석':'단땅', '김율희':'두부', '최세환':'토리', '하유민':'봄옹' }

print(example.keys())
print(example.values())
print(example.items())

for e in example.values():
    print(e)

    for key,values in example.items():
        print(key,values)