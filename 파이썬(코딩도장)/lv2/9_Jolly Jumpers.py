# 2023
iptlist = list(map(int, input('3000 이하의 정수와 수열을 공백으로 구분하여 입력하세요 >> ').split()))
k = iptlist.pop(0)
rstlist = []
for i in range(len(iptlist)-1):
    rstlist.append(abs(iptlist[i]-iptlist[i+1]))
if sorted(rstlist) == [x for x in range(1, k)]:
    print('Jolly')
else:
    print('Not Jolly')



# 처음 코딩
ipt = list(map(int, input('수열의 길이 n(3000 이하)과 Jolly Jumper인지 판단할 수열을 입력하세요 >> ').split()))
cnt = ipt.pop(0)
sublist = []
for i in range(len(ipt) - 1):
    sublist.append(abs(ipt[i] - ipt[i+1]))
if sorted(sublist) == list(range(1, len(sublist)+1)):
    print('Jolly')
else:
    print('Not Jolly')