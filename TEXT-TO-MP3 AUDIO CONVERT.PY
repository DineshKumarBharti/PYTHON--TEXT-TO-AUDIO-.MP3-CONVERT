
#  fiest terminal - pip install gTTs
# Text to Voice convert as google translate- type -text then ans -- audio mp3 file is created by this commnd

from gtts import gTTS
txt=input(" Enter the text:")
langauge= 'en'
voice=gTTS(text=txt,lang=langauge,slow=False)
voice.save("conv.mp3")