# 오후 시간 14:00부터 진행된 파이썬 실습입니다.

a = 3 > 1
# a에는 Boolean 타입의 true가 할당된다.
print("a: ", a)
b = 1 > 3
# b에는 Boolean 타입의 false가 할당된다.
print("b: ", b)

# == 동일함을 확인하는 연산자
# =! 동일하지 않음을 확인하는 연산자

c = 10 == 10
print("c: ", c)

d = 10 != 5
print("d: ", d)

e = 10 != 10
print("e: ", e)

# 문자열 비교

char1 = "Python" == "Python"
char2 = "Python" == "python"
char3 = "Python" != "Python"

charResult = [char1, char2, char3]
print("Char Result: ", charResult)

# And 연산자
# Javascript "&&" 연산자와 유사

andA = True and True
andB = True and False
andC = False and True
andD = False and False

andResult = [andA, andB, andC, andD]
print("Boolean AND result: ", andResult)

# Or 연산자
# Javascript "||" 연산자와 유사

orA = True or True
orB = True or False
orC = False or True
orD = False or False

orResult = [orA, orB, orC, orD]

print("Boolean OR result: ", andResult)

# List 자료형
# List 자료형은 JS의 배열처럼 다양한 자료형을 배열 형태로 추가할 수 있다.
listA = [1, "string", True, {a: 1}, ["list"]]
print(listA, type(listA), type("string"), type(listA[0]))

# ES 최신 문법처럼 -1을 마지막 요소 인덱스로 사용할 수 있다.
# "['list']" 출력
print("last elm: ", listA[-1])
print("- index: ", listA[-2], listA[-3], [listA[-4]])

# Try Catch 문을 통해 except로 예외처리 가능하다.
try:
    print("Inner Try listA[4]: ", listA[5])
except IndexError:
    print("Error: Index out of range")
# Error:Index out of range가 출력된다.
# listA의 인덱스는 0~4까지이기 때문이다.

# **** 중요 *****
# 예외처리 없이 실행 시 런타임 에러로 listA.append부터 실행되지 않는다.
# print("no exception error throw: ", listA[5])


# **** 배열 메서드 append, insert ****
nestedList = []

# append push()와 유사하다. 가장 끝에 추가.
listA.append("last item!")
print("applied append():", listA)
# 개인적인 궁금증에 자기 참조로 실행하였다.

# nestedList self-ref:  [[...]] 1 [[...]] 출력. 자기 참조로 배열 내의 배열 할당이 되긴하였다.
nestedList.append(nestedList)
print("nestedList self-ref: ", nestedList, len(nestedList), nestedList[0])

# insert(삽입 위치 인덱스, 추가 값)
# JS array.splice와 유사하다.
nestedList.insert(0, [0, 0, 0])
print("insert: ", nestedList)

# 배열 간의 + 연산자 : 두 Array의 결합.
plusList = nestedList + [1, 2, 3]
print("+list : ", plusList)
# 주의: [[0, 0, 0], 1, 2, 3] 출력된다 배열 [1,2,3]은 개행되어 하나의 배열이 된다.
# 즉 합집합 형태가 됨. 고차 배열을 연산하는 경우 혼동될 수 있을 것.
# JS의 Set 메서드 중 union, intersection이 떠오르는 부분. 쉬워서 혼동될 수 있겠다.


# len() = JS의 .length (배열 프로토타입) 과 같지만, 함수 형태만 제공한다.
# applied append(): [1, 'string', True, {True: 1}, ['list'], 'last item!']
# 6 출력됨
listALeng = len(listA)
print(listALeng)

# del - 마찬가지로 splice와 유사
delList = [0, 1, 2, 3, 4]
del delList[0]
print("del: ", delList, delList[0])
# del:  [1, 2, 3, 4], 1이 출력된다.
# JS의 배열 조작처럼 배열 전체의 길이와 인덱스가 변경된다.

# remove
removeList = [1, 2, 5, 5]
removeList.remove(1)
print("remove: ", removeList)
# remove 함수 실행 이후에 "1"이 완전히 삭제된다. 즉 원본값에 변경이 생긴다.
removeList.insert(0, 1)
# 다시 1을 추가한 뒤, remove(5)를 실행한다.
removeList.remove(5)
print("remove(5): ", removeList)
# "순차"적으로 삭제된다. 즉 0부터 먼저 중복된 값을 삭제한다.
removeList.insert(0, 5)
# removeList = [5, 1, 2, 5]
print("[5, 1, 2, 5]", removeList)
removeList.remove(5)
print("[1, 2, 5]", removeList)
# 출력 시 removeList = [1, 2, 5]

