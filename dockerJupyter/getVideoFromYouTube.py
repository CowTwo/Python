import pytube

linkFromYoutube=[
"https://www.youtube.com/watch?v=mpjREfvZiDs"
]

for n in range(0,len(linkFromYoutube),+1):
    yt = pytube.YouTube(linkFromYoutube[n])
    stream = yt.streams.first()
    stream.download("/myCode/temp/tmp/")
