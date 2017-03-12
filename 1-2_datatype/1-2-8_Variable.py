#자료형의 값을 저장하는 공간, 변수

a = 1
b = "python"
c = [1,2,3]

#변수를 만들 때는 위의 예처럼 =(assignment) 기호를 사용한다.

#변수명 = 변수에 저장할 값

#변수란?

a = 3

# a는 변수의 이름, 3는 정수형 객체가 저장된 메모리 위치를 가르킨다.
# 변수 a는 객체가 저장된 메모리의 위치를 가리키는 레퍼런스(Reference)라고도 할 수 있다.

a.real
print(a.real) # <class 'int>

a = 3
b = 3

a is b # a와 b가 동일한 객체를 가리키는 지 판단
print(a is b)

#a,b,c는 정말 같은 객체를 가리키는 걸까?

import sys
sys.getrefcount(3)

a = 3
print(sys.getrefcount(3))

b = 3
print(sys.getrefcount(3))

c = 3
print(sys.getrefcount(3))

#변수를 만드는 여러가지 방법

print('\n변수를 만드는 여러가지 방법\n')

#튜플(상수정렬형 자료구조)

a,b = ('python', 'life')
(a,b) = 'python','life'

#리스트(삽입정렬형 자료구조)

[a,b] = ['python','life']
a,b = ['python','life']

#여러 개의 변수에 같은 값을 대입
a = b = 'python'

a = 3
b = 5
a, b = b, a
print(a)
print(b)

#메모리에 생성된 변수 없애기

print('\n메모리에 생성된 변수 없애기\n')

a = 3
b = 3
del(a)
del(b)

#리스트를 변수에 넣고 복사하고자 할 때
print('\n리스트를 변수에 넣고 복사하고자 할 때\n')

#Call by reference

print('\nCall by reference\n')

a = [1,2,3]
b = a
a[1] = 4
print(a)
print(b)

#Call by value
#b 변수를 생성할 떄 a와 값은 값을 가지도록 복사해 넣으면서 a가 가리키는 리스트와는 다른 리스트를 가리키게 하는 방법

print('\nCall by value\n')

#1.[:] 이용

print('1.[:] 이용\n')

a = [1,2,3]
b = a[:]
a[1] = 4
print(a)
print(b)


#2.copy 모듈 이용

print('\n2.copy 모듈 이용\n')

from copy import copy
b = copy(a)
b is a
print(b is a)

