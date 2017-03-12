# 집합 자료형(set)
# 집합(set)은 파이썬 2.3부터 지원되기 시작한 자료형으로, 집합에 관련된 것들을 쉽게 처리하기 위해 만들어진 자료형이다.

# 집합 자료형은 다음과 같이 set 키워드를 이용해 만들 수 있다.

print('\n집합 자료형 만드는 법\n')

s1 = set([1, 2, 3])
print(s1)

s2 = set("Hello")
print(s2)  # {'e', 'l', 'o', 'H'}

# 집합 자료형의 특징
# 1. 중복을 허용하지 않는다.
# 2. 순서가 없다.(Unordered)

# set 자료형은 순서가 없기 떄문에 인덱싱으로 값을 얻을 수 없다.
# set 자료형에 저장된 값을 인덱싱으로 접근하려면 다음과 같이 리스트나 튜플로 변환한 후 해야한다.

print()

s1 = set([1, 2, 3])
l1 = list(s1)  # 리스트로 변환
print(l1)
print(l1[0])

t1 = tuple(s1)
print(t1)
print(t1[0])

# 집합 자료형 활용하는 방법

print('\n집합 자료형 활용하는 방법')

# 교집합, 합집합, 차집합 구하기

print('\n교집합, 합집합, 차집합 구하기\n')

s1 = set([1, 2, 3, 4, 5, 6])
s2 = set([4, 5, 6, 7, 8, 9])

# 1. 교집합(&) 혹은 intersection 함수

print('\n교집합(&) 혹은 intersection 함수\n')

s1 & s2
print(s1 & s2)  # {4,5,6}

# s2.intersection(s1)을 해도 결과는 같다.
s1.intersection(s2)
print(s1.intersection(s2))  # {4,5,6}

# 2. 합집합(| 혹은 union 함수)

print('\n합집합(| 혹은 union 함수)\n')

s1 | s2
print(s1 | s2)  # { 1,2,3,4,5,6,7,8,9 }

s1.union(s2)
print(s1.union(s2))  # { 1,2,3,4,5,6,7,8,9 }

# 3. 차집합(- 혹은 difference 함수)

print('\n3. 차집합(- 혹은 difference 함수)\n')

s1 - s2
print(s1 - s2)  # {1,2,3}

s1.difference(s2)
print(s1.difference(s2))  # {1,2,3}

#집합 자료형 관련 함수들

print('\n집합 자료형 관련 함수들\n')

#값 1개 추가하기(add)
#이미 만들어진 set 자료형에 값을 추가할 수 있다. 1개의 값만 추가(add)할 경우에는 아래와 같이 한다.

print('\n값 1개 추가하기(add)\n')

s1 = set([1,2,3])
s1.add(4)
print(s1)

#값 여러 개 추가하기(update)

print('\n값 여러 개 추가하기(update)\n')

s1 = set([1,2,3])
s1.update([4,5,6])
print(s1)

#특정 값 제거하기(remove)

print('\n특정 값 제거하기(remove)\n')

s1 = set([1,2,3])
s1.remove(2)
print(s1)