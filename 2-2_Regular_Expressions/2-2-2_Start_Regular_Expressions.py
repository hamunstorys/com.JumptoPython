# 정규 표현식 시작하기

# 정규식이란?
# 복잡한 문자열을 처리할 때 사용하는 기법(문자열의 패턴인식)

# 정규 표현식의 기초, 메타 문자
# 정규 표현식에서 사용하는 메타 문자(meta characters)에는 다음과 같은 것들이 있다.

# 메타 문자란? 원래 그 문자가 가진 뜻이 아닌 특별한 용도로 사용되는 문자를 말한다.
# .^$*+?{[]\|()

# 문자 클래스[]

# 문자 클래스로 만들어진 정규식은 '[ 와 ] 사이의 문자들과 매치'라는 의미를 가진다.
# 정규표현식이 [abc]라면 이 표현식의 의미는 'a,b,c 중 한개의 문자와 매치'를 뜻한다.

#               문자열     매치여부                            설명
#                 a          yes        "a는 정규식과 일치하는 문자인 "a"가 있으므로 매치
# 정규식 [abc]  before       yes        "before"는 정규식과 일치하는 문자인 "b"가 있으므로 매치
#                dude`        no        "dude"는 정규식과 일치하는 문자인 a,b,c 중 어느 하나도 포함하고 있지 않으므로 매치되지 않음

# 정규식의 []안의 두 문자 사이에 하이픈(-)을 사용하게 되면 두 문자 사이의 범위(From - To)를 의미한다.
# [a-zA-Z] : 알파벳 모두
# [0-9] : 숫자

# 문자 클래스 내 ^ 메타 문자가 사용될 경우에는 반대(not)이라는 의미를 갖는다.
# [^0-9]라는 정규 표현식은 숫자가 아닌 문자만 매치된다.

# Dot(.)
# 정규 포현식의 Dot(.) 메타 문자는 줄바꿈 문자인 \n를 제외한 모든 문자와 매치됨을 의미한다.

# a.b a와 b 사이에 줄밖무 문자를 제외한 어떤 문자가 들어가도 모두 매치 = "a + 모든 문자 + b"

#               문자열     매치여부                            설명
#                aab          yes        "aaa"는 가운데 문자 "a"가 모든 문자를 의미하는 .과 일치하므로 정규식과 매치
# 정규식 a.b     a0b          yes        "a0b"는 가운데 문자 "0"이 모든 문자를 의미하는 .과 일치하므로 정규식과 매치
#                abc           no        "abc"는 "a" 문자와 "b" 문자 사이에 어떤 문자라는 하나는 있어야 하는 이 정규식과 일치하지 않으므로 매치되지 않음

# a[.]b a와 b 사이에 Dot(.) 문자가 있으면 매치 = " a + Dot(.)문자 + b "

# 반복

# ca*t * 문자 바로 앞에 있는 a가 0번 이상 반복되면 매치

#               문자열     매치여부                            설명
#                ct         yes        "a"가 0번 반복되어 매치
# 정규식 ca*t    cat        yes        "a"가 0번 이상 반복되어 매치(1번 반복)
#                caat       no         "a"가 0번 이상 반복되어 매치(3번 반복)

# 반복(+)
# 반복을 나타내는 또 다른 메타 문자로 +가 있다. +는 최소 1번 이상 반복될 때 사용한다. 즉, *가 반복 횟수 0부터라면 +는 반복 횟수 1부터인 것이다.

# ca+t 문자 바로 옆에 있는 a가 1번 이상 반복되면 매치 = "c + a(1번 이상 반복) + t"

#               문자열     매치여부                            설명
#                ct         no          "a"가 0번 반복되어 매치되지 않음
# 정규식 ca+t    cat        yes         "a"가 0번 이상 반복되어 매치(1번 반복)
#                caat       yes         "a"가 0번 이상 반복되어 매치(3번 반복)

# 반복({m,n}.?}
# 반복 횟수를 3회만 또는 1회부터 3회까지 제한하고 싶을 때 사용
# {} 메타 문자를 이용하면 반복 횟수를 고정시킬 수 있다.
# {m,n} 정규식을 사용하면 반복 횟수가 m부터 n까지 인것을 매치할 수 있다.

# 1.{m}

