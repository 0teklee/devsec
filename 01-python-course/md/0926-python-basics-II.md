# Python basics II

- 이 글은 아래 파이썬 실습 시간 중에 작성했던 `.py` 글을 마크다운 형태로 정리한 내용입니다.
- MD 링크:
- 파이썬 파일 링크
  - 수업 시간에 내주신 예제 등에서 개인적인 궁금증에 추가 내용과 코드를 작성했습니다.
  - https://github.com/0teklee/devsec/tree/main/01-python-course

## 핵심 포인트

- **문자열 메서드**: `join`, `upper/lower`, `strip/lstrip/rstrip`, `replace`, `split`
- **조건문**: `if / elif / else`, `input()`과 형 변환, 함수로 추상화
- **반복문**: `for-range`, `while`, `break`, `continue`, 간단한 문제(짝수, 배수, FizzBuzz)
- **파일 입출력**: `open()` 모드(`r/w/a`), `write`, `readline`, `readlines`, 개행/인코딩 주의

---

### 1. 문자열(String) 메서드

간단한 메서드 동작과 반환 타입, 그리고 **JS와의 비교 관점**에서 이해합니다.

join() 메서드가 왠지 혼동되는 부분이 있었습니다.

```python
# join: 구분자를 기준으로 요소를 하나의 문자열로 결합
join = ",".join("JOIN")
print(join)  # J,O,I,N

charUD = "string"
print(charUD.upper(), charUD.lower())  # STRING string

# 공백 제거 (양끝/왼쪽/오른쪽)
s = "\t  h i  \t"
print(s.strip(), len(s.strip()))
print(s.lstrip())
print(s.rstrip())

# 문자열 치환
print("Apple, Banana, Apple".replace("Apple", "+"))  # +, Banana, +

# 분리: 기본 공백, 혹은 구분자 지정
print("life is too short".split())      # ['life', 'is', 'too', 'short']
print("a,b,c,d".split(","))            # ['a', 'b', 'c', 'd']
```

리스트를 자연스러운 문장으로 만들기:

```python
a = ["My", "name", "is", "Tim"]
print(" ".join(a))  # "My name is Tim"

# 반복문으로도 가능
solB = ""
for word in a:
    solB += word + " "
print(solB.rstrip())
```

---

### 2. 조건문(Condition)

`if / elif / else`는 다른 언어와 동일한 개념이며, 콜론(`:`)과 들여쓰기로 블록을 구분합니다.

```python
condX = 5
if condX == 5:
    print(True)
elif condX <= 5:
    print(True)
else:
    print(False)
```

함수로 분기 로직을 추상화합니다.

아직 함수를 배우지 않았지만, 이 부분에서 강사님께서 조건문/반복문/함수를 간략히 설명해주셔서 적용했습니다.

```python
def condition(x: int) -> None:
    if x == 30:
        print("30입니다.")
    elif x != 50:
        print("50이 아닙니다.")
    else:
        print("50입니다.")

condition(30)
condition(50)
condition(70)
```

`input()` 사용 시에는 형 변환과 예외에 유의합니다.

```python
# 문자열 입력을 정수로 변환
x = int(input())
condition(x)
# 잘못된 문자열을 입력하면 ValueError 발생
```

홀짝 판별(반복문 + 함수 호출):

```python
def even_or_odd(num: int) -> None:
    if num == 0:
        print("0입니다.")
    elif num % 2 == 0:
        print(f"{num}은 짝수입니다.")
    else:
        print(f"{num}은 홀수입니다.")

for n in [50, 51, 0, 22]:
    even_or_odd(n)
```

---

### 3. 반복문(Loops)

`for-range` 기본 형태와 `while`의 제어 흐름(`break`, `continue`)을 익힙니다.

```python
# for + range
for i in range(3):
    print(i)  # 0, 1, 2

for i in range(1, 4):
    print(i)  # 1, 2, 3

# while + 증가/감소 + break/continue
i = 0
while i < 10:
    i += 1
    if i % 10 == 0:
        print("continue point")
        continue
    if i % 7 == 0:
        print("break point")
        break
    print("i=", i)
```

짝수 출력 두 가지 방식:

```python
def print_evens_while(max_num: int) -> None:
    i = 0
    while i < max_num:
        i += 1
        if i % 2 != 0:
            continue
        if i == max_num:
            break
        print(i)

def print_evens_for(max_num: int) -> None:
    for i in range(2, max_num):
        if i % 2 == 0:
            print(i)

print_evens_while(20)
print_evens_for(20)
```

배수 관련 문제들:

```python
# t의 배수를 max까지 출력 (지속적으로 t씩 증가)
def print_target_multiples(t: int, max_num: int) -> None:
    i = t
    while i <= max_num:
        print(i)
        i += i

print_target_multiples(10, 100)

# t의 배수이면서 plus의 배수는 아닌 수만 출력
def multiples_excluding(t: int, plus: int, max_num: int) -> None:
    for i in range(t, max_num + 1):
        if i % t == 0 and i % plus != 0:
            print(i)

multiples_excluding(5, 30, 100)
```

FizzBuzz:

```python
def fizz_buzz(n: int) -> None:
    if n % 15 == 0:
        print(n, "FizzBuzz")
    elif n % 3 == 0:
        print(n, "Fizz")
    elif n % 5 == 0:
        print(n, "Buzz")

for i in range(1, 101):
    fizz_buzz(i)
```

---

### 4. 파일 입출력(File I/O)

`open(파일명, 모드)`로 파일을 열고, 사용 후에는 `close()` 합니다. 쓰기 모드(`w`)는 기존 내용을 덮어쓰고, 추가 모드(`a`)는 이어 붙입니다.

```python
# 쓰기
f = open("0926-python-basics-6-file-io-test.txt", "w")
content = "----start----"
for i in range(1, 6):
    content += f"\n| LINE {i} |\n-----------"
f.write(content)
f.close()

# 읽기 (readline + read)
r = open("0926-python-basics-6-file-io-test.txt", "r", encoding="utf8")
first_line = r.readline()
rest = r.read()
print("1st:", first_line)
print(rest)
r.close()

# 줄 단위 반복 (readline in loop)
f = open("0926-python-basics-6-file-io-test.txt", "r", encoding="utf8")
while True:
    line = f.readline()
    if not line:
        break
    print(line.rstrip())  # 개행 제거
f.close()

# 전체를 리스트로 (readlines)
f = open("0926-python-basics-6-file-io-test.txt", "r", encoding="utf8")
lines = f.readlines()
print(type(lines), len(lines))
for line in lines:
    print("readlines():", line.rstrip())
f.close()
```

참고 메모:

- **개행 문자**: LF(`\n`), CR(`\r`)
- **인코딩**: 텍스트 파일 처리 시 `encoding="utf8"` 권장
- **모드 요약**: `r`(읽기), `w`(쓰기/덮어쓰기), `a`(추가)

---

읽어주셔서 감사합니다.
