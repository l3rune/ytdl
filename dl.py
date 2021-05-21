import os

os.system("P:\youtubedl\youtube-dl.exe -o P:\youtubedl\dl\%(title)s.%(ext)s --audio-format best https://www.youtube.com/playlist?list=PLmkXyPv4qj46aNoDM5BPXpBktCLD-ZfYk")
filenames = os.listdir("P:\youtubedl\dl")

for fl in filenames:
	os.system("P:\youtubedl\\ffmpeg.exe -i \"P:\youtubedl\dl\\"+fl+"\" \""+fl[:-5]+"\".mp3")
