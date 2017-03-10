# 문자열(String)

# 문자열은 어떻게 만들고 사용하는 가?

# 1.큰따옴표로 양쪽 둘러싸기
# 2.작은따옴표로 양쪽 둘러싸기
# 3.큰따옴표 3개를 연속으로 써서 양쪽 둘러싸기
# 4.작은따옴표 3개를 연속으로 써서 양쪽 둘러싸기

print("문자열은 어떻게 만들고 사용하는 가?\n")

print("1.Hello World!")
print('2.Python is fun')
print("""3.Life is too short, You need python""")
print('''4.Life is too short, You nedd python\n''')

# 문자열 안에 작은따옴표나 큰 따옴표를 포함시키고 싶을 때

print("문자열 안에 작은따옴표나 큰 따옴표를 포함시키고 싶을 떄\n")

# 1.문자열에 작은따옴표(')을 포함시키기
# Python's favorite food is perl

food = "Python's favorite food is perl";
print("1." + food);

# 2.문자열에 큰따옴표(") 포함시키기
# Python is very easy." he says

say = '"Python is very easy." he says.'
print('2.' + say);

# 3.\(Backslash)를 이용해서 작은따옴표(')와 큰따옴표(")를 문자열에 포함시키기

food = 'Python\'s favorite food is perl';
print('3.' + food);
say = "\"Python is very easy\" he says.";
print('3.' + say + '\n');

# 여러 줄인 문자열을 변수에 대입하고 싶을 때

print('여러 줄인 문자열을 변수에 대입하고 싶을 때\n')

# 1.줄을 바꾸기 위한 이스케이프 코드 \n 삽입하기

multiline = "Life is too short\nYou need python";
print('1.' + multiline);

# 2.연속된 작은따옴표 3개(''') 또는 큰따옴표 3개를(""') 이용

multiline = '''Life is too short
You need python
'''
print('2-1.' + multiline);

multiline = """Life is too short
You need python
"""
print('2-2.' + multiline);

# 문자열 연산하기

print("문자열 연산하기\n")

# 1.문자열 더해서 연결하기(Concatenation)

head = "Python"
tail = " is fun!";
head + tail;
print('1.' + head + tail);

# 2.문자열 곱하기

a = "python";
a * 2;
print('2.' + a * 2 + '\n');

# 문자열 곱하기 응용

print("=" * 50)
print("My Program")
print("=" * 50 + '\n')

# 문자열 인덱싱

print("문자열 인덱싱\n")

a = "Life is too short, You need Python"
a[3];
print(a[3]);

a = "Life is oo short, You need Python"
a[0]
print(a[0])
a[12]
print(a[12])
a[-1]
print(a[-1])
a[-0]
print(a[-0])
a[-2]
print(a[-2])
a[-5]
print(a[-5] + '\n')

# 문자열 슬라이싱

print("문자열 슬라이싱\n")

a = "Life is too short, You need Python"
b = a[0] + a[1] + a[2] + a[3]
print(b)

# 슬라이싱할 자료구조[시작 인덱스:인덱스의 범위]

a = "Life is too short, You need Python"
b = a[0:4]
print(b)

b = a[0:3] # 0<=b<3
print(b)

# 문자열을 슬라이싱하는 구체적인 방법

b = a[0:5] # 0<=b<5
print(b)
b = a[5:7] # 5<=b<7
print(b)
b = a[12:17] # 12<=b<17
print(b)

# 슬라이싱할 자료구조[시작 인덱스:슬라이싱할 인덱스의 범위] 에서 인덱스 범위를 생략할 경우 자료구조의 인덱스의 끝까지 검색
b = a[19:]
print(b)

# 슬라이싱할 자료구조[시작 인덱스:슬라이싱할 인덱스의 범위]에서 시작 인덱스를 지정하지 않을 경우 문자열의 첫번째 인덱스부터 지정한 슬라이싱 인덱스 범위를 검색
b = a[:17]
print(b)

# 슬라이싱할 자료구조[시작 인덱스:슬라이싱할 인덱스의 범위]에서 둘 다 미지정일 경우
b = a[:]
print(b)

# 슬라이싱할 자료구조[시작 인덱스:슬라이싱할 인덱스의 범위]에서도 마이너스(-) 기호를 사용 가능하다.
b = a[19:-7]
print(b + "\n")

# 슬라이싱으로 문자열 나누기0

print("슬라이싱으로 문자열 나누기\n")

a = "20010331Rainy"

date = a[:8]
print(date)

