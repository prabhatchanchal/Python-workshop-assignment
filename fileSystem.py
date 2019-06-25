import os

path = os.getcwd()
print("path is:",path)

print(os.name)
print(os.getlogin())
print(os.getppid())

path = "/Users/rajha/Documents/Customer.csv"
print("Is path exisiting: ",os.path.exists(path))
print("Is path a Drirectory: ",os.path.isdir(path))
print("Is path a File: ",os.path.isfile(path))

path = "/Users/rajha/Documents"
print("**************all doccuments**********************")

files = os.walk(path)
allFiles = list(files) # Convert into a list
for file in allFiles:
    print(file)

path = "/Users/rajha/Music"
print("**************all Music**********************")


files = os.walk(path)
allFiles = list(files) # Convert into a list
for file in allFiles:
    print(file)
path = "/Users/rajha/Videos"
print("**************all Videos**********************")


files = os.walk(path)
allFiles = list(files) # Convert into a list
for file in allFiles:
    print(file)


# Assignment
# List all the files for Documents, Music and Videos
