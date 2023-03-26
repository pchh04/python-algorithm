# 처음 코딩(공백제외 149)
def f():
    a = '*'.center(11)
    print(a+'\n'+a)
f()
l = [4, 3, 2, 0, 2, 3, 4]
for i in range(7):
    if i == 3:
        print('**       **')
        continue
    print(('*'+' '*(1+(4-l[i])*2)+'*').center(11))
f()

# 단순 출력코딩
print("     *\n     *\n    * *\n   *   *\n  *     *\n**       **\n  *     *\n   *   *\n    * *\n     *\n     *")

# 간단화
r = range(-5, 6)
for y in r:
    l=''
    for x in r:
        a,b=abs(x),abs(y)
        l+=(' ','*')[a+b==4 or(5,0)in[(a,b),(b,a)]]
    print(l)