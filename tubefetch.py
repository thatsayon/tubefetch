import inquirer
from pyfiglet import Figlet
from pytube import YouTube
from yaspin import yaspin
from link_check import is_youtube_link
from options import options, video_res_options
import os
import ffmpeg

intro = Figlet(font="slant")
print(intro.renderText("YT Down"))

answer = inquirer.prompt(options)
if answer['option'].lower() == 'download youtube video':
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

            input_video = ffmpeg.input(high_res_video)

            input_audio = ffmpeg.input(new_file)

            ffmpeg.concat(input_video, input_audio, v=1,
                          a=1).output('song.mp4').run()
        print("give a youtube link")
