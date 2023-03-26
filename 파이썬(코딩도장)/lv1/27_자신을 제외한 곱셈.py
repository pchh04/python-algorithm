# 처음 코딩
ipt = input('수를 공백으로 구분하여 입력하세요 >> ').split()
for i in range(len(ipt)):
    ipt[i] = int(ipt[i])
print(ipt)
optlist = []
for i in range(len(ipt)):
    prod = 1
    for j in range(len(ipt)):
        if i != j:
            prod *= ipt[j]
    optlist.append(prod)

print(optlist)