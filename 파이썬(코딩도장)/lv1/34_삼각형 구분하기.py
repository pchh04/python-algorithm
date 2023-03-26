# 처음 코딩 - 음수 각 포합하지 않음
ipt = list(map(int, input('3개의 각을 입력하세요 >> ').split()))
if len(ipt) != 3 or 0 in ipt or sum(ipt) != 180:
    print('삼각형이 아닙니다.')
else:
    for i in range(3):
        if ipt[i] > 90:
            print('둔각삼각형입니다.')
            break
    else:
        if 90 in ipt:
            print('직각삼각형입니다.')
        else:
            print('예각삼각형입니다.')

# 간단화 + 음수 각 포함
def tri(v):
    if len(v) != 3 or sum(v) != 180 or min(v) <= 0: print('삼각형이 아닙니다.')
    else: print('둔각 삼각형' if max(v) > 90 else '직각삼각형' if 90 in v else '예각삼각형')
tri(list(map(int, input('세 각을 입력하세요 >> ').split())))