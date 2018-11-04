# execute by "python ./getMp3FromVideo.py"
#

import subprocess, os
import shutil
import os

videoRootdir = "/myCode/temp/video/"
mp3Rootdir = "/myCode/temp/mp3/"
videoExtName = "mp4"

for parent, dirnames, filenames in os.walk(videoRootdir):
    for filename in filenames:
        print("\tHas file=%s" %filename)
        baseName=os.path.basename(filename)
        print("baseName= "+baseName)
        base = os.path.splitext(baseName)[0]
        print("base= "+base)
        ext = os.path.splitext(baseName)[1][1:]
        print("ext= "+ext)
        if (ext == videoExtName):
            print("found matched")
            videoFullPathName = videoRootdir+baseName
            print("videoFullPathName= "+videoFullPathName)
            mp3FullPathName = mp3Rootdir+base+".mp3"
            print("mp3FullPathName= "+mp3FullPathName)
            subprocess.call(['ffmpeg','-i',videoFullPathName,'-vn','-ab','128k',mp3FullPathName])
            

