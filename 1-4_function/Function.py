# 함수(fucntion)

# 함수를 사용하는 이유는 무엇일까?
# 반복되는 부분이 있을 경우 '반본적으로 사용되는 가치 있는 부분'을 하나의 식으로 만들어 '어떤 입력값을 주었을 때 어떤 결과값을 돌려준다'

# 파이썬 함수의 구조

print('\n파이썬 함수의 구조\n')


# def 함수명(입력 인수)
#   수행할 문장1
#   수행할 문장2

# 이 함수의 이름(함수명)은 sum이고 입력 인수로 2개의 값(a 와 b)을 받으며 결과값은 2개의 입력값을 더한 값이다.

def sum(a, b):
    return a + b


a = 3
b = 4
c = sum(a, b)
print(c)

# 입력값과 결과값에 따른 함수의 형태

print('\n입력값과 결과값에 따른 함수의 형태\n')

print('입력값 → 함수 → 결과값')

# 일반적인 함수

print('\n일반적인 함수\n')


# def 함수명(입력 인수):
#   수행할 문장
#   ...
#   return 결과값

def sum(a, b):
    result = a + b
    return result  # a+b의 결과값 리턴


a = sum(3, 4)
print(a)

# 입력값이 없는 함수
# 결과값을 받을 변수 = 함수명()

print('\n입력값이 없는 함수\n')


def say():
    return 'Hi'


a = say()
print(a)

# 결과값이 없는 함수 함수명(입력 인자1, 입력 인자2, 입력 인자n)

print('\n결과값이 없는 함수\n')


def sum(a, b):
    print("%d, %d 합은 %d입니다." % (a, b, a + b))


sum(3, 4)
a = sum(3, 4)
print(a)

# 입력값도 결과값도 없는 함수 함수명()

print('\n입력값도 결과값도 없는 함수\n')


def say():
    print("Hi")


say()

# 입력값이 몇 개가 될지 모를 때는 어떻게 해야 할까?

print('\n입력값이 몇 개가 될지 모를 때는 어떻게 해야 할까?\n')

# def 함수명(*입력 변수):
#   수행할 문장
#   ...

# 여러 개의 입력값을 받는 함수 만들기

print('\n여러 개의 입력값을 받는 함수 만들기\n')


def sum_many(*args):
    sum = 0
    for i in args:
        sum = sum + i
    return sum


result = sum_many(1, 2, 3)
print(result)

result = sum_many(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(result)


def sum_mul(choice, *args):
    if choice == "sum":  # 입력 인수 choice에 'sum'을 입력받았을 때
        result = 0
        for i in args:
            result = result + i  # *args에 입력받은 모든 값을 더한다.
    elif choice == "mul":  # 입력 인수에 choice에 'mul'을 입력받았을 때
        result = 1
        for i in args:
            result = result * i  # *args에 입력받은 모든 값을 곱한다.
    return result


result = sum_mul('sum', 1, 2, 3, 4, 5)
print(result)

result = sum_mul('mul', 1, 2, 3, 4, 5)
print(result)

# 함수의 결과값은 언제나 하나이다.

print('\n함수의 결과값은 언제나 하나이다.\n')


def sum_and_mul(a, b):
    return a + b, a * b


# sum_and_mul 함수의 결과값 a+b와 a*b는 튜플 값인(a+b,a*b)로 돌려준다.

result = sum_and_mul(3, 4)
result = (7, 12)

sum, mul = sum_and_mul(3, 4)  # 이렇게 호출하면 sum,mul=(7,12)가 되어 sum은 7이 되고 mul은 12가 된다.


def sum_and_mul(a, b):
    return a + b
    return a * b


result = sum_and_mul(2, 3)
print(result)  # 첫번째 return문만 실행되고 두번째 return문은 실행되지 않는다.

# 위 함수는 아래의 함수와 완전히 동일한 함수이다.
# def sum_and_mul(a,b):
#    return a+b

# return의 또 다른 쓰임새
# 어떤 특별한 상황이 되면 함수를 빠져나가고자 할 떄는 return을 단독으로 써서 함수를 즉시 빠져나갈 수 있다.

print("\nreturn의 또 다른 쓰임새\n")


def say_nick(nick):
    if nick == "바보":
        return
    print("나의 별명은 %s입니다." % nick)


say_nick('야호')
say_nick('바보')

# 입력 인수에 초깃값미리 설정하기

print('\n입력 인수에 초깃값 미리 설정하기\n')


def say_myself(name, old, man=True):
    print("나의 이름은 %s입니다." % name)
    print("나이는 %d살입니다." % old)
    if man:
        print("남자입니다.")
    else:
        print("여자입니다.")


say_myself("박응용", 27)
say_myself("박응용", 27, True)

say_myself("박응선", 27, False)

# 함수 입력 인수에 초깃값을 설정할 때 주의할 사항
# 입력인수는 항상 뒤에 위치시킨다.

# def say_myself(name, man=True, old):
#     print("나의 이름은 %s입니다." % name)
#     print("나이는 %d입니다." % old)
#     if man:
#         print("남자입니다.")
#     else:
#         print("여자입니다.")

# SynataxError : non-default argument floows default argument
# 초기값을 설정해 놓은 입력 인수 뒤에 초기값을 설정해 놓지 않은 입력 인수는 사용할 수 없다

# 함수 안에서 선언된 변수의 효력 범위

print('\n함수 안에서 선언된 변수의 효력 범위\n')

a = 1  # 함수밖의 변수 a


def vartset(a):
    a = a + 1


vartset(a)
print(a)


def vartest(hello):
    hello = hello + 1


vartset(3)
print(a)

# 함수 안에서 함수 밖의 변수를 변경하는 방법

print('\n함수 안에서 함수 밖의 변수를 변경하는 방법\n')

# 1. return 이용하기

print("1. return 이용하기")

a = 1
def vartest(a):
    a = a + 1
    return a

a = vartest(a)
print(a)

# 2. global 명령어 이용하기

print('\n2.global 명령어 이용하기\n')

a = 1
def vartset():
    global a
    a = a + 1


vartset()
print(a)
