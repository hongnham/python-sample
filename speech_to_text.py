import speech_recognition as sr

recognizer = sr.Recognizer()

''' recording the sound '''

with sr.Microphone() as source:
    print("Start hearing....../n Please speak ")
    recognizer.adjust_for_ambient_noise(source, duration=1)
    print("Bat dau nghe ban noi trong 4s")
    recorded_audio = recognizer.listen(source, timeout=4)
    print("Da hoan tat viec nghe ban noi")

''' Recorgnizing the Audio '''
try:
    print("Chuyen giong noi cua ban thanh van ban")
    text = recognizer.recognize_google(
            recorded_audio, 
            language="en-US"
        )
    print("Ban da noi : {}".format(text))

except Exception as ex:
    print(ex)
