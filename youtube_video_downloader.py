from pytube import YouTube
import tkinter as tk
from tkinter import filedialog

def download_video1(url, save_path):
    try:
        yt = YouTube(url)
        streams = yt.streams.filter(progressive=True, file_extension="mp4").order_by('resolution').desc()
        highest_res_stream = streams.first()

        if highest_res_stream:
            highest_res_stream.download(output_path=save_path)
            print("Video downloaded successfully!")
        else:
            print("No suitable stream found. Try a different URL.")
    
    except Exception as e:
        print(f"An error occurred: {e}")

import yt_dlp

def download_video(url, save_path):
    ydl_opts = {
        'outtmpl': f'{save_path}/%(title)s.%(ext)s',
    }
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        print("Download completed successfully!")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == '__main__':
    video_url = input("Please enter a YouTube URL: ")
    save_dir = "C:/Users/ruban/Downloads/youtbe test"  # Replace with desired directory
    download_video(video_url, save_dir)


def open_file_dialog():
    folder = filedialog.askdirectory()
    if folder:
        print(f"Selected folder: {folder}")
    else:
        print("No folder selected.")
    return folder

if __name__ == '__main__':
    root = tk.Tk()
    root.withdraw()

    video_url = input("Please enter a YouTube URL: ")
    save_dir = open_file_dialog()

    if save_dir:
        print("Started downloading...")
        download_video(video_url, save_dir)
    else:
        print("Please select a folder.")