weather = a[8:]
print(weather)

year = a[:4]
day = a[4:8]
weather = a[8:]

print(year + day + weather + '\n')

# 문자열 포매팅

print('문자열 포매팅\n')

# 문자열 포매팅 따라하기

# 1.숫자 바로 대입

print("I eat %d apples." % 3)

# 2.문자열에 바로 대입

print("I eat %s apples." % "five")

# 3.숫자 값을 나타내는 변수로 대입
number = 3
print("I eat %d apples." % number)

# 4.2개 이상의 값을 넣기
number = 10
day = "three"
print("I ate %d apples. so I was sick for %s days." % (number, day))

# %s 포맷 코드는 어떤 형태의 값이든 String datatype으로 변환해서 입력 가능하다.

print("I have %s apples" % 3)
print("rate is %s" % 3.234)

# 포매팅 연산자 %d와 %를 같이 쓸 때는 %%를 쓴다.

print("Error is %d%%.\n" % 98)

# 포캣 코드와 숫자 함께 사용하기

print("포맷 코드와 숫자 함께 사용하기\n")

# 1.정렬과 공백

print("%10s" % "hi")
print("%-10sjane" % "hi")

# 2.소수점 표현하기
print("%0.4f" % 3.42134234)
print("%10.4f\n" % 3.42134234)

# 문자열 관련 함수들

print("문자열 관련 함수들\n")

# 문자 개수 세기(count)

a = "hobby"
a.count('b')
print(a.count('b'))

# 문자 위치 알려주기(find)

a = "Python is best choice"

a.find('b')
print(a.find('b'))

a.find('k')
print(a.find('k'))

# 문자 위치알려주기2(index)

a = "Life is too short"

a.index('t')
print(a.index('t'))

# 문자열 삽입(join)

a = ","
a.join('abcd')
print(a.join('abcd'))

# 소문자를 대문자로 바꾸기(upper)

a = "hi"
a.upper()
print(a.upper())

# 대문자를 소문자로 바꾸기(lower)

a = "HI"
a.lower()
print(a.lower())

# 왼쪽 공백 지우기(lstrip)

a = " hi "
a.lstrip()
print(a.lstrip())

# 오른쪽 공백 지우기(rstrip)

a = " hi "
a.rsplit()
print(a.rstrip())

# 양쪽 공백 지우기(strip)

a = " hi "
a.strip()
print(a.strip())

# 문자열 바꾸기(replace)

a = "Life is too short"
a.replace("Life", "Your leg")
print(a.replace("Life", "Your leg"))

# 문자열 나누기(split)

a = "Life is too short"
a.split()
print(a.split())

# 고급 문자열 포매팅

print("\n고급 문자열 포매팅\n")

# 숫자 바로 대입하기
"I eat {0} apples".format(3)
print("I eat {0} apples".format(3))

#문자열 바로 대입하기
"I eat {0} apples".format("five")
print("I eat {0} apples".format("five"))

#숫자 값을 가진 변수로 대입하기

number = 3
"I eat {0} apples".format(number)
print("I eat {0} apples".format(number))

#2개 이상의 값 넣기

number = 10
day = "three"
"I ate {0} apples. so I was sick for {1} days".format(number,day)
print("I ate {0} apples. so I was sick for {1} days".format(number,day))

#이름으로 넣기

"I ate {number} apples. so I was sick for {day} days.".format(number=10, day=3)
print("I ate {number} apples. so I was sick for {day} days.".format(number=10, day=3))

#인덱스와 이름을 혼용해서 넣기

"I ate {0} apples. so I was sick for {day} days.".format(10, day=3)
print("I ate {0} apples. so I was sick for {day} days.".format(10, day=3))

#왼쪽 정렬(:<)

"{0:<10}".format("hi")
print("{0:<10}".format("hi"))

#오른쪽 정렬(:>)

"{0:>10}".format("hi")
print("{0:>10}".format("hi"))

#가운데 정렬(^)

"{0:^10}".format("hi")
print("{0:^10}".format("hi"))

#공백 채우기

"{0:=^10}".format("hi")
print("{0:=^10}".format("hi"))

"{0:!<10}".format("hi")
print("{0:!<10}".format("hi"))

#소수점 표현하기

y = 3.42134234
"{0:0.4f}".format(y)
print("{0:0.4f}".format(y))

"{0:10.4f}".format(y)
print("{0:10.4f}".format(y))

#{ 또는 } 문자 표현하기

"{{ and }}".format()
print("{{ and }}".format())