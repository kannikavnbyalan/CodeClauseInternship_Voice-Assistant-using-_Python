
import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia

listener = sr.Recognizer()
engine = pyttsx3.init()

def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    try:
        with sr.Microphone() as source:
            print("Listening...")
            voice = listener.listen(source)
            command = listener.recognize_google(voice).lower()
            if 'jarvis' in command:
                command = command.replace('jarvis', '')
                print(command)
    except sr.UnknownValueError:
        command = "Could not understand audio. Please repeat."
    except sr.RequestError as e:
        command = f"Error with the request: {e}"
    return command

def run_jarvis():
    command = take_command()
    print(command)

    if 'play' in command:
        song = command.replace('play', '')
        talk(f"Playing {song}")
        pywhatkit.playonyt(song)

    elif 'time' in command:
        current_time = datetime.datetime.now().strftime('%I:%M %p')
        talk(f"The current time is {current_time}")

    elif 'date' in command:
        current_date = datetime.datetime.now().strftime('%d/%m/%Y')
        talk(f"Today's date is {current_date}")

    elif 'how are you' in command:
        talk('I am fine, thank you. How about you?')

    elif 'what is your name' in command:
        talk('I am Jarvis. What can I do for you?')

    elif 'who is' in command:
        person = command.replace('who is', '')
        info = wikipedia.summary(person, 1)
        talk(info)

    else:
        talk("Sorry, I didn't understand that. Can you please repeat?")

if __name__ == "__main__":
    run_jarvis()
