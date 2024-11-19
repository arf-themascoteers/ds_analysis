import os
import pandas as pd
import numpy as np

original_folder = "data/original/lucas"
output_folder = "data/output/lucas_crop"
os.makedirs(output_folder, exist_ok=True)

spectra_src_dir = f"{original_folder}/LUCAS2015_Soil_Spectra_EU28"
topsoil_file = f"{original_folder}/lucas_shp.csv"
output_file = f"{output_folder}/lucas_crop_a.csv"
output_reflectance_file = f"{output_folder}/lucas_crop.csv"


def link_them():
    topsoil_df = pd.read_csv(topsoil_file)
    topsoil_df = topsoil_df[topsoil_df['LC0_Desc'] == "Cropland"].reset_index(drop=True).copy()
    out = open(output_file, "w")
    spec = 400
    while spec <= 2499.5:
        val = spec
        if int(val) == val:
            val = int(val)
        val = str(val)
        out.write(f"{val},")
        spec = spec+0.5
    out.write("oc")
    out.write("\n")
    done = []

    for file in os.listdir(spectra_src_dir):
        path = os.path.join(spectra_src_dir, file)
        a_df = pd.read_csv(path)

        exclude_columns = ['source', 'SampleID', 'NUTS_0', 'SampleN','PointID']
        columns_to_average = [col for col in a_df.columns if col not in exclude_columns]
        df_grouped = a_df.groupby('PointID')[columns_to_average].mean().reset_index()

        for index, row in df_grouped.iterrows():
            empties = row.isna().sum()
            if empties != 0:
                print(file, row["PointID"])
                continue

            point_id = row['PointID']
            if point_id in done:
                print(f"{point_id} is done")
                continue
            rows = (topsoil_df.loc[topsoil_df['Point_ID'] == point_id])
            if len(rows) == 0:
                #print(point_id)
                continue
            if len(rows) > 1:
                print(f"Multiple {point_id}")
            topsoil_row = rows.iloc[0]

            spec = 400
            while spec <= 2499.5:
                val = spec
                if int(val) == val:
                    val = int(val)
                val = str(val)
                out.write(f"{row[val]},")
                spec = spec + 0.5
            out.write(f"{topsoil_row['OC']}")
            out.write("\n")
            done.append(point_id)
            if len(done)%1000 == 0:
                print(f"Done {len(done)}")

    out.close()
    print("done")


def to_reflectance():
    df = pd.read_csv(output_file)
    df.iloc[:, 0:-1] = np.round(1 / (10 ** df.iloc[:, 0:-1]), 5)
    df.to_csv(output_reflectance_file, index=False)


def check(f):
    df = pd.read_csv(f)
    has_nan = df.isnull().values.any()
    non_numeric = df.apply(lambda x: pd.to_numeric(x, errors='coerce')).isnull().values.any()
    print(has_nan)
    print(non_numeric)


link_them()
check(output_file)
to_reflectance()
check(output_reflectance_file)