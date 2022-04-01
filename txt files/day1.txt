#05 출력하기, print()
print('Hello world!')
print(1, 2, 3)
print([1, 2, 3])
print('My name', 'is ' + 'Cheon Jeonghwan')

#06 입력하기, input()
name = input('이름을 입력하세요 :')
age = input('당신의 나이는? :')

#07 변수와 변수이름 (숫자로 시작, 띄어쓰기 금지)
my_int = 1
print(my_int * 100)

#08 기본재료1 : 숫자형, 문자열, 불린(True, False)
my_int = 3
print(my_int)
my_float = 3.14
print(my_float)
my_string = 'Hello'
print(my_string)
print(type(my_int), type(my_float), type(my_string))

#09 기본재료2 : 리스트[], 튜플(), 딕셔너리{}
my_list = ['1', 'two', '삼', 4, '5ive']
print(my_list)
my_list[3] = 44
print(my_list)
my_tuple = ('1', 'two', '삼', 4, '5ive')
print(my_tuple)
my_dict = {'1': 1, 'two': 2, '삼': 3, 4: 4, '5ive': 5}
for dic in my_dict:
    print(my_dict[dic])
my_dict[4] = 44
print(my_dict)

#10 자료형 변환하기
# 정수로 변환 : int(), 실수로 변환 : float(), 문자열로 변환 : str(), 리스트로 변환 : list()

#11 주석
#를 사용하면 컴퓨터가 인식하지 않는다.

#12 문자열
my_str = "천정환은 공부중"
print(my_str, type(my_str))
my_str = """천정환
설경훈
양해규
"""
print(my_str)

#13 문자열 포맷팅 (C스타일)
my_str = "My name is %s" %'천정환'
print(my_str)
# 정수형 : %d, 실수형 : %f, 문자형 : %s

#14 format() (python 스타일)
my_str = "My name is {}" .format('천정환')
print(my_str)
print('{0} x {1} = {2}' .format(11, 3, 33))
#여러개 : {0}, {1}, {2}...

#15 문자열 인덱싱
game = "League Of Legends"
print(game[0]+game[7]+game[10])
print(game[-2]+game[-10]+game[-5])

#16 문자열 슬라이싱
game_2 = "Maplestory"
print(game_2[:5])
print(game_2[5:])

#17 문자열 메서드, .split()
real_name = 'Cheon Jeong Hwan'
print(real_name.split())

#18 독스트링
"""이것도 주석입니다."""

#19 end, 이스케이프 코드 \n : 줄바꿈, \t : 탭(tab)
for i in range(1, 5):
    print(i)
for i in range(1, 5):
    print(i, end = ' ')
print('섹시\n도발')
print('어\t느새\t부터\t힙~합은\t안 멋져')