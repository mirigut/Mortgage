ps aux | grep '9999' | grep -v grep | awk '{print $2}' | xargs kill -9
