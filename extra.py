from pytube import YouTube
def remove_same(urls):
     
    src = '/mnt/d/projects/spotifree_v2/stuff/downloaded.txt'
    with open(src,'r') as f:
        s = f.read()
        rows = s.split("\n")
        # print("r",rows)
        # print("u",urls)
        
        a = []

        for i in range(0,len(urls)):
            for j in rows:
                if urls[i] == j:
                    a.append(urls[i])
        
        for i in a:
            yt = YouTube(i)
            print(f"Skipping... {yt.title}")
            try:
                urls.remove(i)
            except ValueError:
                pass
        return urls
                
