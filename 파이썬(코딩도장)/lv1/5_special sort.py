#2023
iptstr = input('숫자 입력')
iptlist = iptstr.split(' ')
newlist = []
minuscnt = 0
for i in range(len(iptlist)):
    if iptlist[i][0] == '-':
        newlist.insert(minuscnt, iptlist[i])
        minuscnt += 1
    else:
        newlist.append(iptlist[i])
print(newlist)

#다른 코딩
iptstr = input('숫자 입력')
iptlist = iptstr.split(' ')
newlist = []
popcnt = 0
for i in range(len(iptlist)):
    if iptlist[i-popcnt][0] == '-':
        newlist.append(iptlist[i-popcnt])
        iptlist.pop(i-popcnt)
        popcnt += 1
newlist.extend(iptlist)
print(newlist)


# 처음 코딩
str = '-1 1 3 -2 2'
sstr = str.split(' ')
for i in range(len(sstr)):
    if sstr[i][0] == '-':
        cnt = 0
        for k in range(i):
            if sstr[k][0] == '-':
                cnt += 1
        sstr.insert(cnt, sstr[i])
        del sstr[i+1]
for i in range(len(sstr)):
    print('{}'.format(sstr[i]), end = ' ')

print()
# list 활용 다른 예시
str = '-1 1 3 -2 2'
num = str.split(' ')
alist = []
blist = []
for i in range(len(num)):
    if int(num[i]) > 0:
        alist.append(num[i])
    elif int(num[i]) < 0:
        blist.append(num[i])
for i in range(len(sstr)):
    print('{}'.format((blist+alist)[i]), end = ' ')

print()
# 간단한 답
s = '-1 1 3 -2 2'
def do(str):
    nlist = str.split(' ')
    return [x for x in nlist if int(x)<0] + [x for x in nlist if int(x)>0]
for i in range(len(s.split(' '))):
    print('{}'.format(do(s)[i]), end = ' ')
