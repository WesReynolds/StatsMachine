# Written by: Wesley Reynolds

from Vector import *
from NormalDatabaseUI import *


# Takes a line and creates a vector where each component is the
# contents of the relevant cell in the csv. Assumes that
# no commas ',' are present in the data.
# RETURNS - Vector that represents the line of the csv file

# string --> Vector
def lineToVectorCSV(line):
    cur = ""    # String to store cell data in
    temp = []   # Array to store strings of cell data
    # Fill temp with cell data
    for char in line:
        if char != ',':
            cur += char
        else:
            temp.append(cur)
            cur = ""
    temp.append(cur[:-1])    # Don't include newline character of last cell
    # Return the Vector representing the array constructed from 'line'
    return arrayToVector(temp)


# Given a file descriptor 'fd', fillVectorCSV()
# reads the current line referred to by 'fd'.
# RETURNS a Vector with each component containing the string present in that cell of the CSV

# fd --> Vector
def fillVectorCSV(fd):
    line = fd.readline()
    return lineToVectorCSV(line)


# Similar to fillVectorCSV, but also ensures that each entry is a valid data type
# RETURNS - same as fillVectorCSV

# fd --> Vector
def fillDataTypesVectorCSV(fd):
    vector = fillVectorCSV(fd)  # Fill the vector
    # Ensure that every data type is either "Numeric" or "Categorical"
    for dataType in vector.components:
        if dataType != "Numeric" and dataType != "Categorical":
            invalidDataTypeMsg(dataType)    # in NormalDatabaseUI

    return vector


# Creates a Vector to be used as a "training" attribute of a NormalDatabase
# Each component of the Vector will be a Vector that represents a data point.
# The dimension of the returned Vector is the size of the data set
# RETURNS - Vector to be used as "training" attribute of a NormalDatabase

# fd --> Vector
def fillTrainingCSV(fd):
    training = Vector(0)    # Create empty training Vector, to be returned
    line = fd.readline()    # Get current entry/line
    i = 0
    # For every non-empty entry, create a Vector and store it in "training"
    while line != "":
        entry = lineToVectorCSV(line)
        training.components.append(entry)
        line = fd.readline()

    return training
