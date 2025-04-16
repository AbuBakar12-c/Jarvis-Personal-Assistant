🧠 Jarvis Personal Assistant

Jarvis is a Python-based voice-activated desktop assistant that performs tasks like opening apps, searching the web, and retrieving information using natural speech. It integrates pyttsx3 for text-to-speech and speech_recognition for converting voice to commands. Designed for productivity and hands-free control, Jarvis offers a smart, interactive experience on your PC.

⚙️ How It Works
When you run the script, Jarvis greets you based on the time of day.

It uses your microphone to listen for commands, processes your speech with Google's speech recognition, and then responds using TTS (text-to-speech).

Based on your command, it executes specific tasks such as:

Opening applications (like Notepad or Camera)

Searching on Wikipedia or Google

Opening/closing websites like YouTube, Gmail, GitHub, or ChatGPT

Telling your IP address

Closing apps via system processes

Jarvis loops continuously, always ready for your next command until you say "no thanks" to exit.

🌟 Features
🎤 Voice-controlled using real-time speech recognition

🗣️ Text-to-Speech interaction for a natural experience

🧾 Wikipedia search and summaries

📹 Open/close Camera feed using OpenCV

🌐 Browser automation for Google, YouTube, Gmail, ChatGPT, GitHub

📄 Open/Close Notepad and other native apps

🌐 Get your public IP address instantly

🔄 Continuous listening loop with polite exit option

⚙️ Setup
Create a virtual environment
Open your terminal or command prompt and run:

python -m venv jarvis-env

Activate the virtual environment

jarvis-env\Scripts\activate

Install dependencies from requirements.txt

pip install -r requirements.txt
