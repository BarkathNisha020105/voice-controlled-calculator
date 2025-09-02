import speech_recognition as sr
import pyttsx3

# Initialize recognizer and text-to-speech engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    """Convert text to speech"""
    engine.say(text)
    engine.runAndWait()

def listen():
    """Listen to microphone and recognize speech"""
    with sr.Microphone() as source:
        print("🎙️ Listening...")
        audio = recognizer.listen(source)
        try:
            command = recognizer.recognize_google(audio)
            print(f"👉 You said: {command}")
            return command.lower()
        except sr.UnknownValueError:
            speak("Sorry, I didn't understand that.")
            return None
        except sr.RequestError:
            speak("Sorry, speech service is unavailable.")
            return None

def calculate(expression):
    """Evaluate a math expression safely"""
    try:
        result = eval(expression)
        return result
    except Exception as e:
        return f"Error: {e}"

# Main loop
speak("Welcome to Voice Calculator. Say your calculation.")
while True:
    command = listen()
    if command:
        if "exit" in command or "quit" in command:
            speak("Goodbye!")
            break
        else:
            result = calculate(command)
            print("🧮 Result:", result)
            speak(f"The result is {result}")
