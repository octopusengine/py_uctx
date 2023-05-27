#!/usr/bin/env python3
"""
$ pip install pytube
python ytd.py www...link
"""
from sys import argv
from pytube import YouTube

__version__ = "0.1.0" # 2021/01

#dw_path = "data/" 
download_path = "../video_ytd/" # download

if len(argv) > 1:
    url = argv[1]
else:
    url = 'https://www.youtube.com/watch?v=dQw4w9WgXcQ'

print("-"*39)
print("URL:", url)

video = YouTube(url)
print("Title:", video.title)
print("Views:", video.views)
print('Length:', video.length, 's')
print("-"*39)

stream = video.streams.get_highest_resolution()
stream.download(download_path)
