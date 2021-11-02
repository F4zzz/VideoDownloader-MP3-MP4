import time, os
from tkinter import *
from pytube import YouTube
import moviepy.editor as mp
def mp4():
    url = entry.get()
    video = YouTube(url)
    video = video.streams.get_highest_resolution()
    video.download("mp4")
def mp3():
    url = entry.get()
    title = 'mp3Download'
    video = YouTube(url).streams.get_audio_only()
    video.download("mp3", filename=f'{title}.mp4')
    titname = str(video.title)
    time.sleep(1)
    clip = mp.AudioFileClip(rf"mp3/{title}.mp4")
    time.sleep(0.5)
    clip.write_audiofile(rf"mp3/{title}.mp3")
    os.remove(rf"mp3/{title}.mp4")
    try:os.rename(rf'mp3/{title}.mp3', rf'mp3/{str(titname)}.mp3')
    except:pass
root = Tk()
root.geometry('300x200')
root.title("F4 - Video/Music YT Downloader")
entry = Entry(root, width=50)
entry.pack(pady=15, padx=20)
entry.insert(0,'Cole aqui o link do video')
b1 = Button(root, text='MP3', command=mp3, bg='red', width= 15, height=2)
b1.pack(side=LEFT,padx=8)
b2 = Button(root, text='MP4', command=mp4, bg='red', width= 15, height=2)
b2.pack(side=RIGHT,padx=8)
root.mainloop()
