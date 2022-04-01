#37 if
my_name = input('이름을 입력하세요 :')
if my_name == '천정환':
    print('만나서 반가워요,', my_name)

#38 else, elif
my_name = input('이름을 입력하세요 :')
if my_name == '천정환':
    print('만나서 반가워요,', my_name)
elif my_name == '밀키스카우':
    print('어서오세요,', my_name)
else:
    print('죄송하지만 누군지 모르겠네요..')

#39 while
cnt = 0
while cnt < 3:
    print('횟수:', cnt)
    cnt += 1

#40 continue, break
cnt = 0
while cnt < 10:
    cnt += 1
    if cnt < 4:
        continue
    print('횟수:', cnt)
    if cnt == 8:
        break

#41 딕셔너리
my_dict = {}
my_dict[0] = 'a'
my_dict['나'] = '천정환'
my_dict[1] = '밀키스카우'
print(my_dict)
del my_dict[0]
my_dict[1] = '1'
print(my_dict)

#42 딕셔너리 메서드, .values(), .keys(), items()
my_dict = {'나' : '천정환', 'one' : 1, '이' : 2, '삼' : 3, '야' : '왜'}
for val in my_dict.values():
    print(val, end = ' ')
print('')
for val in my_dict.keys():
    print(val, end = ' ')
print('')
for val in my_dict.items():
    print(val, end = ' ')
print('')
