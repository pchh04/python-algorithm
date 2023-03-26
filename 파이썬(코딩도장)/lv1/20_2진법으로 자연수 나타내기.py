# 2023
iptnum = int(input('자연수 N을 입력하세요 >> '))
output = ''
while True:
    output  = str(iptnum%2) + output
    iptnum //= 2
    if iptnum == 1:
        output = '1' + output
        break
print(output)

# 재귀
def binary(d):
    return '' if d == 0 else binary(d//2) + str(d%2)
print(binary(int(input('자연수 입력 >> '))))

# 처음 코딩
ipt = int(input('2진수로 변환할 10진수를 입력하세요 >> '))
opt = ''
while True:
    opt = str(ipt % 2) + opt
    ipt = ipt // 2   # divmod 함수를 이용하여 몫과 나머지를 동시에 받을 수 있음
    if ipt < 2:
        opt = str(ipt) + opt
        break
print(opt)