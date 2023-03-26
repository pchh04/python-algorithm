# 2023
print(sum([str(x).count('8') for x in range(1, 10001)]))

# 처음 코딩
lst = []
for i in range(1, 10000):
    for j in range(len(str(i))):
        lst.append(str(i)[j])
print(lst.count('8'))

# 한 줄 코딩 - 하나의 문자열에서 개별 문자의 수를 count로 셀 수 있음
print(str(list(range(1, 10001))).count('8'))