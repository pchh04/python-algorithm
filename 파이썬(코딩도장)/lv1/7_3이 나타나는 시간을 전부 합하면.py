#2023
count = 0
for i in range(24):
    if '3' in str(i):
        count += 60*60
    else:
        for j in range(60):
            if '3' in str(j):
                count += 60
print(count)

# 처음 코딩
exist3 = []
for i in range(24):
    for j in range(60):
        if (str(3) in str(i)) or (str(3) in str(j)):
            exist3.append(str(i*100 + j).zfill(4))
print('3이 표시되는 총 시간은 {}초 입니다.'.format(len(exist3)*60))
#print(exist3) # 3이 들어가는 시간 보기