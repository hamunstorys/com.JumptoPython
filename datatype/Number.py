# Single line Python Block Comment Remark

"""
Multiple line Python Block Comment Remark

"""

# 정수형(integer)

# 1. 양의 정수
# 2. 음의 정수
# 3. 0

print("정수형(Integer)\n");
a = 123;
print(a);

a = -178;
print(a);

a = 0;
print(a);
print();

# 실수형(Floating-point)

# 4.24e10 또는 4.24E10처럼 표현한다(e와 E 둘 중 어느 것을 사용해도 무방하다). 여기서 4.24E10은 4.24∗1010,  4.24e-10은 4.24∗10−10을 의미한다.
# e = 10
# e10 = 10의 10제곱을 의미
# e-10 = 10의 -10제곱을 의미

print("실수형(Floating-point)\n");

a = 4.24e10;
print(a);

a = 4.24e-10;

print(a);
print();

# 8진수와 16진수
# 8진수(Octal)를 만들기 위해서는 숫자가 0o 또는 0O(숫자 0 + 알파벳 소문자 o 또는 대문자 O)로 시작하면 된다.

# 8진수 0o 혹은 0O로 시작

print("8진수(Octal)\n");

a = 0o177;

print(a);
print();

# 16진수 0x 혹은 0X로 시작

print("16진수(Hexadecimal)\n")

a = 0x8ff;
print(a);

b = 0xABC;
print(b);
print();

# 사칙연산

print("사칙연산\n");
a = 3
b = 4

a + b
print(a + b);
a * b
print(a * b);
a / b
print(a / b);
print();

# x의 y제곱을 나타내는 ** 연산자

print("x의 y제곱을 나타내는 ** 연산자\n");

a = 3;
b = 4;
a ** b;
print(a ** b);
print();

# 나눗셈 후 나머지를 반환하는 % 연산자

print("나누셈 후 나머지를 반환하는 % 연산자\n");

7 % 3
print(7 % 3);

3 % 7
print(3 % 7);
print();

# 나눗셈 후 소수점 아랫자리를 버리는 // 연산자

print("나눗셈 후 소수점 아랫자리를 버리는 // 연산자\n");

7 / 4
print(7 / 4);

7 // 4
print(7 // 4);

-7 / 4
print(-7 / 4);

-7 // 4
print(-7 // 4);
print();
