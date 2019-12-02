"""
Utility functions for working with dataframes
"""

import pandas as pd
from sklearn.model_selection import train_test_split

def tvt_split(X):
    """
    A function that splits a dataframe into train, valdation, and test
    """

    train, test = train_test_split(X)
    train, val = train_test_split(train)

    return train,test,val
