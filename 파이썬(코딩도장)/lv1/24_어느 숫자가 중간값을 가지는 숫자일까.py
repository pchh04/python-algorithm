# 처음 코딩
numlist = input('3개의 숫자를 공백으로 구분하여 입력하세요 >> ').split()
for i in range(3):
    numlist[i] = int(numlist[i])
print(sorted(numlist)[1])