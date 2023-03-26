# 2023
iptlist = list(map(int, input('오름차순으로 정렬된 수를 공백으로 구분하여 입력하세요 >> ').split()))
res = iptlist[1] - iptlist[0]
for i in range(1, len(iptlist) - 1):
    if iptlist[i+1] - iptlist[i] < res:
        res = iptlist[i+1] - iptlist[i]
        a, b = i, i+1
print('({}, {})'.format(iptlist[a], iptlist[b]))

# 처음 코딩
ipt = list(map(int, input('1차원 값들을 공백 한 칸으로 구분하여 입력하세요 >> ').split()))
ipt.sort()
rst = []
for i in range(len(ipt)-1):
    rst.append(int(ipt[i+1]) - int(ipt[i]))
cnt = rst.count(min(rst))
for i in range(cnt):
    print('거리가 최소인 쌍은 {' + '{}, {}'.format(ipt[rst.index(min(rst), i)],
         ipt[rst.index(min(rst), i) + 1]) + '}')

# zip 사용 간단화
s = [1, 3, 5, 8, 13, 17, 20]
pairs = list(zip(s[0:], s[1:]))
pairs.sort(key = lambda x : x[1] - x[0])
print(pairs[0])