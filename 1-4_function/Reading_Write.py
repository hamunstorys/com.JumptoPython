# 파일 읽고 쓰기

print('\n파일 읽고 쓰기\n')

# 파일 생성하기

print('\n파일 생성하기\n')

f = open("새파일.txt", 'w')
f.close()

# 파일 객체 = open(파일 이름, 파일 열기 모드)

# 파일 열기 모드
# r : 읽기 모드 - 파일을 읽기만 할때 사용
# w : 쓰기 모드 - 파일에 내용을 쓸 때 사용
# a : 추가 모드 - 파일의 마지막에 새로운 내용을 추가할 때 사용

# 파일을 쓰기 모드로 열어 출력값 적기

print("\n파일을 쓰기 모드로 열어 출력값 적기\n")

f = open("새파일.txt", 'w')
for i in range(1, 11):
    data = "%d번쨰 줄입니다.\n" % i
    f.write(data)
f.close()

# for i in range(1, 11):
#     date = "%d번째 줄입니다.\n " % i
#     print(data)

# 프로그램의 외부에 저장된 파일을 읽는 여러 가지 방법

print("\n프로그램의 외부에 저장된 파일을 읽는 여러 가지 방법\n")

# readline() 함수 이용하기
# 파일의 첫 번째 줄을 읽어 출력하는 함수

print("\nreadline() 함수 이용하기\n")

f = open("새파일.txt", "r")
line = f.readline()
print(line)
f.close()

f = open("새파일.txt", "r")
while True:
    line = f.readline()
    if not line: break
    print(line)
f.close()

while 1:
    data = input()
    if not data: break
    print(data)

# readlines() 함수 이용하기
# 파일의 모든 라인을 읽어서 각각의 줄을 요소로 갖는 리스트로 리턴

print("\nreadlines() 함수 이용하기\n")

f = open("새파일.txt", 'r')
lines = f.readlines()
for line in lines:
    print(line)
f.close()

# read() 함수 이용하기
# 파일의 내용 전체를 문자열로 리턴하는 함수

print("\nread()함수 이용하기\n")

f = open("새파일.txt", "r")
data = f.read()
print(data)
f.close()

# 파일에 새로운 내용 추가하기
# 원래 가지고 있던 내용 바로 다음부터 결과값을 적기 시작한다.

print("\n파일에 새로운 내용 추가하기\n")

f = open("새파일.txt", 'a')
for i in range(11, 20):
    data = "%d번째 줄입니다.\n" % i
    f.write(data)
f.close()

# with문과 함께 사용하기

f = open("foo.txt", "w")
f.write("Life is too short, you need python")
f.close()

with open("foo.txt", "w") as f:
    f.write("Life is too short, you nedd python")
