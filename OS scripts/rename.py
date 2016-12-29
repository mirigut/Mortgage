import os
import datetime
import shutil


def move_all_to_raw(folder):
	print "--------------------------" 
	print folder
	files = os.listdir(folder)
	
	if not os.path.exists(folder + "/RAWs/"):
		os.makedirs(folder + "/RAWs/")
	for file in files:
		print folder + "/" + file
		shutil.move(folder + "/" + file, folder + "/RAWs/" + file)



target = "/Users/mashag/Desktop/New Zealand"
os.chdir(target)

subfolders = os.listdir(target)
for subfolder in subfolders:
	
	folder = target + "/" + subfolder
	if subfolder[:1] == "1":
		move_all_to_raw(folder)



