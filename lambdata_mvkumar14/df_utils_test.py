import unittest
from df_utils import tvt_split
import pandas as pd
import numpy as np

test_df = pd.DataFrame(np.ones([10,10]))
train = pd.DataFrame(np.ones([5,10]))
val = pd.DataFrame(np.ones([2,10]))
test = pd.DataFrame(np.ones([3,10]))

class DfUtilsTests(unittest.TestCase):
    """ Function to test df_utils module in lambdata package"""
    def test_tvt_split(self):
        self.assertEqual((tvt_split(test_df).shape),train.shape)
        # The above actually fails because the indexes are different
        # for a random selection of a DF compared to a df of the same
        # size. A reindex of tv

if __name__ == '__main__':
    unittest.main()
