# StatsMachine
By Wesley Reynolds

A library that seeks to automate statistical visualizations and calculations.
The NormalDatabase, Vector, and SAnalysis libraries serve to provide common data structures
that can be of benefit for storing and calculating desired statistics given a data file.

The StatsMachine library seeks to offer a platform for which users can compute various statisitcal analyses
while only having information about their data file and its location. 
To do this, I have created a data structure (NormalDatabase) that can be used by many to create 
statistical analysis packages to their heart's desire. I also created a library (ReadCSV) that includes
a set of methods that can used to create a NormalDatabase object from a given ".csv" file and filepath.

# What to Develop Next:
- Statistical Analysis Packages: As of now, the only statistical package available is "KMC". There are
very few limits to what these packages can do. The only requirements is that it should be able to make
all calculations while only being given an appropriate NormalDatabase and SAnalysis object.

- File Extension Support: An example of this is the "ReadCSV" library. These libraries should be able to create
a completed NormalDatabase object given a valid file descriptor.

# What to Use to Develop Further:
There are 3 main libraries:

- NormalDatabase: A NormalDatabase data structure can be used to store information about
training data, instructions, data types, dimensional labels, and dimensional statistics.
All numerical data in a NormalDatabase is stored as a z-score. Additional information about (non-normalized)
data is stored in the dimensionalStats attribute. This library also include a variety of functions
that are useful in creating, updating, and querying a NormalDatabase object.

- Vector: A Vector data structure contains an array and an attribute titled "group".
This "group" attribute can be used for various statistical calculations and debugging purposes.
The array is used to store the values in the vector. Like the NormalDatabase library,
the Vector library also includes various functions to aid in creating, updating, and querying Vector objects.

- SAnalyis: An SAnalysis data structure is used to store information about the flags that
determine what is to be done. The attribute, called "flags", is an argument-vector-style array of strings. 
The strings still include the '-' at the begining of a flag.
