# Nexus Voice Assistant

A Python-based voice assistant that listens for wake words and executes voice commands. Nexus can open web applications, play music/videos, send WhatsApp messages, fetch news, and answer questions using OpenAI's GPT.

## Stack

- **Language:** Python 3
- **Core Libraries:**
  - `speech_recognition` — speech-to-text via Google Speech Recognition API
  - `pyttsx3` — text-to-speech synthesis
  - `openai` — integration with GPT for intelligent responses
  - `pywhatkit` — WhatsApp messaging automation
  - `requests` — HTTP requests for news API

## How it's organized

Nexus_voice_assistant/ ├── main.py Main voice assistant loop - wake word detection and command processing ├── client.py OpenAI API client test script ├── musicLibrary.py Dictionary of song names and YouTube links ├── videos.py Dictionary of video names and YouTube links ├── voice_test.py Test script to verify text-to-speech functionality ├── contacts.py (gitignored) Contact mappings for WhatsApp messages ├── .env (gitignored) Environment variables with API keys └── .gitignore Excludes sensitive files

**How it fits together:**

The assistant runs a continuous loop that listens for the wake word "nexus" using Google Speech Recognition. Once activated, it captures a voice command and routes it to `processCommand()`. Commands can open websites (Google, Facebook, YouTube, Instagram, WhatsApp), play music/videos from the configured libraries, send WhatsApp messages to saved contacts, fetch news headlines, or be forwarded to OpenAI's GPT for intelligent responses. Text responses are spoken aloud via `pyttsx3`.

## How to run it

### Prerequisites

Install dependencies:

```bash
pip install speech_recognition pyttsx3 openai pywhatkit requests gtts
```
>> Configuration
1. Create a contacts file (contacts.py):
```python
contacts = {
    "alice": "+1234567890",
    "bob": "+0987654321"
}
```

2. Set up environment variables (.env):
```
OPENAI_API_KEY=your-openai-api-key
NEWS_API_KEY=your-newsapi-key
```

3. Update API keys in code (for now, they're hardcoded in main.py):

 Replace the OpenAI API key placeholder at line 27
 Replace the News API key placeholder at line 108

4. Customize music and videos:

Edit musicLibrary.py to add your favorite songs
Edit videos.py to add your favorite videos

### Run the assistant
```bash
python main.py
```
The assistant will initialize and begin listening for the wake word "nexus". Speak "nexus" followed by your command:

Open applications: "nexus, open google" / "nexus, open youtube"
Play media: "nexus, play hayat" / "nexus, play leo"
Send messages: "nexus, send message" (will prompt for contact and message)
Get news: "nexus, news"
General Q&A: "nexus, what is recursion?" (uses GPT)

> Test text-to-speech
```bash
python voice_test.py
````
Try asking
How do I add more songs to the music library and have Nexus play them?
Can I use a different speech-to-text engine instead of Google's API?
How should I securely manage the OpenAI and News API keys without hardcoding them?
</hr>
Note: This is a personal project in early stages. There are several areas for improvement, including proper environment variable handling, error recovery, and support for additional voice commands.

```
This README provides a complete overview with setup instructions, configuration details, and practical examples. It's ready to paste into the repository!
```
