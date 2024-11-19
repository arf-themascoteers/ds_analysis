import pandas as pd


#df = pd.read_csv("../data/output/lucas/shp.csv")
df = pd.read_csv("../data/original/lucas/lucas_shp.csv")
print(df.columns)
unique_values_with_counts = df['LC0_Desc'].value_counts()
print(unique_values_with_counts)
#
# df = pd.read_csv("../data/output/lucas/lucas_lc0_s_r.csv")
# print(df.columns[-1])
# unique_values_with_counts = df['lc'].value_counts()
# print(unique_values_with_counts)