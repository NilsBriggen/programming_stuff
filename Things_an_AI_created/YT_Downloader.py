from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as wait

from pytube import YouTube as yt
import sys

def setDownloadPath():
    """
    set Download Path
    """
    download_path = input("Download Path: ")
    return download_path

def getVideoURL(driver):
    """
    get Video URL
    """
    video_url = input("Video URL: ")
    driver.get(video_url)
    return video_url

def getDownloadCommand():
    """
    get Download Command
    """
    quality = input("Quality: ")
    download_command = "yt.streams.get_by_itag(" + quality + ").download()"
    return download_command

def getDownloadPath():
    """
    get Download Path
    """
    return input("Download Path: ")

def youtubeDownloader(video_url, download_command, download_path):
    """
    Download Video
    """
    yt = yt(video_url)
    yt.set_filename("Video")
    yt.streams.get_by_itag(quality).download(download_path)
    print("Downloaded")

def main():
    """
    main()
    """
    video_url = getVideoURL()
    download_command = getDownloadCommand()
    download_path = getDownloadPath()
    youtubeDownloader(video_url, download_command, download_path)

if __name__ == "__main__":
    main()