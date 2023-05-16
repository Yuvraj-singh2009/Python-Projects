
# l = ["yuvraj","singh"]
# str = "Shout out to "
# for i in l:
#     print(str + i)

# import gtts
# import playsound
# text = "Hello yuvraj how may i help you"
# sound = gtts.gTTS(text, lang="en")
# sound.save("welcome.mp3")
# playsound.playsound("welcome.mp3")

import pyttsx3
# engine = pyttsx3.init()
# engine.say("I will speak this text")
# l = ["Rahul", "Nishant", "Harry"]
# a = "Shoutout to "
# for i in l:
# 	engine.say(a+i)

# engine.runAndWait()
# 	print(a + i)
engine = pyttsx3.init()
engine.say("Hey yuvraj! time to drink water")
engine.runAndWait()
