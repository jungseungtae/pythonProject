###########################
# 전세계 음주 데이터 분석하기 #
###########################
import numpy as np
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

# 대륙의 이름을 저장한다.
labels = drinks['continent'].value_counts().index.tolist()
# 대륙 안의 국가의 수를 저장한다.
fracs1 = drinks['continent'].value_counts().values.tolist()
# 원 그래프의 조각 분리 간격을 설정한다.
explode = (0, 0, 0, 0.1, 0, 0)

# plt.pie(fracs1, explode = explode, labels = labels, autopct = '%0.f%%')
# plt.title('Null data to \'OT\'')
# plt.show()

# 그룹단위 데이터 분석
result = drinks.groupby('continent').spirit_servings.agg(['mean', 'min', 'max', 'sum'])
# print(result)

# 전체 평균 이상 알코올 섭취하는 대륙
total_mean = drinks.total_litres_of_pure_alcohol.mean()
continent_mean = drinks.groupby('continent')['total_litres_of_pure_alcohol'].mean()
over_continent = continent_mean[continent_mean >= total_mean]
# print(over_continent)
# print(continent_mean)

# 맥주 소비가 가장 많은 대륙
beer_top = drinks.groupby('continent').beer_servings.mean().idxmax()
# print(beer_top)

# 분석결과 시각화
# n_groups = len(result.index)
# means = result['mean'].tolist()
# mins = result['min'].tolist()
# maxs = result['max'].tolist()
# sums = result['sum'].tolist()
#
# index = np.arange(n_groups)
# bar_width = 0.1
#
# rects1 = plt.bar(index, means, bar_width, color = 'r', label = 'Mean')
# rects2 = plt.bar(index + bar_width, mins, bar_width, color = 'g', label = 'Min')
# rects3 = plt.bar(index + bar_width * 2, maxs, bar_width, color = 'b', label = 'Max')
# rects3 = plt.bar(index + bar_width * 3, sums, bar_width, color = 'y', label = 'Sum')

# plt.xticks(index, result.index.tolist())
# plt.legend()
# plt.show()

# 대륙별 퓨어 알콜
# continents = continent_mean.index.tolist()
# continents.append('mean')
#
# x_pos = np.arange(len(continents))
# alcohol = continent_mean.tolist()
# alcohol.append(total_mean)
#
# bar_list = plt.bar(x_pos, alcohol, align = 'center', alpha = 0.5)
# bar_list[len(continents) - 1].set_color('g')
# plt.plot([0, 6], [total_mean, total_mean], 'k--')
# plt.xticks(x_pos, continents)
#
# plt.ylabel('Total litres of Pure alcohol')
# plt.title('Total litres of Pure alcohol by Continent')
#
# plt.show()

# 대륙별 맥주 소비량
# beer_mean = drinks.groupby('continent')['beer_servings'].mean()

beer_group = drinks.groupby('continent')['beer_servings'].sum()
continents = beer_group.index.tolist()

# x_pos = np.arange(len(continents))
y_pos = np.arange(len(continents))
alcohol = beer_group.tolist()

bar_list = plt.bar(y_pos, alcohol, align = 'center', alpha = 0.5)
bar_list[continents.index('EU')].set_color('r')

# plt.plot([0, 6], [beer_mean, beer_mean], 'k--')
# plt.xticks(x_pos, continents)

plt.xticks(y_pos, continents)
plt.ylabel('beer Servings')
plt.title('Beer servings by Continent')

plt.show()