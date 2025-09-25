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

