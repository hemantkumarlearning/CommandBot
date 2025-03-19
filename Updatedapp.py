import os
import speech_recognition as sr
import requests
import pyttsx3
import webbrowser


engine = pyttsx3.init()
engine.setProperty('rate', 150)


GROQ_API_KEY = 'YOUR-GROQ-API-KEY'

def ask_llm(prompt):
    url = 'https://api.groq.com/openai/v1/chat/completions'
    headers = {
        'Authorization':f'Bearer {GROQ_API_KEY}',
        'Content-Type': 'application/json'
    }

    data = {
        'model':'llama-3.3-70b-versatile',
        'messages':[{'role':'user','content':f'Convert this requests into a window system command give me the system command only without preamble (no backticks or special formatting):{prompt}'}],
        'temperature':0.5
    }

    response = requests.post(url,headers=headers,json=data)
    if response.status_code != 200:
        return f"Error: Unable to reach the API. Status code {response.status_code}. Response: {response.text}"
    result = response.json()

    return result['choices'][0]['message']['content'].strip()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        command = recognizer.recognize_google(audio).lower()
        print(f"You said: {command}")
        return command
    except sr.UnknownValueError:
        return None
    except sr.RequestError:
        return None

def execute_command(command):
    try:
        if command.startswith('http'):
            webbrowser.open(command)
            return f'Opened:{command}'
        
        elif "exit" in command or "shutdown" in command:
            speak("Shutting down assistant.")
            os._exit(0)

        os.system(command)
        return f'Executed:{command}'
        
    except Exception as e:
        return f'Error executing command:{e}'
    

speak("AI assistant is running.")

while True:
    user_input = listen()
    command = ask_llm(user_input)
    if command:
        execute_command(command)