# cat{2}t a가 2번 반복되면 매치 = "c + a(반드시 2번 반복) + t"

#               문자열     매치여부                            설명
# 정규식 ca{2}t  cat        no          "a"가 1번만 반복되어 매치되지 않음
#                caat       yes         "a"가 2번 반복되어 매치

# 2. {m,n}

# ca{2,5}t a가 2~5번 반복되면 매치 = "c + a(2~5번 반복) + t"

#                  문자열     매치여부                            설명
# 정규식 ca{2,5}t   cat        no          "a"가 1번만 반복되어 매치되지 않음
#                   caat       yes         "a"가 2번 반복되어 매치
#                 caaaaaat     yes         "a"가 5번 반복되어 매치

# 3. ?
# ? 메타 문자가 의미하는 것은 {0,1}이다.

# ab?c b가 0~1번 사용되면 매치 = "a + b(있어도 되고 없어도 된다) + c"

#                  문자열     매치여부                            설명
# 정규식 ab?c       abc        yes          "b"가 1번만 사용되어 매치
#                   ac         yes          "b"가 0번 사용되어 매치
# 즉, b문자가 있거나 업거나 둘 다 매치되는 경우이다.

# 파이썬에서 정규 표현식을 지원하는 re 모듈

import re

p = re.compile('ab')

# 정규식을 이용한 문자열 검색

#   메서드     목적
#   match()     문자열의 처음부터 정규식과 매치되는지 조사한다.
#   search()    문자열 전체를 검색하여 정규식과 매치되는지 조사한다.
#   findall()   정규식과 매치되는 모든 문자열(substring)을 리스트로 리턴한다.
#   finditer()  정규식과 매치되는 모든 문자열(substring)을 반복 가능한 객체로 리턴한다.

# match, serach는 정규식과 매치될때는 match 객체를 리턴하고, 매치되지 않을 때는 None을 리턴한다.

import re

p = re.compile('[a-z]+')

# match
# match 함수는 문자열의 처음부터 정규식과 매치되는 지 조사한다.

m = p.match("python")
print(m)  # match 객체가 리턴됨

m = p.match("3 python")
print(m)

# p = re.compile(정규 표현식)
# m = p.match("조사할 문자열")
# if m:
#   print('Match found:',m.group())
# else:
#   print('No match')

# search
# 컴파일된 패턴 객체 p를 가지고 이번에는 search 함수를 수행한다.

m = p.search("python")
print(m)

m = p.search("3 python")
print(m)

# findall

result = p.findall("life is too short")
print(result)

# finditer
# findall과 동일하나 반복 가능한 객체(iterator object)를 리턴한다.

result = p.finditer("life is too short")
print(result)

for r in result: print(r)

# match 객체의 메서드
# 어떤 문자열이 매치되었는가?
# 매치된 문자열의 인덱스는 어디부터 어디까지인가?

#   메서드     목적
#   group()     매치된 문자열을 리턴한다.
#   start()     매치된 문자열의 시작 위치를 리턴한다.
#   end()       매치된 문자열의 끝 위치를 리턴한다.
#   span()      매치된 문자열의 (시작, 끝)에 해당되는 튜플을 리턴한다.

import re

p = re.compile('[a-z]+')
m = p.match("python")
m.group()
print(m.group())
m.start()
print(m.start())
m.end()
print(m.end())
m.span()
print(m.span())

m = p.search("3 python")
m.group()
print(m.group())
m.start()
print(m.start())
m.end()
print(m.end())
m.span()
print(m.span())

# 모듈 단위로 수행하기

p = re.compile('[a-z]+')
m = p.match("python")

m = re.match('[a-z]+', "python")

# 컴파일 옵션

#   옵션명     약어      설명
#   DOTALL      S       줄바꿈 문자를 포함하여 모든 문자와 매치할 수 있도록 한다.
#   IGNORECASE  I       대,소문자에 관계 없이 매치할 수 있도록 한다.
#   MULTILINE   M       여러 줄과 매치할 수 있도록 한다.(^,$ 메타 문자의 사용과 관계가 있는 옵션이다.)
#   VERBOSE     X       verbose 모드를 사용할 수 있도록 한다.(정규식을 보기 편하게 만들 수도 있고 주석 등을 사용할 수 도 있다.)

