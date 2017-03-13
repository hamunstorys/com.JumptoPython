import random as ramdom

# if문

# True(참) 일경우와 False(거짓) 일 경우 각각의 조건에 맞게 결과를 출력하는 제어문

print('\nif문\n')

print('True(참) 일경우와 False(거짓) 일 경우 각각의 조건에 맞게 결과를 출력하는 제어문\n')

money = 1
if money:
    print("택시를 타고 가라")
else:
    print("걸어 가라")

# if문의 기본 구조

print('\nif문의 기본 구조\n')

# if 조건문:
#   수행할 문장1
#   수행할 문장2
# else:
#   수행할 문장1
#   수행할 문장2

# 들여쓰기
# Python 문법에서는 같은 깊이에서 실행되는 처리식을 들여쓰기로 표현한다.

# 들여쓰기는 Tab을 사용하거나 Python 커뮤니티에서는 Space를 4번 사용하는 것을 권장하고 있다.

if money:
    print("택시를 타고 가라")  # 들여쓰기
else:
    print("걸어 가라.")  # 들여쓰기

    #  조건문이란 무엇인가?

print('\n조건문이란 무엇인가?\n')

print('숫자 : 0이 아닌 숫자면 참, 0이면 거짓')
print('문자 : 값을 가지고 있으면("abc") 참, 없으면 거짓')
print('리스트 : 요소 값을 가지고 있으면([1,2,3]) 참, 없으면 거짓')
print('튜플 : 요소 값을 가지고 있으면((1,2,3)) 참, 없으면 거짓')
print('딕셔너리 : Key와 Value가 쌍을 이루고 있으면({"a":"b"}) 참, 없으면 거짓')

# 비교연산자

print('\n비교연산자\n')

print('x<y : x가 y보다 작다')
print('x>y : x가 y보다 크다')
print('x==y : x와 y가 같다')
print('x!=y : x와 y가 같지 않다')
print('x>=y : x가 y보다 크거나 같다.')
print('x<=y : x가 y보다 작거나 같다.')

x = 3
y = 2
x > y  # 3>2
print(x > y)  # x에 3을, y에 2를 대입한 다음에 x>y라는 조건문을 수행하면 True를 리턴한다. x>y라는 조건문이 참이기 때문이다.
print(x < y)  # 이 조건문은 거짓이기 때문에 False를 리턴한다.
print(x == y)  # 이 조건문은 거짓이기 때문에 False를 리턴한다.
print(x != y)  # x와 y는 같지 않다. 따라서 위의 조건문은 참이다.

# "만약 3천원 이상의 돈을 가지고 있으면 택시를 타고 그렇지 않으면 걸어가라" 라는 조건문을 if문으로 작성한다면

print('\n"만약 3천원 이상의 돈을 가지고 있으면 택시를 타고 그렇지 않으면 걸어가라" 라는 조건문을 if문으로 작성한다면\n')

money = ramdom.randrange(10, 10000)
if money >= 3000:
    print("택시를 타고 가라")
else:
    print("걸어가라.")

# and, or , not

print("\nand, or, not\n")

print('조건을 판단하기 위해 사용하는 다른 연산자로는 and, or, not이 있다. 각각 연산자는 다음과 같이 작동한다.')
print('x or y : x와 y 둘 중에 하나만 참이면 참이다.')
print('x and y : x와 y 모두 참이어야 참이다.')
print('not x : x가 거짓이면 참이다.')

# "돈이 3천원 이상 있거나 카드가 있다면 택시를 타고 그렇지 않으면 걸어 가라"

print("\n돈이 3천원 이상 있거나 카드가 있다면 택시를 타고 그렇지 않으면 걸어 가라라는 조건문을 if문으로 작성한다면\n")

money = ramdom.randrange(10, 10000)
card = ramdom.randrange(0, 1)
if money >= 3000 or card:
    print("택시를 타고 가라")
else:
    print("걸어서 가라")

# x in s, x not in s

print('\nx in s, x not in s\n')

# 리스트

1 in [1, 2, 3]  # 1이 리스트 [1,2,3] 안에 있는가?
print(1 in [1, 2, 3])
1 not in [1, 2, 3]  # 1이 리스트 [1,2,3] 안에 없는가?
print(1 not in [1, 2, 3])

'a' in ('a', 'b', 'c')  # 'a'가 튜플 ('a','b','c')안에 있는가?
print('a' in ('a', 'b', 'c'))
'a' not in ('a', 'b', 'c')  # 'a'가 튜플 ('a','b','c')안에 없는가?
print('a' not in ('a', 'b', 'c'))

# "만약 주머니에 돈이 있으면 택시를 타고, 없으면 걸어 가라" 라는 조건문에 in을 적용한다면

print('\n"만약 주머니에 돈이 있으면 택시를 타고, 없으면 걸어 가라" 라는 조건문에 in을 적용한다면\n')

pocket = ['paper', 'cellphone', 'money']  # 주머니 안에 종이, 휴대전화, 돈이 있다.
if 'money' in pocket:
    print("택시를 타고 가라")
else:
    print("걸어가라")

# 조건문에서 아무 일도 하지 않게 설정하고 싶다면?

print('\n조건문에서 아무 일도 하지 않게 설정하고 싶다면?\n')

# "주머니에 돈이 있으면 가만히 있고 주머니에 돈이 없으면 카드를 꺼내라"

pocket = ['paper', 'cellphone', 'money']  # 주머니 안에 종이, 휴대전화, 돈이 있다.
if 'money' in pocket:
    pass
else:
    print('카드를 꺼내라')

# 다양한 조건을 판단하는 elif

# 주머니에 돈이 있으면 택시를 타고, 주머니에 돈은 없지만 카드가 있으면 택시를 타고, 돈도 없고 카드도 없으면 걸어가라

print('\n다양한 조건을 판단하는 elif\n')

pocket = ['paper', 'cellphone']  # 주머니 안에 종이, 휴대전화가 있다.
card = 1  # 카드를 가지고 있다.
if 'money' in pocket:
    print("택시를 타고 가라")
else:
    if card:
        print("택시를 타고 가라")
    else:
        print("걸어 가라")

pocket = ['paper', 'cellphone']
card = 1
if 'money' in pocket:
    print("택시를 타고 가라")
elif card:
    print("택시를 타고 가라")
else:
    print("걸어 가라")

# if문을 한 줄로 작성하기

print("\nif문을 한 줄로 작성하기\n")

pocket = ['paper', 'cellphone', 'money']
if 'money' in pocket: pass
else: print("카드를 꺼내라")