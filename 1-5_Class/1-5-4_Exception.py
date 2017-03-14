# 예외 처리

# 오류는 어떤 때 발생하는 가?

# FileNotFoundError
# 디렉토리 안에 없는 파일을 열려고 시도했을 때 발생하는 오류

# ZeroDivisionError
# 숫자 타입의 자료를 0으로 나누려고 시도했을 때 발생하는 오류

# IndexError
# 리스트 혹은 튜플 등의 인덱싱이 가능한 자료형에서 인덱싱할 수 없는 값을 참조하려할 때 발생하는 오류

# 오류 예외 처리 기법

# try, except문

# try:
#   ...
# ecept[발생 오류[as 오류메세지 변수]]:
#   ...

# ecept[발생 오류[as 오류 메세지 변수]]:

# 1. try,except만 쓰는 방법
# 이 경우는 오류 종류에 상관없이 오류가 발생하기만 하면 except 블록을 수행한다.


# try:
#   ...
# excpt:
#   ...

# 2. 발생 오류만 포함한 except문
# 이 경우는 오류가 발생했을 때 except문에 미리 정해 놓은 오류 이름과 일치 할 때만 except 블록을 수행한다는 뜻이다.

# 3. 발생 오류와 오류 메세지 변수까지 포함한 except문
# 이 경우는 두 번째 경우에서 오류 메세지의 내용까지 알고 싶을 떄 사용하는 방법이다.

try:
    4 / 0
except ZeroDivisionError as e:
    print(e)

# try ..else
# try문은 else절을 지원한다. else절은 예외가 발생하지 않은 경우에 실행되며 반드시 except절 바로 다음에 위치해야 한다.

if __name__ == '__main__':
    try:
        f = open('foo.txt', 'r')
    except FileNotFoundError as e:
        print(str(e))
    else:
        data = f.read()
        f.close()

# try..finally
# try문에는 finally절을 사용할 수 있다. finally절은 try문 수행 도중 예외 발생 여부에 상관없이 항상 수행된다. 보통 finally절은 사용한 리소스를 close해야 할 경우에 많이 사용된다

f = open('foo.txt', 'w')
try:
    print("무언가를 수행한다.")
finally:
    f.close()

# foo.txt라는 파일을 쓰기 모드로 연 후에 try문이 수행된 후 예외 발생 여부에 상관없이 finally절에서 f.close()로 열린 파일을 닫을 수 있다.

# 오류 회피하기
# 프로그래밍을 하다 보면 특정 오류가 발생할 경우 그냥 통과시켜야 할 떄가 있을 수 있다. 다음의 예를 보자.

try:
    f = open("나없는파일", 'r')
except FileNotFoundError:  # 팡리이 없더라도 오류를 발생시키지 않고 통과한다.
    pass


# 오류 일부러 발생시키기(raise 명령어)

class Bird:
    def fly(self):
        pass


# raise NotImplementedError  NotimplementedError는 파이썬 내장 오류로, 꼭 작성해야 하는 부분이 구현되지 않을 경우 일부러 오류를 발생시키고자 사용한다.


# class Eagle(Bird):
#     pass

class Eagle(Bird):
    def fly(self):
        print("very fast")


eagle = Eagle()
eagle.fly()
