import os.path
rootdir = "d:/temp/google photo test"
for parent, dirnames, filenames in os.walk(rootdir):
    print("parent is : "+parent)
    for dirname in dirnames:
        print("\tHas folder={0}".format(dirname))
    print("\n")
    for filename in filenames:
        print("\tHas file={0}".format(filename))


