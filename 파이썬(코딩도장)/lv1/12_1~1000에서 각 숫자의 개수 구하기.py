# 2023
list = []
for i in range(1, 1001):
    for j in str(i):
        list.append(j)
for i in range(10):
    print('{}의 개수는 {}개'.format(i, list.count(str(i))))

# 처음 코딩
numlist = list(range(10))
wholenumlist = []
for i in range(1, 1001):
    for j in range(len(str(i))):
        wholenumlist.append(str(i)[j])
for k in range(10):
    print('{}의 개수 : {}'.format(k, wholenumlist.count(str(k))))

# 딕서너리 이용 간단화
count = {x:0 for x in range(10)}
for x in range(1, 1001):
    for i in str(x):
        count[int(i)] += 1
for i in range(10):
    print('{}의 개수 : {}'.format(i, count[i]))

# 간단화
for i in range(10):
    print('{}의 개수 : {}'.format(i, str(list(range(1, 1001))).count(str(i))))