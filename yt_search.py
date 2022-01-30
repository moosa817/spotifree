from os import replace
import requests
import re

def yt_search(search):
    # search = search+" audio"
    search = search.replace(" ","+")

    html = requests.get("https://www.youtube.com/results?search_query="+search)

    video_ids = re.findall(r"watch\?v=(\S{11})", html.text)
    # print(video_ids)

    vid = video_ids[0]

    vid = "https://www.youtube.com/watch?v="+vid
    return vid
    # print(vid)