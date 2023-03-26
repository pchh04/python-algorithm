#2023
a, b = input("총 건수, 한 페이지에 보여줄 게시물 수를 콤마로 구분하여 입력 >> ").split(', ')
print("총 페이지 수 : {}".format((int(a)//int(b))+1))


#처음 코딩

from math import *

m = int(input('총 건수를 입력하세요 >>'))
n = int(input('한 페이지에 보여줄 게시물 수를 입력하세요 >>'))
print('총 페이지 수 : {}'.format(ceil(m/n)))