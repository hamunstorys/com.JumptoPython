# 3과 5의 배수 합하기

# 10 미만의 자연수에서 3과 5의 배수를 구하면, 3,5,6,9이다. 이들의 총합은 23이다.
# 1000미만의 자연수에서 3의 배수와 5의 총합을 구하라

def find_multiple_number(maxrange, matterfactor):
    result = []
    count = 0
    if type(matterfactor) == int:
        for number in range(1, maxrange):
            if number % matterfactor == 0:
                result.append(number)
    else:
        for number in range(1, maxrange):
            if number % matterfactor[count] == 0:
                result.append(number)
                if count < len(matterfactor) - 1:
                    count += 1
                else:
                    count = 0
    return result


print(find_multiple_number(1000, [3, 4]))
