from pytube import YouTube

link = input("Enter YouTube link: ")
yt = YouTube(link)

ys = yt.streams.get_highest_resolution()
ys.download()
print("Download completed")