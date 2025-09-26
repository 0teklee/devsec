# 문제 1
asia = {"한국", "중국", "일본"}
asia.add("베트남")
asia.add("중국")
asia.remove("일본")
asia.update({"한국", "홍콩", "태국"})
print("문제 1 :", asia)

# 문제 2
lol = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]
print("문제 2 :", lol[0])
print("문제 2 :", lol[2][1])
for sub in lol:
    for item in sub:
        print(item, end=" ")
    print()

# 문제 3
x, y = 100, 200
print("문제 3 :", x == y)

# 문제 4
a = 100
result = 0
for i in range(1, 3):
    result = a >> i
    result = result + 1
print("문제 4 :", result)


# 문제 5
class CharClass:
    a = ["Seoul", "Kyeongi", "Inchon", "Daejeon", "Daegu", "Pusan"]


myVar = CharClass()
str01 = " "
for i in myVar.a:
    str01 = str01 + i[0]
print("문제 5 :", str01)


# 문제 6
a = "REMEMBER NOVEMBER"
b = a[0:3] + a[12:16]
c = "R AND %s" % "STR"
print("문제 6 :", b + c)

# 문제 7
x, y = input("x, y의 값을 공백으로 구분하여 입력 : ").split(" ")
print("문제 7 : x의 값 :", x)
print("문제 7 : y의 값 :", y)

# 문제 8
def func(num1, num2 = 2):
	print("문제 8 : a =", num1, "b =", num2)
func(20)

# 문제 9
a = sum = 0
while a < 10:
	a += 1
	if a%2 == 1:
		continue
	sum += a
print("문제 9 :", sum)

# 문제 10
a, b = 2, 3
c = a & b
print("문제 10 :", c)

# 문제 11
hap = 0
for i in range(1, 11):
    hap += i
print("문제 11 :", i, hap)

# 문제 12
a, c = 32, -3
b = a << 2
a >>= 3
c = c << 2
print("문제 12 :", a, b, c)

# 문제 13
i, hap = 0, 0
while True:
	i += 1
	hap += i
	if i >= 100:
		break
print("문제 13 :", hap)

# 문제 14
str = 'ctxatppa'
n = len(str)
st = list()
for k in range(n):
	st.append(str[k])
print("문제 14 :", end = '')
for k in range(n-1, -1, -1):
	print(st[k], end = '')

# 문제 15
a = [[1, 1, 0, 1, 0],
	[1, 0, 1, 0]]
tot, totsu = 0, 0
for i in a:
	for j in i:
		tot += j
	totsu = totsu + len(i)
print("문제 15 :", totsu, tot)

# 문제 16
def cnt(str, p):
	result = 0;
	for i in range(len(str)):
		sub = str[i:i+len(p)]
		if sub == p:
			result += 1
	return result
str = "abdcabcabca"
p1 = "ca"
p2 = "ab"
print(f'문제 16 : ab{cnt(str, p1)} ca{cnt(str, p2)}')