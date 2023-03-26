# 처음 코딩
ipt = input('입력하세요 >> ')
opt = ''
numlist = [x for x in '1234567890']
for i in range(len(ipt)):
    if ipt[i] in numlist:
        opt += ipt[i]
print(opt)

# 간단화 - .isdigit()
print(''.join(i for i in input("입력하세요 >> ") if i.isdigit()))