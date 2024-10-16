import numpy as np
import scipy.io as sio
import pandas as pd
import os


def dump(X_file,gt_file,dump_file,X_key,gt_key):
    X_img = sio.loadmat(X_file)
    gt_img = sio.loadmat(gt_file)
    X = X_img.get(X_key).astype('float64')
    gt = gt_img.get(gt_key).astype('float64')

    X = X.reshape(X.shape[0] * X.shape[1], X.shape[2])
    gt = gt.reshape(-1)

    columns = [str(i) for i in range(X.shape[1])] + ["class"]
    data = np.concatenate((X,gt.reshape(-1,1)), axis=1)
    df = pd.DataFrame(columns=columns, data=data)
    df.to_csv(dump_file, index=False)


original_folder = "data/original/hyp"
output_folder = "data/output/hyp"

os.makedirs(output_folder, exist_ok=True)

dump(f"{original_folder}/Indian_pines_corrected.mat", f"{original_folder}/Indian_pines_gt.mat", f"{output_folder}/indian_pines.csv",'indian_pines_corrected','indian_pines_gt')
dump(f"{original_folder}/PaviaU.mat", f"{original_folder}/PaviaU_gt.mat", f"{output_folder}/paviaU.csv",'paviaU','paviaU_gt')
dump(f"{original_folder}/Salinas_corrected.mat", f"{original_folder}/Salinas_gt.mat", f"{output_folder}/salinas.csv",'salinas_corrected','salinas_gt')