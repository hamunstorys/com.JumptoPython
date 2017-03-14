# 모듈(Module)

# 모듈 만들고 불러오기
# 모듈 불러오기 : import 모듈 이름

import mod1

print(mod1.sum(3, 4))
print(mod1.safe_sum(3, 4))
print(mod1.safe_sum(3, 'a'))
print(mod1.sum(10, 20))

# 모듈 함수를 사용하는 또 다른 방법

# from 모듈이름 import 모듈 함수

from mod1 import sum

sum(3, 4)
print(sum(3, 4))

from mod1 import sum, safe_sum

sum(3, 4)
safe_sum(3, 4)

from mod1 import *

sum(3, 4)
safe_sum(3, 4)

# if __name__ =="__main__":의 의미
# if__name_=="__main__"을 사용하면 직접 이 파일을 실행시켰을 때는 __name__=="__main__" 참이 되어 if문 다음 문장들이 수행된다.
# 반대로 대화형 인터프리터나 다른 파일에서 이 모듈을 불러서 사용할 떄는 __name__=="__main__"이 거짓이 되어 if문 다음 문장들이 수행되지 않는다.

# 클래스나 변수 등을 포함한 모듈

import mod2

# 모듈에 포함된 변수, 클래스, 함수 사용하기

print(mod2.PI)

a = mod2.Math()
print(a.solv(2))

# 새 파일 안에서 이전에 만든 모듈 불러오기

result = mod2.sum(mod2.PI, 4.4)  # mod2.py 파일의 sum 함수 호출
print(result)  # sum 함수의 결과값 출력

# 모듈을 불러오는 또 다른 방법

# 1.sys.path.append(모듈을 저장한 디렉터리) 사용하기

# sys 모듈은 파이썬을 설치할 때 함께 설치되는 라이브러리 모듈이다.
import sys

# sys.path는 파이썬 라이브러리들이 설치되어 있는 디렉터리들을 보여준다.
# ['D:\\Workspace\\Python\\com.JumptoPython\\1-5_Class', 'D:\\Workspace\\Python\\com.JumptoPython', 'D:\\Develoment_tool_kits\\python\\python3.6\\python36.zip', 'D:\\Develoment_tool_kits\\python\\python3.6\\DLLs', 'D:\\Develoment_tool_kits\\python\\python3.6\\lib', 'D:\\Develoment_tool_kits\\python\\python3.6', 'D:\\Develoment_tool_kits\\python\\python3.6\\lib\\site-packages']

sys.path
print(sys.path)

# 만약 파이썬 모듈이 위의 디렉터리에 들어 있다면 모듈이 저장된 디렉터리로 이동할 필요 없이 바로 불러서 사용할 수가 있다.
# 그렇다면 sys.path에 D:\Workspace\Python\Mymodules라는 디렉터리를 추가하면 아무데서나 사용할 수 있지 않을 까?

sys.path.append("D:\Python\com.JumptoPython\1-5_Class\Mymodules")
print(sys.path)

print(mod2.sum(3, 4))

# 2.PYTHONPATH 환경 변수 사용하기

# 모듈을 불러와서 사용하는 또 다른 방법으로는 PYTHONPATH 환경 변수를 사용하는 방법이 있다.

# 다음과 같이 따라 해보자.

# C:\Users\home>set PYTHONPATH=C:\Python\Mymodules
# C:\Users\home>python
# Python 3.5.1 (v3.5.1:37a07cee5969, Dec 6 2015, 01:54:25) [MSC v.1900 64 bit (AM...
# Type "help", "copyright", "credits" or "license" for more information.
# >>> import mod2
# >>> print(mod2.sum(3,4))
# 7
# set 도스 명령어를 이용해 PYTHONPATH 환경 변수에 mod2.py 파일이 있는 C:\Python\Mymodules 디렉터리를 설정한다. 그러면 디렉터리 이동이나 별도의 모듈 추가 작업 없이 mod2 모듈을 불러와서 사용할 수 있다.
