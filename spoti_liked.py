import json
import requests
import base64 

ff = open("/mnt/d/projects/spotifree_v2/config.json","r")
data = json.load(ff)
client_id = data["client_id"]
client_secret = data["client_secret"]


def liked(access_code):

    


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
    data = {
    'grant_type': 'authorization_code',
    'code': access_code,
    'redirect_uri': 'https://happens817.000webhostapp.com/'
    }

    r = requests.post(token_url,data=data,headers=header)

    repsonse = r.json()
    token1 = repsonse["access_token"]
    token2 = repsonse["refresh_token"]
    

    sauce = "https://api.spotify.com/v1/me/tracks?offset=0&limit=50"

    a = token1
    header = {
        "content_type": "appliaction/json",
        "Authorization": f"Bearer {a}",
        
    }


    r = requests.get(sauce,headers=header)
    S = []
    
    stuff = r.json()
    # print(stuff["next"])
    for k in range(0,len(stuff["items"])):
        S.append(stuff["items"][k]["track"]["name"])

    a = []

    while stuff["next"]!=None:
        sauce = stuff["next"]
        r = requests.get(sauce,headers=header)
        stuff = r.json()
        O = stuff["items"]
        for k in range(0,len(O)):
            artist = O[k]["track"]["artists"][0]["name"]
            song = stuff["items"][k]["track"]["name"]
            P = song +" "+artist+" audio"
            S.append(P)


    return S

