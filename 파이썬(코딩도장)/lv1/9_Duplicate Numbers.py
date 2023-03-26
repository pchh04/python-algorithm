# 2023
ipt = input('문자열을 입력하세요 >> ')
numlist = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
check = True
if len(ipt) != 10:
    check = False
else:
    for i in range(10):
        if numlist[i] not in ipt:
            check = False
print(check)


# 처음 코딩
def chknum(num):
    numlist = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    iptnumlist = [x for x in str(num)]
    chk = True
    if len(num) == 10:
        for i in range(10):
            chk = num[i] in numlist and iptnumlist.count(numlist[i]) == 1
            if chk == False:
                break
    else:
        chk = False
    print(chk)

num = input('숫자를 입력하세요 >> ')
chknum(num)

# 간단화 1 (list의 sort 활용)
def chknum2(num):
    if sorted([i for i in num]) == list(range(10)):   # list.sort()가 아닌 sorted(list)를 사용하여야 함 : list.sort()는 리스트를 정렬된 상태로 변환시키기는 하지만, list.sort()의 출력값이 정렬된 리스트는 아님. 반면 sorted(list)를 사용하면 리스트의 값은 변화시키지 않으나 정렬된 리스트를 출력해 줌
        print(True)
    else:
        print(False)
ipt = input('숫자를 입력하세요 >> ')
chknum2(ipt)

# 간단화 2 (set 활용 : 중복 안되는 성질 활용)
def chknum3(num):
    if len(num) == len(set(num)) == 10:
        print(True)
    else:
        print(False)
ipt = input('숫자를 입력하세요 >> ')
chknum3(ipt)