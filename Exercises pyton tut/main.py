import playsound as ps
import time
from winotify import Notification, audio

toast = Notification(app_id="Desktop notification",
                     title="Water break reminder",
                     msg="Time to drink water🥛"
                     )
while True:
    toast.show()
    time.sleep(2)
    ps.playsound("E:\\exercise of python\\sound.mp3")
    time.sleep(15)


