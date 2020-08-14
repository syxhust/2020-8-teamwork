
# %%
def draw(df):
    from matplotlib import pyplot as plt
    import pandas as pd
    import seaborn as sns
    raw_time = pd.to_datetime(df.pop('trade_date'), format='%Y%m%d')
    raw_time.head()
    plt.plot(raw_time, df['close'])
    plt.xlabel('time')
    plt.ylabel('share price')
    plt.title('trend')
    plt.show()
    daily_return = df['close'][0::2].pct_change().dropna()
    plt.plot(raw_time[0::2][:10], daily_return[:10])
    plt.xlabel('Time')
    plt.ylabel('Rise and Fall')
    plt.show()
    sns.kdeplot(daily_return)
