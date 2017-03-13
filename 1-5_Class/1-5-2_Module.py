# 모듈(Module)

# 모듈 만들고 불러오기
# 모듈 불러오기 : import 모듈 이름

import mod1

print(mod1.sum(3, 4))
print(mod1.safe_sum(3, 4))
print(mod1.safe_sum(3, 'a'))
print(mod1.sum(10, 20))

# 모듈 하무를 사용하는 또 다른 방법

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

import mod2

print(mod2.PI)

a = mod2.Math()
print(a.solv(2))
