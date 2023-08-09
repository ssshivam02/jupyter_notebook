import pyttsx3

assistant = pyttsx3.init('sapi5')
voices = assistant.getProperty('voices')
print(voices)
assistant.setProperty('voices', voices[0].id)

def speak(audio):
    print("  ")
    assistant.say(audio)
    print("  ")
    assistant.runAndWait()
speak('hello shivam sonu help,hello')