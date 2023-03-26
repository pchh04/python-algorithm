# 처음 코딩
lst = []
iptlist = []
numdict = dict(zip([x for x in 'ABCDEFGHIJKLMNOPRSTUVWXY'], [x for x in '222333444555666777888999']))
for i in range(int(input('입력할 전화번호의 개수를 입력하세요 >> '))):
    iptlist.append(input('전화번호를 입력하세요 >> '))
    for j in range(iptlist[j].count('-')):
        iptlist.pop(iptlist.index('-'))
    for j in range(len(iptlist[j])):