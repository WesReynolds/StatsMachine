# Written by: Wesley Reynolds

from KMC_Stats import *


class Vector:
    # A Vector object is created with dimension 'm' meaning
    # that the 'components' attribute of the vector will be
    # an array of size 'm'. The 'group' attribute is simply
    # an empty array of size 1 that programmers can use to store various bits of information

    # int --> void
    def __init__(self, m):
        self.components = [None] * m
        self.group = [None]

    # The string to represent a Vector is its components

    # void --> void
    def __repr__(self):
        return str(self.components)

    # Two Vectors are said to be equal if their components are equal
    # RETURNS - True if the given Vector has the same components as this Vector, False otherwise

    # Vector --> boolean
    def __eq__(self, other):
        if type(other) != type(self):   # Check that a Vector was passed
            return False
        return self.components == other.components

    # Given an index 'n' and a NumericDimension object, this method
    # update this Vector such that the 'n' index is normalized (z-scores)

    # int, NumericDimension --> void
    def normalizeIndex(self, n, numDim):
        try:
            self.components[n] = numDim.getNormalData(float(self.components[n]))
        except ValueError:  # If there is an invalid entry, assume the mean
            self.components[n] = numDim.mean

    # Given another Vector, this method calculates the total variance
    # between each dimension of both Vectors

    # Vector --> float
    def getVectorVariance(self, vector):
        variance = 0
        for component in range(len(self.components)):
            variance += getDiffSquaredKMC(self.components[component], vector.components[component])     # in KMC_Stats
        return variance

    # Given an array of Vectors, determine which Vector is closest to this one

    # Vector[] --> Vector
    def findNearestVector(self, vectors):
        # By default, assume first Vector is closest
        nearestVec = vectors[0]
        nearestDist = self.getVectorVariance(vectors[0])
        # Check to see if other Vectors are closer
        for vector in vectors[1:]:
            distance = self.getVectorVariance(vector)
            # Update variables if new closest is found
            if distance < nearestDist:
                nearestVec = vector
                nearestDist = distance
        return nearestVec


# Takes an array and makes the array the components of a Vector
# RETURNS - a Vector with 'array' as the components

# [] --> Vector
def arrayToVector(array):
    vector = Vector(len(array))
    vector.components = array
    return vector


# Given an array of Vectors, calculate the Center of Mass (Categorical data replaced with 0's)
# RETURNS - Vector to represent the center of mass of the array

# Vector[] --> Vector
def getCOMofVecArray(vectors):
    com = []
    if len(vectors) < 2:
        print("Outlier was selected as random starting Vector. Please try again")
        exit(1)
    # Calculate the Center of each dimension
    for dimension in range(len(vectors[1].components)):
        dimMean = 0
        # Determine the center by taking the average (component at index 'dimension') of each Vector
        for vector in vectors[1:]:
            # Discard values if they are non-numeric
            try:
                dimMean += float(vector.components[dimension])
            except ValueError:
                pass
        com.append(dimMean / len(vectors))
    return arrayToVector(com)


# Given a Vector to update and an array of vectors, this function
# will update the Vector if it exists in the array, otherwise it
# will append the Vector to the array. *Updating the Vector will only
# update the 'group' attribute.
# RETURNS - array with updated/new Vector object

# Vector, Vector[] --> Vector[]
def updateVecInVecArray(vector, vecArray):
    for index in range(len(vecArray)):
        if vector == vecArray[index]:   # The Vector method '__eq__ ' defines Vector equality
            vecArray[index].group = vector.group
            break
    return vecArray


# Given an array of Vectors, this function will determine the
# mean Vector and variance of the array about the mean.
# RETURNS - The total variance of the 'vecArray' about the mean

# Vector[] --> float
def getVarOfVecArray(vecArray):
    totalVar = 0
    meanVec = getCOMofVecArray(vecArray)    # Get mean Vector of array
    # Calculate the sum of Vector variances about the mean
    for vector in vecArray:
        totalVar += meanVec.getVectorVariance(vector)

    return totalVar
