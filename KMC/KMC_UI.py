# Written by: Wesley Reynolds

from NormalDatabase import *
import KMC


# The KMC package requires there be exactly one flag, namely the "-n" flag

# void --> void
def usageMsg():
    print("Usage: sMac path fileType kmc -n")
    print("Where: n = the number of mean vector desired.\n\nThere must be exactly \"-n\" flag present")
    exit(1)


# If the "-n" contains a value that cannot be interpreted as an integer,
# notify and exit

# string --> void
def invalidNFlag(flag):
    print("%s could not be recognized as an integer")
    usageMsg()


# Given an array of mean Vectors and a label Vector from a NormalDatabase,
# this method will print all Vectors to stdout

# Vector[], NormalDatabase --> void
def displayKMeans(meanVectors, db):
    displayLabels(db)
    displayCleanVectorArray(meanVectors, db)
    displayVarianceInfo(meanVectors, db)


# Given an array of Vectors and a NormalDatabase with 'training' data,
# this method will display the variance explained by the model

# Vector[], NormalDatabase --> void
def displayVarianceInfo(vecArray, db):
    nullVar, altVar, percentExp = KMC.getVarianceInfo(vecArray, db)
    print("\nVariance with no model: %6.2f\n   Variance with model: %6.2f" % (nullVar, altVar))
    print("\t Percent explained: %3.4f" % percentExp)


# Displays the labels of all Numeric dimensions that are not to be dismissed

# NormalDatabase --> void
def displayLabels(db):
    for dimension in range(db.dimension):
        if db.checkDisplayCondition(dimension):
            print("%6.6s" % db.labels.components[dimension], end=" ")
    print()


# Displays all of the Numeric data in the given Vector array.
# "Clean" in this case means that unwanted data is not presented and the data is properly padded

# Vector[] --> void
def displayCleanVectorArray(vectors, db):
    for vector in vectors:
        displayCleanVector(vector, db)


# Prints all the numeric data in a Vector that is not to be dismissed with padding

# Vector, NormalDatabase
def displayCleanVector(vector, db):
    for dimension in range(db.dimension):
        if db.checkDisplayCondition(dimension):
            print("%6.3f" % vector.components[dimension], end=" ")
    print()
