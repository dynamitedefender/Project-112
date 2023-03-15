import os
import shutil

fromdir = "Test.py"
todir = "ABC.txt"
list_of_files = os.listdir(fromdir)
#print(list_of_files)
for file_name in list_of_files:
    name, extension = os.path.splitext(file_name)
    #print(name)
    #print(extension)
    
    if extension == "":
        continue
    
    if os.path.exists(fromdir + "/" + extension):
        shutil.move(fromdir + "/" + file_name, fromdir + "/" + extension + "/" + file_name)
    else:
        os.mkdir(fromdir + "/" + extension)
        shutil.move(fromdir + "/" + file_name, fromdir + "/" + extension + "/" + file_name)
    