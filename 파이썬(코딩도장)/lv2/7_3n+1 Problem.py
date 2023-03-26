# 2023
a, b = map(int, input('두 숫자를 공백으로 구분하여 입력하세요 >> ').split())
optlist= []
for i in range(a, b+1):
    lst = [i]
    while i != 1:
        if i%2 == 0:
            i /= 2
            lst.append(i)
        else:
            i = i * 3 + 1
            lst.append(i)
    optlist.append(len(lst))
print(max(optlist))



# 처음 코딩
i, j = map(int, input('정수 i와 j를 입력하세요 >> ').split())
cntlist = []
for x in range(i, j+1):
    cnt = 0   # count를 0이 아닌 1로 시작하여 한 줄 줄일 수 있음
    while x != 1:
        if x % 2 == 1:
            cnt += 1
            x = x* 3 + 1
        else:
            cnt += 1
            x = x / 2   # whlie 내부의 과정을 << -(n%2-1)*(n/2) + (n%2)*(n*3+1) >> 의 과정으로 한줄 축약할 수 있음
    cnt += 1
    cntlist.append(cnt)
print('{}\t{}\t{}'.format(i, j, max(cntlist)))