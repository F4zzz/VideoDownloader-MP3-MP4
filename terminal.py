from pytube import YouTube
import moviepy.editor as mp
import os, time
user = os.getenv("USERNAME")
url = input('URL: ')
ext = input('''[1] MP3
[2] MP4
-> ''')
if ext == '1':
    title = 'mp3Download'
    video = YouTube(url).streams.get_audio_only()
    video.download("mp3", filename=f'{title}.mp4')
    titname = str(video.title)
    time.sleep(0.5)
    clip = mp.AudioFileClip(rf"mp3/{title}.mp4")
    time.sleep(0.5)
    clip.write_audiofile(rf"mp3/{title}.mp3")
    os.remove(rf"mp3/{title}.mp4")
    try:os.rename(rf'mp3/{title}.mp3', rf'mp3/{str(titname)}.mp3')
    except:pass
elif ext == '2':
    print('Fazendo o download...')
    video = YouTube(url)
    video = video.streams.get_highest_resolution()
    video.download("mp4")
