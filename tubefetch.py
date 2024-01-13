import inquirer
from pyfiglet import Figlet
from pytube import YouTube
from yaspin import yaspin
from link_check import is_youtube_link
from options import options, video_res_options
import os
import ffmpeg
from moviepy.editor import VideoFileClip, AudioFileClip, concatenate_videoclips

intro = Figlet(font="slant")
print(intro.renderText("tubefetch"))


def combine_audio(vidname, audname, outname, fps=25):
    video_clip = VideoFileClip(vidname)
    audio_clip = AudioFileClip(audname)
    final_clip = video_clip.set_audio(audio_clip)
    final_clip.write_videofile(outname + ".mp4")


answer = inquirer.prompt(options)
if answer['option'].lower() == 'download youtube video':
    while True:
        video_link = input("Enter YouTube Video Link: ")
        if is_youtube_link(video_link):
            video_res = inquirer.prompt(video_res_options)
            with yaspin(text="Downloading", color="yellow") as spinner:
                yt = YouTube(video_link)
                video = yt.streams.filter(only_audio=True).first()
                out_file = video.download(output_path=".")
                base, ext = os.path.splitext(out_file)
                new_file = base + "_audio" + '.webm'
                os.rename(out_file, new_file)
                spinner.write("> audio file downloaded")

                high_res_video = yt.streams.order_by(
                    'resolution').desc().first().download()

            combine_audio(high_res_video, new_file, "song")
        print("Give a valid YouTube link")

elif answer['option'].lower() == 'quit':
    quit()
