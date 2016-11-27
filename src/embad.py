import numpy as np
from functools import partial
from skbio import DistanceMatrix
from pyemd import emd


def embad(table):
    """
    Calculates the pairwise Earth Mover's distance.

    Assumes that the table is sorted.

    Parameters
    ----------
    table : pd.DataFrame
        Contingency table where the columns are features and the
        rows are samples.

    Returns
    -------
    skbio.DistanceMatrix
        Pairwise distance matrix of Earth Mover's distances
    """

    numsamples, numfeatures = table.shape
    sample_permutation = range(numsamples)

    def emd_dist_matrix( numfeatures ):
        D = np.zeros((numfeatures, numfeatures))
        for i in range(numfeatures):
            for j in range(numfeatures):
                D[i, j]=abs(i-j)
        D = D.astype(np.float64)
        return D

    D = emd_dist_matrix (numfeatures)
    distance_metric = partial(emd, distance_matrix = D)
    table_values = table.values.astype(np.float)
    sample_distance = DistanceMatrix.from_iterable(np.ascontiguousarray(table_values),
                                                   distance_metric)
    sample_distance.ids = table.index[sample_permutation]
    return sample_distance

