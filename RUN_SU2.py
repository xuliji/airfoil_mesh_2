import os
import subprocess
import numpy as np
import pandas as pd
from tqdm import tqdm


# child = subprocess.check_output('su2_cfd inv_NACA0012.cfg', cwd=r'C:\Users\23844\Desktop\SU2-master\QuickStart', shell=True)
# print(child)
# 获取cfg文件
def create_cfg(mesh_name):
    f = open('unsteady_naca0012.cfg', 'r', encoding='utf-8')
    f1 = open('./Meshes/coarse/' + mesh_name[:-4] +'/' + mesh_name[:-4] + '.cfg', 'w', encoding='utf-8')
    lines = f.readlines()
    for i in range(len(lines)):
        if 'MESH_FILENAME= unsteady_naca0012_mesh.su2' in lines[i]:
            new_line = lines[i].replace('unsteady_naca0012_mesh.su2', mesh_name[:-4]+'.su2')
            lines[i] = new_line
        elif 'CONV_FILENAME= history' in lines[i]:
            new_line = lines[i].replace('CONV_FILENAME= history', 'CONV_FILENAME= ' + mesh_name[:-4] + '_history')
            lines[i] = new_line
        elif 'VOLUME_FILENAME= flow' in lines[i]:
            new_line = lines[i].replace('VOLUME_FILENAME= flow', 'VOLUME_FILENAME= ' + mesh_name[:-4] + '_flow')
            lines[i] = new_line

    f1.writelines(lines)
    f.close()
    f1.close()



file_list = np.loadtxt("UIUC_series.txt", dtype=str)[:300]
for mesh_name in tqdm(file_list, desc='CL_CD_CFD'):
    create_cfg(mesh_name)
    # child = subprocess.check_output('su2_cfd ' + mesh_name[:-4] + '.cfg', cwd='./Meshes/corase/', shell=False)  # 运行su2_cfd
    # print(str(child, encoding='utf-8'))
