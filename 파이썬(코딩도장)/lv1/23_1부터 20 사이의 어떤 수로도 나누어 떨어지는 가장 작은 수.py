# 처음 코딩
num = 20
chk = False
while True:
    for i in range(1, 21):
        if num%i != 0:
            break
    else: chk = True
    if chk == True:
        print(num)
        break
    else:
        num += 20

# 간단화 : 소수들의 곱으로 나누어 떨어져야 하고, 11~20으로 나누어 떨어지는지만 검사하면 됨(그럼 1~10까지는 자동으로 나누어짐)
num = 2*3*5*7*11*13*17*19
chk = False
while True:
    for i in range(11, 21):
        if num%i != 0:
            break
    else: chk = True
    if chk == True:
        print(num)
        break
    else:
        num += 2*3*5*7*11*13*17*19

# reduce 함수 이용..~