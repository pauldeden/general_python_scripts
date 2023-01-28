import sounddevice as sd
from gtts import gTTS
import os

# specify the text you want to convert to speech
text = "Hello, this is an example of using gTTS on WSL"

# create an instance of gTTS
tts = gTTS(text=text, lang='en')

# save the speech to a file
tts.save("example.mp3")

# load the mp3 file
data, sr = sd.read(example.mpe, dtype='float32')

# play the mp3 file
sd.play(data, sr)
