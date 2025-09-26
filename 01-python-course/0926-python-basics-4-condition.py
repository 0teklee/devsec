"0926 오전 파이썬 실습 시간의 내용입니다."

# 조건문 if
condX = 5
if condX == 5:
    print(True)
else:
    print(False)
# ":"으로 else, if 구문을 나눈다.

# if, elif, else
# JS 조건문과 동일하다 "elif" == "else if"
if condX == 4:
    print(True)
elif condX <= 5:
    print(True)
else:
    print(False)


# Quiz
# x가 30/50인 경우 30/50 입니다 문자열 출력
def condition(x):
    if x == 30:
        print("30입니다.")
    elif x != 50:
        print("50이 아닙니다.")
    else:
        print("50입니다.")


condition(30)
condition(50)
condition(70)

# input() 메서드를 사용하여 풀어보기
x = int(input())
print(
    f"""
input() condition(input())
---------------------------
x : {x} type: {type(x)}
---------------------------
"""
)

# input() 메서드 = 코드 실행 중 터미널에 값을 입력하여 값을 할당할 수 있다.
condition(x)
"""
input() int 타입 메서드에 "문자열" 입력 시 에러
Traceback (most recent call last):
    x = int(input())
ValueError: invalid literal for int() with base 10: '"문자열"'
"""


# Quiz
"홀수 짝수를 판별하세요"
numA = 50
numB = 51
numC = 0
numD = 22

quizL = [numA, numB, numC, numD]
# 반복문 사용하기
for num in quizL:
    if num == 0:
        print(f"반복문: 0입니다.")
    elif num % 2 == 0:
        print(f"반복문: {num}은 짝수입니다.")
    else:
        print(f"반복문: {num}은 홀수입니다.")


# 심화 내용 함수 :
def evenOrOdd(num):
    if num == 0:
        print("함수 호출 : 0입니다.")
    elif num % 2 == 0:
        print(f"함수 호출: {num}은 짝수입니다.")
    else:
        print(f"함수 호툴: {num}은 홀수입니다.")


# 반복문 내부에서 함수 호출
for num in quizL:
    evenOrOdd(num)
