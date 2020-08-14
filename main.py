# %%
import pandas as pd
import getdata
import corrheatmap as co
import secondStockPlot as ss
import thirdStockPlot as ts
import third_key_factor as tk
import firstStock as fs

# 得到三种数据，并写入到csv里面
getdata.get_data1()
getdata.get_data2()
getdata.get_data3()

# %%
# 第一部分数据
data = pd.read_csv('firstStock.csv')
df = pd.DataFrame(data)
fs.draw(df)
correlation = co.cor_data1(df)

# %%
# 第二部分数据
data = pd.read_csv('secondStock.csv')
df = pd.DataFrame(data)
ss.plotContrast(df)
ss.plotKline(df)
correlation = co.cor_data2(df)

# %%
# 第三部分数据
data = pd.read_csv('thirdStock.csv')
df = pd.DataFrame(data)
print(df)
df['close'] = df['close'].astype('float')
df = tk.cal_macd(df)
Volume = tk.Volume(df)
df = tk.cal_rsi(df)
avg = tk.moving_average(df)
tk.plot_MA(df, avg[0], avg[1])
tk.plot_macd(df)
print(Volume[100:160])
tk.plot_Volume(df)
tk.plot_rsi(df)
ts.plotScatter(df)
ts.plotBox(df)
correlation = co.cor_data3(df)
