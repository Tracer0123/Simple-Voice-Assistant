import pyttsx3
import speech_recognition as sr
import datetime
import pywhatkit
import os
import webbrowser
import yfinance as yf
import pyjokes 
import wikipedia


# listen to microphone and return the text of hte audio using google

def speech_to_text():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 2
        audio_input = r.listen(source)
        try:
            print("I am listening")
            query = r.recognize_google(audio_input, language="en")
            print(query)
            return query
        except sr.UnknownValueError:
            print("sorry I did not understand")
            return "I am waiting"
        except sr.RequestError:
            print("Sorry the service is down")
            return "I am waiting"
        except:
            return "I am waiting"

#speech_to_text()

# Converting the transcribed text to speech
def text_to_speech(message):
    engine = pyttsx3.init()
    engine.say(message)
    engine.runAndWait()


#text_to_speech(" Hello Hello to the yellow world")


# identifying the different voices on your pc
# engine = pyttsx3.init()
# for voice in engine.getProperty('voices'):
#     print(voice)

####setting the voice assistant to a particular voice type
# id='HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-GB_HAZEL_11.0'
# engine.setProperty('voice',id)
# engine.say('Hello Hello to the yellow world')
# engine.runAndWait()


#return the weekday name
def query_day():
    day = datetime.date.today()
    print(day)
    weekday = day.weekday()
    print(weekday)
    mapping = {
        0:'Monday',1:'Tuesday',2:'Wednesday',3:'Thursday',4:'Friday',5:'Saturday',6:'Sunday'
    }
    try:
        text_to_speech(f'Today is {mapping[weekday]}')
    except:
        pass



#returns the time
def query_time():
    time = datetime.datetime.now().strftime("%H:%M") # read datetime documentation
    print(time)
    text_to_speech(f"{time} o'clock ")


query_day()
query_time()

# booting greetings
def greetings():
    text_to_speech("Hi, my name is Baymax. How may I help you ")


greetings()



# main functionality of the assistant 
def querying():
    greetings()
    start = True
    while(start):
        query = speech_to_text().lower()
        if "start youtube" in query:
            text_to_speech("starting youtube. just a second.")
            webbrowser.open('https://www.youtube.com')
            continue
        elif "start browser" in query:
            text_to_speech("opening Browser type it yourself lazy boy")
            webbrowser.open('https://www.google.com')
            continue
        elif "day" in query:
            query_day()
            continue
        elif "time" in query:
            query_time()
            continue
        elif "shutdown" in query:
            #break
            text_to_speech('I guess this is where we say our good byes.')
            break
        elif "from wikipedia" in query:
            text_to_speech("checking in wiki")
            query = query.replace("from wikipedia","")
            result = wikipedia.summary(query,sentences = 3)
            text_to_speech("this is what i found on wiki ")
            text_to_speech(result)
            continue

        elif "your name" in query:
            text_to_speech("I am Baymax")
            continue

        elif "search web" in query:
            pywhatkit.search(query)
            text_to_speech("that is what i found")
            continue

        elif "play" in query :
            query = query.replace("play","")
            text_to_speech(f'playing {query}')
            pywhatkit.playonyt(query)
            continue

        elif "joke" in query:
            text_to_speech(pyjokes.get_joke())
            continue

        elif "stock price" in query:
            search = query.split("of")[-1].strip()
            lookup = {'apple':'AAPL','amazon':'AMZN'}

            try:
                stock = lookup[search]
                stock = yf.Ticker(stock)
                currentprice = stock.info["regularMarketPrice"]
                text_to_speech(f'found it, the price is, {currentprice}')
            except:
                text_to_speech(f'sorry i have not found {search} price')




querying()
