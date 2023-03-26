# 파이썬에서의 배열 : 여러 원소를 하나의 묶음으로 관리 + 원소간 순서 존재 -> 리스트, 튜플

# 2023
n = int(input('입력할 정수의 개수를 입력하세요 >> '))
sum = 0
for i in range(n):
    sum += int(input('정수를 입력하세요 >> '))
print('합 :', sum)
print('평균 :', sum/n)
del n, sum

# 처음 코딩(리스트는 배열)
num = int(input('입력할 정수의 개수 입력 >> '))
numlist = input('정수를 공백 한 칸으로 구분하여 입력 >> ').split(' ')
for i in range(num):
    numlist[i] = int(numlist[i])
print('입력한 정수의 합 : {}, 입력한 정수의 평균 : {}'.format(sum(numlist), sum(numlist)/num))
del num, numlist, i

# 배열 사용하지 않고 코딩
num = int(input('입력할 정수의 개수 입력 >> '))
nsum = 0
for i in range(num):
    iptnum = int(input('{}번째 정수 입력 >> '.format(i+1)))
    nsum += iptnum
print('입력한 정수의 합 : {}, 입력한 정수의 평균 : {}'.format(nsum, nsum/num))
del num, nsum, i, iptnum