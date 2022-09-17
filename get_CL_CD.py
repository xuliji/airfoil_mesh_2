import numpy as np
import pandas as pd
import os
from tqdm import tqdm

# file_list = np.loadtxt("UIUC_series.txt", dtype=str)
# for mesh_name in tqdm(file_list, desc='CL_CD_CFD'):
#     data_path = './Meshes/' + mesh_name[:-4] + '_history' + '.dat'
#     data = np.loadtxt(data_path, dtype=float, delimiter=',', skiprows=2)
#     cl_cd = data[-1]
#     np.save('./CL_CD/' + mesh_name[:-4] + '_cl_cd.npy', cl_cd)
data = np.load('CL_CD/2032c_cl_cd.npy')
print(data)