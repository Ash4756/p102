import os
import shutil

fromdir = "C:/Users/Arimitra Das/Downloads"
todir = "F:/documents"

listoffiles = os.listdir(fromdir)
print(listoffiles)

for file in listoffiles:
    name,ext = os.path.splitext(file)
    if ext == " ":
        continue
    if ext in [ ".txt", ".doc", ".docx"]:

        path1 = fromdir + '/' + file
        path2 = todir + '/' + "doc"
        path3 = todir + '/'  +  "doc" + '/' + file
        if os.path.exists(path2):
           print("moving" + file + ".......")
           shutil.move(path1,path3)
        else :
            os.makedirs(path2)
            print("moving" + file + "......")
            shutil.move(path1,path3)
            