# import os library to access files and directories
import os

# Accept from user the path where files are present
path = input("Enter the complete path where files are present: ")

i=101
try:
    for filename in os.listdir(path):           # for loop to go through each file in the directory
        file = os.path.splitext(filename)       # split filename into the root name and extension
        os.rename(f'{path}/{filename}',f'{path}/Voucher {i}{file[1]}')     # rename each file
        i+=1
    print("Files are renamed successfully")
except TypeError:
    print("Invalid Path")
except PermissionError:
    print("Insufficient permissions to read the contents of the directory")
except OSError as e:
    print("Error! ", e)

