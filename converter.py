import os
import pydub
from rich.progress import track
import glob
def convert(src):
    wma_files = glob.glob(f'{src}*.wma')
    avi_files = glob.glob(f'{src}/*.avi')
    mkv_files = glob.glob(f'{src}/*.mkv')
    webm_files = glob.glob(f'{src}/*.webm')
    wav_files = glob.glob(f'{src}/*.wav')
    m4a_files = glob.glob(f'{src}/*.m4a')
    mp4_files = glob.glob(f'{src}/*.mp4')


    all_files = [wma_files, avi_files, mkv_files, webm_files, wav_files,
                m4a_files, mp4_files]
    print("\n\n\n CONVERTING ALL FILES TO .MP3")
    for files in track(all_files):
        for file in files:
            mp3_file = os.path.splitext(file)[0] + '.mp3'
            print("converting: ", file)
            sound = pydub.AudioSegment.from_file(file)
            sound.export(mp3_file, format="mp3")
            os.remove(file)


#convert("/mnt/d/songs/")
