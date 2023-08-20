from enum import Enum
from distance_calc.functions import chebyshev_distance, cosine_distance, euclidean_distance, hamming_distance, jaccard_distance,manhattan_distance, minkowski_distance

class DistanceFuncs(Enum):
    EUCLIDEAN = "euclidean"
    MANHATTAN = "manhattan"
    COSINE = "cosine"
    MINKOWSKI = "minkowski"
    JACCARD = "jaccard"
    HAMMING = "hamming"
    CHEBYSHEV = "chebyshev"

distance_funcs = {
    DistanceFuncs.EUCLIDEAN: euclidean_distance,
    DistanceFuncs.MANHATTAN: manhattan_distance,
    DistanceFuncs.COSINE: cosine_distance,
    DistanceFuncs.MINKOWSKI: minkowski_distance,
    DistanceFuncs.JACCARD: jaccard_distance,
    DistanceFuncs.HAMMING: hamming_distance,
    DistanceFuncs.CHEBYSHEV: chebyshev_distance
}

