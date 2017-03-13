# while문
# while문은 조건문이 참인 동안 계속해서 while문 안의 내용을 반복적으로 수행한다.

# while문의 기본 구조

print('\nwhile문의 기본 구조\n')

# while 조건문:
#   수행할 문장1
#   수행할 문장2
#   수행할 문장3

# treeHit = 0
# while treeHit < 10:
#     treeHit = treeHit + 1
#     print("나무를 %d번 찍었습니다." % treeHit)
#     if treeHit == 10:
#         print("나무 넘어갑니다")

# while문 직접 만들기

print('\nwhile문 직접 만들기\n')

prompt = """
    1.Add
    2.Del
    3.List
    4.Quit

    Enter number."""

# number = 0
# while number != 4:
#     print(prompt)
#     number = int(input())

# while문 강제로 빠져나가기

print('\nwhile문 강제로 빠져나가기\n')

# coffee = 10
# money = 300
# while money:
#     print("돈을 받았을 때 커피를 줍니다.")
#     coffee = coffee - 1
#     print("남은 커피의 양은 %d개입니다." % coffee)
#     if not coffee:
#         print("커피가 다 떨어졌습니다. 판매를 중지합니다.")
#         break

# break문 이용해 자판기 작동 과정 만들기

print('\nbreak문 이용해 자판기 작동 과정 만들기\n')

# coffee = 10
# while True:
#     money = int(input("돈을 넣어 주세요.: "))
#     if money == 300:
#         print("커피를 줍니다.")
#         coffee = coffee - 1
#     elif money > 300:
#         print("거스름돈 %d를 주고 커피를 줍니다." % (money - 300))
#         coffee = coffee - 1
#     else:
#         print("돈을 다시 돌려주고 커피를 주지 않습니다.")
#         print("남은 커피의 양은 %d개입니다." % coffee)
#     if not coffee:
#         print("커피가 다 떨어졌습니다. 판매를 중지합니다.")
#         break

# 조건에 맞지 않는 경우 맨 처음으로 돌아가기

print('\n조건에 맞지 않는 경우 맨 처음으로 돌아가기\n')

# a = 0
# while a < 10:
#     a = a + 1
#     if a % 2 == 0: continue
#     print(a)

#무한 루프

print('\n무한 루프\n')

# while True:
#     print("Ctrl+F2를 눌러야 while문을 빠져나갈 수 있습니다.")
