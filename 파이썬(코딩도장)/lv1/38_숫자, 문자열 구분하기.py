# 처음 코딩
numlist = [x for x in '1234567890']
ipt = input('문자열을 입력하세요 >> ')
stropt = ''
numopt = ''
for i in ipt:
    if i in numlist:
        numopt += i
    else:
        stropt += i
print('str : {}\nint : {}'.format(stropt, numopt))

# .join(), .isdigit() 이용하여 간단화 가능 - 문자열에 대한 메소드
ipt = input('문자열을 입력하세요 >> ')
print('str : {}\nint : {}'.format(''.join(x for x in ipt if not x.isdigit()), ''.join(x for x in ipt if x.isdigit())))