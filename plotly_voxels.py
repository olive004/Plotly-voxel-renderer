
# Generates voxel plotly graph

from options import Options
from data_loader import load_data
from VoxelData import VoxelData
import plotly.graph_objects as go
import matplotlib.pyplot as plt
import numpy as np

if __name__ == "__main__":
    
    opt = Options().parse()
    data = load_data(opt)

    Voxels = VoxelData(data)
    # print("Voxels.og_data",Voxels.og_data)
    print("Voxels.vertices",Voxels.vertices)

    # fig = go.Figure(data=go.Mesh3d(
    #     x=Voxels.x,
    #     y=Voxels.y,
    #     z=Voxels.z
    #     ))
    # fig.show()






