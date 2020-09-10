# Written by: Wesley Reynolds

from KMC_UI import *
from Vector import *
from random import *


######################################################################################
# How to use KMC
#
# Command:
# sMac path dataType kmc -n
# WHERE:
#     n: the number of mean vectors wanted
######################################################################################

# Checks to ensure that there is exactly one flag (the "-n" flag)

# string[] --> void
def checkFlagCount(flags):
    if len(flags) != 1:
        usageMsg()


# Function called by preformAnalysis() that expects a complete NormalDatabase
# and an argument-vector-style array of strings to determine what should be done.
# preformKMC() gets the data needed to do all of the visualizations requested.

# NormalDatabase, string[] --> void
def preformKMC(db, flags):
    checkFlagCount(flags)   # Must be just one flag ("-n")
    k = getK(flags)
    kMeans = getKMeans(db, k)  # kMeans is a Vector[]
    displayKMeans(kMeans, db)


# From the 'flags' array, the desired value of k is determined.
# RETURNS - the value of k specified by the caller

# string[] --> int
def getK(flags):
    try:
        return int(flags[0][1:])
    except ValueError:
        invalidNFlag(flags[0][1:])


# Given the training Vector in the NormalDatabase 'db', and the integer 'k' means wanted,
# this function determines the 'k' mean vectors to represent the data
# RETURNS - Vector with components being the 'k' mean vectors of the data

# NormalDatabase, int --> Vector[]
def getKMeans(db, k):
    kMeansArray = getInitialMeanVectors(db, k)    # kMeansArray is an array of Vectors
    notConverged = True

    while notConverged:
        notConverged, kMeansArray = updateMeanVectors(kMeansArray, db.training)

    return kMeansArray


# Pick 'k' random vectors from the training data in the
# NormalDatabase 'db' as the initial mean vectors.
# RETURNS - array of 'k' mean Vectors

# NormalDatabase, int --> Vector[]
def getInitialMeanVectors(db, k):
    meanVectors = []    # Initialize array to return
    dataSetSize = len(db.training.components)
    # Pick 'k' random Vectors from the training data
    for i in range(k):
        randVecIdx = int(random() * dataSetSize) % dataSetSize
        meanVectors.append(db.training.components[randVecIdx])

    return meanVectors


# Given an array of current mean Vectors and all of the training data,
# calculate a new set of mean Vectors and determine if the amount of
# variance explained by the new mean vectors is significantly better
# than the amount of variance explained by the given mean vectors.
# RETURNS - True if convergence is believed to be reached (insignificant change in variance explained)
#           False otherwise, followed by the new array of mean Vectors

# Vector[], Vector --> boolean, Vector[]
def updateMeanVectors(meanVectors, training):
    variance, meanVectors = assignGroups(meanVectors, training)  # updates the 'group' attribute of the mean Vectors
    meanVectors = getCOMVectors(meanVectors)
    newVariance, meanVectors = assignGroups(meanVectors, training)
    return checkVarSignificance(variance, newVariance), meanVectors


# Given an array of mean Vectors and the training data of a NormalDatabase,
# this method goes through each Vector in the training data and appends it
# to the group of its nearest mean vector. This method also clears the groups
# of all non-mean Vectors.
# RETURNS - total variance between training Vectors and their nearest means

# Vector[], Vector --> float
def assignGroups(meanVectors, training):
    variance = 0
    for vector in training.components:
        nearestMean = vector.findNearestVector(meanVectors)     # find the Vector in meanVectors that is closest
        nearestMean.group.append(vector)    # add current Vector to group of its nearest mean Vector
        meanVectors = updateVecInVecArray(nearestMean, meanVectors)
        variance += vector.getVectorVariance(nearestMean)   # update variance
    return variance, meanVectors


# Given an array of mean Vectors, calculate the Center of Mass of each Vector
# and all of the Vectors in its group.
# RETURNS - array of new Vectors to represent the Centers of Mass of the groups

# Vector[] --> Vector[]
def getCOMVectors(meanVectors):
    newCOMs = []
    # Get a Center of Mass Vector for each group
    for vector in meanVectors:
        vector.group.append(vector)     # Include the Vector as a member of its group
        newCOMs.append(getCOMofVecArray(vector.group))

    return newCOMs


# Gets the data needed by displayVarianceInfo.
# RETURNS - total variance assuming 1 mean, followed by total variance assuming k means,
#           followed by the percent of variance that is explained by using k means.

# Vector[], NormalDatabase --> float, float, float
def getVarianceInfo(vecArray, db):
    nullVar = getVarOfVecArray(db.training.components)  # Get variance of training data
    # Sum variances of each group to determine total variance explained
    altVar = 0
    for vector in vecArray:
        altVar += getVarOfVecArray(vector.group[1:])
    percentExp = abs(altVar - nullVar) / nullVar

    return nullVar, altVar, percentExp
