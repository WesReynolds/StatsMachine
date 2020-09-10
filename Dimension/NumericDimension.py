# Written by: Wesley Reynolds

import NumericDimensionStats


class NumericDimension:
    # A NumericDimension object is used to store information
    # about the dimension as a whole such as the mean and standard deviation.

    # float, float --> void
    def __init__(self, mean, sd):
        self.mean = mean
        self.sd = sd

    # RETURNS - the z-score of the given 'data'

    # float --> float
    def getNormalData(self, data):
        return (data - self.mean) / self.sd


# Constructor used to create a NumericDimension object given
# the "training Vector" of the NormalDatabase and an index to
# indicate which dimension in the data is to be altered.
# RETURNS - NumericDimension object to represent the 'dim' dimension of the data

# Vector, int --> NumericDimension
def createNumericDimension(training, dimension):
    mean, dimVector = NumericDimensionStats.getDimVectorAndMean(training, dimension)
    sd = NumericDimensionStats.getSD(mean, dimVector)

    return NumericDimension(mean, sd)
