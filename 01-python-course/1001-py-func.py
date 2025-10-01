# 1001 py func


def add(a, b):
    print("%d+%d=%d" % (a, b, a + b))


# Format String %d=digit, %s=string

add(3, 5)
add(8, 10)


# 매개 변수를 지정할 수 있습니다. 너무 좋습니다.
add(b=3, a=5)
# 출력: 5+3=8, "b"가 앞에 와도 지정했기에 순서가 상관없습니다.


# ****Tuple***
# "*args"로 시작 시 자동으로 인자를 튜플로 만듭니다!
#  Tuple = 변경/삭제가 되지 않는 리스트 형태. "(arg1, arg2)"
def add_many(*args):
    result = 0
    for i in args:
        result = result + i
    return result


# 함수 인자의 갯수를 알 수 없을 때 유용하게 쓰입니다. (=동적으로 인자 전달)
# JS에서 비슷한 상황에 문법이 복잡해지는 반면, 이 방식은 깔끔해서 좋습니다.
# ex) TS: [...args] -> 타입 inspection이 불가능하여 타입 가드가 무시됨
#       + JS/TS에서 함수 인자가 배열array가 아닌 경우, runtime error가 발생할 수 있음.
# ex) JS/TS에서 올바른 *args 구현을 위해 추가 함수가 필요함.
# 함수 인자가 배열 타입이

print(add_many(1))
print(add_many(1, 2, 3))
print(add_many(1, 2, 3, 4, 5))

# ***** Kwargs : dict ******
# "*args"와 유사하지만, dict 형태로 넣습니다.
# JS의 deconstructing과 유사하지만, {} 사용이 없는 점이 다릅니다.


def print_kwargs(**kwargs):
    print(kwargs)


print_kwargs(a=1)
print_kwargs(name="foo", age=3)


# Early Return
def check_err(*args):
    for i in args:
        if i < 0:
            return
        else:
            print(f"pass: {i}")


# 함수 지역변수 | 전역변수
# 파이썬에서 스코프를 살펴봅니다:
a = 1


def local_global(a):
    a = a + 1


local_global(a)
print("local_global a:", a)
# 1 출력

"""
JS와 아주 큰 차이점은 함수 내부에서 로컬 전역변수에 접근하여 값을 변경하여도,
함수 실행이 끝난 이후 전역변수의 값에 변경이 생기지 않는 점입니다.
"""
# global 예약어와 함수 리턴을 지역/전역 변수에 재할당하여 사용합니다.
# global은 전역변수 접근 예약어입니다. 통상적으로 전역변수 변경은 권장하지 않습니다.

# 함수 리턴 + 재할당
reloc = 0


def return_var(a):
    a = a + 1
    return a


reloc += return_var(1)

# global 예약어 사용
glob_var = 0


def use_global():
    global glob_var
    glob_var += 1


use_global()
print(f"glob_var : {glob_var}")
# 주의 : use_global가 호출되는 횟수만큼 전역변수 glob_var의 데이터가 변경됩니다.

for i in range(1, 11):
    use_global()

print(f"after FOR glob_var : {glob_var}")

# Quiz 1


def totalSum(num):
    result = 0
    for cur in range(1, num + 1):
        result += cur
    return result


print(totalSum(5))
print(totalSum(10))

# Quiz 2


def check_score(score: int):
    if score >= 100:
        return "S"
    elif 80 <= score < 100:
        return "A"
    elif 60 <= score < 80:
        return "B"
    else:
        return "C"


print(check_score(5))
print(check_score(101))
print(check_score(80))
