import pandas as pd
import os

original_file = "data/original/ghisaconus/GHISACONUS_2008_001_speclib.csv"
intermediate_file_1 = "data/intermediate/ghisaconus_health/1.csv"
output_file = "data/output/ghisaconus_health/ghisaconus.csv"


def create_intermediate_file():
    os.makedirs('data/intermediate/ghisaconus_health', exist_ok=True)
    with open(original_file, 'r') as file:
        lines = file.readlines()[6:]

    with open(intermediate_file_1, 'w') as file:
        file.writelines(lines)


def sanitize():
    os.makedirs('data/output/ghisaconus_health', exist_ok=True)
    df = pd.read_csv(intermediate_file_1)
    cols = [col for col in df.columns if col.startswith('X') and not df[col].isna().all()]
    df_filtered = df[cols + ['Crop']].rename(columns={'Stage': 'health'})
    nan_count = df_filtered.isna().any(axis=1).sum()
    print(nan_count)
    df_filtered = df_filtered.dropna()
    df_filtered.to_csv(output_file, index=False)


def check_sanity():
    df = pd.read_csv(output_file)
    print(df.isna().sum().sum())


create_intermediate_file()
sanitize()
check_sanity()