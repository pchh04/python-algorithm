# 2023
iptstr = input('문자열을 입력하세요 >> ')
iptnum = int(input('자연수 n을 입력하세요 >> '))
apb = [x for x in 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz']
for i in iptstr:
    print(apb[apb.index(i) + 2*iptnum], end = '')



# 처음 코딩
uapb = [x for x in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ']
lapb = [x for x in 'abcdefghijklmnopqrstuvwxyz']
ipt = input('변환할 문장과 숫자 n을 입력하세요 >> ')
cnt = int(ipt[-1])
newstr = str()
for i in ipt[:-2]:
    if i in uapb:
        newstr += uapb[(uapb.index(i) + cnt) % len(uapb)]
    elif i in lapb:
        newstr += lapb[(lapb.index(i) + cnt) % len(lapb)]
    else:
        newstr += i
print(newstr)