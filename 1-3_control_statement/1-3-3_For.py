# for문

# for문의 기본 구조

# for 변수 in 리스트(또는 튜플, 문자열):
#   수행할 문장1
#   수행할 문장2

# 예제를 이용해 for문 이해하기

print('\n예제를 이용해 for문 이해하기\n')

# 1. 전형적인 for문

print('\n1. 전형적인 for문\n')

test_list = ['one', 'two', 'three']
for i in test_list:  # 'one','two','three'를 순서대로 i에 대입
    print(i)

# 2. 다양한 for문의 사용

print('\n2. 다양한 for문의 사용\n')

a = [(1, 2), (3, 4), (5, 6)]
for (first, last) in a:
    print(first + last)

# 3. for문의 응용

print('\n3. for문의 응용\n')

# "총 5명의 학생이 시험을 보아는데 시험 점수가 60점이 넘으면 합격이고 그렇지 않으면 불합격이다. 합격인지 불합격인지 결과를 보여주시오."

student_score = [90, 25, 67, 45, 80]  # 학생들의 시험 점수 리스트
student_number = 0  # 학생에게 붙여줄 번호
for score in student_score:  # 90,25,67,45,80를 순서대로 대입
    student_number += 1
    if score >= 60:
        print("%d번 학생은 합격입니다." % student_number)
    else:
        print("%d번 학생은 불합격입니다." % student_number)

# for문과 continue
#  for문 안의 문장을 수행하는 도중에 continue문을 만나게 되면 for문의 처음으로 돌아가게 된다.

print('\nfor문과 continue\n')

student_score = [90, 25, 67, 45, 80]  # 학생들의 시험 점수 리스트
student_number = 0  # 학생에게 붙여줄 번호
for score in student_score:
    student_number += 1
    if score < 60: continue
    print("%d번 학생 축하합니다. 합격입니다." % student_number)

# for와 함께 자주 사용하는 range 함수

print("\nfor문과 함께 자주 사용하는 range 함수\n")
a = range(10)  # range(10)은 0부터 10미만의 숫자를 포함하는 range 객체를 만들어준다.
print(a)  # 0,1,2,3,4,5,6,7,8,9

a = range(1, 11)
print(a)  # 1,2,3,4,5,6,7,8,9,10

# range 함수의 예시 살펴보기

print('\nrange 함수의 예시 살펴보기\n')

sum = 0
for i in range(1, 11):
    sum += 1
    print(sum)

student_score = [90, 25, 67, 45, 80]
for number in range(len(student_score)):  # len 함수는 리스트 내 요소의 개수를 리턴하는 함수이다.
    if student_score[number] < 60: continue  # 점수가 60점미만이면 맨 처음으로 돌아간다.
    print("%d번 학생 축하합니다. 합격입니다." % (number + 1))

# for와 range를 이용한 구구단

print('\nfor와 range를 이용한 구구단\n')

for i in range(2, 10):
    for j in range(1, 10):
        print(i * j, end=" ")  # 입력 인수 end는 해당 결과값을 출력할 때 다음 줄로 넘기지 않고 그 줄에 계속해서 출력한다.
    print('')

# 리스트 안에 for문 포함하기

print('\n리스트 안에 for문 포함하기\n')

a = [1, 2, 3, 4]
result = []
for num in a:
    result.append(num * 3)
print(result)

result = [num * 3 for num in a]
print(result)

resul = [num * 3 for num in a if num % 2 == 0]
print(result)

# 리스트 내포의 일반적인 문법

# [표현식 for 항목 in 반복 가능한 객체 if 조건]

# 리스트 내포의 이중for문 사용

# [표현식 for 항목1 in 반복 가능한 객체1 if 조건1
#   for 항목2 in 반복 가능한 객체2 if 조건2
#   for 항목n in 반복 가능한 객체n if 조건n

result = [x * y for x in range(2, 10)
          for y in range(1, 10)]
print(result)
