# 처음 코딩
cnt = 1
n = 0
while cnt <= 31:
    n += 1
    print('com : ', end = '')
    while cnt <= 4*n - 2:
        print(cnt, end = ' ')
        cnt += 1
    print()
    ipt = input('수를 공백으로 구분하여 입력하세요 >> ')
    cnt = int(ipt.split()[-1]) +1
print('당신이 졌습니다.')