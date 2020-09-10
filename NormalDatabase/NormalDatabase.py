# Written by: Wesley Reynolds

import NormalDatabaseUI
from Vector import *
from ReadCSV import *
from DimensionInfo import *
from NumericDimension import *


# Check that the data type is recognized.
# Report if the data type is not recognized.

# string --> void
def checkValidDataType(data):
    data.strip()  # Clear off trailing whitespace
    # The only recognized types are "Numeric" and "Categorical"
    if data != "Numeric" and data != "Categorical":
        invalidDataTypeMsg(data)  # in NormalDatabaseUI


class NormalDatabase:
    # A NormalDatabase object is an object that is used as a common
    # data structure to store information about the data set that others will develop packages for.
    #
    # dimension: int - dimension of the vectors in the data set
    # instructions: Vector - Vector object where each component corresponds
    #                        with the instruction for that dimension of the data
    # labels: Vector - each component contains a string with the title/label of the dimension
    # dataTypes: Vector - contains either "Numeric" or "Categorical"
    # dimensionalStats - a DimensionInfo object that stores info about each dimension in the data
    # training: Vector - each component is a Vector that represents the an element of dataset

    # void --> void
    def __init__(self):
        self.dimension = None
        self.instructions = None
        self.labels = None
        self.dataTypes = None
        self.training = None
        self.dimensionalStats = None

    # fileType is an int that represents the file type
    # First line: instructions
    # Second line: labels
    # Third line: data types
    # Rest: training
    # Returns the dimension of the input vectors

    # fd, int --> void
    def fillSets(self, fd, fileType):
        # CSV (.csv): 1
        if fileType == 1:
            self.instructions = fillVectorCSV(fd)   # in ReadCSV. Fills a vector with the next line indicated by the fd
            self.labels = fillVectorCSV(fd)
            self.dataTypes = fillDataTypesVectorCSV(fd)   # Similar to fillVectorCSV but also ensures valid data types
            self.training = fillTrainingCSV(fd)
        # File type is unrecognized
        else:
            invalidFileTypeMsg()

    # This method is used to set the dimension of the NormalDatabase
    # and to create a DimensionInfo object of the size of the training data

    # void --> void
    def updateDimensionInfo(self):
        # After parsing the whole file, update the dimension and dimensionalStats attributes
        self.dimension = (len(self.instructions.components))
        self.dimensionalStats = DimensionInfo(len(self.training.components))

    # Checks that the dimension in question, 'n', is "Numeric" data
    # and that it is not to be dismissed

    # int --> boolean
    def checkValidNumericDimension(self, n):
        return self.instructions.components[n] == "" and self.dataTypes.components[n] == "Numeric"

    # Given a dimension index 'n', normalizeDimension normalizes all
    # of the training data at dimension 'n'

    # int --> void
    def normalizeDimension(self, n):
        # Normalize the data in the 'n' dimension of all training Vectors
        for entry in self.training.components:
            entry.normalizeIndex(n, self.dimensionalStats.dimensions[n])

    # Normalizes all data such that all Numeric data is stored as a z-score
    # rather than the raw numbers in the data.

    # void --> void
    def normalizeNumericData(self):
        for dimension in range(self.dimension):     # Go through each dimension
            if self.checkValidNumericDimension(dimension):  # Ensure valid "Numeric" dimension
                # Create a normalized NumericDimension object, add it to DimensionInfo
                numDim = createNumericDimension(self.training, dimension)
                self.dimensionalStats.dimensions[dimension] = numDim
                # Normalize the training data
                self.normalizeDimension(dimension)

    # Data is to be displayed only if the dimension it exists in is both Numeric and not to be dismissed.
    # RETURNS - True if condition is met, False otherwise

    # int --> boolean
    def checkDisplayCondition(self, dim):
        return self.instructions.components[dim] == "" and self.dataTypes.components[dim] == "Numeric"


# Given a file descriptor and file type descriptor, read the file
# and create a NormalDatabase object to represent the data.
# fileType is an int that represents the file type.
# RETURNS - NormalDatabase object that represents the data file given

# fd, int --> NormalDatabase
def makeNormalDB(fd, fileType):
    normData = NormalDatabase()
    normData.fillSets(fd, fileType)
    normData.updateDimensionInfo()
    normData.normalizeNumericData()

    return normData
