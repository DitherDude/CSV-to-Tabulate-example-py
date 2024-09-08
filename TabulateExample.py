# Writing the import line as such makes
# Tabulate accessibe through 'tb' instead of
# 'tabulate.tabulate' for easier use.
from tabulate import tabulate as tb
print("(1) On your marks...")
# end="" tells python not to go down to the next line of the
# console output, so the next print() command continues on that line.
print("(2) Locating data... ", end="")
# Try to open the data file.
try:
    # The proovided sample data file is written in the following format:
    # Name,YearOfBirth,Age,Carrots
    # e.g. Billy,2000,24,5
    file = open("RabbitBytes.csv", "r")
except FileNotFoundError:
    # File is not found.
    print("Missing data file! exitting...")
    quit()
# Program continues as file has been located.
print("done!")
print("(3) Loading data...", end="")
rawdata = file.readlines()
# Remove the \n character from the end of each line
for i in range(len(rawdata)):
    rawdata[i] = rawdata[i].replace("\n", "")
# Now we need to convert the data so tabulate understands it -
# from [..., ..., ..., ...] to [[...],[...],[...],[...]]
# as it is currently just a string array.
# However, tabulate needs an array of arrays to mimic
# a table format.
data = []
for bit in rawdata:
    bit = bit.split(",")
    data.append(bit)
print("done!\n")
# Looks good! now we can print it.
print(tb(data, headers=["Name", "YoB", "Age", "Carrots"]))
