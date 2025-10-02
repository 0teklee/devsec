# Exception 예외처리

"""
크롤링 도중 오류 발생
- 서버 장애
- IP 차단
- 나의 네트워크 문제
- 존재하지 않는 파일을 read하려 해서 에러 발생
- n/0 에러 발생 -> js는 그렇지 않음

비동기 처리를 위해 사용되는 것으로 이해했습니다.
"""

# divZ = 4 / 0
# 프린트 출력되지 않고 변수 할당에서 중단됨
# print(f"divided by 0 : {divZ}")


# 예외처리 적용하기

try:
    scope = 10
    txt = open("dummy.txt", "w")
    nullF = open("none.csv", "r")
    print("none:")
    nullF.close()
except:
    print("Caught!")

finally:
    print(f"scope test : {scope}")
    txt.close()

# finally 블록에서도 scope 10 출력됩니다.
# Javascript try catch finally와 유사합니다.

# 마찬가지로 outer func scope: 10 출력 됩니다.
print(f"outer func scope: {scope} | txt: {txt}")


# 함수 스코프 + 클로저가 궁금해서 다시 작성해봅니다.

# def funcScope(param:int):
#     try:
#         a = (1,2,3)
#         b = a * param
#         f = open("dummy.txt", "a")
#         line = ""
#         for i in range(0, param):
#             line
#


"""
Try - Except 
비동기 처리를 위해 사용되는 것으로 이해됩니다.
"""
