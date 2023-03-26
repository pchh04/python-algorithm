# 처음 코딩(어떤 계수가 0인 경우는 제외)
print('''1. ax + by + c = 0
2. a'x + b'y + c' = 0
각각의 계수를 입력하세요.

a, b, c, a', b', c' 순서로 공백으로 구분하여 입력하세요''')
lst = list(map(int, input().split()))
k = lst[0]/lst[3]
if k == lst[1]/lst[4]:
    if k == lst[2]/lst[5]:
        print('해가 무수히 많습니다.')
    else:
        print('해가 없습니다.')
else:    
    y = (k*lst[5] - lst[2]) / (lst[1] - k*lst[4])
    x = (-lst[1]*y - lst[2]) / lst[0]
    print('x = {}, y = {}'.format(x, y))