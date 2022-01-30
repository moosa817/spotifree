import os
import shutil
import csv
import csv

def downloaded(links):
    with open("/mnt/d/projects/spotifree_v2/stuff/downloaded.csv","a") as user_data:
        for i in links:
            user_writer = csv.writer(user_data,delimiter=",")
            user_writer.writerow(str(i))

# links = [1,2]
# downloaded(links)