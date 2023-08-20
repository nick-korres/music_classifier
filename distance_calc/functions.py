import numpy as np
from distance_calc.comparable_attributes import comparable_attributes
from scipy.spatial import distance
from distance_calc.dict_to_vector import dict_to_vector

def euclidean_distance(inputA,inputB):
    vectorA = dict_to_vector(inputA,comparable_attributes)
    vectorB = dict_to_vector(inputB,comparable_attributes)
    return distance.euclidean(vectorA,vectorB) 


def manhattan_distance(inputA,inputB):
    vectorA = dict_to_vector(inputA,comparable_attributes)
    vectorB = dict_to_vector(inputB,comparable_attributes)
    return distance.cityblock(vectorA,vectorB)

def cosine_distance(inputA,inputB):
    vectorA = dict_to_vector(inputA,comparable_attributes)
    vectorB = dict_to_vector(inputB,comparable_attributes)
    return distance.cosine(vectorA,vectorB)

def minkowski_distance(inputA,inputB):
    vectorA = dict_to_vector(inputA,comparable_attributes)
    vectorB = dict_to_vector(inputB,comparable_attributes)
    return distance.minkowski(vectorA,vectorB)

def jaccard_distance(inputA,inputB):
    vectorA = dict_to_vector(inputA,comparable_attributes)
    vectorB = dict_to_vector(inputB,comparable_attributes)
    return distance.jaccard(vectorA,vectorB)

def hamming_distance(inputA,inputB):
    vectorA = dict_to_vector(inputA,comparable_attributes)
    vectorB = dict_to_vector(inputB,comparable_attributes)
    return distance.hamming(vectorA,vectorB)

def chebyshev_distance(inputA,inputB):
    vectorA = dict_to_vector(inputA,comparable_attributes)
    vectorB = dict_to_vector(inputB,comparable_attributes)
    return distance.chebyshev(vectorA,vectorB)