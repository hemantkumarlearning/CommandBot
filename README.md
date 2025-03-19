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
git clone https://github.com/hemantkumarlearning/CommandBot.git
cd CommandBot
```

#### 2. Set Up a Virtual Environment

To ensure project dependencies don’t interfere with your system’s Python packages, it’s recommended to create and activate a virtual environment.

On Windows:
```
python -m venv venv
.\venv\Scripts\activate
```

#### 3. Install the required dependencies: 

This project requires Python 3.7+ and several Python packages.

```
pip install -r requirements.txt
```
#### 4. Setup the SpeechRecognition library:

Ensure you have a microphone connected and working.

#### 5. Groq LLaMA Model:

To use the Groq LLaMA model, you need a Groq API key. Follow these steps to set it up:

Obtain a Groq API Key: Go to the Groq website and sign up for an account if you haven't already. After signing in, navigate to the API section to generate an API key and You're  Good To Go.

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
