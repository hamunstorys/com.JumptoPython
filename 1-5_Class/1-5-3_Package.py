# 패키지(Package)

# 패키지(Packages)는 도트(.)를 이용하여 파이썬 모듈을 계층적(디렉터리 구조)으로 관리할 수 있게 해준다.
# 예를 들어 모듈명이 A,B인 경우 A는 패키지명이 되고 B는 A 패키지의 B 모듈이 된다.

# 가상의 game 패키지 예

# game/
#     __init__.py
#     sound/
#         __init__.py
#         echo.py
#         wav.py
#     graphic/
#         __init__.py
#         screen.py
#         render.py
#     play/
#         __init__.py
#         run.py
#         test.py

# 패키지 만들기

# 패키지 기본 구성 요소 준비하기

# 1. C:/Python이라는 디렉터리 밑에 game 및 기타 서브 디렉터리들을 생성하고 .py 파일들을 다음과 같이 만들어 보자(만약 C:/Python이라는 디렉터리가 없다면 먼저 생성하고 진행하자).

# C:/Python/game/__init__.py
# C:/Python/game/sound/__init__.py
# C:/Python/game/sound/echo.py
# C:/Python/game/graphic/__init__.py
# C:/Python/game/graphic/render.py

# 2. 각 디렉터리에 __init__.py 파일을 만들어 놓기만 하고 내용은 일단 비워 둔다.
#
# 3. echo.py 파일은 다음과 같이 만든다.
#
# # echo.py
# def echo_test():
#     print ("echo")
# 4. render.py 파일은 다음과 같이 만든다.
#
# # render.py
# def render_test():
#     print ("render")
# 5. 다음 예제들을 수행하기 전에 우리가 만든 game 패키지를 참조할 수 있도록 다음과 같이 도스 창에서 set 명령을 이용하여 PYTHONPATH 환경 변수에 C:/Python 디렉터리를 추가한다. 그리고 파이썬 인터프리터(Interactive shell)를 실행하자.
#
# C:\> set PYTHONPATH=C:/Python
# C:\> python
# Python 3.5.1 (v3.5.1:37a07cee5969, Dec 6 2015, 01:54:25) [MSC v.1900 64 bit (AM...
# Type "help", "copyright", "credits" or "license" for more information.
# >>>
# 여기까지 준비가 되었다면 다음을 따라 해본다.


import sys

sys.path.append("D:\Workspace\Python\com.JumptoPython\\1-5_Class")
print(sys.path)

# 패키지 안의 함수 실행하기

import game.sound.echo

game.sound.echo.echo_test()

from game.sound import echo

echo.echo_test()

from game.sound.echo import echo_test

# import game을 수행하면 game 디렉터리의 모듈 또는 game 디렉터리의 __init__.py에 정의된 것들만 참조할 수 있다.
# 포인터 연산자(.)를 사용해서 import a.b.c처럼 import할 때 가장 마지막 항목인 c는 반드시 모듈 또는 패키지여야만 한다.

# __init__.py 의 용도
# __init__.py 파일은 해당 디렉터리가 패키지의 일부임을 알려주는 역할을 한다.
# 만약 game, sound, graphic 등 패키지에 포함된 디렉터리에 __init__.py 파일이 없다면 패키지로 인식되지 않는다.

# __all__의 용도
# __all__이 의미하는 것은 디렉터리 내에서 * 기호를 이용하여 import할 경우 __init__.py 내에 __all__에 정의된 모듈만 import된다는 의미이다.
# __all__ = ['echo']
# Python 3에서는 __all__을 정의하지 않으면 모든 모듈이 import된다.

from game.sound import *

echo.echo_test()

# relative 패키지
# 만약 graphic 디렉터리의 render.py 모듈이 sound 디렉터리의 echo.py 모듈을 사용하고 싶다면 어떻게 해야 할 까?

# . 현재 디렉토리
# .. 부모 디렉토리
