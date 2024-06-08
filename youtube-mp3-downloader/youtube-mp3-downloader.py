from pytube import YouTube  
import argparse
import os

def download_mp3(link, download_path):
    """
    Downloads an MP3 from a YouTube video link.

    Args:
        link (str): URL of the YouTube video.
        download_path (str): Directory to save the downloaded MP3.
    """
    try:
        # Create a YouTube object with the provided link
        yt = YouTube(link)

        # Print video title and view count
        print(f"Title: {yt.title}")
        print(f"Views: {yt.views}")

        # Filter to get only the audio stream
        yd = yt.streams.filter(only_audio=True).first()
        print("Downloading...")

        # Download the audio stream to the specified path
        out_file = yd.download(download_path)

        # Change the file extension from its current format to .mp3
        base, ext = os.path.splitext(out_file)
        new_file = base + '.mp3'
        os.rename(out_file, new_file)
        
        print(f"Download Complete, saved to {download_path}")

    except Exception as e:
        print(e)

def main():
    """
    Parses command-line arguments and downloads the specified YouTube video as an MP3.
    """
    parser = argparse.ArgumentParser(description="YouTube MP3 Downloader")

    # Add command-line arguments for the YouTube link and the download path
    parser.add_argument("-l", "--link", help="URL of the YouTube video you want to download")
    parser.add_argument("-p", "--path", default=".", help="Path to save the downloaded MP3")

    # Parse the arguments
    args = parser.parse_args()

    # If no link is provided via command-line, prompt the user to input it
    if not args.link:
        args.link = input("Paste the link of the YouTube Video>> ")

    # If the default path is used, prompt the user to optionally provide a path
    if args.path == ".":
        user_path = input(r"Paste the path where you want to save the downloaded MP3 (Press Enter to use current directory)>> ")
        
        if user_path:
            args.path = user_path

    # Call the download function with the provided link and path
    download_mp3(args.link, args.path)

if __name__ == "__main__":
    main()
