# Holds voxel data with one segmentation class value >0 and bg class = 0
import numpy as np

class Coordinate():

    def __init__(self, xyz):
        self.x = xyz[0]
        self.y = xyz[1]
        self.z = xyz[2]


class VoxelData():

    
    def __init__(self,data):
        self.data = data
        self.xyz = self.get_coords(data)
        # self.x = self.xyz[0,:]
        # self.y = self.xyz[1,:]
        # self.z = self.xyz[2,:]
        self.x_length = np.size(data,0)
        self.y_length = np.size(data,1)
        self.z_length = np.size(data,2)
        self.vertices = self.make_edge_verts()
        # self.triangles 


    def get_coords(self, data):
        indices = np.nonzero(data)
        indices = np.stack((indices[0], indices[1],indices[2]))
        return indices

    def has_voxel(self,neighbor_coord):
        return self.data[neighbor_coord[0],neighbor_coord[1],neighbor_coord[2]]


    def get_neighbor(self, voxel_coords, direction):
        x = voxel_coords[0]
        y = voxel_coords[1]
        z = voxel_coords[2]
        offset_to_check = CubeData.offsets[direction]
        neighbor_coord = [x+ offset_to_check[0], y+offset_to_check[1], z+offset_to_check[2]]

        # return 0 if neighbor out of bounds or nonexistent
        if (any(np.less(neighbor_coord,0)) | (neighbor_coord[0] >= self.x_length) | (neighbor_coord[1] >= self.y_length) | (neighbor_coord[2] >= self.z_length)):
            return 0
        else:
            return self.has_voxel(neighbor_coord)


    def make_face_verts(self, voxel_coords):
        cube = []
        for direction in range(len(CubeData.direction)):
            if np.any(self.get_neighbor(voxel_coords, direction)):
                continue
            else: 
                cube = np.append(cube,'face')
        return cube


    def make_edge_verts(self):
        edge_verts = []
        num_voxels = np.size(self.xyz, 1)
        for voxel in range(num_voxels):
            faces = self.make_face_verts(self.xyz[:, voxel])
            edge_verts = np.append(edge_verts, faces)
        return edge_verts
        

    
class CubeData:
    face_triangles = {
		'North':  [0, 1, 2, 3 ],
        'East': [ 5, 0, 3, 6 ],
	    'South': [ 4, 5, 6, 7 ],
        'West': [ 1, 4, 7, 2 ],
        'Up': [ 5, 4, 1, 0 ],
        'Down': [ 3, 2, 7, 6 ]
	}

    direction = [
        'North',
        'East',
        'South',
        'West',
        'Up',
        'Down'
    ]

    # xyz direction corresponding to 'Direction'
    offsets = [             
        [0, 0, 1],
        [1, 0, 0],
        [0, 0, -1],
        [-1, 0, 0],
        [0, 1, 0],
        [0, -1, 0]
    ]


