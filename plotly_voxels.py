
# Generates voxel plotly graph

from options import Options
from data_loader import load_data
from VoxelData import VoxelData

if __name__ == "__main__":
    
    opt = Options().parse()
    data = load_data(opt)

    Voxels = VoxelData(data)
    print(Voxels.xyz)

    # fig = go.Figure(data=go.Mesh3d(
    #     x=Voxels.x
    #     y=Voxels.x
    #     z=Voxels.y
    #     ))
    # fig.show()






