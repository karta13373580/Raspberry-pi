import speech_recognition as sr
import wave, pyaudio
import MySQLdb

FORMAT= pyaudio.paInt16
CHUNK = 1024
RATE = 16000
CHANNELS = 1
RECORD_SECONDS = 5
a=""
def recordWave():
    pa = pyaudio.PyAudio()
    stream = pa.open(format=FORMAT,
                     channels=CHANNELS,
                     rate=RATE,
                     input=True,
                     frames_per_buffer=CHUNK)
    print('Recording...')
    buffer = []
    for i in range(0, int(RATE/CHUNK*RECORD_SECONDS)):
        audio_data = stream.read(CHUNK)
        buffer.append(audio_data)
    print('Record Done')
    stream.stop_stream()
    stream.close()
    pa.terminate()
    wf = wave.open('record.wav', 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(pa.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(buffer))
    wf.close()
    
def main():
    print('wait command...')
    command = input()
    if command =='s':
        recordWave()
        r = sr.Recognizer()
        with sr.AudioFile("record.wav") as source:
            sound = r.listen(source)
        try:
            print('Recognizing')
            target = r.recognize_google(sound, language="zh-TW")
            a=str(target)
            print(a)
            return a
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
        except sr.RequestError as e:
            print("No response from Google Speech Recognition service: {0}".format(e))
            
if __name__ =='__main__':
    a=main()
    # 打开数据库连接
db = MySQLdb.connect(host='192.168.0.100',
                             user='lihen',
                             password='12345678',
                             db='lihen_', charset='utf8' )

# 使用cursor()方法获取操作游标 

cursor = db.cursor()
try:
   
   # 执行sql语句
   cursor.execute("INSERT INTO speech(target) VALUES ('%s')" %(a))
   # 提交到数据库执行
   db.commit()
except:
   # Rollback in case there is any error
   db.rollback()

# 关闭数据库连接
db.close()    
    
  
    



    
    