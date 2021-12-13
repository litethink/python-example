import numpy as np
import pandas as pd

df =pd.io.parsers.read_csv(
                "ASH.csv",
                header=0, index_col=0, parse_dates=True, 
            )

d = pd.DataFrame(index=df.index)
d["price"] = 0
d.loc[d.index.day==6] = df.close
d[d["price"]==0] = np.nan
d = d.fillna( method='pad')
d = d.fillna(method="backfill)
print(d)
             
             
