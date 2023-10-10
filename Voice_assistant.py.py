import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import pyjokes
import openai
import webbrowser
from googletrans import Translator


def translate_text(text, target_language):
    try:
        translator = Translator()
        translated = translator.translate(text, dest=target_language)
        return translated.text
    except Exception as e:
        return str(e)


# count = 3
openai.api_key = "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"
name = "brahmagyani"
listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def say(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:

            print("Listening...")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if name in command:
                command = command.replace(name, ' ')
                print(command)
            print("You : ", command)

    except:
        command = "^"
        pass

    return command


def run_command():
    command = take_command()
    # command = "play heeriye"

    global count
    if 'translate' in command:
        if 'gujarati' in command:
            search = command.split('translate')[0]
            result = translate_text(search, 'gu')
            print(name, ' : '+result)
            say(result)
            return False
        elif 'hindi' in command:
            search = command.split('translate')[0]
            result = translate_text(search, 'hi')
            print(name, ' : '+result)
            say(result)
            return False
    elif 'play' in command:
        song = command.replace('play', '')
        print(name, ' : Playing'+song)
        say('Playing'+song)
        pywhatkit.playonyt(song)
        print(name, ' : Bye! ,Enjoy your music, If you need anything run me again')
        say('Bye! ,Enjoy your music, If you need anything run me again')
        return False

    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print(name, ' : current time is '+time)
        say('current time is '+time)
        return False
    elif 'bye' in command:
        print(name, ' : Bye! , See you soon')
        say('Bye..., See you soon , ')
        return False
    elif 'joke' in command:
        joke = pyjokes.get_joke()
        print(name, " : ", joke)
        say(joke)
        return False
    elif 'how are you' in command:
        print(name, ' : I am fine!, what about you')
        say('I am fine!, what about you')
        return False
    elif 'what is your name' in command:
        print(name, ' : My name is '+name)
        say('My name is '+name)
        return False
    elif 'who are you' in command:
        print(name, ' : I am '+name+", your persnol assistant.")
        say('I am '+name+", your persnol assistant.")
        return False

    elif 'open' in command:
        search = command.replace('open', '')
        webbrowser.open_new_tab('https://www.google.com/search?q='+search)
        print(name, ' : Opening in webbrowser')
        say('Opening in webbrowser')
        return False

    elif 'search on ai' in command:
        search = command.replace('search on ai', '')
        response = openai.Completion.create(
            # Use the 'text-davinci-002' engine for natural language processing
            engine="text-davinci-002",
            prompt=search,
            max_tokens=50,  # You can adjust the max tokens based on your preference
        )
        print(name, " : ", response.choices[0].text.strip())
        say(response.choices[0].text.strip())
        return False
    elif 'photos' in command:
        webbrowser.open_new_tab('https://www.google.com/search?q='+command)
        print(name, ' : Opening in webbrowser')
        say('Opening in webbrowser')
        return False

    elif "^" in command:
        print(name, " : Sorry, I didn't  get that , can you please repeat it")
        say("Sorry, I didn't  get that , can you please repeat it")
        # count -= 1
        # if count == 0:
        #     print(name, ' : Bye! , If you need anything run me again')
        #     say('Bye! , If you need anything run me again')
        #     return False

        return False

    else:
        webbrowser.open_new_tab('https://www.google.com/search?q='+command)
        print(name, ' : Opening in webbrowser')
        say('Opening in webbrowser')
        return False


while run_command():
    run_command()
