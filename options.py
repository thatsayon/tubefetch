import inquirer

options = [
    inquirer.List('option',
                  message="What do you want to?",
                  choices=['Download YouTube Video',
                           'Download YouTube Playlist',
                           'Get YouTube Video Info',
                           'Quit'],
                  ),
]

video_res_options = [
    inquirer.List('video_res',
                  message="Select Video Resolution",
                  choices=['Download the highest possible resolution',
                           'Check available resolutions'],
                  ),
]
