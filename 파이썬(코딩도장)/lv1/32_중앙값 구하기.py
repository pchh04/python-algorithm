# 처음 코딩
ipt = list(map(int, input('수를 공백으로 구분하여 입력하세요 >> ').split()))
if len(ipt) % 2 == 0:
    print((ipt[len(ipt)//2 -1] + ipt[len(ipt)//2])/2)
else:
    print(ipt[len(ipt)//2])