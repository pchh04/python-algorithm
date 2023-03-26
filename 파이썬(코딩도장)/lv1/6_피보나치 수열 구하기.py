#2023
ipt = int(input('정수 n 입력'))
flist = [0, 1]
cnt = 2
if ipt <= 0:
    print('0')
else:
    print('0 1', end = ' ')
    while True:
        flist.append(flist[cnt-2]+flist[cnt-1])
        if flist[cnt] > ipt: break        
        print(flist[cnt], end = ' ')
        cnt += 1



# 처음 코딩 <n번째 까지의 피보나치 수열 출력>
cnt = int(input('정수를 입력하세요 >> '))
if cnt == 1:
    rst = 0
    print('{}'.format(rst), end = '')
elif cnt == 2:
    rst = 0
    print('{}'.format(rst), end = '')
    rst = 1
    print(', {}'.format(rst), end = '')
else:
    rst = 0
    print('{}'.format(rst), end = '')
    bef2 = rst
    rst = 1
    bef1 = rst
    print(', {}'.format(rst), end = '')
    for i in range(cnt-2):
        rst = bef2 + bef1
        print(', {}'.format(rst), end = '')
        bef2 = bef1
        bef1 = rst
print()

# 처음 코딩 <n 이하의 피보나치 수열 출력>
n = int(input('정수를 입력하세요 >> '))
if n == 0:
    print('0')
# elif n == 1:
#     print('0, 1, 1')     --> 두 줄 삭제 가능
else:
    bef2 = 0
    print(bef2, end = ', ')
    bef1 = 1
    print(bef1, end = '')
    while True:        
        rst = bef2 + bef1
        if rst > n:
            break
        print(', {}'.format(rst), end = '')
        bef2 = bef1
        bef1 = rst
print()


# 간단화 <n 이하의 피보나치 수열 출력>
n = int(input('정수를 입력하세요 >> '))
a, b = 0, 1
print('0', end = '')
while b <= n:
    print(', {}'.format(b), end = '')
    a, b = b, a+b # 동시에 선언해야만 함
print()

# 리스트 이용
n = int(input('정수를 입력하세요 >> '))
result = [0, 1]
while 1:
    temp = result[-1] + result[-2]
    if temp <= n:
        result.append(temp)
    else:
        break
for i in range(len(result)):
    print(result[i], end = ' ')