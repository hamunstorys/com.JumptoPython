# 하위 디렉터리 검색하기

# 특정 디렉터리부터 시작해서 그 하위의 모든 파일 중 파이썬 파일(*.py)만 출력해 주는 프로그램을 만들려면 어떻게 해야할까?

# D:\Workspace\Python\sub_dir_search.py

# 1. sub_dir_search.py 파일 작성

def search(dirname):
    print(dirname)


print(search("D:\Workspace"))

# 2. 디렉터리에 있는 파일들을 검색할 수 있도록 소스를 변경한다.

import os


def search(dirname):
    filenames = os.listdir(dirname)
    for filename in filenames:
        full_filename = os.path.join(dirname, filename)
        print(full_filename)


search("D:\Workspace\Python")

# 3. D:\Workspace\ 디렉터리에 있는 파일들 중 확장자가 .py인 파일들만을 출력하도록 코드를 변경한다.

# D:\Workspace\Python\sub_dir_search.py

import os


def search(dirname):
    filenames = os.listdir(dirname)
    for filename in filenames:
        full_filename = os.path.join(dirname, filename)
        ext = os.path.splitext(full_filename)[-1]
        if ext == '.py':
            print(full_filename)


search("D:\Workspace")

# 4. D:\Workspace\ 바로 밑에 있는 파일 뿐만 아니라 그 하위 디렉터리(sub directory)를 포함한 모든 파이썬 파일들을 검색하는 것이다. 하위 디렉터리도 검색이 가능하게 하기 위해서는 다음과 같이 코드를 변경해야한다.

import os


def search(dirname):
    try:
        filenames = os.listdir(dirname)
        for filename in filenames:
            full_filename = os.path.join(dirname, filename)
        if os.path.isdir(full_filename):
            search(full_filename)
        else:
            ext = os.path.splitext(full_filename)[-1]
            if ext == '.py':
                print(full_filename)
    except PermissionError:
        pass


search("D:\Workspace")

# 하위 디렉터리 검색을 쉽게 해주는 os.walk
# 시작 디렉터리부터 시작하여 그 하위의 모든 디렉터리를 차례대로 방문하게 해주는 함수이다.

import os

for (path, dir, files) in os.walk("D:\Worksapce"):
    for filename in files:
        ext = os.path.splitext(filename)[-1]
        if ext == '.py':
            print("%s%s" % (path, filename))
