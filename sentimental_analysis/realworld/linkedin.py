import youtube_comment_scraper_python
import requests
import bot_studio

from youtube_comment_scraper_python import *
import pandas as pd
import time

url = input("enter url = ")
file = input("enter output file = ")

youtube.open(url)
fullcomments = []
for i in range(0, 10):
    result = youtube.video_comments()
    data = result['body']
    fullcomments.extend(data)

dataframe = pd.DataFrame(data)
print(dataframe)
time.sleep(7)
dataframe.to_csv(file)
