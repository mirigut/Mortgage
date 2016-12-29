import os
import datetime


def rename_files_in_target(target):
	os.chdir(target)
	print target
	allfiles = os.listdir(target)
	for filename in allfiles:
		t = os.path.getmtime(filename)
		v = datetime.datetime.fromtimestamp(t)
		
		orig_name = filename.split("_")[1]
		new_name = v.strftime('%m-%d-%Y-%H%M%S_' + orig_name)

		os.rename(filename,new_name)
	#	print folder_name	

base_base_target = "/Users/mashag/Desktop/New Zealand/"
os.chdir(base_base_target)
dirs = os.listdir(base_base_target)
for dir in dirs:
	base_target = base_base_target + dir
#	base_target = "/Users/mashag/Desktop/New Zealand/11-08-2016/"
	folders = ["GOPRO videos", "GOPRO photos", "GOPRO RAWs"]
	for folder in folders:
		target = base_target + "/" + folder
		if (os.path.isdir(target)):
			rename_files_in_target(target)

