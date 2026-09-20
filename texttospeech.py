from gtts import gTTS

text="Hello How are you"

tts=gTTS(text=text,lang="en")

tts.save("voice.mp3")

print("Audio Saved Succesfully")