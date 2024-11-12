import pandas as pd
import os

original_file = "../data/original/ghisaconus/GHISACONUS_2008_001_speclib.csv"
intermediate_file_1 = "../data/intermediate/ghisaconus/1_rough.csv"
output_file = "data/output/ghisaconus/ghisaconus.csv"


def create_intermediate_file():
    os.makedirs('data/intermediate/ghisaconus', exist_ok=True)
    with open(original_file, 'r') as file:
        lines = file.readlines()[6:]

    with open(intermediate_file_1, 'w') as file:
        file.writelines(lines)


def sanitize():
    df = pd.read_csv(intermediate_file_1)
    cols = [col for col in df.columns if col.startswith('X') and df[col].isna().all()]
    print(cols)
    df_filtered = df[cols]
    columns_with_nan = df.columns[df.isnull().any()].tolist()
    print(columns_with_nan)


def check_sanity():
    df = pd.read_csv(output_file)
    print(df.isna().sum().sum())


create_intermediate_file()
sanitize()