# 처음 코딩
odd = even = 0
ipt = list(map(int, input('수를 공백으로 구분하여 입력하세요 >> ').split()))
for i in ipt:
    if i%2 == 0:
        even += 1
    else:
        odd += 1
print('홀수 {}개, 짝수 {}개'.format(odd, even))

# 간단화 : 짝수의 개수는 (전체 개수) - (홀수 개수)\
odd = 0
ipt = list(map(int, input('수를 공백으로 구분하여 입력하세요 >> ').split()))
for i in ipt:
    if i%2 == 1:
        odd += 1
print('홀수 {}개, 짝수 {}개'.format(odd, len(ipt)-odd))
