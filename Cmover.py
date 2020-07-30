import os
import datetime


#filenames = os.listdir("G:/DCIM/100CANON")

#lists of file types
#video_types = ["mp4"]
#picture_types = ["cr2", "jpg"]
#print (filenames)

#tee variable paiva joka on kyseinen päivä muodossa 30072020


# Directory päivittyvä kansio nimi

# Parent Directory path
parent_dir = "F:/herra MSTKs"
# Path
#path = os.path.join(parent_dir, directory)
# Create the directory
# 'GeeksForGeeks' in
# '/home / User / Documents'
#os.mkdir(path)
#print("Directory '% s' created" % directory)


#päivämäärä kansion nimeksi
date = datetime.datetime.now()
print(type(date))
if int(date.month)<10:
	month = "0" + str(date.month)
paiva = str(date.day) + month + str(date.year)
print(paiva)

directory = paiva

#tee kansiot ennen looppia
pictures = []
videos = []
'''
for i in filenames:
    if "jpg" in i or "cr2" in i:
    	pictures.append(i)
    else:
    	videos.append(i)
'''   	
