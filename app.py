import sys
import pytube
import argparse

# The name of this file could be the same in argparse library
def parse_argument():
    parser = argparse.ArgumentParser(description="Download youtube video")
    
    # Add an argument
    parser.add_argument("-t", "--type", help="Type of download (video or audio)", type=str, required=True)
    parser.add_argument("-l", "--link", help="Youtube video link", type=str, required=True)
    parser.add_argument("-lp", "--location_path", help="Location path", type=str, required=True)
    parser.add_argument("-r", "--resolution", help="Video resolution (lowest/default/highest)", type=str, required=False, default="highest")

    arguments = parser.parse_args()

    return arguments


def validate_link(link):
    ...


def download_video():
    ...


def download_audio():
    ...


def main():
    arguments = parse_argument()
    print(arguments)

if __name__ == "__main__":
    main()
