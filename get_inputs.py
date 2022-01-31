import json


def inputs():
    f = open("/mnt/d/projects/spotifree_v2/config.json")
    data = json.load(f)

    src1 = data["default_src"]
    playlist_id = data["default_playlist"]
    
    if src1 == "":
        src = input("Enter folder path: ")
    else:
        src = input("Enter folder path (press enter for default): ")
        if src == "":
            src = src1

    if playlist_id == "":
        print("make ur playlist public if private")
        id = input("enter playlist id or 'liked' for liked songs: ")
    else:
        print("make ur playlist public if private")
        id = input("enter playlist id or 'liked' for liked songs (enter for default playlist id) : ")
        print("\n\n")
        if id == "":
            id = playlist_id
    
    return id,src

