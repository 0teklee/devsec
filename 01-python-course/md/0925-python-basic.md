# Python basics I

### 핵심 포인트

- **불리언/비교 연산**: `==`, `!=`, `and`, `or`
- **리스트 연산**: 인덱싱, `append`, `insert`, `len`, `del`, `remove`, `in`
- **예외 처리**: `try ... except IndexError`
- **딕셔너리**: 키/값 조작, `in`, `get`, `type`
- **집합**: 생성, `add`, `clear`, `union`, `difference`, `intersection`
- **튜플**: 불변 시퀀스
- **문자열**: 삼중 따옴표, 곱셈, 길이
- **중복 제거 문제**: `set` 사용 vs 반복문 비교

하단의 파이썬 코드는 모두 깃헙에 공개되어 있습니다.

1. [0925-pythong-basics.py](https://github.com/0teklee/devsec/blob/main/01-python-course/0925-python-basics.py)
2. [0925-pythong-basics-2.py](https://github.com/0teklee/devsec/blob/main/01-python-course/0925-python-basics-2.py)

---

### 1. 0925 오전 파이썬 실습

```python
# PyCharm 자주 사용하는 단축키
# cmd + / 주석처리 ide 거의 동일

a = 80
b = 70
c = 55

leng = 3
sumItems = a + b + c

avg = sumItems / leng
# avg (average) 평균 68.3333.... 출력
print(avg)
# int 타입 출력 68
avgInt = int(avg)
print(avgInt)

# float 타입 num : 68.0 출력
floatNum = float(avgInt)
print('floatNum: ',floatNum)

# % 모듈러 연산 (나머지) 출력 1
modAvg = sumItems % leng
print(modAvg)

# 실수
floatNum = avg - modAvg
print('floatNum: ',floatNum)


# type 함수 출력 80, <class 'int'>
print(a, type(a))
# 10, class str 출력
print(10, type('10'))


#  파이썬 조건문 : Not same 출력
if 10 == '10':
    print('Same')
else:
    print('Not same')
```

- **핵심 포인트**
  - **평균 계산**: `sumItems / leng`
  - **형 변환**: `int()`, `float()`
  - **나머지 연산**: `%`
  - **타입 확인**: `type()`
  - **조건식 비교**: 정수와 문자열 비교는 False

---

### 2. 0925 python 오후

오후 실습으로, 불리언 연산, 리스트/딕셔너리/집합/튜플, 예외 처리, 문자열, 간단한 문제 해결(중복 제거)까지 폭넓게 다룹니다.

```python
# 오후 시간 14:00부터 진행된 파이썬 실습입니다.
# PyCharm 자주 사용하는 단축키
# cmd + / 주석처리 ide 거의 동일

a = 80
b = 70
c = 55

leng = 3
sumItems = a + b + c

avg = sumItems / leng
# avg (average) 평균 68.3333.... 출력
print(avg)
# int 타입 출력 68
avgInt = int(avg)
print(avgInt)

# float 타입 num : 68.0 출력
floatNum = float(avgInt)
print('floatNum: ',floatNum)

# % 모듈러 연산 (나머지) 출력 1
modAvg = sumItems % leng
print(modAvg)

# 실수
floatNum = avg - modAvg
print('floatNum: ',floatNum)


# type 함수 출력 80, <class 'int'>
print(a, type(a))
# 10, class str 출력
print(10, type('10'))


#  파이썬 조건문 : Not same 출력
if 10 == '10':
    print('Same')
else:
    print('Not same')

```

---

파이썬 재밌습니다.
