# 2023
for i in range(1, 1000):
    for j in range(1, 1000-i+1):
        for k in range(1, 1000-i-j+1):
            if i**2+j**2 == k**2 and i+j+k == 1000:
                print(i, j, k)
                print(i*j*k)
                break


# 처음 코딩 -> 시간 오래 걸림
for c in range(1000):
    for b in range(c):
        for k in range(b):
            a = k
            if a + b + c == 1000 and a**2 + b**2 == c**2:
                print(a, b, c)
                print(a * b * c)

# 삼각형의 성질 이용한 간단화
# 제일 긴 변의 길이는 나머지 두 변의 길이의 합보다 작다 -> a < b < c < 500
for a in range(500):
    for b in range(a, 500):    # a <= b
        for c in range(b, 500):    # a <= b <= c < 500
            if a+b+c == 1000 and a**2 + b**2 == c**2:
                print('a = {}, b = {}, c = {}, a*b*c = {}'.format(a, b, c, a*b*c))

# 간단화, i**2 / (1000-i)는 한 변의 길이에 대한 공식
import numpy as np
a_b = [i for i in range(1, 500) if (i**2 / (1000-i)) % 1 == 0] # 여기서 i는 c를 의미
print(np.prod(a_b)* (1000 - sum(a_b))) # np.prod는 리스트 내부의 원소들의 곱을 반환해줌, 즉, np.prod(a_b) = a*b