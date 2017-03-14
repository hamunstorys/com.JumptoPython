# 외장 함수

# sys
# sys 모듈은 파이썬 인터프리터가 제공하는 변수들과 함수들을 직접 제어할 수 있게 해주는 모듈이다.

# 명령 행에서 인수 전달하기 - sys.argv
# C:/User/home>python test.py abc pey guido

# 강제로 스크립트 종료하기 - sys.exit
# sys.exit()

# 자신이 만든 모듈 불러와 사용하기
# sys.payh는 파이썬 모듈들이 저장되어 이는 위치를 나타낸다.
# sys.path

# pickle
# pickle은 객체의 형태를 그대로 유지하면서 파일에 저장하고 불러올 수 있게 하는 모듈이다.

import pickle

f = open("test.txt", 'wb')
data = {1: 'python', 2: 'you need'}
pickle.dump(data, f)
f.close()

import pickle

f = open("test.txt", 'rb')
data = pickle.load(f)
print(data)

# OS 모듈
# OS 모듈은 환경 변수나 디렉터리, 파일 등의 OS 자원을 제어할 수 있게 해주는 모듈이다.

# 내 시스템의 환경 변수값을 알고 싶을 때 - os.environ
# 시스템은 제각기 다른 환경 변수값을 가지고 있는데, os.environ은 현재 시스템의 환경 변수 값들을 보여준다.

import os

os.environ
print(os.environ)

# 디렉터리 위치 변경하기 - os.chdir
# os.chdir을 이용하면 아래와 같이 현재 디렉터리의 위치를 변경할 수 있다.

os.chdir("C:\Windows")

# 디렉터리 위치 리턴받기 - os.getcwd
# os.getcwd는 현재 자신의 디렉터리 위치를 리턴한다.

os.getcwd()
print(os.getcwd())

# 시스템 명령어 호출하기 - os.system
# 시스템 자체의 프로그램이나 기타 명령어들을 파이썬에서 호출할 수도 있다. os.system("명령어")처럼 사용한다.

os.system("dir")

# 실행한 시스템 명령어의 결과값 리턴받기 - os.popen
# os.popen은 시스템 명령어를 시스템 명령어를 실행시킨 결과값을 읽기 모드 형태의 파일 객체로 리턴한다.

f = os.popen("dir")
print(f.read())

# 기타 유용한 os 관련 함수

# os.mkdir(디렉터리) : 디렉터리를 생성한다.
# os.rmdir(디렉터리) : 디렉터리를 삭제한다. 단, 디렉터리가 비어 이어야 삭제가 가능하다.
# os.unlink(파일 이름) : 파일을 지운다
# os.rename(src,dst) :src라는 이름의 파일을 dst라는 이름으로 바꾼다.

# shutil → Python 3.6.0 아래 방법으로 실행 되지 않는다.
# shutil은 파일을 복사해 주는 파이썬 모듈이다.

# 파일 복사하기 -shutil.copy(src, dst)
# src라는 이름의 파일을 dst로 보가한다. 만약 dst가 디렉터리 이름이라면 src라는 파일 이름으로 dst라는 디렉터리에 복사하고 동일한 파일 이름이 있을 경우에는 덮어쓴다.

# glob
# 가끔 파일을 읽고 ㅡ는 기능이 있는 프로그램을 만들다 보면 특정 디렉터리에 있는 파일 이름 모두를 알아야 할 때가 있다. 이럴 때 사용하는 모듈이 바로 glob이다.

# 디렉터리에 있는 파일들을 리스트로 만들기 - glob(pathname)
# glob 모듈은 디렉터리 내의 파일들을 읽어서 리턴한다. *,? 등의 메타 문자를 써서 원하는 파일만 읽어 들일 수 있다.

import glob

glob.glob("C:/Python/q*")

# tempfile
# 파일을 임시로 만들어서 사용할 때 유용한 모듈이 바로 tempfile이다 tempfile.mktemp()는 중복되지 않는 임시 파일의 이름을 무작위로 만들어서 리턴한다.

import tempfile

filename = tempfile.mktemp()
print(filename)

# tempfile.TemporaryFile()은 임시 저장 공간으로 사용될 파일 객체를 리턴한다. 이 파일은 기본적으로 바이너리 쓰기 모드(wb)를 갖는다. f.close()가 호출되면 이 파일 객체는 자동으로 사라진다.

import tempfile

f = tempfile.TemporaryFile()
f.close()  # 생성한 임시 파일이 자동으로 삭제됨

# time
# 시간과 관련된 유용한 함수가 굉장히 많다.

# time.time
# time.time()은 UTC를 이용하여 현재 시간을 실수 형태로 리턴하는 함수이다. 1970년 1월 1일 0시 00분 0초를 기준으로 지난 시간을 초단위로 리턴한다.

import time

time.time()
print(time.time())

