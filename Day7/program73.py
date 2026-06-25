from pathlib import Path
import pandas as pd

csv_path = Path(__file__).resolve().parent / "archive (1)" / "used_car_price_prediction_1M.csv"
df = pd.read_csv(csv_path)

print("First 10 rows:")
print(df.head(10))

print("\nDataFrame shape:", df.shape)
print("\nLast 10 rows:")
print(df.tail(10))

print("\nBasic information:")
print(df.info())

print("\nNon-null counts:")
print(df.count())

print("\nSecond row using iloc:")
print(df.iloc[1])

print("\nFirst 5 rows:")
print(df.head())

print("\nModel value at row 0:")
print(df.loc[0, "Model"])
