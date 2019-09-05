from gtts import gTTS #it is google text to speech, used for to read or record the audio and parse the text
import speech_recognition as sr
import os
import webbrowser
import smtplib

def talkToMe(audio):
    print(audio)
    tts=gTTS(text=audio,lang='en')
    tts.save('audio.mp3')#to save the audio file in same folder
    os.system('mpg123 audio.mp3')#in built audio file

#listens for commands
def myCommand():
    r=sr.Recognizer()

    with sr.Microphone() as source:
        print('I am ready for your next command')
        r.pause_threshold=1 #it will wait for a moment
        r.adjust_for_ambient_noise(source,duration=1)#the backround sound or excess noise it will adjust to that
        audio=r.listen(source)#it will listen through it to what we are speaking

    try:
        command=r.recognize_google(audio)#it is used to store in the command variable that the audio variable
        print('You said :' +command+'/n')

#loop back to continue to listen for commands -when audio is unrecognized or when there is too much of noise instead it throws error or quit we loop back
    except sr.UnknownValueError:
        assistant(myCommand())

    return command

#if statements for executing commands
def assistant(command): #3 things doing her first is how to open reddit , 2nd how to send email and lastly just ask whats up.
    if 'open Reddit python' in command:#here we can put different commands for opening diff urls
        chrome_path='C:\\Program Files (x86)\\Google\\Chrome\\Application'#get the path of our browser n for mac n linux we have to set the file path.
        url='https://www.reddit.com/r/python'
        webbrowser.get(chrome_path).open(url)

    if 'what\'s up' in command:
        talkToMe('Chillin bro')

    if 'email' in command:
        talkToMe('who is the recipient')
        recipient=myCommand()#it will return the value which is the recipient name

        if 'anushka' in recipient:
            talkToMe('What should I say')
            content=myCommand()

            #init gmail smtp
            mail=smtplib.SMTP('smtp.gmail.com',587)

            #identify to server
            mail.ehlo()

            #encrypt session
            mail.starttls()

            #login
            mail.login('','')                   #enter username, #password in strings)

            #send message
            mail.sendmail('anushka', 'anushkabommakanty@gmail.com')#person name,email address in string,content)

            #close connection
            mail.close()

            talkToMe('Email sent.')

talkToMe('I am ready for your command')

while True:
    assistant(myCommand())

#i can be used for variety of things like play music,desktop progs or open other website
