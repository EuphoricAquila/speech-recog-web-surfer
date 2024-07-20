import sys
import webbrowser
import speech_recognition as sr
import pyttsx3 as tts
from googleapiclient.discovery import build
import google.generativeai as genai
#import django

wakeword = "sigma"

engine = tts.init()

recog = sr.Recognizer()

def search_videos(query):
   youtube = build('youtube', 'v3', developerKey='AIzaSyDQ94OgZak3h36BrpY5hdn2twpXwEDydnM')
   request = youtube.search().list(part='id', type='video', q=query, maxResults=5)
   response = request.execute()
   return response

while True:
    
    try:
               
        with sr.Microphone() as source:
            recog.adjust_for_ambient_noise(source, duration=0.5)
            audio = recog.listen(source)
            bitchass = recog.recognize_wit(audio, key="WX5PIGPCIB6GCHDO7UTMSZWFERJE6MJY")
            bitchass = bitchass.lower()

            if wakeword in bitchass:
                engine.say("Yes, Master, how may I assist you?")

                if "youtube" in bitchass:
                       query = bitchass.replace("youtube", "").replace(wakeword, "")
                       results = search_videos(query)

                       video_ids = [item["id"]["videoId"] for item in results["items"]]

                       ytlink = "https://www.youtube.com/watch?v=" + video_ids[0]
                       webbrowser.open_new(ytlink)
              
                elif "com" in bitchass:
                       website = bitchass.replace(" ", "").replace(wakeword, "")
                       webbrowser.register("Chrome", None, webbrowser.BackgroundBrowser("C:\Program Files\Google\Chrome\Application\chrome.exe"))
                       webbrowser.get("Chrome").open_new(website)

                elif "euphonics" in bitchass:
                        playlist = "https://open.spotify.com/playlist/1dp2pbwpRoafNqMmZCh6Il"
               
                        webbrowser.open(playlist)

                elif "gemini" in bitchass:
                        genai.configure(api_key='AIzaSyAbva3iBY6jBcwxORpDqPynemvCDySlF2o')
                        model = genai.GenerativeModel('gemini-pro')
                        hoopa = bitchass.replace("gemini", "").replace(wakeword, "")
                        response = model.generate_content(hoopa).text
                        #print(bitchass)
                        print(response)

                        #engin = tts.init()
                        #engin.say(response)

                elif "google" or "what" or "how" or "where" or "why" or "when" or "who" or "will" in bitchass:
                       glink = "https://www.google.com/search?q=" + bitchass.replace("google", "").replace(wakeword, "")
                       webbrowser.open(glink)
                       
            elif "stop" in bitchass:
                sys.exit()  
            
    except sr.UnknownValueError:
         jok = "Speak louder"
         #engine = tts.init() 
         #engine.say(jok) 
         #engine.runAndWait()
    
    except sr.RequestError as e:
    # Handle the case when there is an issue with the speech recognition service
        print("Wit error; {0}".format(e))
