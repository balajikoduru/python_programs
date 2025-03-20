import gtts
from gtts import gTTS
from playsound import playsound
audio="speech1.mp3"
language="en-US"
text=("We’ve trained a model called ChatGPT which interacts in a conversational way."
      " The dialogue format makes it possible for "
      "ChatGPT to answer followup questions, admit "
      "its mistakes, challenge incorrect premises, and reject "
      "inappropriate requests.")
sp=gtts.gTTS(text, lang=language, slow=False)
sp.save(audio)
playsound(audio)
print("playing the audio ")

