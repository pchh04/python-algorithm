# 처음 코딩
from random import *
rsp = ['가위', '바위', '보']
com = choice(rsp)
user = input('가위, 바위, 보 중 하나를 입력하세요 >> ')
if com == user:
    print('컴퓨터 : {}, 사용자 : {}   ...   비겼습니다.'.format(com, user))
elif (com == '가위' and user == '보') or (com == '바위' and user == '가위') or (com == '보' and user == '바위'):
    print('컴퓨터 : {}, 사용자 : {}   ...   졌습니다.'.format(com, user))
else:
    print('컴퓨터 : {}, 사용자 : {}   ...   이겼습니다.'.format(com, user))