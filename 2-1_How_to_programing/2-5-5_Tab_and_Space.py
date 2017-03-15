# 탭을 4개의 공백으로 바꾸기

# C:\Python/tabto4.py

# python tabto4.py a.txt b.txt


# 1.파일 작성

import sys

src = sys.argv[1]
dst = sys.argv[2]

# 2.출력확인

# C:\Python>python tabto4.py a.txt b.txt

# 3. 테스트를 위한 원본 파일 a.txt를 다음가 같이 작성한다. 각 단어들은 탭으로 분리되도록 입력

# Life   is  too short
# You    need    python

# 4. 이제 탭 문자를 포함한 a.txt 파일을 읽어서 탭을 공백 4개로 변환할 수 있도록 코드를 변경한다.

# C:\Python\tabto4.py
import sys

src = src.argv[1]
dst = sys.argv[2]

f = open(src)
tab_content = f.read()
f.close()

space_content = tab_content.replace("\t", " " * 4)
print(space_content)

# 5. tabto4.py를 위와 같이 변경한 후 다음과 같은 명령을 수행한다.

# C:\Python>python tabto4.py a.txt b.txt

# 6. 이제 변경된 내용을 b.txt 파일에 저장할 수 이도록 다음과 같이 프로그램을 변경한다.

import sys

src = sys.argv[1]
dst = sys.argv[2]

f = open(src)
tab_content = f.read()
f.close()
space_content = tab_content.replace("\t", " " * 4)

f = open(dst, 'w')
f.write(space_content)
f.close()

# 7.프로그램을 실행하기 위해 다음과 같은 명령을 수행한다.

# C:\Python>python tabto4.py a.txt b.txt
