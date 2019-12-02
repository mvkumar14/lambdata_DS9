"""
lambdata - a collection of data science helper functions
"""

import pandas as pd
import numpy as np

#sample code
# it is best practice to have data in caps
ONES = pd.DataFrame(np.ones(10))
ZEROES = pd.DataFrame(np.zeros(50))

#Example functions
def increment(num):
    return (num+1)
