# Generates voxel plotly graph from input (3D) array

# Output from our segmentation models is in 3D numpy arrays where 
# each segmented class is coded by a single number

# - load numpy array input
# - choose if you want voxel output or marching cubes
# - make voxel class with input giving coords and values
# - each unique value corresponds to a plotly viz thing
# - 


# - get seg class number 
# - for each seg class in the input add trace
# - Voxel: 
#     - VoxelMesh vertex data
#         - make vertices only if they're not inside
#         - get neighbor 
#     - Voxel triangle data
#         - neighbor info per voxel
#             - don't make tri's if neighbor exists
#         - get triangles to be rendered (render style voxel or marching) --> render all triangles on outside of seg
        
# - make trace Mesh3d (per class?)
#     - with data being voxel positions
#     - only load the triangles to be displayed (either voxel or marching)
# - show figure with voxels
# - Buttons:
#     - Class: all | 1 | 2 | ... | none
#     - 3D Style: voxel | marching cubes
# - give embeddable figure link


# class VoxelData:
    
#     getNeighbor



# - number corresponds to a color for toggling


# just testign out plotly functionality https://plotly.com/python/3d-volume-plots/ 
# and https://plot.ly/python/3d-isosurface-plots/ 

import csv    # for import to plotly
import matplotlib.pyplot as plt
import numpy as np
import plotly.graph_objects as go

np.random.seed(0)
cube = np.random.rand(3, 6)

voxels = VoxelData()

fig = go.Figure(data=go.Mesh3d(
    x=cube[0], # X.flatten(),
    y=cube[1], # Y.flatten(),
    z=cube[2] # Z.flatten(),
    # delaunayaxis = "z",
    ))
fig.show()




