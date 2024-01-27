from scipy.spatial import KDTree
import numpy as np


def distance_sum(input_pts, preset_pts):
    kdtree = KDTree(input_pts) # dont need leaf size since data sample will usually always be bigger
    d, i = kdtree.query(preset_pts)
    # print("closest point:", d, v[i]) # prints distance + point
    return sum(d)


def damerau_levenshtein(s1, s2):
    # let s1 be written string and s2 be given string
    d = [[0] * (len(s1)+1) for i in range(len(s2)+1)] # s1 horizontal, s2 vertical
    maxdist = len(s1)+len(s2)
    d[-1][-1] = maxdist

    for i in range(len(s2)+1): d[i][0] = i # row index
    for j in range(len(s1)+1): d[0][j] = j # column index

    for i in range(1, len(s2)+1):
        for j in range(1, len(s1)+1): 
            if i == j and j == 1: d[i][j] = 0 # base case
            cost = 1 if s1[j-1] != s2[i-1] else 0

            d[i][j] = min(d[i-1][j]+1, d[i][j-1]+1, d[i-1][j-1]+cost)

            if i > 1 and j > 1 and s1[j-1] == s2[i-1-1] and s1[j-1-1] == s2[i-1]:
                d[i][j] = min(d[i][j], d[i-2][j-2] + cost)           
    
    # normalization of accuracy score
    return round(max(0,(1-(d[-1][-1])/len(s2))*100)) 

print (damerau_levenshtein("98427985798743", "hi"))


