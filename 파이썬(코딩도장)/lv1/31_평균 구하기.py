# 처음 코딩
ipt = input('수를 공백으로 구분하여 입력하세요 >> ').split()
for i in range(len(ipt)):
    ipt[i] = int(ipt[i])
print(sum(ipt)/len(ipt))

# map 이용 간단화 : map object를 list로 변환한 후 사용
ipt = list(map(int, input('수를 공백으로 구분하여 입력하세요 >> ').split()))
print(sum(ipt)/len(ipt))