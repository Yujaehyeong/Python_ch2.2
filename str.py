# 한 줄 문자열 정의

s =''
str1 = 'Hello world'
print(type(s), type(str1))
print(isinstance(str1, str))


# 여러줄 문자열
str2 = '''
ABC
1234
가나다라'''
print(str2)

'''
여기는 주석입니다.
여러 라인 주석을 대체할 수 있습니다.
'''

#escape
print('Hello\nWorld\nI Say "Hello World"')


# 문자열 연산
str1 = 'First String'
str2 = 'Second String'

# 1. 인덱싱
print(str1[0], str1[1], str1[2])

# 2. Slicing
str3 = str2[2:5] # Start Index : End Index : Step  start부터 end-1 까지 슬라이싱됨
print(str3)
# print(str2[2:len(str2):1)
print(str2[2:])

s= "Python"
print(s[-1]) # 마지막문자
print(s[-2:]) # 마지막2개문자
print(s[:-2]) # 마지막2개문자 제외한 전체 문자열

print(s[::-1])   # reverse
print(s[1::-1])  # 1번째, 2번째 문자 문자 s[1:0:-1]
print(s[:-3:-1]) # 마지막 2개 문자
print(s[-3::-1]) # 마지막 2개 문자 제외한 전체문자

# 연결(+)
print(str1 +' '+str2)
# 리터럴 연결시 + 생략 가능
# str3 = '1st' + ' ' + '2nd'
str3 = '1st' + ' ' + '2nd'
print(str3)

# 문자열 객체 연결은 문자열끼리만 할 수 있다.
name ='둘리'
age = 10
# print(name + 10)

# 반복(*)
print(str1 * 3)

# len함수
print(len(str1))

# in, not in 연산
print('F' in str1)
print('S' not in str1)

# str 객체는 immutable이다
# str1[0] = 'f';

# 서식(formatting) = format 함수
print("name: " + name + ", age: "+ str(age))
