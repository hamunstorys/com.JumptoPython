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

b = a[0:3]
print(b)

# 문자열을 슬라이싱하는 구체적인 방법

b = a[0:5]
print(b)
b = a[5:7]
print(b)
b = a[12:17]
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
print(b+"\n")

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

print(year+day+weather)

# 문자열 포매팅

