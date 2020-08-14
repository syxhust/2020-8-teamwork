def cor_data1(df):
    from matplotlib import pyplot as plt
    import pandas as pd
    import seaborn as sns
    df['ts_code'] = pd.to_datetime(df.pop('Unnamed: 0'))
    a = df.corr()
    sns.heatmap(a, annot=True)
    plt.title('correlation')
    plt.show()
    return a


def cor_data2(df):
    from matplotlib import pyplot as plt
    import pandas as pd
    import seaborn as sns
    df['trade_date'] = pd.to_datetime(df.pop('trade_date'), format='%Y%m%d')
    df['ts_code'] = pd.to_datetime(df.pop('Unnamed: 0'))
    sz1 = df[::2].set_index('trade_date')
    sz2 = df[1::2].set_index('trade_date')
    correlation1 = sz1.corr()
    correlation2 = sz2.corr()
    sns.heatmap(correlation1, annot=True)
    plt.title('correlation of first stock')
    plt.show()
    sns.heatmap(correlation2, annot=True)
    plt.title('correlation of second stock')
    plt.show()


def cor_data3(df):
    from matplotlib import pyplot as plt
    import pandas as pd
    import seaborn as sns
    df['day'] = pd.to_datetime(df.pop('day'))
    df['ts_code'] = pd.to_datetime(df.pop('Unnamed: 0'))
    a = df.corr()
    sns.heatmap(a, annot=True)
    plt.title('correlation')
    plt.show()
    return a
