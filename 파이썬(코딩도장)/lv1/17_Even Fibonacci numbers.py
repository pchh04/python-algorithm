# 2023
flist = [1, 2]
cnt = 0
while True:
    k = flist[cnt]+flist[cnt+1]
    if k <= 4000000:
        flist.append(k)
        cnt += 1
    else:
        break
print(sum([x for x in flist if x%2 == 0]))


# 처음 코딩
fib = [1, 2]
sum = 0
while True:
    if fib[-1] + fib[-2] > 4000000:
        break
    fib.append(fib[-1] + fib[-2])
for i in range(len(fib)):
    if fib[i] % 2 == 0:
        sum += fib[i]
print(sum)

# 간단화
a, b = [0, 1]    # 이와 같은 방법으로도 변수 지정 가능
sum = 0
while b <= 4000000:
    a, b = b, a + b
    if b % 2 == 0:
        sum += b    # 굳이 리스트에 넣지 않고 바로 더하기
print(sum)