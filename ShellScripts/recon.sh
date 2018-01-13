ps aux | grep '5555' | grep -v grep | awk '{print $2}' | xargs kill -9
ssh -D5555 devvm273.lla2.facebook.com -fN
