# matrix 쓰는 건지?

a, b = input('두 개의 수를 공백 한 칸으로 구분하여 입력 >> ').split(' ')
a, b = int(a), int(b)
while True:
    for i in range(a*b):
        print(i, end = '  ')