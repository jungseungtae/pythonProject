import pandas as pd
from numpy import NaN
import copy

###############################################
### 데이터 전처리 ###
# 1. 데이터 프레임 생성
# 2. 칼럼명 추출, 변경
# 3. copy
# 4. Series
# 5. loc, iloc
###############################################

df = pd.DataFrame({'a' : [1,2,3], 'b' : [4,5,6],'c' : [7,8,9]})

# print(type(df))

# df.columns = ['d', 'e','f']
# df.rename(columns = {'d' : '디', 'f' : '에프'}, inplace = True)
# print(df)
# print(df)

# 같은 객체를 공유
# df2 = df
# 다른 객체로 복사
# df2 = copy.deepcopy(df)
# df.columns = ['d', 'e','f']
# print(df2)
# print(df)

# print(df['a'])

a = pd.Series([1,2,3,1,2,3], index = ['a','b','c','d','e','f'])
# print(a['e'])

df = pd.DataFrame({'a' : [1,2,3,1,2,3], 'b' : [4,5,6,6,7,8],'c' : [7,8,9,10,11,12]})
# a = df['a']
# 중복제거
# print(a.unique())
# print(a.unique()[2])

# err. 시리즈는 동시에 두 가지 컬럼을 호출 할 수 없다.
print(df['a', 'b'])

a = [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
df3 = pd.DataFrame(a)

# 컬럼 이름 설정
# df3.columns = ['a', 'b', 'c']

# print(df3)

com = {'Company' : ['abc', '회사', '123'], '직원수' : [400, 10, 6]}
com1 = {'Company' : ['abc', '회사', '123'], '직원수' : [400, 10, 6], '위치' : ['Seoul', NaN, 'Busan']}
com2 = {'Company' : ['abc', '회사', '123'], '직원수' : [400, 10, 6], '위치' : ['Seoul','' , 'Busan']}

df4 = pd.DataFrame(com)
df5 = pd.DataFrame(com1)
df6 = pd.DataFrame(com2)

# print(df4)
# print(df5)
# print(df6)

# loc, iloc 원하는 위치 데이터 추출