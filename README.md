# YOUR PROJECT TITLE
#### Video Demo:  <URL HERE>
#### Description:

Saving youtube video as an mp4 or mp3 (audio only) to your computer

Language: python

How to use:

input link via command line argument per the below:

- Download video
    python3 program.py -t video -l (youtube link) -p (location path) -r (video resolution)
    
- Download audio
    python3 program.py -t audio -l (youtube link) -p (location path)
    

Example input:

python3 youtube_downloader.py -t video -l https://www.youtube.com/watch?v=xvFZjo5PgG0 -lp ./video -r lowest

python3 youtube_downloader.py -t audio -l https://www.youtube.com/watch?v=d020hcWA_Wg -lp ./audio

Library use:

- sys
- argparse
- pytube
- re
- pytest
    