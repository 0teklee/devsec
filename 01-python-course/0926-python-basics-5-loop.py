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


# T의 배수를 max까지 max번 프린트하는 함수:
def targetNumPrint(t, max):
    i = t
    while i <= max:
        print(f"cycle: {i} / {max} i = {i}")
        i += i
    return i


targetNumPrint(10, 100)


"------------------------------"


"------------------------------"
