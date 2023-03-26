from random import choice
randnum = choice(range(1, 101))
cnt = 1
while True:
    ipt = int(input('1~100 숫자 입력 >> '))
    if ipt < randnum:
        print('UP')
        cnt += 1
    elif ipt > randnum:
        print('DOWN')
        cnt += 1
    else:
        print('정답입니다! {}회 만에 맞혔네요'.format(cnt))
        break