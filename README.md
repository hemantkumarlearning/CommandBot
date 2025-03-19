# AI Voice Assistant for System Commands

This project is an AI-powered voice assistant that allows users to issue system commands using voice input. The assistant leverages SpeechRecognition for capturing voice commands and Groq LLaMA model for converting voice commands into corresponding Windows system commands. These commands are then executed using Python’s os module or webbrowser module.

## Features

- Voice Command Input: The assistant listens to user commands via microphone input.
  
- Groq LLaMA Model: Converts user voice commands into system commands using natural language processing (NLP).
  
- Command Execution: Executes the system commands on a Windows environment using Python’s os and webbrowser modules.
  
- Multi-functionality: Capable of performing a variety of tasks like opening programs, browsing websites, and running system commands.
  
## Installation

#### 1. Clone the repository:

```
git clone https://github.com/yourusername/ai-voice-assistant.git
cd ai-voice-assistant
```
#### 2. Install the required dependencies: 

This project requires Python 3.7+ and several Python packages.

```
pip install -r requirements.txt
```
#### 3. Setup the SpeechRecognition library:

Ensure you have a microphone connected and working.

#### 4. Groq LLaMA Model:

Follow any setup instructions for the Groq LLaMA model or ensure it’s integrated with the project. You may need to install the model using specific tools or APIs.

## Usage

#### 1. Run the Assistant: To start the assistant, simply run the Updatedapp.py file:

```
python Updatedapp.py
```
#### 2. Provide a Voice Command:

Once the assistant is running, you can speak any of the following types of commands:

- "Open Google Chrome"
  
- "Launch Notepad"
  
- "Open my Python project"
  
- "Go to https://example.com"
  
- The assistant will convert your voice input into a system command and execute it.


## Acknowledgments

- SpeechRecognition: For enabling speech-to-text functionality.
- Groq LLaMA Model: For providing the natural language processing capabilities.
- Python: For being the programming language used to develop this assistant.
