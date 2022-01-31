from pytube import YouTube
import os 
from rich.progress import track

"https://www.youtube.com/watch?v=IJYDVPPAkT0"


def download(urls,src):
    print("\n\nDownloading stuff..")
    for url in track(urls):
        try:
            yt = YouTube(url)
            
            stream = yt.streams.get_by_itag(251)
            print("Downloading... "+ yt.title)
            stream.download(src)
                        
            with open("/mnt/d/projects/spotifree_v2/stuff/downloaded.txt","a")as user_data:
                    user_data.write(f"{url}\n")
        except TypeError:
            pass
                    

# download("https://www.youtube.com/watch?v=IJYDVPPAkT0","/mnt/d/projects/spotifree_v2/tast/")
