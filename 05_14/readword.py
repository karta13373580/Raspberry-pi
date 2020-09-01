from gtts import gTTS
from pygame import mixer

def WordToSound(text):
    file_name = 'test2.mpg'
    tts = gTTS(text, lang='zh-tw')
    tts.save(file_name)
    mixer.init()
    mixer.music.load(file_name)
    mixer.music.play()
    while mixer.music.get_busy() == True:
        continue
    mixer.music.stop()
    mixer.quit()
    
def main():
    print('input a sentence to TTS!')
    text = input()
    WordToSound(text)
    
if __name__ == '__main__':
    main()