# Written by: Wesley Reynolds

class DimensionInfo:
    # A DimensionInfo object has an array of length equal to the dimensionality of the dataset.
    # dimensions: an array of NumericDimension objects that store statistical info about the specific dimension

    # int --> void
    def __init__(self, n):
        self.dimensions = [None] * n    # NumericDimension[]
