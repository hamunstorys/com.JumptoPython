# 튜플 자료형(Tuple)

# 튜플은 어떻게 만드는가?

# 튜플은 리스트는 [ 와 ]로 둘러쌓아 요소를 정의하지만 튜플은 ( 과 )로 둘러싼다.
# 튜플은 리스트와 달리 그 값의 생성만 가능하며, 수정 삭제는 불가능한 상수이다.

t1 = ()
t2 = (1,)
t3 = (1, 2, 3)
t4 = 1, 2, 3
t5 = ('a', 'b', ('ab', 'cd'))

# 튜플의 요소값을 지우거나 변경하려고 하면 어떻게 될까?

print('\n튜플의 요소값을 지우거나 변경하려고 하면 어떻게 될까?\n')

# 1.튜플 요소값 삭제 시 오류
# 튜플의 요소를 리스트처럼 del 함수로 지우려고 할 떄 튜플은 요소를 지우는 행위가 지원되지 않는다는 메세지를 확인할 수 있다.

# 2.튜플 요소값 변경 시 오류
# 튜플의 요소값을 변경하려고 해도 마찬가지로 오류가 발생한다.

# 튜플의 인덱싱과 슬라이싱 더하기(+), 곱하기(*)

print('\n튜플의 인덱싱과 슬라이싱, 더하기(+), 곱하기(*)')

# 1. 인덱싱하기

print('\n1. 인덱싱하기\n')

t1 = (1,2,'a','b')
t1[0]
print(t1[0])
t1[3]
print(t1[3])

#2. 슬라이싱하기

print('\n2. 슬라이싱하기\n')

t1 = (1,2,'a','b')
t1[1:]
print(t1[1:])

#3.튜플 더하기

print('\n3. 튜플 더하기\n')

t2 = (3,4)
t1 + t2
print(t1+t2)

#4.튜플 곱하기

print('\n4. 튜플 곱하기\n')

t2*3
print(t2*3)
