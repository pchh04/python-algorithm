# 처음 코딩
ipttime = list(map(int, input('현재 시간을 입력하세요 >> ').split(':')))
gohome = 17*60*60 + 30*60 + 0
remaintime = gohome - (ipttime[0]*60*60 + ipttime[1]*60 + ipttime[2])
if remaintime < 0: remaintime += 24*60*60
h = remaintime // 3600
m = (remaintime % 3600) // 60
s = (remaintime % 3600) % 60
print('남은 시간은 {}:{}:{} 입니다.'.format(str(h).zfill(2), str(m).zfill(2), str(s).zfill(2)))