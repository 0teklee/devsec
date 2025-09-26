"0926 오후 시간의 파이썬 실습입니다."

# 파일 입출력 시스템
"""
• open(파일 이름, 파일 열기 모드)
• 파일 열기 모드
• r (read) : 읽기모드
• w (write): 쓰기모드
• 파일을 쓰기 모드로 열면 해당 파일이 이미 존재할 경우 원래 있던 내용이 모두 사라짐
• a (append): 추가모드

---
node.js의 파일 시스템 fs가 언어에 내장되어 있음으로 이해했습니다.
"""

# 파일 생성하기
testText = open("0926-python-basics-6-file-io-test.txt", "w")
# 내용을 작성합니다.
inputTxt = "----start----"
for i in range(1, 11):
    inputTxt = (
        inputTxt
        + """
   | LINE %d |
   ----------- 
    """
        % i
    )
testText.write(inputTxt)

testText.close()
# "w" write 모드 - 실행 후 파일 생성 확인했습니다. 유용합니다.
# 실행 이후 파일을 닫았습니다.
# 첫 실행 시 파일 생성 - 두번째부터는 w 모드에서 덮어쓰기로 이해했습니다.
# 따라서 open("file", 'a')로 열어야합니다. unix cli의 nano로 이해했습니다.
# 파일 쓰기 - write mode로 파일을 수정합니다.

# 파일 읽기
r = open("0926-python-basics-6-file-io-test.txt", "r")
r_line_1 = r.readline()
print("1st line: ", end=r_line_1)
r_line_2 = r.read()
print(
    f"""
entire line: 
{r_line_2}
"""
)
r.close()

"""
1st line:  ----start----

entire line:     | LINE 1 |
   ----------- 
    
   | LINE 2 |
   ----------- 
"""

# readline()
"""
파일의 내용에서 한 줄만 읽어오는 함수
• 줄 바꿈이 2번 들어가는 이유??
• line에 개행문자(\n)가 포함 되어 있기 때문임
• => strip()을 사용하면 개행문자를 없앨 수 있음
"""
f = open("0926-python-basics-6-file-io-test.txt", "r", encoding="utf8")
while True:
    line = f.readline()
    if not line:
        break
    print(line)
f.close()

# readlines()
"""
readlines()
    • 파일 내용을 모두 불러와서 **리스트** 형태로
    저장하는 함수
"""
f = open("0926-python-basics-6-file-io-test.txt", "r", encoding="utf8")
lines = f.readlines()
print(f"lines: {lines}  type: {type(lines)}")

# type class 'list'  출력
# lines: ['----start----\n',... -> 개행 문자까지 포함되어 프린트
for line in lines:
    print("readlines():", line)
f.close()

# Encoding

"""

메모:
- LF(0x0A)
- CR(0x0D)
이 둘은 줄 바뀜에 사용되는 특수 문자.
DDOS 공격의 Slow HTTP Dos 기법에서 사용될 수 있다.
"""
