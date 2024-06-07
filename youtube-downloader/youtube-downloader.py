from pytube import YouTube  
import argparse

def download_video(link, download_path):
    try:
        yt = YouTube(link)

        print(f"Title: {yt.title}")
        print(f"Views: {yt.views}")

        yd = yt.streams.get_highest_resolution()
        print("Downloading...")

        yd.download(download_path)
        print(f"Download Complete, saved to {download_path}")

    except Exception as e:
        print(e)

def main():
    parser = argparse.ArgumentParser(description="Youtube Video Downloader")

    parser.add_argument("-l", "--link", help="URL of the YouTube video you want to download")
    parser.add_argument("-p", "--path", default=".", help="Path to save the downloaded video")

    args = parser.parse_args()

    if not args.link:
        args.link = input("Paste the link of the YouTube Video>> ")

    if args.path == ".":
        user_path = input(r"Paste the path where you want to save the downloaded video (Press Enter to use current directory)>> ")
        
        if user_path:
            args.path = user_path

    download_video(args.link, args.path)

if __name__ == "__main__":
    main()