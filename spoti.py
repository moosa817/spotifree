import requests
import base64
import datetime
client_id = "ea4b936d7a58423bb3cf513c1135046c"
client_secret = "7cbcdf518f8e443ca4a20400360277be"



def get_playlist(id):
    client_creds = f"{client_id}:{client_secret}"
    client_creds_bs64 = base64.b64encode(client_creds.encode())
    print(client_creds_bs64)

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
    print(repsonse)

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


