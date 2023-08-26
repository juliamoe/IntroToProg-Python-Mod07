# Title
**Dev:** *JMoekkoenen*  
**Date:** *8/25/2023*  
## Introduction
The goal of the assignment was to research and explore pickling and error handling in Python. An example script was created to accomplish both of the tasks. The code performed simple calculations and prompted the user to provide input values. After performing the calculations the user could write and/or read the data into a binary file.

## Pickling
Pickling allows the user to read, write, and append data to/from a .dat file. Instead of the common read = ‘r’, write = ‘w’, and append = ‘a’ commands, pickling used ‘rb’, ‘wb’, and ‘ab’ respectively. In append and write cases the file is opened in ‘ab’ or ‘wb’ modes, and pickle.dump() function is applied to add data into the file. When reading data the file is opened in ‘rb’ mode and pickle.load() function is used to load the data. The advantages of pickling are that it keeps track of the objects it has already processed and won’t duplicate them, this way saving space on the machine [GeeksforGeeks](https://www.geeksforgeeks.org/understanding-python-pickling-example/). To use pickling an external pickle module has to be imported into the code by using ‘import pickle’ function.

### Error Handling
Error handling helps the developer to limit the type of answers the user could give. For example, in Figure 1.3 the questions are expecting the user to provide an integer values 1 and 2. If the user inputs an answer that isn’t an integer, the program will prompt the user to input an integer instead and break the loop. The error is caught by try-except clause, but if no exceptions are detected the except clause will be skipped and the script moves on to the next line below [Handling Exceptions](https://docs.python.org/3/tutorial/errors.html).
## Summary
The goal of the assignment was to research and explore pickling and error handling in Python. The script created for this accomplished both tasks by reading, and saving data into a binary file by using pickling, and error handling by checking if the values given for the value 1 and value 2 were actually integers. 
