import pandas
dataFrame = pandas.read_json("/home/ali/Documents/myFile.json")
print(dataFrame)

print(dataFrame.set_index("ID"))

#Slicing
#loc -- range inthe form of label
#iloc -- range in the form of index number
# ix -- range mixed labels and index
