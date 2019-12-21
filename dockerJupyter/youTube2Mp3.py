"""
Run this script in jupyter docker container
Pre-requisite:
pip install youtube_dl
"""

from __future__ import unicode_literals
import youtube_dl

ydl_opts = {
            'format': 'bestaudio/best',
            'postprocessors': [{
                                    'key': 'FFmpegExtractAudio',
                                    'preferredcodec': 'mp3',
                                    'preferredquality': '192'
                               }],
            'postprocessor_args': [
                                    '-ar', '16000'
                                  ],
            'prefer_ffmpeg': True,
            'keepvideo': False
            }

with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        #ydl.download(['http://www.youtube.com/watch?v=BaW_jenozKc'])
        ydl.download(['https://www.youtube.com/watch?v=G8kiCj6HPzo'])
