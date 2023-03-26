#2023
namelist = '이유덕,이재영,권종표,이재영,박민호,강상희,이재영,김지완,최승혁,이성연,박영서,박민호,전경헌,송정환,김재성,이유덕,전경헌'.split(',')
kcount = lcount = ljycount = 0
for i in range(len(namelist)):
    if namelist[i][0] == '김':
        kcount += 1
    elif namelist[i][0] == '이':
        lcount += 1
        if namelist[i] == '이재영':
            ljycount += 1
print('김씨는 {}명, 이씨는 {}명 입니다. 이재영이란 이름은 {}번 반복됩니다.'.format(kcount, lcount, ljycount))
namelist = list(set(namelist))
print(namelist)
print(sorted(namelist))


#처음 코딩
str = '이유덕,이재영,권종표,이재영,박민호,강상희,이재영,김지완,최승혁,이성연,박영서,박민호,전경헌,송정환,김재성,이유덕,전경헌'
name = str.split(',')

# 김씨와 이씨가 몇 번 반복되는지 + 이재영이 몇 번 반복되는지
kimcnt = leecnt = ljycnt = 0
for i in range(len(name)):
    if name[i][0] == '김':
        kimcnt += 1
    elif name[i][0] == '이':
        leecnt += 1
        if name[i] == '이재영':
            ljycnt += 1
print('김씨는 {}명, 이씨는 {}명 입니다.'.format(kimcnt, leecnt))
print('이재영은 {}번 반복됩니다.'.format(ljycnt))

# 중복을 제거한 이름 출력
nameset = set()
for i in range(len(name)):
    nameset.add(name[i])
print('중복을 제거한 이름 : {}'.format(nameset))
print('중복을 제거한 이름을 오름차순으로 정렬 : {}'.format(sorted(nameset)))

######################################
# 간단화(17줄 -> 5줄)
print('-'*50)
# 김씨/이씨 반복 횟수 출력
firstname = [i[0] for i in name]
print('김씨는 {}명, 이씨는 {}명 입니다.'.format(firstname.count('김'), firstname.count('이')))
# 이재영 반복 횟수
print('이재영은 {}번 반복됩니다.'.format(name.count('이재영')))
# 중복을 제거한 이름 출력(리스트로 출력한다고 가정)
print('중복을 제거한 이름 : {}'.format(list(set(name))))
# 중복제거 + 오름차순 정렬
print('중복을 제거한 이름을 오름차순으로 정렬 : {}'.format(sorted(list(set(name)))))