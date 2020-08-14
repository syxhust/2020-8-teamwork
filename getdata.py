# %%
import pandas as pd
import tushare as ts
import akshare as ak
from datetime import datetime


# 一只股票短时间数据data1
def get_data1():
    pro = ts.pro_api('4fcc5bd1890c228a9df404fcc3bddfc4ec11471a26a5db2e4cadf53f')
    df = pro.daily(ts_code='000001.SZ', start_date='20200701', end_date='20200730')
    df = pd.DataFrame(df)
    df = df.dropna()
    df.head()
    df.to_csv('firstStock.csv')
    print(df)


# 两只股票半年数据data2
def get_data2():
    pro = ts.pro_api('4fcc5bd1890c228a9df404fcc3bddfc4ec11471a26a5db2e4cadf53f')
    df = pro.daily(ts_code='000001.SZ,600000.SH,', start_date='20180101', end_date='20180630')
    df = pd.DataFrame(df)
    df = df.dropna()
    df.head()
    df.to_csv('secondStock.csv')
    print(df)


# 1只股票分钟数据data3
def get_data3():
    stock_zh_a_minute_df = ak.stock_zh_a_minute(symbol='sh000300', period='1')
    df = pd.DataFrame(stock_zh_a_minute_df)
    df.dropna()
    df.head()
    df.to_csv('thirdStock.csv')