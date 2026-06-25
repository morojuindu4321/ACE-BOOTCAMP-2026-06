import pandas as pd
fn = "/workspaces/ACE-BOOTCAMP-2026-06/Day7/archive/WorldCupMatches.csv"
df = pd.read_csv(fn)
print(df.head(10))
print(df.shape)
print(df.tail(10))
print(df.info(0))
print(df.count())
df.iloc[1]
print(df.head())
