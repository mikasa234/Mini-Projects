import webbrowser
import time
count = 0

print("The program starts at"+time.ctime())
while count<3 :
    time.sleep(10)
    webbrowser.open("https://www.youtube.com/watch?v=nTjc1sPktlY")
    count = count+1

