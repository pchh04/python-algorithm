# 처음 코딩
from math import sqrt
numlist = list(map(int, input('밑변과 높이를 공백으로 구분하여 입력하세요 >> ').split()))
print(sqrt(numlist[0]**2 + numlist[1]**2))

# sqrt 함수를 **0.5로 대체 가능, list(map(int, list))를 list로 받지 않고 두 개의 변수에 바로 저장 가능
a, b = list(map(int, input('밑변과 높이를 공백으로 구분하여 입력하세요 >> ').split()))
print((a**2 + b**2)**0.5)