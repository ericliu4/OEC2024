from scipy.spatial import KDTree
import numpy as np


def distance_sum(input_pts, preset_pts):
    kdtree = KDTree(input_pts) # dont need leaf size since data sample will usually always be bigger
    d, i = kdtree.query(preset_pts)
    # print("closest point:", d, v[i]) # prints distance + point
    return sum(d)
