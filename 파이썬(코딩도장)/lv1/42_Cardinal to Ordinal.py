# 처음 코딩
iptlist = input('기수를 공백으로 구분하여 입력하세요 >> ').split()
for i in range(len(iptlist)):
    if iptlist[i][-1:] == '1' and iptlist[i][-2:] != '11':
        print(iptlist[i] + 'st', end = ' ')
    elif iptlist[i][-1:] == '2' and iptlist[i][-2:] != '12':
        print(iptlist[i] + 'nd', end = ' ')
    elif iptlist[i][-1:] == '3' and iptlist[i][-2:] != '13':
        print(iptlist[i] + 'rd', end = ' ')
    else:
        print(iptlist[i] + 'th', end = ' ')