import unittest
import pandas as pd
import pandas.util.testing as pdt
from embad import *
from skbio import DistanceMatrix


class TestEmbad(unittest.TestCase):

    def setUp(self):
        self.table = pd.DataFrame(
            [[1, 1, 0, 0, 0],
             [0, 1, 1, 0, 0],
             [0, 0, 1, 1, 0],
             [0, 0, 0, 1, 1,]],
            index = ['S1', 'S2', 'S3', 'S4'],
            columns = ['o1', 'o2', 'o3', 'o4', 'o5']
        )


    def test_embad(self):
        exp = DistanceMatrix([
            [0, 2, 4, 6],
            [2, 0, 2, 4],
            [4, 2, 0, 2],
            [6, 4, 2, 0]])
        exp.ids = ['S1', 'S2', 'S3', 'S4']
        res = embad(self.table)
        self.assertEquals(exp, res)


if __name__ == "__main__":
    unittest.main()
