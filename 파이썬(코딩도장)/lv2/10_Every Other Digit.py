# 2023
ipt = input('문자열을 입력하세요 >> ')
for i in range(len(ipt)):
    if ipt[i].isdigit() and (i+1)%2 == 0:
        print('*', end = '')
    else:
        print(ipt[i], end = '')



# 처음 코딩
ipt = input('문자열을 입력하세요 >> ')
numlist = list(map(str, list(range(10))))
for i in range(len(ipt)):
    if ipt[i] in numlist and i%2 == 1:   # if문 대신 range함수에서 step = 2로 지정하면 짝수만 받아올 수 있다.
        print('*', end = '')
    else:
        print(ipt[i], end = '')

# 간단화 : True, False가 리스트의 인덱스로 쓰일 경우 각각 1, 0으로 변환되어 쓰임
s = input('문자열을 입력하세요 >> ')
print(''.join([[s[i], '*'][i&1 == 1 and s[i].isdigit()] for i in range(len(s))]))