# time.localtime
# time.localtime은 time.time()에 의해서 변한된 실수값을 이용해서 연도, 달, 월, 시, 분, 초,...의 형태로 바꾸어 주는 함수이다.

time.localtime(time.time())
print(time.localtime(time.time()))

# time.asctime
# time.asctime은 위의 time.localtime에 의해서 반환된 튜플 형태의 값을 인수로 받아서 날짜와 시간을 알아보기 쉬운 형태로 리턴하는 함수이다.

time.asctime(time.localtime(time.time()))
print(time.asctime(time.localtime(time.time())))

# time.ctime
# time.asctime(time.localtime(ime.time()))은 time.ctime()을 이용해 간편하게 표시할 수 있다. asctime과 다른 점은 ctime은 항상 현재 시간만을 리턴한다는 점이다.

time.ctime()

# time.strtime('출력할 형식 포맷 코드', time.localtime(time.time()))
# strftime 함수는 시간에 관계된 것을 세밀하게 표현할 수 있는 여러 가지 포맷 코드를 제공한다.

time.strftime('%x', time.localtime(time.time()))
print(time.strftime('%x', time.localtime(time.time())))
time.strftime('%c', time.localtime(time.time()))
print(time.strftime('%c', time.localtime(time.time())))

# time.sleep
# time.sleep 함수는 주로 루프 안에서 많이 사용된다. 이 함수를 사용하면 일정한 시간 간격을 두고 루프를 실행할 수 있다.

# for i in range(10):
#     print(i)
#     time.sleep(1)  # 실수 형태로도 함수의 인수 입력 가능

# calendar
# calendar는 파이썬에서 달력을 볼 수 이게 해주는 모듈이다.

# calendar.calendar(연도)로 사용하면 그 해의 전체 달력을 볼 수 있다. 결과값은 달력이 너무 길어 생략하겠다.

import calendar

print(calendar.calendar(2017))

# calendar.calendar(연도)를 사용해도 위와 똑같은 같이 출력된다.

calendar.calendar(2017)

# 다음의 예는 2015년 12월의 달력만 보여준다.

calendar.prmonth(2015, 12)

# calendar.weekday
# calendar 모듈의 또 다른 유용한 함수를 보자. weekday(연도, 월, 일) 함수는 그 날짜에 해당하는 요일 정보를 리턴한다.
# 월요일은 0, 화요일 1, 수요일 2, 목요일 3, 금요일 4, 토요일 5, 일요일 6

calendar.weekday(2015, 12, 31)
print(calendar.weekday(2015, 12, 31))

# calendar.monthrange
# monthrage(연도, 월)함수는 입력받은 달의 1일이 무슨 요일인지와 그 달이 며칠까지 있는 지를 튜플 형태로 리턴한다.

calendar.monthrange(2015, 12)
print(calendar.monthrange(2015, 12))

# random
# random은 난수(규칙이 없는 임의의 수)를 발생시키는 모듈이다. random과 randint에 대해서 알아본다.

import random

random.random()
print(random.random())

random.randint(1, 10)
print(random.randint(1, 10))

random.randint(1, 55)
print(random.randint(1, 55))

import random


def random_pop(data):
    number = random.randint(0, len(data) - 1)
    return data.pop(number)


if __name__ == "__main__":
    data = [1, 2, 3, 4, 5]
    while data: print(random_pop(data))

# random.choice 함수는 입력으로 받은 리스트에서 무작위로 하나를 선택하여 리턴한다.

if __name__ == '__main__':
    def random_pop(data):
        number = random.choice(data)
        data.remove(number)
        return number

# 리스트의 항목을 무작위로 섞고 싶을 때는 random.shuffle 함수를 이용하면 된다

data = [1, 2, 3, 4, 5]
random.shuffle(data)
print(data)

# webbrowser
# webbrowser는 자신의 시스템에서 사용하는 기본 웹 브라우저가 자동으로 실행되게 하는 모듈이다. 아래의 예제는 웹 브라우저를 자동으로 실행시키고 해당 URL인 http://google.com으로 가게 해준다.

import webbrowser

webbrowser.open("http://google.com")

# webbrowser.open_new는 이미 웹 브라우저가 실행된 상태이더라도 새로운 창으로 해당 주소가 열리도록 한다.

webbrowser.open_new("http://google.com")

# 스레드를 다루는 threading 모듈

import threading
import time


def say(msg):
    while True:
        time.sleep(1)
        print(msg)


for msg in ['you', 'need', 'python']:
    t = threading.Thread(target=say, args=(msg,))
    t.daemon = True
    t.start()

for i in range(100):
    time.sleep(0.1)
    print(i)


class MyThread(threading.Thread):
    def __init__(self, msg):
        self.msg = msg
        self.daemon = True

    def run(self):
        while True:
            time.sleep(1)
            print(self.msg)


for msg in ['you', 'need', 'python']:
    t = MyThread(msg)
    t.start()

for i in range(100):
    time.sleep(0.1)
    print(i)
