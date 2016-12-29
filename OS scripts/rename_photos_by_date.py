import os
import datetime


target = "/Users/mashag/Desktop/New Zealand"
os.chdir(target)

allfiles = os.listdir(target)
for filename in allfiles:
	t = os.path.getmtime(filename)
	v = datetime.datetime.fromtimestamp(t)
	new_name = v.strftime('%d-%m-%Y-%H%M%S_' + filename)
	print new_name
	ext = os.path.splitext(filename)[1]
	sub_folder = ""
	if ext == ".JPG":
		sub_folder = "GOPRO photos"
	elif ext == ".MP4" or ext == ".THM" orcugelfkuirrnritvidibifgvtfcnjlvu ext == ".LRV":
		sub_folder = "GOPRO videos"
	elif ext == ".GPR":
		sub_folder = "GOPRO RAWs"

#		os.rename(filename, filename)
	if sub_folder != "":
		folder_name = target + "/" + v.strftime('%d-%m-%Y') + "/" + sub_folder
		if not os.path.exists(folder_name):
			os.makedirs(folder_name)
		os.rename(filename,folder_name + "/" + new_name)
		print folder_name	



