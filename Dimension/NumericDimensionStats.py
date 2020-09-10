# Written by: Wesley Reynolds

from Vector import *
from NumericDimensionUI import *
import math


# Given the training data of a NormalDatabase and an index
# for which dimension of the data that is of interest, this function
# will calculate and...
# RETURN - the mean value of the dimension followed by
#          a Vector with components representing the dimension.

# Vector, int --> float, Vector
def getDimVectorAndMean(training, dimension):
    total = 0
    dimArray = []   # Array to store data temporarily
    # Add the 'dimension' element of each training Vector to dimArray
    for entry in training.components:
        dimArray.append(entry.components[dimension])
        total += stringToFloat(entry.components[dimension])

    mean = total / len(dimArray)
    return mean, arrayToVector(dimArray)    # Convert dimArray to Vector before return


# Given the mean of the dimension and a Vector representing the dimension (dimVector),
# getSD() will return the square root of the total variance within dimVector
# RETURNS - Standard deviation within the given vector with the given mean

# float, Vector --> float
def getSD(mean, dimVector):
    variance = 0
    for entry in dimVector.components:
        variance += ((float(entry) - mean) ** 2)
    return math.sqrt(variance)
