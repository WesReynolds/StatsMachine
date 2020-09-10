# Written by: Wesley Reynolds

# The message to be displayed if "Numeric" data can not be
# recognized as numeric data

# string --> void
def invalidNumericData(string):
    print("The value \"%s\" could not be recognized as \"Numeric\"" % string)
    print("*Note that a number with a comma in it ',' will not be recognized")
    exit(1)


# Attempts to convert the given string to a float. Catches ValueErrors (non-numeric strings)

# string --> float
def stringToFloat(string):
    try:
        return float(string)
    except ValueError:
        invalidNumericData(string)
