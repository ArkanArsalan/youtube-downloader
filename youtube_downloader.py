import sys
import argparse
import re
import os
from pytube import YouTube


# The name of this file could be the same in argparse library
def parse_argument():
    parser = argparse.ArgumentParser(description="Download youtube video")
    
    # Add an argument
    parser.add_argument("-t", "--type", help="Type of download (video or audio)", type=str, required=True)
    parser.add_argument("-l", "--link", help="Youtube video link", type=str, required=True)
    parser.add_argument("-lp", "--location_path", help="Location path", type=str, required=True)
    parser.add_argument("-r", "--resolution", help="Video resolution (lowest/default(720p)/highest)", type=str, required=False, default="default")

    arguments = parser.parse_args()

    # Validate value of the type argument
    if not validate_download_type(arguments.type):
        sys.exit("Invalid download type")

    # Validate the youtube link
    if not validate_link(arguments.link):
        sys.exit("Invalid link")

    return arguments


def validate_download_type(s):
    valid_type = ["video", "audio"]
    return s in valid_type


def validate_link(link):
    youtube_link_pattern = r"(?:(?:https|http)://)?(?:www.)?youtube.com/(\w+)"
    if re.search(youtube_link_pattern, link):
        return True
    else:
        return False


def download_video(link, location_path, resolution):
    yt_link = YouTube(link)

    print("Title: ", yt_link.title)

    if resolution == "highest":
        video = yt_link.streams.get_highest_resolution()
    elif resolution == "default":
        video = yt_link.streams.get_by_resolution("720p")
    elif resolution == "lowest":
        video = yt_link.streams.get_lowest_resolution()
    else:
        video = yt_link.streams.get_by_resolution(resolution)

    try:
        video.download(location_path)
    except AttributeError:
        sys.exit(f"Video doesn't support {resolution} resolution")

    return f"Download successful"



def download_audio(link, location_path):
    audio = YouTube(link)

    print("Title: ", audio.title)

    audio_file = audio.streams.get_audio_only().download(location_path)

    # Change format to mp3
    filename, file_format = os.path.splitext(audio_file)
    new_filename = filename + ".mp3"
    os.rename(audio_file, new_filename)

    return f"Download successful"


def main():
    arguments = parse_argument()
    
    if arguments.type == "video":
        print(download_video(arguments.link, arguments.location_path, arguments.resolution))
    elif arguments.type == "audio":
        print(download_audio(arguments.link, arguments.location_path))


if __name__ == "__main__":
    main()
