# from pytube import YouTube
import os 
import yt_dlp

from rich.progress import track

"https://www.youtube.com/watch?v=IJYDVPPAkT0"


def download(urls,src):
    print("\n\nDownloading stuff..")
    for url in track(urls):
        if url == None:
            pass
        else:
            # yt = YouTube(url)
                
            # stream = yt.streams.get_by_itag(251)
            # print("Downloading... "+ yt.title)
            # stream.download(src)
                            
            class MyLogger:
                def debug(self, msg):
                    # For compatibility with youtube-dl, both debug and info are passed into debug
                    # You can distinguish them by the prefix '[debug] '
                    if msg.startswith('[debug] '):
                        pass
                    else:
                        self.info(msg)

                def info(self, msg):
                    pass

                def warning(self, msg):
                    pass

                def error(self, msg):
                    print(msg)


            # ℹ️ See the docstring of yt_dlp.postprocessor.common.PostProcessor
            class MyCustomPP(yt_dlp.postprocessor.PostProcessor):
                # ℹ️ See docstring of yt_dlp.postprocessor.common.PostProcessor.run
                def run(self, info):
                    self.to_screen('Doing stuff')
                    return [], info


            # ℹ️ See "progress_hooks" in the docstring of yt_dlp.YoutubeDL
            def my_hook(d):
                if d['status'] == 'finished':
                    pass
                    # print('Done...')



            ydl_opts = {
                'extract-audio':True,
                'format': "bestaudio",
                'extract-audio':True,
                'audio-format':'mp3',
                'postprocessors': [{
                    # Embed metadata in video using ffmpeg.
                    # ℹ️ See yt_dlp.postprocessor.FFmpegMetadataPP for the arguments it accepts
                    'key': 'FFmpegMetadata',
                    'add_chapters': True,
                    'add_metadata': True,
                }],
                'logger': MyLogger(),
                'progress_hooks': [my_hook],
            }


            # Add custom headers

            yt_dlp.utils.std_headers.update({'Referer': 'https://www.google.com'})

            # ℹ️ See the public functions in yt_dlp.YoutubeDL for for other available functions.
            # Eg: "ydl.download", "ydl.download_with_info_file"
            os.chdir(src)
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.add_post_processor(MyCustomPP())
                info = ydl.extract_info(url,download=False)
                print(info["filesize"])

                if info["filesize"] > 12582912:
                    print("Skipping ....,",info["title"]," too big awh")
                    continue
                    
                else:
                    print(f"Downloading ..{info['title']}")
                    ydl.download(url)



                with open("/mnt/d/projects/spotifree_v2/stuff/downloaded.txt","a")as user_data:
                    user_data.write(f"{url}\n")
                        

# download(["https://www.youtube.com/watch?v=RfnE6QIpyl0"],"/mnt/d/projects/spotifree_v2/test/")
