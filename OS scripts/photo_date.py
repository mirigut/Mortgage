import os, time, shutil, sys

dir = '/Users/mashag/Desktop/New Zealand/1/RAWs'
os.chdir(dir)
for f in os.listdir('.'):
    ftime = time.gmtime(os.path.getmtime(f))
    ctime_dir = str(ftime.tm_mon) +  '-' +  str(ftime.tm_mday) + '-' + str(ftime.tm_year)
    if not os.path.isdir(ctime_dir):
        os.mkdir(ctime_dir)
    dst = ctime_dir + '/' + f
    print f
    shutil.move(f, dst);
    print('File ' + f + ' has been moved to ' + dst)