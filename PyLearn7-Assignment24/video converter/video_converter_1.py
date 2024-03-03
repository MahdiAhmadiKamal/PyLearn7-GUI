from time import time
from moviepy import editor


start_time = time()

def convert(input_address,output_address):
    video = editor.VideoFileClip(input_address)
    video.audio.write_audiofile(output_address)


movies = [['input/video1.mp4', 'output/audio1.mp3'],
          ['input/video2.mp4', 'output/audio2.mp3'],
          ['input/video3.mp4', 'output/audio3.mp3'],
          ['input/video4.mp4', 'output/audio4.mp3'],
          ['input/video5.mp4', 'output/audio5.mp3']]

for movie in movies:
    convert(movie[0], movie[1] )

end_time = time()

print(end_time - start_time)