# 처음 코딩
numlist = list(map(int, [x for x in input('양의 정수를 입력하세요 >> ')]))
print('각 자릿수의 합은 {}입니다.'.format(sum(numlist)))

# 간단화 1 : map인자에 sum함수 사용 가능, map은 리스트 컴프리헨션 과정 없이도 문자열을 자동으로 분리해줌
print(sum(map(int, input('양의 정수를 입력하세요 >> '))))

# 간단화 2 : eval 함수 사용
print(eval('+'.join(input('양의 정수를 입력하세요 >> '))))