import pandas as pd


df = pd.read_csv("data/intermediate/ghisaconus/1.csv")
unique_values_with_counts = df['Crop'].value_counts()
print(unique_values_with_counts)
print(len(df.columns))
print(len(df))
