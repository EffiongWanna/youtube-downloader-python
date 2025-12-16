from pytube import YouTube
try:
    user_link = input("Enter Link: ")
    video_quality = input("1. Highest quality video\n2. Lowest quality video\n3. Audio only: \n")
    yt = YouTube(user_link)
    if video_quality == "1":
        video = yt.streams.get_highest_resolution()
        video.download()
        print("Download completed successfully")
    elif video_quality == "2":
        video = yt.streams.get_lowest_resolution()
        video.download()
        print("Download completed successfully")
    elif video_quality == "3":
        video = yt.streams.filter(only_audio=True).first()
        video.download()
        print("Download completed successfully")
    else:
        print("Invalid Selection!")
except Exception as e:
    print("An Error occurred (Invalid Youtube url or Check internet connection)", e)

