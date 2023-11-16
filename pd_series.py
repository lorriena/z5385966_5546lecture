""" lec_pd_series.py

Companion codes for the lecture on pandas Series
"""

import pandas as pd


# ----------------------------------------------------------------------------
#   The dates and prices lists
# ----------------------------------------------------------------------------
dates = [
  '2020-01-02',
  '2020-01-03',
  '2020-01-06',
  '2020-01-07',
  '2020-01-08',
  '2020-01-09',
  '2020-01-10',
  '2020-01-13',
  '2020-01-14',
  '2020-01-15',
  ]

prices = [
  7.1600,
  7.1900,
  7.0000,
  7.1000,
  6.8600,
  6.9500,
  7.0000,
  7.0200,
  7.1100,
  7.0400,
  ]

# ----------------------------------------------------------------------------
#   Create a Series instance
# ----------------------------------------------------------------------------
# Create a series object
ser = pd.Series(prices, index=dates)
#print(ser)

# Select Qantas price on '2020-01-02' ($7.16) using ...

# ... the `prices` list
prc0 = prices[0]
#print(prc0)

# ... the `ser` series
prc1  = ser['2020-01-02']
#print(prc1)

# ----------------------------------------------------------------------------
#   Slicing series
# ----------------------------------------------------------------------------
# Unlike dictionaries, you can slice a series
prcs  = ser[:3]
#print(prcs)

# ----------------------------------------------------------------------------
#   Accessing the underlying array
# ----------------------------------------------------------------------------

# Use `.array` to get the underlying data array
ary  = ser.array
#print(ary)

# Like any instance, you can get its type (i.e., the class used to create the
# instance)
#print(type(ser.array))
#同时获取数据和索引（即日期和价格）
#考虑使用其他方法，例如将 Series 转换为一个 Python 字典，或者直接访问索引和数据属性
# 转换为字典
# data_dict = ser.to_dict()
# print(data_dict)

# 或者分别访问索引和数据
# index = ser.index
# data = ser.values  # 注意这里使用的是 .values，不是 .array，因为.values 返回的是一个 NumPy 数组，它是 pandas 处理数据的底层结构。
#
# print("Index:", index)
# print("Data:", data)


# Use the `index` attribute to get the index from a series
the_index  = ser.index
#print(the_index)

# Like any instance, you can get its type (i.e., the class used to create the
# instance).
#print('The type of `the_index` is', type(the_index))

# ----------------------------------------------------------------------------
#   Changing the index by assignment
# ----------------------------------------------------------------------------

# The old index is:
#
# Index(['2020-01-02', '2020-01-03', '2020-01-06', '2020-01-07', '2020-01-08',
#    '2020-01-09', '2020-01-10', '2020-01-13', '2020-01-14', '2020-01-15'],
#   dtype='object')

# Replace the existing index with another with different values
# Note the -4 and 1000
ser.index = [0, 1, 2, 3, -4, 5, 6, 7, 8, 1000]

# The new index is:
#Int64Index([0, 1, 2, 3, -4, 5, 6, 7, 8, 1000], dtype='int64')


# ----------------------------------------------------------------------------
#   Selecting obs using the new index
# ----------------------------------------------------------------------------
# Lets see how the series looks like
#print(ser)

# This will return 7.04
x  = ser[1000]
#print(x)

# Compare the following cases:
# 1. This will return the element associated with the index label -4
#    (or 6.86)
#print(ser[-4])

# 2. This will return the fourth element from the end of the **list** `prices`
#    (or 7.00)
#print(prices[-4])