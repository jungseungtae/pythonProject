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

### 3. 

