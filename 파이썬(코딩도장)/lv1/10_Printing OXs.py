# 처음 코딩
n = int(input('수를 입력하세요 >> '))
for i in range(n):
    print('{}{}'.format('O'*(n-i-1), 'X'*(i+1)))