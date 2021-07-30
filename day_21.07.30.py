### 1. 10~99 사이 난수 생성 중 13 나오면 중단

# import random
#
# n = int(input('난수의 개수 입력 : '))
#
# for _ in range(n):
#   r = random.randint(10, 99)
#   print(r, end = ' ')
#   if r == 13:
#     print('\nexit Program')
#     break
# else:
#   print('\nend Randint')

### 2. print Number Skip

# for i in range(1, 13):
#   if i == 8:
#     continue
#   print(i, end = ' ')
# print()

### 2-1. 판단이 많아 개선

# for i in list(range(1, 8)) + list(range(9, 13)):
#   print(i, end = ' ')
# print()

### 3. 2자리 양수(10~99) 입력받기

# print('2자리 양수 입력')
#
# while True:
#   no = int(input('값 입력 : '))
#   # if 10 <= no <= 99:
#   if not (no < 10 or no > 99):  #드로므간의 법칙
#     break
# print(f'입력받은 양수는 {no}입니다.')

### 4. 구구단

# print('-' * 27)
# for i in range(2, 10):    # 행
#   for j in range(1, 10):  # 열
#     print(f'{i * j:3}', end = '') # 자리수를 3자리로
#   print()
# print('-' * 27)

### 5. * 직각 삼각형

n=int(input('짧은 변의 길이 입력 : '))

for i in range(n):
  for j in range(i+1):
    print('*', end = '')
  print()

### 5-1 반대로 출력

