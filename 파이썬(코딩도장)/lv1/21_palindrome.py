# 처음 코딩
from math import ceil
numlist = []
for i in range(100, 1000):
    for j in range(100, 1000):
        if str(i*j)[:ceil(len(str(i*j))/2)] == str(i*j)[ceil(len(str(i*j))/2):][::-1]:
            numlist.append(i*j)
print(max(numlist))

# 대칭 판별 방법 : if str[::-1] == str~ ->  line 6 수정 가능
numlist = []
for i in range(100, 1000):
    for j in range(100, 1000):
        if str(i*j)[::-1] == str(i*j):
            numlist.append(i*j)
print(max(numlist))