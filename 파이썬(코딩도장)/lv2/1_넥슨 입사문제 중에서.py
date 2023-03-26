# 2023
numset = {x for x in range(1, 5001)}
for i in range(1, 5001):
    k = i
    for j in str(i):
        k += int(j)
    numset -= {k}
print(sum(numset))

# 처음 코딩(함수 활용 : 숫자가 바껴도 쓸 수 있도록)
def self_num(n):
    global gen_num
    gen_num = set()
    for i in range(1, n):
        sum = 0
        for j in range(len(str(i))):
            sum += int(str(i)[j])
        sum += i
        gen_num.add(sum)
    whole_num = set(list(range(n)))      # list에서 set으로 변환할 필요 없이 set에서도 range함수 사용 가능
    return whole_num - gen_num
print('{}'.format(sum(self_num(5000))))

# 처음 코딩(n = 5000일때의 값만 출력)
# <주의사항> -- 위 코딩에서는 sum이 함수 내 지역변수로 사용되어 문제가 없었지만
#              아래의 코딩에서는 sum을 변수로 사용하게 되면 함수 sum과 혼동되어 오류가 남
gen_num = set()
for i in range(1, 5000):
    sumn = 0
    for j in range(len(str(i))):
        sumn += int(str(i)[j])
    sumn += i
    gen_num.add(sumn)
print(sum(set(list(range(5000))) - gen_num))

# set comprehension(list comprehension과 유사)을 이용한 한줄코딩
# comprehension 안에 comprehension 사용 가능
print(sum(set(range(1, 5000)) - {i + sum([int(x) for x in str(i)]) for i in range(1, 5000)}))