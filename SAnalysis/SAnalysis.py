# Written by: Wesley Reynolds

from KMC import *
import SAnalysisUI


class SAnalysis:
    # An SAnalysis object is used to store information about
    # a specific statistical analysis package routine to be run.
    # The 'tag' is a string that can used to identify the type
    # of statistical analysis requested during debugging.
    # The 'flags' are an array of strings. The array contains
    # all the arguments relevant to the statistical package in order, similar to an argument vector

    # string, string[]
    def __init__(self, tag, flags):
        self.tag = tag
        self.flags = flags  # argv-esc

    # This function will call the preformX routine (Statistical package specific)

    # NormalDatabase --> void
    def preformAnalysis(self, database):
        # K Means Clustering: "kmc"
        if self.tag == "kmc":
            preformKMC(database, self.flags)
        # Invalid package requested
        else:
            SAnalysisUI.invalidPackageMsg(self.tag)
