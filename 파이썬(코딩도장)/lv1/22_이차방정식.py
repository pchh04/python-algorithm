#처음 코딩
from math import sqrt
a, b, c = input('a, b, c를 공백으로 구분하여 입력하세요 >> ').split()
a, b, c = float(a), float(b), float(c)
ansset = set()
if b**2-4*a*c < 0:
    print('해가 없습니다.')
else:
    ansset.add(round((-b+sqrt(b**2-4*a*c))/(2*a)))
    ansset.add(round((-b-sqrt(b**2-4*a*c))/(2*a)))
if len(ansset) == 1:
    print('중근을 가집니다.', ansset)
elif len(ansset) == 2:
    print('두 개의 해를 가집니다.', ansset)