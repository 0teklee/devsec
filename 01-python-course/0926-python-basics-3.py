# 0926 Python 실습 강의입니다.
# 문자열 메서드
# Join

join = ",".join("JOIN")
print(f"join: {join}")
# join: J,O,I,N 출력

print(
    f"""
   return type: {type(join)} 
   JS join() 인덱스와 동일. 구분자를 포함하여 하나의 문자열로.
   [1,2,3,4].join("+")
   리스트를 1+2+3+4의 문자열로 배열하지 못한다.
   AttributeError: 'list' object has no attribute 'join'
"""
)

# Upper, Lower 대소문자. 모든 언어와 유사.
charUD = "string"
print(f"upper(): {charUD.upper()} lower(): {charUD.lower()}")

# strip, l/r strip 공백 제거**
# JS String.trim()과 유사

strip = "\t  h i  \t"
print(
    f"""
    origin: {strip} | length: {len(strip)}
    ---
    strip(): {strip.strip()} | length: {len(strip.strip())}
    ---
    lstrip: {strip.lstrip()}  | length: {len(strip.lstrip())}
    ---
    rstrip(): {strip.rstrip()} | length: {len(strip.rstrip())}
"""
)

# replace 문자열 변경 JS의 String.replaceAll()과 동일
rplc = "Apple, Banana, Apple"
print(
    f"""
 {rplc.replace("Apple", "+")}
"""
)
#  +, Banana, + 모든 Apple이 변경됨

#  split 문자열 배열로

charQ = "life is too short"
print(
    f"""
charQ : {charQ.split()}
[a,b,c,d] : {"a,b,c,d".split(",")}
"""
)
# charQ : ['life', 'is', 'too', 'short']
# --> param 없을 시 공백 단위로 요소
# [a,b,c,d] : ['a', 'b', 'c', 'd']

# Quiz list A를 "My name is Tim" 이라는 문자열로 변경 후 출력
a = ["My", "name", "is", "Tim"]
# 낯선 점 : join을 리스트에 사용하는 방법. JS와 파람, 메서드 위치가 반대라 헷갈림.
# Sol A
print(f"A: {" ".join(a)}")

# Sol B 반복문 사용
solB = ""
for char in a:
    solB += char + " "
solB = solB.rstrip()
print(f"solB: {solB}")
