#30 할당 연산자
val = 1
val += 1
print(val)
val -= 1
print(val)
val *= 2
print(val)
val /= 2
print(val)

#31 산술 연산자
# 더하기: +, 빼기: -, 곱하기: *, 나누기: /, 제곱: **, 몫: //, 나머지: %

#32 %로 홀짝 구분하기
num = [1, 2, 3, 4, 5, 6, 7]
for i in num:
    if i % 2 == 1:
        print('{}는 홀수입니다' .format(i))
    else:
        print('{}는 짝수입니다' .format(i))

#33 문자열 연산자 +, *
print('안녕'+'하세요')
print('안녕'*10)
def cls():
    print('\n' * 100)
cls()

#34 비교 연산자
# 같다: ==, 같지 않다: !=, 초과미만: >,<, 이상이하: >=,<=

#35 논리 연산자 and, or, not
height = 170
age = 19
print(height > 160 and age > 20)
print(height > 180 or age > 18)
print(not age < 20)

#36 멤버쉽 연산자 in, not in
BR31 = ['체리쥬빌레', '뉴욕치즈케이크', '고디바초콜릿', '레인보우샤베트', '요거트', '베리베리스트로베리']
print('요거트' in BR31)
print('레인보우샤베트' not in BR31)
print('슈팅스타' in BR31)
print('슈팅스타' not in BR31)