import pandas as pd

## chipotle 주문 데이터 분석하기

file_path = 'C:/Users/jstco/Downloads/chipotle.tsv'
chipo = pd.read_csv(file_path, sep = '\t')

# 1. 기초 데이터 탐색

# 전체 행, 열
# print(chipo.shape)

# 테이블 정보와 데이터 타입
# print(chipo.info())

# 처음부터 10개의 row 데이터 출력
# print(chipo.head(10))

# 컬럼 정보
# print(chipo.columns)

# row 개수
# print(chipo.index)

# 주문번호는 숫자 의미가 없기 때문에 str로 변환
chipo['order_id'] = chipo['order_id'].astype(str)

# 데이터의 기초통계량 출력
# print(chipo.describe())

# 중복제거를 통하여 주문의 전체 개수 파악
# print(len(chipo['order_id'].unique()))

# 아이템의 전체 개수 파악
# print(len(chipo['item_name'].unique()))

# 주문이 가장 많은 10개의 아이템의 순위와 이름, 회수 출력
item_count = chipo['item_name'].value_counts()[:10]
# for idx, (val, cnt) in enumerate(item_count.iteritems(), 1):
#   print('Top', idx, ':', val, cnt)

item_sel = chipo['item_name'].value_counts().index.tolist()[0]

# print(item_sel)

# enumerate : 반복문의 index를 확인 가능. 인덱스와 원소를 tuple형태로 반환

# t = [1,5,7,33,39,52]
#
# for p in enumerate(t):
#   print(p)
#
# for i, v in enumerate(t):
#   print('index : {}, value :{}'.format(i,v))

# 아이템의 주문 개수 구하기
order_count = chipo.groupby('item_name')['order_id'].count()
# print(order_count[:10])

item_quantity = chipo.groupby('item_name')['quantity'].sum()
# print(item_quantity[0:])

# 2. 데이터 시각화 하기

import numpy as np
import matplotlib.pyplot as plt

# item_name을 인덱스로 설정하여 판매량을 그래프로 표현
# item_name_list = item_quantity.index.tolist()
# x_pos = np.arange(len(item_name_list))
# order_cnt = item_quantity.values.tolist()
#
# plt.bar(x_pos, order_cnt, align = 'center')
# plt.ylabel('ordered_item_count')
# plt.title('Distribution of all orderd item')

# plt.show()

# 2-1. pandas value_count()와 unique 차이 알기

# value_count() : Series
# print(chipo['item_name'].value_counts()[:10])
# print(type(chipo['item_name'].value_counts()[:10]))

# unique() : np.array
# print(chipo['item_name'].unique()[:10])
# print(type(chipo['item_name'].unique()[:10]))

# 3. 데이터 전처리

# print(chipo.info())
# print(chipo['item_price'].head())

# item의 가격에 대한 기초 통계량
chipo['item_price'] = chipo['item_price'].apply(lambda x: float(x[1:]))
# print(chipo.describe())

# price 데이터가 object -> float
# print(chipo['item_price'].head())

# 4. 탐색적 분석

# 주문당 평균 매출
order_price_mean = chipo.groupby('order_id')['item_price'].sum().mean()
# print(order_price_mean)

# 주문당 평균 매출의 기초 통계량
order_price_des = chipo.groupby('order_id')['item_price'].sum().describe()
# print(order_price_des)

# 한 주문에 10달러 이상 구매한 주문번호 출력
orderid_group = chipo.groupby('order_id').sum()
results = orderid_group[orderid_group.item_price >= 10]

# 각 아이템의 가격 구하기
chipo_one_item = chipo[chipo.quantity == 1]
price_per_item = chipo_one_item.groupby('item_name').min()
price_per_item.sort_values(by = 'item_price', ascending = False)[:10]

# 아이템 가격 분포 그래프 출력
# item_price_list = price_per_item.index.tolist()
# x_pos = np.arange(len(item_price_list))
item_price = price_per_item['item_price'].tolist()
#
# plt.bar(x_pos, item_price, align = 'center')
# plt.ylabel('item price($)')
# plt.title('Distribution of item price')

# plt.show()

# 히스토그램
# plt.hist(item_price)
# plt.ylabel('counts')
# plt.title('Histogram of Item Price')
#
# plt.show()

# 가장 비싼 주문에서 item 판매 개수
top_order_cnt = chipo.groupby('order_id').sum().sort_values(by = 'item_price', ascending = False)[:5]

# 특정 메뉴 주문 횟수 구하기
chipo_salad = chipo[chipo['item_name'] == 'Veggie Salad Bowl']
chipo_salad = chipo_salad.drop_duplicates(['item_name', 'order_id'])

# print(len(chipo_salad))
# print(chipo_salad.head(5))

# 메뉴를 2개 이상 주문한 횟수
chipo_chicken = chipo[chipo['item_name'] == 'Chicken Bowl']
chipo_chicken_result = chipo_chicken[chipo_chicken['quantity'] >= 2]

# 2개 이상 주문한 고객들의 메뉴 총 주문 수량
chipo_chicken_ordersum = chipo_chicken.groupby('order_id').sum()['quantity']
chipo_chicken_total_result = chipo_chicken_ordersum[chipo_chicken_ordersum >= 2]

# print(len(chipo_chicken_total_result))
# print(chipo_chicken_total_result)

