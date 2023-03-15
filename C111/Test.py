import os
import shutil
e = os.getcwd()
#print(e)
#os.mkdir("/Users/Test")
os.listdir()
#print(os.listdir())
os.path.exists("Test.py")
#print(os.path.exists("Test"))
Root,ext = os.path.splitext("ABC.txt")
#print(ext)
source = "ABC.txt"
destination = "Test.py/ABC.txt"
shutil.copy(source, destination)

if extension == "":
    continue

