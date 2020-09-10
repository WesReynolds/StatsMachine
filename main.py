# Written by: Wesley Reynolds

import sys

from NormalDatabase import *
from SAnalysis import *


# Prints out the usage message and exits the program
def badArgs():
    print("Usage: sMac path fileType [stats] [flags]")
    print("Where: \"path\" = path of file")
    print("       \"fileType\" = type of file (must be supported file type*)")
    print("       [stats] = name of statistical analysis package**")
    print("       [flags] = flags specific to the statistical analysis package")
    print("\n * Supported file types listed on README")
    print("** More details about each statistical analysis package can be found on README")
    exit(1)


# Takes a string that represents the path to the target file.
# RETURNS a file descriptor for that file if possible,
# exits otherwise.

# string --> fd
def getFD(path):
    try:
        return open(path, "r")
    except FileNotFoundError:
        print("Unable to open file: ", path)
        exit(1)


# Checks if the file type entered is valid or not.
# RETURNS an integer representing the file type if no errors

# string --> int
def checkValidFileType(fileType):
    # CSV(".csv") = 1
    if fileType == "csv":
        return 1;
    else:   # If the file type is not supported, notify and exit
        print("fileType \"%s\" is unrecognized\n" % fileType)
        badArgs()


# Expects a string representing the name of the statistical package wanted.
# RETURNS a integer with a single bit on to represent statistical package

# string --> int
def packageToBitVec(package):
    # KMC = bit 0
    if package == "kmc":
        return 1
    else:   # If package is unsupported, notify and exit
        print("stats \"%s\" is unrecognized\n" % package)


# Expects an argument vector and an index to consider as the start
# of the relevant package info. This method will increment
# the index in the array in order to account for all flags
# . Also expects that the package name has already been identified.
# RETURNS an SAnalysis object for the desired statistical package.

# string[], int --> int
def processPackage(argv, idx):
    # Start at first flag index ('idx' is the index of the name of the stats package)
    i = 1
    # Array to store string representing the flags for particular stats package
    flags = []

    # Check if desired index (idx + i) exists
    if idx + i >= len(argv):
        return SAnalysis(argv[idx], flags)

    # Add all flags to for this package to array
    while argv[idx + i][0] == '-':
        flags.append(argv[idx + i])
        i += 1
        if idx + i >= len(argv):
            break

    return SAnalysis(argv[idx], flags)


# Parses the argument vector to determine all of the packages requested and creates
# an SAnalysis object for each package. An SAnalysis object of an argv-style component
# 'flags' that stores the flags (including the '-' at the beginning)
# RETURNS - array of SAnalysis objects. One SAnalysis object for each package requested

# string[] --> SAnalysis[]
def checkValidStats(argv):
    # Start iterator at 4 because we expect arguments 1, 2, 3 to
    # not contain relevant information
    i = 4
    # Array of SAnalysis objects to be returned
    sAnalysis = []

    # Process each package requested
    while i < len(argv):
        flags = processPackage(argv, i)        # Increment the pointer to the next stats package location
        sAnalysis.append(flags)
        i += len(flags.flags) + 1   # Increment i by the number of flags

    return sAnalysis


# Parses argv to ensure a valid command was entered
# RETURNS:
# fd - File Descriptor for target file
# int - Integer that represents file type
# int - Integer that is a bit vector representing selected statistical packages

# string[] --> fd, int, int
def checkArgs(argv):
    # Check for required argument length (also ensures non-zero length list)
    if len(argv) < 5:
        badArgs()

    # Check that first argument is "dataV"
    if argv[1] != "sMac":
        badArgs()

    # Get a File Descriptor, if possible
    fd = getFD(argv[2])

    # Check if the file type is valid
    # 'fileType' is a non-zero integer representing a file type
    fileType = checkValidFileType(argv[3])

    # Check for valid statistical packages
    # 'sAnalysis' is an array of SAnalysis objects
    sAnalysis = checkValidStats(argv)

    return fd, fileType, sAnalysis


# Main function of the whole program

# string[] --> int
def main(argv):
    # Use information in argv to get:
    # - File Descriptor for file with data
    # - Integer to represent the file type
    # - Array of Statistical Analysis (SAnalysis) objects to represent statistics wanted
    dataFD, fileType, sAnalysis = checkArgs(argv)

    # Create the NormalDataBase object
    normDB = makeNormalDB(dataFD, fileType)
    # Preform and display all requested statistical packages
    for analysis in sAnalysis:
        analysis.preformAnalysis(normDB)

    # Clean up before return
    dataFD.close()

    # All is done, exit
    return 0


if __name__ == "__main__":
    main(sys.argv)
