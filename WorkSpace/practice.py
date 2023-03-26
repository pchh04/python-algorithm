from math import log10
a,b = map(int,input('? ').split())
while all((a,b)):
    print(sum([(lambda x : (a%x+b%x)/x)(10**(n+1)) for n in range(int(max(log10(a),log10(b)))+1)]))
    a,b = map(int,input('? ').split())