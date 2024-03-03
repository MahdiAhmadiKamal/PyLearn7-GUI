from threading import Thread
from moviepy import editor

def convert(input_address,output_address):
    video = editor.VideoFileClip(input_address)
    video.audio.write_audiofile(output_address)


movies = [['input/video1.mp4', 'output/audio1.mp3'],
          ['input/video2.mp4', 'output/audio2.mp3'],
          ['input/video3.mp4', 'output/audio3.mp3'],
          ['input/video4.mp4', 'output/audio4.mp3'],
          ['input/video5.mp4', 'output/audio5.mp3']]

threads = []

for input_address, output_address in movies:
    new_thread = Thread(target=convert, args=[input_address,output_address])
    threads.append(new_thread)
    
for thread in threads:
    thread.start()

for thread in threads:
    thread.join()


