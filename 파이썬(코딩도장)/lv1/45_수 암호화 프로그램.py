# 처음 코딩
from math import floor
num = int(input('수를 입력하세요 >> '))
print('암호화 코드 : {}'.format(floor(num**0.5*1000) - num))