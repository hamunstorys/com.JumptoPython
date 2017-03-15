# 게시판 페이징하기

# 함수이름은? getTotalPage
# 입력 받는 값은? 게시물의 총 건수(m), 한 페이지에 보여줄 게시물 수(n)
# 출력하는 값은? 총 페이지수

# 총 페이지수 = 총 건수 / 한 페이지당 보여줄 건수 +1
def getTotalPage(m, n):
    return m // n + 1  # 소수점 아래 자리를 버리기 위해서 / 대신 //연산자를 사용하였다.


print(getTotalPage(5, 10))
print(getTotalPage(15, 10))
print(getTotalPage(25, 10))
print(getTotalPage(30, 10))


# ZeroDivideError resolve
def getTotalPage(m, n):
    if m % n == 0:
        return m // n
    else:
        return m // n + 1


print(getTotalPage(5, 10))
print(getTotalPage(15, 10))
print(getTotalPage(25, 10))
print(getTotalPage(30, 10))
