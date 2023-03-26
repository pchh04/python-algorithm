# 처음 코딩
ipt = input('수를 입력하세요 >> ')
if ipt.isdigit():
    print('정수입니다.')
else:
    try:
        float(ipt)
    except:
        print('math error')
    else:
        print('소수입니다.')

# 정수 부분, 소수 부분 활용
try:
    ipt = float(input('수를 입력하세요 >> '))
except:
    print('math error')
else:
    if ipt == int(ipt):
        print('정수입니다.')
    else:
        print('소수입니다.')