import pandas as pd


df = pd.read_csv("../data/original/lucas/lucas_shp.csv")
print(df["LC0_Desc"].unique())
vc = df["LC0_Desc"].value_counts()
print(vc)