import sys
import argparse
import re
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
    return re.search(youtube_link_pattern, link)


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


def download_audio():
    ...


def main():
    arguments = parse_argument()
    
    if arguments.type == "video":
        download_video(arguments.link, arguments.location_path, arguments.resolution)


if __name__ == "__main__":
    main()
