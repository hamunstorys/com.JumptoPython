# 파이썬 프로그래밍의 핵심, 클래스(Class)

# 클래스는 도대체 왜 필요한가?
from builtins import print

print("\n클래스는 도대체 왜 필요한가?\n")

result = 0


def adder(num):
    global result
    result += num
    return result


print(adder(3))
print(adder(4))

result1 = 0
result2 = 0


def adder1(num):
    global result1
    result1 += num
    return result1


def adder2(num):
    global result2
    result2 += num
    return result2


print(adder1(3))
print(adder1(4))
print(adder2(3))
print(adder2(7))


class Calculator:
    def __init__(self):
        self.result = 0

    def adder(self, num):
        self.result += num
        return self.result


cal1 = Calculator()
cal2 = Calculator()

print(cal1.adder(3))
print(cal1.adder(4))
print(cal2.adder(3))
print(cal2.adder(4))

# 클래스 개념 잡기
# 클래스는 뽑기의 틀과 비슷하다. 별 모양의 틀(클래스)로 찍으면 별 모양의 뽑기(인스턴스)가 생성되고 하트 모양의 틀(클래스)로
# 찍으면 하트 모양의 뽑기(인스턴스)가 나오는 것이다.
# 클래스란 똑같은 무엇인가를 계속해서 만들어 낼 수 있는 설계 도면 같은 것이고
# 인스턴스란 클래스에 의해서 만들어진 피조물을 뜻한다.

print("\n클래스 개념 잡기\n")


class Simple:
    pass


# 인스턴스는 클래스에 의해서 만들어진 객체로, 1개의 클래스는 무수히 많은 인스턴스를 만들어 낼 수 있다.

a = Simple()

# 이야기 형식으로 클래스 기초 쌓기

print('\n이야기 형식으로 클래스 기초 쌓기\n')


class Service:
    secret = "영구는 배꼽이 두 개다."


pey = Service()

pey.secret

# 클래스 함수

print("\n클래스 함수\n")


class Service:
    secret = "영구는 배꼽이 두 개다."

    def sum(self, a, b):
        result = a + b
        print("%s+%s=%s입니다." % (a, b, result))


pey = Service()
pey.sum(1, 1)

# self 간단히 살펴보기

print("\nself 간단히 살펴보기\n")


def sum(self, a, b):
    result = a + b
    print("%s+%s=%s입니다." % (a, b, result))


pey = Service()
pey.sum(1, 1)

# pey.sum(pey, 1, 1)

# self 제대로 알기
# self는 클래스 자기자신을 참조하는 것(Reference)을 의미한다. → 객체 참조

print("self 제대로 알기")

# class Service:
#     secret = "영구는 배꼽이 두 개다"
#
#     def setname(self, name):
#         self.name = name
#
#     def sum(self, a, b):
#         result = a + b
#         print("%s님 %s + %s = %s입니다." % (self.name, a, b, result))
#
#
# pey = Service()
# pey.setname("홍길동")

# __init__ 이란 무엇인가?
#  클래스의 초기화를 담당한다.
# 인스턴스를 만들 때 항상 실행된다.

print("\n__init__이란 무엇인가?\n")


class Service:
    secret = "영구는 배꼽이 두 개다."

    def __init__(self, name):
        self.name = name

    def sum(self, a, b):
        result = a + b
        print("%s님 %s+%s=%s입니다." % (self.name, a, b, result))


pey = Service("홍길동")
pey.sum(1, 1)

# 클래스 자세히 알기
# 클래스는 인스턴스를 만들어내는 공장과 같다.
# 클래스는 해당 인스턴스의 청사진이다.

print("\n클래스 자세히 알기\n")

# 클래스의 구조

print("\n클래스의 구조\n")

# class 클래스 이름[(상속 클래스명)]:
#   <클래스 변수1>
#   <클래스 변수2>
#   <클래스 변수n>
#   def 클래스 함수1(self[, 인수1,인수2,,,]):
#       <수행할 문장1>
#       <수행할 문장2>
#       <수행할 문장n>
#   def 클래스 함수2(self[, 인수1,인수2,,,]):
#       <수행할 문장1>
#       <수행할 문장2>
#       <수행할 문장n>
#   def 클래스 함수n(self[, 인수1,인수2,,,]):
#       <수행할 문장1>
#       <수행할 문장2>
#       <수행할 문장n>

# 사칙연산 클래스 만들기
# +, - , *, /

print("\n사칙연산 클래스 만들기\n")

# 클래스를 어떻게 만들지 먼저 구상하기

# 클래스 구조 만들기

print("\n클래스 구조 만들기\n")


class FourCal:
    pass


a = FourCal()
type(a)
print(type(a))

# 객체에 숫자 지정할 수 있게 만들기

print("\n객체에 숫자 지정할 수 있게 만들기\n")


