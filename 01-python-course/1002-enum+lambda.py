# ENUM (Enumerate)
# 순서가 있는 자료형을 입력바당 index 값을 부여합니다.

sts = ["a", "b", "c", "d", "e"]
# enumerate object at 0x104d494e0
# 메모리 주소까지 나옵니다.
enumS = enumerate(sts)


print(f"typeof enumS {enumS}")
for student in enumS:
    print(f"student {student}")

# 인덱스와 함께 표시. 아주 편리하겠습니다.
for i, student in enumerate(sts, start=1):
    print(f"st: {i} {student}")


# LAMBDA 람다 함수
# JS IIFE, 화살표 콜백 함수가 떠오릅니다. 익명함수로 이해했습니다.
print((lambda n, m: n if n % 2 == 0 else m)(1, 3))
# 코드량을 많이 줄여주는 기능으로도 이해됩니다. 기본 문법을 익힌 다음에 다시 보겠습니다.

# Quiz 1
# 리스트 정렬
sortL = [1, 3, 5, 4, 2]
result = sorted(sortL)
# sort가 원본 값을 바꾸고 반환값이 없기 때문에 sorted를 사용했습니다.
sortL.sort(reverse=True)


print(f"quiz 1 : result = {result} | sortM = {sortL}")
# https://wikidocs.net/16041
# JS와 유사해서 익숙하지만 함수 param= 지정, 문법 차이로 다소 혼동이 있습니다.

# Quiz 2

student_tuples = [("john", 160), ("jane", 158), ("dave", 179)]

student_tuples.sort(key=lambda x: x[1])

print(f"lambda sorted : {student_tuples}")
# sort 키에 람다 함수를 넣을 수 있습니다!
# 함수 반환값이 평가되는 것인지, deconstructing 같은 문법인지 궁금하네요.
# reverse param도 편해서 좋습니다. sort 메서드는 파이썬이 JS보다 쉬워서 좋습니다.
# 다만 제가 익숙했던 언어 문법에서 벗어나서 익힐 필요가 있어보입니다.
