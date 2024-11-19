import os
import pandas as pd

output_folder = "data/output/lucas_bs_50"
output_file = os.path.join(output_folder, "lucas_crop_50_r.csv")
os.makedirs(output_folder, exist_ok=True)
input_file = "data/output/lucas_bs/lucas_crop_r.csv"


def link_them():
    df = pd.read_csv(input_file)
    df = df[df["oc"]<50].reset_index(drop=True).copy()
    df.to_csv(output_file, index=False)
    print("done")


link_them()
