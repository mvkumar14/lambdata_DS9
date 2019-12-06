"""
Utility functions for working with dataframes
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
from sklearn.model_selection import train_test_split

print("Testing")

def tvt_split(X):
    """
    A function that splits a dataframe into train, valdation, and test
    """

    train, test = train_test_split(X)
    train, val = train_test_split(train)

    return train


def gauss_plot(my_set=None, my_mean=None, my_stdev=None, width=2,
               height=norm.pdf(0), output_plot=False, color='b'):
    """
    This is a function to plot the gaussian distribution, the input can be a
    pandas series, or it can be a specified mean and standard deviation.
    The output can also be specified as plot or xy values.

    Dependencies:
    * scipy.stats.norm.pdf  (from scipy.stats import norm)
    * numpy.arrange         (import numpy as np)
    * matplotlib.pyplot     (import matplotlib.pyplot as plt)
    * pandas                (import pandas as pd)

    Inputs:
    my_set   = a pandas series
    my_mean  = a personally set mean
    my_stdev = a personally set standard deviation
    width = number of standard deviations to plot(bidirectional)
        for example 2 would produce a graph from
        -2 stdevs to 2 stdevs from mean
    height = Scale the y value of the gaussian.
        Note that this does change the shape of the curve, but if you don't
        want to deal with multiple axes then this could be useful
        purely as a visualization tool
        see _insert link here_ for details on how the visualization is affected
        by the height parameter.
    output_plot = should the function output a plot or return x,y values?
        True = plot directly (using matplotlib.pyplot.plot())
        False = return x, and y values (format a,b = thisfunct(your parameters)
    color = color of graph. this only matters if output_plot = True

    Returns:
    if output_plot = True :
      returns nothing, but should print plot (make sure of %matplotlib inline)
    else if output_plot = False:
      returns x and y values of gaussian plot
    """
    try:
        if my_set is None:
            if my_mean is None and my_stdev is None:
                print("You are missing required values")
                return
            else:
                lb = (my_mean - (my_stdev * width))
                ub = (my_mean + (my_stdev * width))
                x_axis = np.arange(lb, ub, 0.01)
                if output_plot is True:
                    plt.plot(x_axis,
                             (norm.pdf(x_axis, my_mean, my_stdev)) * height,
                             color=color)
                    return
                else:
                    return x_axis, (
                        norm.pdf(x_axis, my_mean, my_stdev)) * height
    except ValueError:
        set_mean = my_set.mean()
        set_stdev = my_set.std()
        lb = (set_mean - (set_stdev * width))
        ub = (set_mean + (set_stdev * width))
        x_axis = np.arange(lb, ub, 0.01)
        if output_plot is True:
            plt.plot(x_axis, (norm.pdf(x_axis, set_mean, set_stdev) * height),
                     color=color)
            return
        else:
            return x_axis, (norm.pdf(x_axis, set_mean, set_stdev)) * height


# Testing both "manual" cases
gauss_plot(None, 0, 1, 3, output_plot=True, color='r')
x, y = gauss_plot(None, 1, 3, 3, output_plot=False)
plt.plot(x, y, color='g')
