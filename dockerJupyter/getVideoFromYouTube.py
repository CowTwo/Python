import pytube

linkFromYoutube=[
"https://www.youtube.com/watch?v=xcZBZ1VSyBc&index=6&list=PL2p0OVYqLcbphVH-ya9nN3pPtAtGwvQaW&t=0s",
"https://www.youtube.com/watch?v=xMmvbeHyn8I&index=5&list=PL2p0OVYqLcbphVH-ya9nN3pPtAtGwvQaW&t=0s",
"https://www.youtube.com/watch?v=CcBdJX5OP-U&index=4&list=PL2p0OVYqLcbphVH-ya9nN3pPtAtGwvQaW&t=0s",
"https://www.youtube.com/watch?v=6dXSVgUTxdI&index=3&list=PL2p0OVYqLcbphVH-ya9nN3pPtAtGwvQaW&t=0s",
"https://www.youtube.com/watch?v=Ew4VvF0DPMc&index=2&list=PL2p0OVYqLcbphVH-ya9nN3pPtAtGwvQaW&t=0s",
"https://www.youtube.com/watch?v=i4LVsOt000g&index=16&list=PL2p0OVYqLcbq2zqSmIsxzFTuhZbSHShJE&t=0s",
"https://www.youtube.com/watch?v=UXWFeSrshek&index=15&list=PL2p0OVYqLcbq2zqSmIsxzFTuhZbSHShJE&t=0s",
"https://www.youtube.com/watch?v=FKjQTdamJeM&index=14&list=PL2p0OVYqLcbq2zqSmIsxzFTuhZbSHShJE&t=0s",
"https://www.youtube.com/watch?v=JLfXJHdQd3s&index=13&list=PL2p0OVYqLcbq2zqSmIsxzFTuhZbSHShJE&t=0s",
"https://www.youtube.com/watch?v=e4NwXdxW31c&index=12&list=PL2p0OVYqLcbq2zqSmIsxzFTuhZbSHShJE&t=0s",
"https://www.youtube.com/watch?v=GsWudXPjYlQ&index=11&list=PL2p0OVYqLcbq2zqSmIsxzFTuhZbSHShJE&t=0s",
"https://www.youtube.com/watch?v=NRbVDGcO2oM&index=10&list=PL2p0OVYqLcbq2zqSmIsxzFTuhZbSHShJE&t=0s",
"https://www.youtube.com/watch?v=mRYRQ2h3H38&index=9&list=PL2p0OVYqLcbq2zqSmIsxzFTuhZbSHShJE&t=0s",
"https://www.youtube.com/watch?v=ujrygwH8aS0&index=8&list=PL2p0OVYqLcbq2zqSmIsxzFTuhZbSHShJE&t=0s",
"https://www.youtube.com/watch?v=uxPmDS0fRZE&index=7&list=PL2p0OVYqLcbq2zqSmIsxzFTuhZbSHShJE&t=0s",
"https://www.youtube.com/watch?v=SuAH_RTQ69k&index=6&list=PL2p0OVYqLcbq2zqSmIsxzFTuhZbSHShJE&t=0s",
"https://www.youtube.com/watch?v=OtEJ6LGCW-U&index=5&list=PL2p0OVYqLcbq2zqSmIsxzFTuhZbSHShJE&t=0s",
"https://www.youtube.com/watch?v=F5RE_S8aIF8&index=4&list=PL2p0OVYqLcbq2zqSmIsxzFTuhZbSHShJE&t=0s",
"https://www.youtube.com/watch?v=w_DjvLKuHGc&index=3&list=PL2p0OVYqLcbq2zqSmIsxzFTuhZbSHShJE&t=0s",
"https://www.youtube.com/watch?v=LrTFsg4SGsQ&index=2&list=PL2p0OVYqLcbq2zqSmIsxzFTuhZbSHShJE&t=0s",
"https://www.youtube.com/watch?v=w1oM3kQpXRo&index=11&list=PL2p0OVYqLcbpSM-snYQdTj3O30aFO41Fb&t=0s",
"https://www.youtube.com/watch?v=T4pTMZuAux4&index=10&list=PL2p0OVYqLcbpSM-snYQdTj3O30aFO41Fb&t=0s",
"https://www.youtube.com/watch?v=b4xcpMCPhfE&index=9&list=PL2p0OVYqLcbpSM-snYQdTj3O30aFO41Fb&t=0s",
"https://www.youtube.com/watch?v=VtTRcWXSBwc&index=8&list=PL2p0OVYqLcbpSM-snYQdTj3O30aFO41Fb&t=0s",
"https://www.youtube.com/watch?v=nfWlot6h_JM&index=7&list=PL2p0OVYqLcbpSM-snYQdTj3O30aFO41Fb&t=0s",
"https://www.youtube.com/watch?v=VuNIsY6JdUw&index=6&list=PL2p0OVYqLcbpSM-snYQdTj3O30aFO41Fb&t=0s",
"https://www.youtube.com/watch?v=qUn1tzyTYeo&index=5&list=PL2p0OVYqLcbpSM-snYQdTj3O30aFO41Fb&t=0s",
"https://www.youtube.com/watch?v=WOKOiZo5zAQ&index=4&list=PL2p0OVYqLcbpSM-snYQdTj3O30aFO41Fb&t=0s",
"https://www.youtube.com/watch?v=fWNaR-rxAic&index=3&list=PL2p0OVYqLcbpSM-snYQdTj3O30aFO41Fb&t=0s",
"https://www.youtube.com/watch?v=e-ORhEE9VVg&index=2&list=PL2p0OVYqLcbpSM-snYQdTj3O30aFO41Fb&t=0s"
]

videoDownloadPath = "/myCode/temp/video/"

for n in range(0,len(linkFromYoutube),+1):
    yt = pytube.YouTube(linkFromYoutube[n])
    stream = yt.streams.first()
    print("downloading "+linkFromYoutube[n]+" ....")
    stream.download(videoDownloadPath)
