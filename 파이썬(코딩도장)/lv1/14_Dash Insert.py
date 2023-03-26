# 2023
ipt = input('숫자로 구성된 문자열을 입력하세요 >> ')
numlist = []
for i in range(len(ipt)):
    numlist.append(int(ipt[i])%2)
print(ipt[0], end = '')
for i in range(1, len(numlist)):
    if numlist[i-1] == numlist[i] == 1:
        print('-{}'.format(ipt[i]), end = '')
    elif numlist[i-1] == numlist[i] == 0:
        print('*{}'.format(ipt[i]), end = '')
    else:
        print(ipt[i], end = '')


# 처음 코딩
def dashinsert(str):
    numlist = [int(i)%2 for i in str]
    for i in range(len(numlist)-1):
        print(str[i], end = '')
        if numlist[i] == numlist[i+1]:
            if numlist[i] == 0:
                print('*', end = '')
            else:
                print('-', end = '')
    print(str[len(numlist)-1])

x = input('숫자로 구성된 문자열을 입력하세요 >> ')
dashinsert(x)

# 정규식 ?