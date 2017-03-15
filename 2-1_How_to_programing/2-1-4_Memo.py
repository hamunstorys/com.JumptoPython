# 간단한 메모장 만들기

import sys

option = sys.argv[1]
memo = sys.argv[2]

print(option)
print(memo)

# C:\Python>python memo.py -a "Life is too short"
# -a
# Life is too short

# 메모 저장

# C:\Python\memo.py
# import sys
#
# option = sys.argv[1]
#
# if option == '-a':
#     memo = sys.argv[2]
#     f = open('memo.txt','a')
#     f.write(memo)
#     f.write('\n')
#     f.close()

# 메모 출력

# C:\Python\memo.py
# import sys
#
# if option == '-a':
#   memo = sys.argv[2]
#   f = open('memo.txt','a')
#   f.write(memo)
#   f.write('\n')
#   f.close()
# elif option == '-v':
#   f = open('memo.xt','r')
#   memo = f.read()
#   f.close()
#   print(memo)
