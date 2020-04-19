
# Load numpy data etc.
import os
import os.path
import numpy as np


EXTENSIONS = ['.npy', '.NPY']

def is_acceptable(filename):
    return any(filename.endswith(extension) for extension in EXTENSIONS)

def load_data(opt):
    data_paths = []
    data = []

    # Read in all numpy arrays in curr dir unless 'filename' was specified
    if not opt.file_name:         # if no filename given
        assert os.path.isdir(opt.dataroot), '%s is not a valid directory' % opt.dataroot

        for root, dir, fnames in sorted(os.walk(opt.dataroot)):
            for fname in fnames:
                if is_acceptable(fname):
                    data_path = os.path.join(root,fname)
                    data_paths.append(data_path)
    else: 
        data_paths = opt.file_name

    # Make toy dataset if no files found or opt set
    if opt.toy_dataset | (not data_paths):
        d = opt.toy_dataset
        data = np.floor(np.random.rand(d,d,d)*4)
        data = data > 0

        print('Making toy dataset')
    else:
        data = np.load(data_paths)

    return data

