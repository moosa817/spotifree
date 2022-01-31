import requests
import base64
import datetime
import json
ff = open("/mnt/d/projects/spotifree_v2/config.json","r")
data = json.load(ff)
client_id = data["client_id"]
client_secret = data["client_secret"]



def get_playlist(id):
    client_creds = f"{client_id}:{client_secret}"
    client_creds_bs64 = base64.b64encode(client_creds.encode())

    token_url = "https://accounts.spotify.com/api/token"
    method = "POST"
    token_data = {
        "grant_type":"client_credentials"
    }
    header = {
        "Authorization": f"Basic {client_creds_bs64.decode()}"
    }

    r = requests.post(token_url,data=token_data,headers=header)

    repsonse = r.json()
    

    access_token = repsonse["access_token"]
    expire = repsonse["expires_in"]

    sauce = f"https://api.spotify.com/v1/playlists/{id}"
    header = {
        "Authorization": f"Bearer {access_token}",
        "playlist_id":f"{id}"
    }

    r = requests.get(sauce,headers=header)
    # r.status_code

    stuff = r.json()

    import json
    # json.dump(stuff,f,indent=4)
    O = stuff["tracks"]["items"]


    n = len(O)

    S = []
    for i in range(0,n):
        # print(O[i]["track"]["name"])
        S.append(O[i]["track"]["name"])
    return S    


