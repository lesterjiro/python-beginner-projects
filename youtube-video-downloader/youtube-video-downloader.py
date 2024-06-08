from pytube import YouTube  
import argparse

def download_video(link, download_path):
    """
    Downloads a YouTube video at the highest resolution.

    Args:
        link (str): URL of the YouTube video.
        download_path (str): Directory to save the downloaded video.
    """
    try:
        # Create a YouTube object with the provided link
        yt = YouTube(link)

        # Print video title and view count
        print(f"Title: {yt.title}")
        print(f"Views: {yt.views}")

        # Get the highest resolution stream available
        yd = yt.streams.get_highest_resolution()
        print("Downloading...")

        # Download the video to the specified path
        yd.download(download_path)
        print(f"Download Complete, saved to {download_path}")

    except Exception as e:
        print(e)

def main():
    """
    Parses command-line arguments and downloads the specified YouTube video.
    """
    # Create the argument parser
    parser = argparse.ArgumentParser(description="YouTube Video Downloader")

    # Add command-line arguments for the YouTube link and the download path
    parser.add_argument("-l", "--link", help="URL of the YouTube video you want to download")
    parser.add_argument("-p", "--path", default=".", help="Path to save the downloaded video")

    # Parse the arguments
    args = parser.parse_args()

    # If no link is provided via command-line, prompt the user to input it
    if not args.link:
        args.link = input("Paste the link of the YouTube Video>> ")

    # If the default path is used, prompt the user to optionally provide a path
    if args.path == ".":
        user_path = input(r"Paste the path where you want to save the downloaded video (Press Enter to use current directory)>> ")
        
        if user_path:
            args.path = user_path

    # Call the download function with the provided link and path
    download_video(args.link, args.path)

if __name__ == "__main__":
    main()
