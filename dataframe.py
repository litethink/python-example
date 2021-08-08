l1 = [{'id': 1619837024, 'close': '0.07935000', 'open': '0.08110000', 'low': '0.07836000', 'high': '0.08116000', 'cur_amount': 7416364.8}, {'id': 1619837083, 'close': '0.07936000', 'open': '0.08110000', 'low': '0.07836000', 'high': '0.08116000', 'cur_amount': 7478281.2}, {'id': 1619837115, 'close': '0.07944000', 'open': '0.08110000', 'low': '0.07836000', 'high': '0.08116000', 'cur_amount': 7485026.8}, {'id': 1619837136, 'close': '0.07944000', 'open': '0.08110000', 'low': '0.07836000', 'high': '0.08116000', 'cur_amount': 7486147.1}, {'id': 1619837147, 'close': '0.07945000', 'open': '0.08110000', 'low': '0.07836000', 'high': '0.08116000', 'cur_amount': 7505410.6}, {'id': 1619837187, 'close': '0.07943000', 'open': '0.08110000', 'low': '0.07836000', 'high': '0.08116000', 'cur_amount': 7505993.7}, {'id': 1619837207, 'close': '0.07939000', 'open': '0.08110000', 'low': '0.07836000', 'high': '0.08116000', 'cur_amount': 7510610.5}, {'id': 1619837255, 'close': '0.07947000', 'open': '0.08110000', 'low': '0.07836000', 'high': '0.08116000', 'cur_amount': 7514652.4}, {'id': 1619837277, 'close': '0.07952000', 'open': '0.08110000', 'low': '0.07836000', 'high': '0.08116000', 'cur_amount': 7515667.0}]
l2 = [{'id': 1619836952, 'close': '0.00000791', 'open': '0.00000804', 'low': '0.00000783', 'high': '0.00000804', 'cur_amount': 251531.0}, {'id': 1619836967, 'close': '0.00000792', 'open': '0.00000804', 'low': '0.00000783', 'high': '0.00000804', 'cur_amount': 251718.0}, {'id': 1619837001, 'close': '0.00000796', 'open': '0.00000804', 'low': '0.00000783', 'high': '0.00000804', 'cur_amount': 251857.0}, {'id': 1619837030, 'close': '0.00000796', 'open': '0.00000804', 'low': '0.00000783', 'high': '0.00000804', 'cur_amount': 251861.0}, {'id': 1619837041, 'close': '0.00000795', 'open': '0.00000804', 'low': '0.00000783', 'high': '0.00000804', 'cur_amount': 252001.0}, {'id': 1619837095, 'close': '0.00000796', 'open': '0.00000804', 'low': '0.00000783', 'high': '0.00000804', 'cur_amount': 252067.0}, {'id': 1619837115, 'close': '0.00000795', 'open': '0.00000804', 'low': '0.00000783', 'high': '0.00000804', 'cur_amount': 252714.0}, {'id': 1619837164, 'close': '0.00000798', 'open': '0.00000804', 'low': '0.00000783', 'high': '0.00000804', 'cur_amount': 252910.0}, {'id': 1619837235, 'close': '0.00000795', 'open': '0.00000804', 'low': '0.00000783', 'high': '0.00000804', 'cur_amount': 254083.0}, {'id': 1619837285, 'close': '0.00000796', 'open': '0.00000804', 'low': '0.00000783', 'high': '0.00000804', 'cur_amount': 254145.0}]
l3 = [{'id': 1619836991, 'close': '0.99798000', 'open': '0.99504000', 'low': '0.99333000', 'high': '0.99798000', 'cur_amount': 7.71436}, {'id': 1619837086, 'close': '0.99798000', 'open': '0.99504000', 'low': '0.99333000', 'high': '0.99798000', 'cur_amount': 7.71447}, {'id': 1619837209, 'close': '0.99798000', 'open': '0.99504000', 'low': '0.99333000', 'high': '0.99798000', 'cur_amount': 7.71482}]
l4 = [{'id': 1619837072, 'close': '0.00000137', 'open': '0.00000139', 'low': '0.00000135', 'high': '0.00000140', 'cur_amount': 2482389.0}, {'id': 1619837277, 'close': '0.00000137', 'open': '0.00000139', 'low': '0.00000135', 'high': '0.00000140', 'cur_amount': 2513830.0}]


import pandas as pd
d = pd.DataFrame()
d1= pd.DataFrame(l1,dtype=float)
d2= pd.DataFrame(l2,dtype=float)
d3= pd.DataFrame(l3,dtype=float)
d4= pd.DataFrame(l4,dtype=float)

#d["c3"] = d3["close"]

close = pd.DataFrame()
close = pd.concat([close,d1["close"]],axis=1)
close.rename(columns={"close":"d1"},inplace=True)
close = pd.concat([close,d2["close"]],axis=1)
close.rename(columns={"close":"d2"},inplace=True)
close = pd.concat([close,d3["close"]],axis=1)
close.rename(columns={"close":"d3"},inplace=True)
close = pd.concat([close,d4["close"]],axis=1)
close.rename(columns={"close":"d4"},inplace=True)

#reverse
close.d3.iloc[::-1]


close = pd.concat([close,kline["close"]],axis=1)
close.rename(columns={"close":symbol.uni_name},inplace=True)
volumn = pd.concat([volumn,kline["cur_amount"].diff(1) * kline["close"]],axis=1)
volumn.rename(columns={0:symbol.uni_name},inplace=True)

#no oder data
e = pd.DataFrame([[2,3,1,4]],columns=["d2","d3","d1","d4"])

#timestamp 直接转换为str
dt = pd.to_datetime(df.id, unit="s")

#csv 指定行首为列名及分割符
df = pd.read_csv("history.csv",header=1,sep=",")

#小时 1h 4小时 4h，时间序列要连续
five_min_df = pd.DataFrame(m_df.loc[:, ['price', 'volume']], index=m_df.index).resample('5T', closed='left', label='left').mean().copy()
five_min_df["volume"] = pd.DataFrame(m_df.loc[:, ['price', 'volume']], index=m_df.index).resample('5T', closed='left', label='left').sum().copy()["volume"]
