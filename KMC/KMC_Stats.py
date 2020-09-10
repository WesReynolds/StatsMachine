# Written by: Wesley Reynolds

# Given numbers 'n' and 'm', return the square of their difference.
# RETURNS - the square of the difference between 'n' and 'm'

# float, float --> float
def getDiffSquaredKMC(n, m):
    try:
        return (float(n) - float(m)) ** 2
    except ValueError:  # If values are not integers, return 0
        return 0


# Given two separate variances, determine if the difference between them is significant
# RETURNS - True if there is a significant difference, False otherwise

# float, float --> boolean
def checkVarSignificance(n, m):
    percentChange = (float(abs(m - n)) / float(n))
    return percentChange > 0.05
