# Holds voxel data with one segmentation class value >0 and bg class = 0
import numpy as np

class Coordinate():

    def __init__(self, xyz):
        self.x = xyz[0]
        self.y = xyz[1]
        self.z = xyz[2]


class VoxelData():

    
    def __init__(self,data):
        self.xyz = self.get_coords(data)
        # self.x = self.xyz[0,:]
        # self.y = self.xyz[1,:]
        # self.z = self.xyz[2,:]
        self.x_length = np.size(data,0)
        self.y_length = np.size(data,1)
        self.z_length = np.size(data,2)
        self.vertices = self.make_edge_verts(self.xyz)
        # self.triangles 

        # xyz direction corresponding to 'Direction'
        self.offsets = [             
            [0, 0, 1],
            [1, 0, 0],
            [0, 0, -1],
            [-1, 0, 0],
            [0, 1, 0],
            [0, -1, 0]
        ]


    def get_coords(self, data):
        indices = np.nonzero(data)
        indices = np.stack((indices[0], indices[1],indices[2]))
        return indices


    def get_neighbor(self, xyz, direction):
        x = xyz[0]
        y = xyz[1]
        z = xyz[2]
        offset_to_check = offsets[direction]
        neighbor_coord = [x+ offset_to_check[0], y+offset_to_check[1], z+offset_to_check[2]]

        if (neighbor_coord[0] < 0 | neighbor_coord[0] >= self.x_length | neighbor_coord[1] < 0 | neighbor_coord[1] >= self.y_length | neighbor_coord[2] < 0 | neighbor_coord[2] >= self.z_length):
            return 0
        else:
            return get_voxel(x, y, z)


    def make_verts(self, voxel_coords):
        for direction in range(len(CubeData.Direction))
            if voxel_coords


    def make_edge_verts(self)
        for voxel in range(np.size(self.xyz, 1))
            make_verts(selx.xyz(:, voxel))

        .
        

    
class CubeData:
    faceTriangles = {
		'North':  [0, 1, 2, 3 ],
        'East': [ 5, 0, 3, 6 ],
	    'South': [ 4, 5, 6, 7 ],
        'West': [ 1, 4, 7, 2 ],
        'Up': [ 5, 4, 1, 0 ],
        'Down': [ 3, 2, 7, 6 ]
	}

    Direction = [
        'North',
        'East',
        'South',
        'West',
        'Up',
        'Down'
    ]


