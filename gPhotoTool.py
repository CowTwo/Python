import os
import os.path
import shutil

lowResolutionRootDir = "d:/temp/google 相簿 test"
highResolutionRootDir = "F:/備份區/照片(20160828整理)"
destinationDir = "d:/temp/原始相簿的結果"

def find_all(name, path):
    result = []
    for root, dirs, files in os.walk(path):
        for file in files:
            if (str.lower(name)==str.lower(file)):
                result.append(os.path.join(root, file))
    return result


for parent, dirnames, filenames in os.walk(lowResolutionRootDir):
    print("LowResolution parent is : "+parent)
    for dirname in dirnames:
        print("\tLowResolution has folder={0}".format(dirname))
    print("\n")
    for filename in filenames:
        print("\tLowResolution has file={0}".format(filename))
        print("\tFind the corresponding HighResolution file in ={0}".format(highResolutionRootDir))
        index=0
        for foundfile in find_all(filename, highResolutionRootDir):
            print("\tCopy foundfile={0}".format(foundfile))
            destfile = destinationDir+"/"+os.path.splitext(filename)[0]+"_js"+str(index)+os.path.splitext(filename)[1]
            print("\tdestfile={0}".format(destfile))
            shutil.copy2(foundfile, destfile)
            index = (index+1)