#  in 연산자
boolIn = 3 in removeList
print("boolIn: ", boolIn)
# False 출력

# Dict 딕셔너리 자료형
# { Key : Value } 형태의 자료형. 객체와 유사하다.

newDict = {
    "a": 1,
    "b": 2,
    "c": 3,
}
# JS처럼 재할당이 가능하고
newDict["c"] = 4
# 필드 추가도 가능하다.
newDict["d"] = 5
# int 형태의 key(5)와 기존과 다른 타입의 값도 할당이 가능하다.
newDict[5] = "string val"

print("newDict: ", newDict)
print("in 연산자도 실행 가능하다 : ", "d" in newDict)
# Key가 있는 지를 확인할 때 사용한다. Typescript의 in 연산자와 동일.
print("dict의 타입은 : ", type(newDict))
# dict의 타입은 :  <class 'dict'> 출력

nonValueFromDict = newDict.get("AA")
if nonValueFromDict == None:
    print("nonValueFromDict == None: ", nonValueFromDict)
else:
    print("nonValueFromDict == NoneElse", nonValueFromDict)
print("None type", type(nonValueFromDict))
# None type <class 'NoneType'> NoneType이 출력되고 에러가 발생하지 않는다.
if nonValueFromDict is None:
    print("var is none : ", nonValueFromDict)
    # None 확인은 is와 함께 많이 사용한다.

# 집합 Set과 메서드
# JS의 Set과 기본 컨셉은 동일하다. 중복된 요소가 없는 집합.
# *중요 : Set 자료형에는 1. 중복 요소 2. 순서 가 없다.
s1 = set([1, 2, 3])
s2 = set("hello")
# {1, 2, 3} {'h', 'l', 'o', 'e'}가 출력된다.
print(s1, s2)
# 리스트[]로 set을 생성하여도
s3 = set(["aaa", "bbb", "ccc"])
s3.add("aaa")
print("add :", s3)
# {"bbb", "ccc", "aaa"} 가 출력된다.
s3.clear()
print("clear: ", s3, type(s3), s3 == None)
# clear:  set() <class 'set'>, False 출력
# 타입은 여전히 set이다.

# 집합 연산자
# JS의 Set.union, intersection, difference 메서드와 동일.
setA = set([1, 2, 3])
setB = set([3, 4, 5])
union = setA.union(setB)
difference = setA.difference(setB)
intersection = setA.intersection(setB)

print(f"union: {union} difference: {difference} intersection: {intersection}")
# union:  {1, 2, 3, 4, 5}
# difference:  {1, 2}
# intersection:  {3}

# 튜플 Tuple
# 저장된 요소를 변경, 추가, 삭제할 수 없다. JS의 Object.freeze()된 객체와 유사.
# Constant 상수 Enum(?) 으로 사용하기 좋을 것 같다.
tupleA = (1, 2, 3)


# 함수

# 문제 : 중복된 요소를 삭제하는 함수 만들기
dupls = [1, 1, 1, 5, 9, 9, 9, 3, 3]
# Solution A set 사용
solA = list(set(dupls))
# 자료형을 set에서 리스트로 바꾸기 위해선 list() 메서드 사용

# Solution B 반복문 사용 O(n) 반복문
solB = []

for value in dupls:
    if value not in solB:
        solB.append(value)
    else:
        pass

print(f"solA: {solA} solB: {solB}")


# 문자형
# 기본 quote 문자, 이스케이프 문자는 동일.
# triple quote 마크로 JS의 백틱처럼 사용함

print(
    f"""
 이렇게 사용할 수 있음 
 이스케이프문자 없이 줄바꿈도 그대로 적용
 dupls: {dupls}
 print(f"...")로 변수 추가 가능
"""
)
# 문자열과 연산자
# + : JS와 동일

문자열곱하기 = "wow " * 3
print(f"문자열 곱하기 : {문자열곱하기}")
# 문자열 곱하기 : wow wow wow 출력.
# 다른 언어를 쓰다 보니 정말 희안하게 느껴짐.

stringLeng = len(문자열곱하기)
print(
    f"""
stringLeng: {stringLeng}
'wow ' => 공백까지 포함해서 length 4 * 3
12 프린트
"""
)
