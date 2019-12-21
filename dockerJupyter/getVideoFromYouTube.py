# execute by "python ./getVideoFromYouTube.py "
# For latest pytube update/example, please check https://python-pytube.readthedocs.io/en/latest/

import pytube
import os

linkFromYoutube=[
"https://www.youtube.com/watch?v=dQ0Yjvdl480",
"https://www.youtube.com/watch?v=G8kiCj6HPzo",
]

videoDownloadPath = "/myCode/temp/video/"
if not os.path.exists(videoDownloadPath):
    os.makedirs(videoDownloadPath)

for n in range(0,len(linkFromYoutube),+1):
    yt = pytube.YouTube(linkFromYoutube[n])
    stream = yt.streams.first()
    print("downloading "+linkFromYoutube[n]+" ....")
    stream.download(videoDownloadPath)
