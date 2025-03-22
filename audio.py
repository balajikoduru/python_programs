import gtts
from gtts import gTTS
from playsound import playsound
audio="speech1.mp3"
language="en-US"
text = ("hello")
sp=gtts.gTTS(text, lang=language,tld="co.in", slow=False)
sp.save(audio)
for i in range(2):
      playsound(audio)
print("playing the audio ")

