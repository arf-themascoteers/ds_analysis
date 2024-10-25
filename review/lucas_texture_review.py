import pandas as pd


df = pd.read_csv("../data/output/lucas/lucas_texture_r.csv")
unique_values_with_counts = df['texture'].value_counts()
print(unique_values_with_counts)