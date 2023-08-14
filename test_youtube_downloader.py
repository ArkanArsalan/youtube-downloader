import pytest
from youtube_downloader import validate_download_type, validate_link, download_video, download_audio
from pytube import exceptions

def test_validate_download_type():
    assert validate_download_type("video") == True
    assert validate_download_type("audio") == True
    assert validate_download_type("display") == False
    assert validate_download_type("") == False


def test_validate_link():
    assert validate_link("https://www.youtube.com/watch?v=xvFZjo5PgG0") == True
    assert validate_link("www.youtube.com/watch?v=xvFZjo5PgG0") == True
    assert validate_link("youtube.com/watch?v=xvFZjo5PgG0") == True
    assert validate_link("instagram.com/watch?v=xvFZjo5PgG0") == False
    assert validate_link("watch?v=xvFZjo5PgG0") == False


def test_download_video():
    assert download_video("https://www.youtube.com/watch?v=xvFZjo5PgG0", "./video", "lowest") == "Download successful"
    with pytest.raises(exceptions.VideoUnavailable):
        download_video("https://www.youtube.com/watch?v=xvFZjo5dga0", "./video", "lowest")
    with pytest.raises(exceptions.RegexMatchError):
        download_video("https://www.youtube.com/watch?v=xPgG0", "./video", "highest")


def test_download_audio():
    assert download_audio("https://www.youtube.com/watch?v=xvFZjo5PgG0", "./audio") == "Download successful"
    with pytest.raises(exceptions.VideoUnavailable):
        download_audio("https://www.youtube.com/watch?v=xvFZjo5dga0", "./audio")
    with pytest.raises(exceptions.RegexMatchError):
        download_audio("https://www.youtube.com/watch?v=xPgG0", "./audio")