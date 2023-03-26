#2023
sum1 = 0
for i in range(1000):
    if i%3 == 0 or i%5 == 0:
        sum1 += i
print(sum1)

# 처음 코딩
num = set()

for i in range(999):
    if (i+1)%3 == 0:
        num.add(i+1)

for i in range(999):
    if (i+1)%5 == 0:
        num.add(i+1)

print(sum(num))

# list comprehension 쓰지 않고 좀 더 간단히
num1 = []
for i in range(1000):   # 더한 값만 출력하면 되므로 0을 더하는 것은 상관없음
    if i%3==0 or i%5==0:
        num1.append(i)
print(sum(num1))

# list comprehension 사용
print(sum(list([x for x in range(1000) if x%3==0 or x%5==0])))

# set 자료형과 교집합 사용
set3 = set(range(3, 1000, 3))
set5 = set(range(5, 1000, 5))
print(sum(set3 | set5))