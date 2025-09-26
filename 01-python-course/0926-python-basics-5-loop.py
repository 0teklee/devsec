# For 반복문

# 1. range()와 함께 사용하는 방법
countA = 0
for i in range(100):
    countA += 1
    print(f"{i} / 100 : countA = {countA}")
# i = 0부터 시작하여 마지막 99에서 마침. countA 100됨.
# range(100)로 -> 0부터 시작하여 99까지 100번 돌림.

countB = 0
for i in range(1, 100):
    countB += 1
    print(f"{i} / {100} : countB = {countB}")
# i = 1부터 시작하여 99에서 끝남. countB 99에서 끝

# range의 stop 수만큼 회전.
# 인덱스를 0, 1에서 시작하여 100을 채울 시에 stop을 101로.

"------------------------------"

# 2. While 조건식으로만 동작. 조건식에 영향을 주는 변화식이 들어간다.

i = 0
while i < 100:
    print(f"{i} / {100} : i = {i}")
    i += 1

# JS while문과 동일. i 외부 변수를 인덱스 자체로 삼는 예제이다.
# 조건 만족 시 break 사용 도 동일하다.

while i > 0:
    print(f"{i} / {100} : i = {i}")
    i -= 1
    if i % 97 == 0:
        print(f"break : i = {i}")
        # break

# continue
# break와 비슷하지만 제어 흐름을 유지한 상태에서 뒤에있는 코드 실행을 건너뜀

while i < 100:
    i += 1
    if i % 10 == 0:
        print(f"{i}---------- continue-----")
        continue
    elif i % 2 == 0:
        print(f"even {i} / {100} : i = {i}")
    else:
        print(f"Odd: {i} / {100} : i = {i}")

    print(f"*****outer inner - cycle {i} ends*****")

"-------------------------------"
# Quiz 2, 3, 5의 배수를 출력하는 코드 작성
#


def evenNumPrint1(max):
    i = 0
    while i < max:
        i += 1
        if i % 2 != 0:
            continue
        elif i == max:
            print(f"------FIN : i = {i} max ------")
            break
        else:
            print(f"Sol A : {i}")


def evenNumPrint2(max):
    for i in range(2, max):
        if i % 2 == 0:
            print(f"Sol B: {i}")


maxCycle = 100
# maxInput = int(input())

evenNumPrint1(maxCycle)
evenNumPrint2(maxCycle)
# evenNumPrint2(maxInput)


# T의 배수를 max까지 n번 프린트하는 함수:
def targetNumPrint(t, max):
    i = t
    while i <= max:
        print(f"cycle: {i} / {max} i = {i}")
        i += i
    return i


targetNumPrint(10, 100)


"------------------------------"
# Quiz 4 n의 배수 + 30일 때만 출력
# 문제를 잘못 이해했으나, 4번 문제를 추상화하여 풀었습니다.
# 파이썬은 보통 스네이크 케이스를 쓰는 지 궁금합니다.
# n의 배수이면서 plus의 배수가 아닌 조건을 프린트합니다.


def target_multiple_surplus(t, plus, max):
    i = t
    while i <= max:
        if i % t == 0 and i % plus != 0:
            print(f"pass✅ num: {i} / {max}")
        i += 1


target_multiple_surplus(5, 30, 100)
"""
5의 배수이면서 30의 배수는 아니고 max가 100일 때
pass✅ num: 5 / 100
pass✅ num: 25 / 100
(30 제외)
pass✅ num: 35 / 100
...
pass✅ num: 55 / 100
(60 제외)
pass✅ num: 65 / 100
pass✅ num: 70 / 100
pass✅ num: 85 / 100
(90 제외)
pass✅ num: 95 / 100
pass✅ num: 100 / 100
"""

"------------------------------"
# Quiz 5 FizzBuzz
"""
• 1에서 100까지 출력
• 3의 배수는 Fizz 출력
• 5의 배수는 Buzz 출력
• 3과 5의 공배수는 FizzBuzz 출력
"""


def fizz_buzz(num):
    # 3, 5의 공배수처리
    if num % 15 == 0:
        print(i, "FizzBuzz")
    elif num % 3 == 0:
        print(i, "Fizz")
    elif num % 5 == 0:
        print(i, "Buzz")


# JS에서 스택 + 문자열로 처리하는 방법이 있었던 것 같은데 궁금합니다.

for i in range(1, 101):
    fizz_buzz(i)
"""
콘솔:
3 Fizz
5 Buzz
6 Fizz
9 Fizz
10 Buzz
12 Fizz
15 FizzBuzz
...
90 FizzBuzz
93 Fizz
95 Buzz
96 Fizz
99 Fizz
100 Buzz
"""

# 추상화 연습 - n개의 배수의 리스트 + n개의 fizz/buzz 단어 리스트 맵핑
# O(n) 이외의 방법으로 풀어보기
# def auto_fizz_buzz(tnum, twords, max):
#     i = 0
#     while i <= max:
#      for num in tnum:
#          if i % num == 0:


"------------------------------"
"------------------------------"
"------------------------------"
"------------------------------"
