# 2023
ipt = k = int(input('숫자를 입력하세요 >> '))
while True:
    if str(ipt).count('1') == len(str(ipt)):
        print(len(str(ipt)))
        break
    else:
        ipt += k


# 처음 코딩
n = int(input('2와 5로 나누어 지지 않는 10000 이하의 정수를 입력하세요 >> '))
cnt = 1
while True:
    if int('1' * cnt) % n == 0:
        break
    else:
        cnt += 1
print(cnt)