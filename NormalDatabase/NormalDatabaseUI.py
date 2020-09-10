# Written by: Wesley Reynolds


# The only recognized data types are "Numeric" and "Categorical"

# string --> void
def invalidDataTypeMsg(dataType):
    print(dataType, "could not be recognized as \"Numeric\" or \"Categorical\"")
    exit(1)


# If an unrecognized file type is requested, notify and exit
# Currently recognized file types:
#   CSV (.csv): 1

# void --> void
def invalidFileTypeMsg():
    print("The file type requested could not be recognized.")
    print("The following file types are recognized:\n\tCSV (.csv)")
    exit(1)
