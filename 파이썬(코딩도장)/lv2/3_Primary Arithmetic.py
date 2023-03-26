# 2023 - 출력 세부사항 적용 x
# line 15에 왜 k가 assignment 전에 사용되었다고 뜨는지 모르겠음
optlist = []
while True:
    lst = list(input('두 양의 정수를 공백으로 구분하여 입력하세요 >> ').split())
    if lst == ['0', '0']:
        break
    cnt = carry =0
    for i in range(max(len(lst[0]), len(lst[1]))):
        try:
            k = int(lst[0][-(i+1)]) + int(lst[1][-(i+1)]) + carry
        except:
            k = int(str(max(int(lst[0]), int(lst[1])))[-(i+1)]) + carry
        finally:
            if k >= 10:
                cnt += 1
                carry = 1
            else:
                carry = 0

    optlist.append(cnt)
for i in range(len(optlist)):
    print('{} carry operation.'.format(optlist[i]))




# 처음 코딩
optlist = []
while True:
    dic = {}
    a, b = input('양의 정수 두 개를 공백으로 구분하여 입력하세요 >> ').split()
    if a == b == '0':
        break
    a, b = a.zfill(max(len(a), len(b))), b.zfill(max(len(a), len(b)))
    dic[a] = b
    cnt = 0
    carry = 0
    for i in range(len(list(dic.keys())[0])):
        if int(list(dic.keys())[0][-(i+1)]) + int(list(dic.values())[0][-(i+1)]) + carry >= 10:
            cnt += 1
            carry = 1
        else:
            carry = 0
    if cnt == 0:
        optlist.append('No carry operation.')
    elif cnt == 1:
        optlist.append('1 carry operation.')
    else:
        optlist.append('{} carry operations.'.format(cnt))
for i in range(len(optlist)):
    print(optlist[i])

# 간단화 : 로그 활용
from math import log10
a,b = map(int, input('? ').split())
while all((a,b)):
    print(sum([(lambda x : (a%x+b%x)/x)(10**(n+1)) for n in range(int(max(log10(a),log10(b)))+1)]))
    a,b = map(int,input('? ').split())