# 2023
iptlist = input('문자열을 공백으로 구분하여 입력하세요 >> ').split()
k = int(iptlist.pop(0))
if k>=0:
    for i in range(k):
        temp = iptlist[-1]
        for j in range(len(iptlist)-1):
            iptlist[-(j+1)] = iptlist[-(j+2)]
        iptlist[0] = temp
else:
    k = -k
    for i in range(k):
        temp = iptlist[0]
        for j in range(len(iptlist)-1):
            iptlist[j] = iptlist[j+1]
        iptlist[-1] = temp
for i in range(len(iptlist)):
    print(iptlist[i], end = ' ')

# 처음 코딩
ipt = input('리스트를 회전할 값과 회전할 리스트를 문자열로 입력하세요 >> ')
cnt, cycle = ipt.split(' ', maxsplit = 1)
cycle = cycle.split()
if int(cnt) > 0:
    a = int(cnt) % len(cycle)
    for i in range(a):
        cycle.insert(i, cycle[-a+i])
    for i in range(a):
        cycle.pop()
elif int(cnt) < 0:
    a = -int(cnt) % len(cycle)
    for i in range(a):
        cycle.append(cycle[0])
        cycle.pop(0)
opt = str()
for i in range(len(cycle)):
    opt += cycle[i] + ' '
print(opt)

# 간단화
data = input('회전수와 문자열을 입력하세요 >> ').split()
rn = int(data.pop(0)) % len(data)  # pop은 첨자위치 항목 삭제와 동시에 삭제값 반환 -> 회전값을 삭제함과 동시에 계산
print(' '.join([(data * 3)[len(data) + i - rn] for i in range(len(data))]))

# collection 모듈의 deque를 활용한 코딩
import collections
datas = input("Input : ").split(" ")
cycleList = collections.deque(datas[1:])
cycleList.rotate(int(datas[0]))   # deque 자료형은 rotate 메소드를 사용 가능
print("Output :", " ".join(cycleList))