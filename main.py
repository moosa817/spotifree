import os
import requests
import time
from rich.progress import track
import csv
import yt_search,spoti,extra,yt_download,fanci,get_inputs,spoti_liked,converter

#from dev 
"05CMUu4kNg2youIpC2w1W5"
"/mnt/d/projects/spotifree_v2/tast/"
"7BKdS2hAIqvU1pfXQxFZIj"


# u_spoti = input("enter playlist id or 'liked' for liked songs: ")
# src = input("Enter folder path: ")

u_spoti,src = get_inputs.inputs()

if u_spoti == "liked":
    print("\n\n Go To the link and copy the auth code and paste")
    print("\nhttps://accounts.spotify.com/authorize?client_id=ea4b936d7a58423bb3cf513c1135046c&response_type=code&redirect_uri=https://happens817.000webhostapp.com/&scope=user-library-read")
    access_code = input("\nEnter your auth code : ")

    songs = spoti_liked.liked(access_code)
    # print(songs)

    print("\n Fetching songs name from spotify")


    for i in track(songs):
        pass
        time.sleep(0.03)
        
    #for links
    links = []
    print("\n\n Fetching youtube links for songs")
    for i in track(songs):
        links.append(yt_search.yt_search(i))

    links = extra.remove_same(links)

    yt_download.download(links,src)

    converter.convert(src)





else:

    #fetching

    songs = spoti.get_playlist(u_spoti)

    
    print("\n Fetching songs name from spotify")


    for i in track(songs):
        pass
        time.sleep(0.03)
        
    #for links
    links = []
    print("\n\n Fetching youtube links for songs")
    for i in track(songs):
        links.append(yt_search.yt_search(i))

    links = extra.remove_same(links)

    yt_download.download(links,src)

    converter.convert(src)


    
        
           





