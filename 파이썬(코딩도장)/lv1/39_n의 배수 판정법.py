# 처음 코딩
numlist = []
for i in range(int(input('입력할 정수의 개수를 입력하세요 >> '))):
    numlist.extend(list(map(int, input('입력 >> ').split())))
for i in range(int((len(numlist)/2))):
    while numlist[2*i]>0:
        numlist[2*i] -= numlist[2*i+1]
    if numlist[2*i] == 0:
        print(1)
    else:
        print(0)

# 간단화 - lambda 함수 이용
f = lambda x, n : x in range(0, x+1, n) # True, False로 결과 반환