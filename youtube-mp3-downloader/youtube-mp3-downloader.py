from pytube import YouTube  
import argparse
import os

def download_mp3(link, download_path):
    try:
        yt = YouTube(link)

        print(f"Title: {yt.title}")
        print(f"Views: {yt.views}")

        yd = yt.streams.filter(only_audio=True).first()
        print("Downloading...")

        out_file = yd.download(download_path)

        base = os.path.splitext(out_file)[0]
        new_file = base + '.mp3'
        os.rename(out_file, new_file)
        print(f"Download Complete, saved to {download_path}")

    except Exception as e:
        print(e)

def main():
    parser = argparse.ArgumentParser(description="Youtube Mp3 Downloader")

    parser.add_argument("-l", "--link", help="URL of the YouTube video you want to download")
    parser.add_argument("-p", "--path", default=".", help="Path to save the downloaded mp3")

    args = parser.parse_args()

    if not args.link:
        args.link = input("Paste the link of the YouTube Video>> ")

    if args.path == ".":
        user_path = input(r"Paste the path where you want to save the downloaded mp3 (Press Enter to use current directory)>> ")
        
        if user_path:
            args.path = user_path

    download_mp3(args.link, args.path)

if __name__ == "__main__":
    main()