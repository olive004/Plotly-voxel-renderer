
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
    print("Voxels.data\n",Voxels.data)
    print("Voxels.vertices\n",Voxels.vertices)
    print("Voxels.triangles\n",Voxels.triangles)

    fig = go.Figure(data=go.Mesh3d(
        x=Voxels.vertices[0],
        y=Voxels.vertices[1],
        z=Voxels.vertices[2],
        i=Voxels.triangles[0],
        j=Voxels.triangles[1],
        k=Voxels.triangles[2]
        ))
    fig.show()






