import pafy
import os

file = open('links.txt')
link = file.readlines()
#link of the videos to be downloaded

 
for url in link:
    url = url[:-1]
    # print(url)
    video = pafy.new(url)
    print(video.title)
    # streams = video.streams
    # for i in streams:
    #     print(i)
        
    # get best resolution regardless of format
    best = video.getbest()
    
    print(best.resolution, best.extension)
    
    # Download the video
    best.download()
    # print("Download COMPLETED")
    print()
    
