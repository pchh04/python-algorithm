# 2023
lst = [False] * int(input('수를 입력하세요 >> '))
for i in range(1, len(lst)+1):
    for j in range(1, len(lst)+1):
        if j%i == 0:
            lst[j-1] = not lst[j-1]
print(['no', 'yes'][lst[-1]])

# 마지막 전구의 최종 상태만 알아내면 됨
ipt = int(input('수를 입력하세요 >> '))
chk = False
for i in range(1, ipt+1):
    if ipt%i == 0:
        chk = not chk
print(['no', 'yes'][chk])



# 처음 코딩
while True:
    n = int(input('전구의 개수를 입력하세요 >> '))
    if n == 0: break
    k = 0
    for i in range(n):
        if n%(i+1) == 0:
            if k == 0:
                k = 1
            elif k == 1:
                k = 0
    if k == 0:
        print('no')
    elif k == 1:
        print('yes')

# 간단화 : 홀수 개의 약수를 가지는 숫자의 특징 - 어떤 수가 제곱수일 떄 홀수 개의 약수를 가짐
from math import *   # sqrt 함수는 math를 import 해서 사용
while True:
    n = int(input('전구의 개수를 입력하세요 >> '))
    if n == 0: break
    if round(sqrt(n)) == sqrt(n):
        print('yes')
    else:
        print('no')