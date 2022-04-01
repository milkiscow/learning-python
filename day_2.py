#20 리스트 (mutable)
std = ['밀키스카우', '자카인', '천정환']
type(std)

#21 리스트 값 추가하기, .append()
obj = ['책상', '무드등', '의자']
obj.append('마이크')
print(obj)

#22 리스트 인덱싱, 슬라이싱, del
print(obj[3] == '마이크')
del obj[1]
print(obj)

#23 리스트 메서드, .sort(), .count()
alpha = ['a', 'b', 'B', 'A', 'C', 'c']
alpha.sort()
print(alpha, alpha.count('a'))

#24 튜플 (immutable)
family = ('엄마', '아빠', '나')
print(type(family))

#25 패킹, 언패킹
vals = 1, 2, 3
val1, val2, val3 = vals
print(val1, val2, val3, vals)
val1, val2 = val2, val1
print(val1, val2, val3)

#26 for
for str in "그날이 오면":
    print(str)
for lst in alpha:
    print(lst)
for tup in vals:
    print(tup)

#27 range()
for i in range(1, 101):
    print(i, end = ' ')

#28 for x 2
for j in range(2, 10):
    cnt = 0
    for i in range(1, 10):
        print('{} x {} = %2s,' .format(j, i) %(j*i), end = ' ')
        cnt += 1
        if cnt == 9:
            cnt = 0
            print(' ')

#29 컴프리헨션
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
odd = []
for num in numbers:
    if num % 2 == 1:
        odd.append(num)
print(odd)
print([number for number in numbers if number % 2 == 1])