# DOTALL, S
# .메타 문자는 줄바꿈 문자(\n)을 제외한 모든 문자와 매치되는 규칙이 있다. 만약 \n문자도 포함하여 매치하고 싶다면 re.DOTALL 또는 re.S 옵션을 사용해 정규식을 컴파일하면 된다.

import re

p = re.compile('a.b')
m = p.match('a\nb')
print(m)

p = re.compile('a.b', re.DOTALL)
m = p.match('a\nb')
print(m)

# IGNORECASE,I
# re.IGNORECASE 또는 re.I 옵션은 대소문자 구분 없이 매치를 수행하고자 할 때 사용하는 옵션이다.

p = re.compile('[a-z]', re.I)
p.match('python')
print(p.match('python'))

p.match('Python')
print(p.match('Python'))

p.match('PYTHON')
print(p.match('PYTHON'))

# MULTILINE, M

import re

# python이라는 문자열로 시작하고 그 뒤에 whitespace, 그 뒤에 단어가 들어와야 한다는 의미
p = re.compile("^python\s\w+")

data = """python one
life is too short
python two
you need python
python three"""

# ^메타 문자에 의해 python이라는 문자열이 사용된 첫번째 라인만 매치
print(p.findall(data))

import re

p = re.compile("^python\s\w+", re.MULTILINE)

data = """python one
life is too short
python two
you need python
python three"""

# re.MULILINE 옵션으로 ^메타 문자가 문자열 전체가 아닌 각 라인의 처음이라는 의미를 갖게 됨
# 즉, re.MULTILINE 옵션은 ^,$메타 문자를 문자열의 각 라인마다 적용해주는 것이다.
print(p.findall(data))

# VERBOS, X

charref = re.compile(r'&[#](0[0-7]+|[0-9]+|x[0-9a-fA-f]+);')

charref = re.compile(r"""
&[#] # Start of a numeric entity reference
(
    0[0-7]+ # Octal form
    | [0-9]+ #Decimal form
    |x[0-9a-fA-f]+ #Hexadecimal form
    )
    ; #railing semicolon
    """, re.VERBOSE)
# re.VERBOS 옵션을 ㅏ용하면 문자열에 사용된 공백은 컴파일 시 제거된다.(단[] 내에 사용된 공백은 제외) 그리고 줄단위로 #기호를 사용해 주석문을 작성할 수 있다.

# 백슬래시 문제

# \SECTION
# \S 문자가 공백으로 해석되어 의도한 대로 매치가 이루어지지 않는다.

# [\t\n\r\f\v]ection \s문자가 이스케이프 코드 \t,\n,\r,\f,\v로 해석된다.

# 의도한 대로 매치하고 싶다면 다음과 같이 변경해야 한다.
# \\section
# 즉 위 정규식에서 사용한 \문자가 문자열 그 자체임을 알려주기 위해 백슬래시 2개를 ㅏ용하여 이스케이프 처리를 해야 하는 것이다.

# 따라서 위 정규식을 컴파일하려면 다음과 같이 작성해야 한다.
# p = re.comfile('\\section')

# 그런데 여기서 또 하나의 문제가 발견된다.
# 위처럼 정규식을 만들어서 컴파일하면 실제 파이썬 정규식 엔진에는 파이썬 문자열 리터럴 규칙에 의하여 \\이 \로 변경되어 \section이 전달되는 것이다.

# 결국 정규식 엔진에 \\ 문자를 전달하려면 파이썬은 \\\\처럼 백슬래시를 4개나 사용해야 한다.
p = re.compile('\\\\section')

# 만약 위와 같이 \를 이용한 표현이 계속 반복되는 정규식이라면 너무 복잡해서 이해하기 쉽지 않을 것이다. 이러한 문제로 인해 파이썬 정규식에는 Raw String이라는 규칙이 생겨나게 되었다.
# 즉, 컴파일해야 하는 정규식이 Raw String임을 알려줄 수 있도록 파이썬 문법이 만들어진 것이다.

p = re.compile(r'\\section')

# 위와 같이 정규식 문자열 앞에 r 문자를 삽입하면
# 이 정규식은 Raw String 규칙에 의해 백슬래시 2개 대신 1개만 써도 2개를 쓴 것과 동일한 의미를 갖게 된다.

