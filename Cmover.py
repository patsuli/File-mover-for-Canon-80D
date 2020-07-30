import os
import datetime


filenames = os.listdir("G:/DCIM/100CANON")

#lists of file types
#video_types = ["mp4"]
#picture_types = ["cr2", "jpg"]
print (filenames)

#tee variable paiva joka on kyseinen päivä muodossa 30072020


# Directory päivittyvä kansio nimi
directory = paiva

# Parent Directory path
parent_dir = "F:/herra MSTKs"
# Path
path = os.path.join(parent_dir, directory)
# Create the directory
# 'GeeksForGeeks' in
# '/home / User / Documents'
os.mkdir(path)
print("Directory '% s' created" % directory)

# Directory
directory = "Geeks"

# Parent Directory path
parent_dir = "D:/Pycharm projects"

# mode
mode = 0o666

# Path
path = os.path.join(parent_dir, directory)

# Create the directory
# 'GeeksForGeeks' in
# '/home / User / Documents'
# with mode 0o666
os.mkdir(path, mode)
print("Directory '% s' created" % directory)


#tee kansiot ennen looppia
pictures = []
videos = []

for i in filenames:
    if "jpg" in i or "cr2" in i:
    	pictures.append(i)
    else:
    	videos.append(i)
