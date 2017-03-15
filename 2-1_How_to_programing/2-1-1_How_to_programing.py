# 내가 프로그램을 만들 수 있을 까?

# 프로그램을 만들려면 가장 먼저 '입력'과 '출력'을 생각하라.

def GuGu(n):
    result = []
    number = 1
    while (number < 10):
        result.append(n * number)
        number += 1
    return result


def GuGu2(n):
    result = []  # 결과값을 저장할 리스트인 result
    i = 1
    while i < 10:
        result.append(n * i)
        i = i + 1  # i += 1
    return result


print(GuGu(2))
