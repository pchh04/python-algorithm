# 2023
ipt1 = input("1번째 버전을 입력하세요 >>")
ipt2 = input("2번째 버전을 입력하세요 >>")
ipt1list = ipt1.split('.')
ipt2list = ipt2.split('.')
for i in range(min(len(ipt1list), len(ipt2list))):
    if int(ipt1list[i]) == int(ipt2list[i]): continue
    else:
        if int(ipt1list[i]) > int(ipt2list[i]):
            result = 1
        else:
            result = 2
        break
print('{}번째 버전이 더 높습니다.'.format(result))



# 처음 코딩
ver1 = input('첫 번째 버전을 입력하세요 >> ')
ver2 = input('두 번째 버전을 입력하세요 >> ')
ver1list, ver2list = ver1.split('.'), ver2.split('.')
for i in range(min(len(ver1list), len(ver2list))):
    if ver1list[i] == ver2list[i]:       # 이때 부등호 양쪽의 값은 문자열이지만, 비교 결과는 동일하게 나옴
        continue
    elif ver1list[i] > ver2list[i]:
        print('{} > {}'.format(ver1, ver2))
        break
    else:
        print('{} > {}'.format(ver2, ver1))
        break