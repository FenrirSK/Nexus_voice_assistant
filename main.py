import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary
import requests
import pywhatkit
from contacts import contacts
from openai import OpenAI
from gtts import gTTS
import videos
import os

recognizer = sr.Recognizer()
engine = pyttsx3.init()
newsapi = "enter your openAi api"



def speak(text):
    engine.say(text)
    engine.runAndWait()
    

    
def aiProcess(command):
    client = OpenAI(
    api_key="########"
    )

    completion = client.chat.completions.create(
        model="gpt-5-nano",
        messages=[
        {"role": "system", "content": "you are poetic assistant, skilled in explaining complex programming concepts with creative flair."},
        {"role": "user", "content": command}
        ]
        )

    return completion.choices[0].message.content
    
def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
        
    elif "open Facebook" in c.lower():
        speak("Opening facebook")
        try:
            os.system("start facebook:")
        except:
            webbrowser.open("https://web.facebook.com")
            
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
        
    elif "open whatsapp" in c.lower():
        speak("Opening WhatsApp")
        try:
            os.system("start whatsapp:")
        except:
            webbrowser.open("https://web.whatsapp.com")
            
    elif "open instagram" in c.lower():
        speak("Opening instagram")
        try:
            os.system("start instagram:")
        except:
            webbrowser.open("https://web.instagram.com")
            
    elif c.lower().startswith("play"):
        item = c.lower().split(" ")[1]

        if item in musicLibrary.music:
            link = musicLibrary.music[item]
            webbrowser.open(link)

        elif item in videos.video:
            link = videos.video[item]
            webbrowser.open(link)

        else:
            print("Sorry, I couldn't find that song or video.")

    elif command.lower().startswith("send message"):
        print("Whom should I send the message to?")
       
        
        with sr.Microphone() as source:
            audio = r.listen(source)
            name = r.recognize_google(audio).lower()

        if name in contacts:
            print("What should I say ?")

            with sr.Microphone() as source:
                audio = r.listen(source)
                message = r.recognize_google(audio)

            print("Sending the message")
            pywhatkit.sendwhatmsg_instantly(
                contacts[name],
                message,
                wait_time=10,
                tab_close=True
            )
        else:
            speak("Sorry, this contact is not saved")

    elif "news" in c.lower():
        r = requests.get("https://newsapi.org/v2/top-headlines?country=us&category=business&apiKey='your api key'")
        # parse the JSON response
        data = r.json()
        
        # Extract the headline
        articles = data.get('articles',[])
        
        # Print the headlines
        for article in articles:
           speak('title')
            
            
    else:
        # Let OpenAI handle the request
        output = aiProcess(c)
        speak(output)
        pass
    
if __name__ == "__main__":
    speak("Initializing Nexus")

    r = sr.Recognizer()

    while True:
        try:
            with sr.Microphone() as source:
                print("Listening for wake word...")
                r.adjust_for_ambient_noise(source, duration=0.5)
                audio = r.listen(source, timeout=5, phrase_time_limit=3)

            word = r.recognize_google(audio).lower()
            print("Heard:", word)

            if "nexus" in word:
                speak("Ya")

                # Listen for command
                with sr.Microphone() as source:
                    print("Nexus active...")
                    audio = r.listen(source)

                command = r.recognize_google(audio)
                print("Command:", command)

                processCommand(command)

        except sr.WaitTimeoutError:
            pass
        except sr.UnknownValueError:
            print("Could not understand audio")             
        except Exception as e:
            print(" error; {0}".format(e))
 