class FourCal:
    def setdata(self, first, second):  # 함수의 입력 인수 self : 객체, first : 4, second : 2
        self.first = first
        self.second = second


a = FourCal()
a.setdata(4, 2)

# 메서드의 또다른 호출 방법

FourCal.setdata(a, 4, 2)


class FourCal:
    def setdata(self, first, second):
        self.first = first
        self.second = second


# 더하기 기능 만들기

print("\n더하기 기능 만들기\n")


class FourCal:
    def setdata(self, first, second):
        self.first = first
        self.second = second

    def sum(self):
        result = self.first + self.second
        return result


a = FourCal()
a.setdata(4, 2)
a.sum()
print(a.sum())

# 곱하기, 빼기, 나누기 기능 만들기

print("\n곱하기, 빼기, 나누기 기능 만들기\n")


class FourCal:
    def setdata(self, first, second):
        self.first = first
        self.second = second

    def sum(self):
        result = self.first + self.second
        return result

    def mul(self):
        result = self.first * self.second
        return result

    def sub(self):
        result = self.first - self.second
        return result

    def div(self):
        result = self.first / self.second
        return result


a = FourCal()
b = FourCal()
a.setdata(4, 2)
b.setdata(3, 7)

print(a.sum())
print(a.mul())
print(a.sub())
print(a.div())

print(b.sum())
print(b.mul())
print(b.sub())
print(b.div())

# '박씨네 집' 클래스 만들기

print("\n박씨네 집 클래스 만들기\n")


# 클래스 구상하기

# 클래스 기능 만들기

class HousePark:
    lastname = "박"

    def setname(self, name):
        self.fullname = self.lastname + name

    def travel(self, where):
        self.where = where
        print("%s, %s에 여행을 가다." % (self.fullname, where))


pey = HousePark()
pey.setname("응용")
pey.travel("부산")


# 초깃값 설정하기

# pey = HousePark()
# pey.travel("부산")

# __init__ 함수로 초깃값을 설정한다.

class HousePark:
    lastname = "박"

    def __init__(self, name):
        self.fullname = self.lastname + name

    def travel(self, where):
        print("%s, %s에 여행을 가다." % (self.fullname, where))


pey = HousePark("응용")
pey.travel("태국")


# 클래스 상속(class 상속받을 클래스명(상속할 클래스명))

class HouseKim(HousePark):
    lastname = "김"


juliet = HouseKim("줄리엣")
juliet.travel("독도")


# 함수 오버라이딩(매서드 오버라이딩)

class HouseKim(HousePark):
    lastname = "김"

    def travel(self, where, day):
        print("%s, %s에 여행을 %d일 가다." % (self.fullname, where, day))


juliet = HouseKim("줄리엣")
juliet.travel("독도", 3)


# 연산자 오버로딩


class HousePark:
    lastname = "박"

    def __init__(self, name):
        self.fullname = self.lastname + name

    def travel(self, where):
        print("%s, %s에 여행을 가다." % (self.fullname, where))

    def love(self, other):
        print("%s, %s 사랑에 빠졌네" % (self.fullname, other.fullname))

    def __add__(self, other):  # 연산자 오버로딩 사용
        print("%s, %s 결혼했네" % (self.fullname, other.fullname))


class HouseKim(HousePark):
    lastname = "김"

    def travel(self, where, day):
        print("%s, %s에 여행을 %d일 가네" % (self.fullname, where, day))


pey = HousePark("응용")
julet = HouseKim("줄리엣")
pey.love(juliet)
pey + juliet  # pey(self) + juliet(other)


# '박씨네 집' 클래스 완성하기

# 박은용은 부산에 놀러가고
# 김줄리엣도 우연히 3일 동안 부산에 놀러 간다.
# 둘은 사랑에 빠져서 결혼하게 된다.
# 그러다가 바로 싸우고 이혼을 하게 된다.

class HousePark:
    lastname = "박"

    def __init__(self, name):
        self.fullname = self.lastname + name

    def travel(self, where):
        print("%s, %s에 여행을 가다." % (self.fullname, where))

    def love(self, other):
        print("%s, %s 사랑에 빠졌네" % (self.fullname, other.fullname))
    def fight(self,other):
        print("%s, %s 싸우네" % (self.fullname, other.fullname))
    def __add__(self, other):  # 연산자 오버로딩 사용
        print("%s, %s 결혼했네" % (self.fullname, other.fullname))

    def __sub__(self, other):
        print("%s, %s 이혼했네" % (self.fullname, other.fullname))


class HouseKim(HousePark):
    lastname = "김"

    def travel(self, where, day):
        print("%s, %s에 여행을 %d일 가네" % (self.fullname, where, day))


pey = HousePark("응용")
juliet = HouseKim("줄리엣")
pey.travel("부산")
juliet.travel("부산",3)
pey.love(juliet)
pey.fight(juliet)
pey + juliet
pey - juliet
