# 처음 코딩
lst = []
for i in range(int(input('입력할 정수의 개수를 입력하세요 >> '))):
    k = int(input('정수를 입력하세요 >> '))
    cnt = 0
    while True:
        if cnt == 1000:
            print('Error')
            break
        if str(k) == str(k)[::-1]:
            lst.append([cnt, k])
            break
        cnt += 1
        k = k + int(str(k)[::-1])
for i in range(len(lst)):
    print(lst[i][0], lst[i][1])


# 재귀 이용 간단화
def fnc(n, chk = 0):
    try:
        if str(n) == str(n)[::-1]:
            print(chk, n)
        else:
            fnc(n + int(str(n)[::-1]), chk + 1)
    except RecursionError:
        print('Error')
for i in range(int(input('입력할 정수의 개수를 입력하세요 >> '))):
    fnc(int(input('정수를 입력하세요 >> ')))