from pytube import YouTube
YouTube('https://youtu.be/0wlg22fYomQ').streams.first().download()
yt = YouTube('https://youtu.be/0wlg22fYomQ')
yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download()