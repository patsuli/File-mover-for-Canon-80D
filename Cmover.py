import os
import datetime


filenames = os.listdir("G:/DCIM/100CANON")

#lists of file types
#video_types = ["mp4"]
#picture_types = ["cr2", "jpg"]
print (filenames)

#tee kansiot ennen looppia

for i in filenames:
    if "jpg" in i or "cr2" in i:
