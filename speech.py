import speech_recognition as sr
r=sr.Recognizer()
while(True):
    with sr.Microphone() as source:
        print("I'm Listening...")
        audio=r.listen(source)
        try:

            text=r.recognize_google(audio)
            print("You said : {}".format(text))
            print("Press 1 if you want to try again, else press 2 to quit!")
            if(int(input())==1):
                pass
            else:
                print("Exiting!")
                break
            
        except:
            print("Sorry! I didn't understand")


