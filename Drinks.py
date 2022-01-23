###########################
# 전세계 음주 데이터 분석하기 #
###########################

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


file_path = "C:/Users/jstco/Downloads/drinks.csv"
drinks = pd.read_csv(file_path)

# 1. 기초 정보 탐색

# print(drinks.info())
# print(drinks.head(10))
# print(drinks.describe())

# 두 피처 간의 상관관계 구하기(corr_pearson)
corr = drinks[['beer_servings', 'wine_servings']].corr(method = 'pearson')
# print(corr)

# 2. 탐색과 시각화

# 모든 피처 간의 상관계수
cols = ['beer_servings', 'spirit_servings', 'wine_servings', 'total_litres_of_pure_alcohol']
corr_total = drinks[cols].corr(method = 'pearson')
# print(corr_total)

# 히트맵
# cols_view = ['beer', 'sprit', 'wine', 'alcohol']
# sns.set(font_scale = 1.5)
# hm = sns.heatmap(corr_total.values,
#   cbar = True,
#   annot = True,
#   square = True,
#   fmt = '.2f',
#   annot_kws = { 'size': 15 },
#   yticklabels = cols_view,
#   xticklabels = cols_view)
# plt.tight_layout()
# plt.show()

# scatter plot
# sns.set(style = 'whitegrid', context = 'notebook')
# sns.pairplot(drinks[['beer_servings', 'spirit_servings',
#                      'wine_servings', 'total_litres_of_pure_alcohol']], height = 2.5)
# plt.show()

# 결측 데이터 전처리
# print(drinks.isnull().sum())
# print(drinks.dtypes)
drinks['continent'] = drinks['continent'].fillna('OT')
# print(drinks.head(10))

# 파이차트
labels = drinks['continent'].value_counts().index.tolist()
fracs1 = drinks['continent'].value_counts().values.tolist()
explode = (0, 0, 0, 0.1, 0, 0)

plt.pie(fracs1, explode = explode, labels = labels, autopct = '%0.f%%')
plt.title('Null data to \'OT\'')
plt.show()
