# 처음 코딩
cnt = 0
for i in range(10000):
    if '8' not in str(i):
        cnt += 1
print(cnt)

# 간단화
print(len([x for x in range(10000) if '8' not in str(x)]))

# 발상의 전환 : 8이 들어가지 않는 수의 개수는 8을 제외한 나머지 9개의 아라비아 숫자 즉 9진법으로 10000
print(int('10000', 9))