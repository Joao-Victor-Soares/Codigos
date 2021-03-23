from pytube import YouTube
link = input("Entre com o link: ")
video = YouTube(link)
stream = video.streams.get_highest_resolution()
stream.download()