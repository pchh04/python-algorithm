# 2023
sum = 0
temp = 1
for i in range(10, 1001):
    for j in str(i):
        temp *= int(j)
    sum += temp
    temp = 1
print(sum)


# 처음 코딩
numsum = 0
for i in range(10, 1001):
    num = 1
    for j in range(len(str(i))):
        num *= int(str(i)[j])
    numsum += num
print(numsum)

# 간단화 : eval 함수는 문자열 상태의 수식을 계산해 주는 함수, join 함수는 리스트가 아닌 문자열에도 적용 가능 - 개별 문자를 구분자로 연결해 줌
print(eval('+'.join('*'.join(str(x)) for x in range(10, 1001))))