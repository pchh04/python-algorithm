#2023
from math import *

# 단순
def perfectnum(num):
    pnumlist = [1]
    for i in range(1, num+1):
        numlist = [x for x in range(1, i) if i%x==0]
        if sum(numlist) == i:
            pnumlist.append(i)
    return pnumlist
iptnum = int(input('자연수 N을 입력하세요 >> '))
print(perfectnum(iptnum))


# 유클리드
def perfectnum(num):
    perfectlist = []
    for i in range(1, num+1):
        list = []
        for j in range(1, floor(sqrt(i))+1):
            if i % j == 0:
                list.append(j)
                list.append(i/j)
        if sum(list) == 2*i:
            perfectlist.append(i)
    return perfectlist
ipt = int(input('자연수 N을 입력하세요 >> '))
print(perfectnum(ipt))



# 처음 코딩
n = int(input('자연수 N을 입력하세요 >> '))
for i in range(1, n+1):
    lst = []
    for j in range(1, i):
        if i%j == 0:
            lst.append(j)
    if sum(lst) == i:
        print(i, end = ' ')

print()
  
# 실행 시간 절감
from math import *

def isPerfectNumber(n):
    divisors = [1, ]
    for i in range(2, floor(sqrt(n)) + 1):
        if n % i == 0:
            divisors.append(i)
            divisors.append(int(n / i))
    return sum(divisors) == n

def main():
    perfectNumbers = []
    N = int(input("Input Number : "))
    for i in range(1, N+1):
        if isPerfectNumber(i):
            perfectNumbers.append(i)
    if perfectNumbers:
        print("PerfectNumber :", perfectNumbers)

if __name__ == '__main__':
    main()
