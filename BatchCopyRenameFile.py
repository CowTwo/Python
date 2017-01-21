import os
import os.path
import shutil

sourceRootDir = "D:\Music\SongFromKtv"
destinationDir = "D:\Music\SongFromKtv_Result"

for parent, dirnames, filenames in os.walk(sourceRootDir):
    print("parent is : "+parent)
    for dirname in dirnames:
        print("\t has folder={0}".format(dirname))
    print("\n")
    for filename in filenames:
        destfile = destinationDir+"/"+os.path.splitext(filename)[0]+"_JsPri100_"+os.path.splitext(filename)[1]
        print("\tdestfile={0}".format(destfile))
        shutil.copy2(os.path.join(parent, filename), destfile)


