import os
import datetime
import shutil

source="G:\DCIM\\100CANON"
filenames = os.listdir(source)

#lists of file types
#video_types = ["mp4"]
#picture_types = ["cr2", "jpg"]
#print (filenames)

#tee variable paiva joka on kyseinen päivä muodossa 30072020


# Directory päivittyvä kansio nimi

# Parent Directory path
parent_dir = "F:\herra MSTK"
# Path

# Create the directory
# 'GeeksForGeeks' in
# '/home / User / Documents'
#os.mkdir(path)
#print("Directory '% s' created" % directory)


#päivämäärä kansion nimeksi
date = datetime.datetime.now()
#print(type(date))
if int(date.day)<10:
	day = "0" + str(date.day)
if int(date.month)<10:
	month = "0" + str(date.month)
paiva = day + month + str(date.year)
#print(paiva)

directory = paiva
path = os.path.join(parent_dir, directory)
print(path)
#luo kansio jos kansioo ei löydy
if not os.path.isdir(path):
	os.mkdir(path)
	videopath = os.path.join(path,"videot")
	os.mkdir(videopath)
	picpath = os.path.join(path,"kuvat")
	os.mkdir(picpath)

#tee kansiot ennen looppia
pictures = []
videos = []


for i in filenames:
    if "jpg" in i or "cr2" in i:
    	pictures.append(i)
    else:
    	videos.append(i)

for pic in pictures:
	shutil.copyfile(source+"/"+pic, path+"/kuvat")

for vid in videos:
	shutil.copyfile(source+"/"+vid, path+"/videot")
