
## Voice/Text Transcription App 

This is a simple and powerful web app built with **Flask** that helps you **convert speech to text** and **text to speech** — all right in your browser.

✨ It’s designed to make it easy for anyone to:
- **Speak and see the text appear live on screen**
- **Upload audio files and get the transcription**
- **Type or upload text, and have your computer read it aloud**
- **Save your transcripts for later**
- **Switch between light and dark mode for comfort**
- **Track word counts as you go**



## 🚀 What can it do?

✅ **Real-time speech-to-text** — Speak into your mic and watch it transcribe live  
✅ **Audio file transcription** — Upload audio (like MP3, WAV) and get text back  
✅ **Text-to-speech** — Type something (or upload a document) and the app will read it out loud  
✅ **File upload support** — Works with audio files, PDFs, Word docs  
✅ **Save your transcripts** — Download your text as a file  
✅ **Dark mode** — Switch between light and dark themes to suit your eyes  
✅ **Live word count** — See how many words you’ve transcribed  



## 🛠 Requirements

- Python 3.7+
- `Flask`
- `SpeechRecognition`
- `pydub` (requires ffmpeg installed on your system)
- `mammoth`
- `pdfminer.six`

![voice_to_text](https://github.com/user-attachments/assets/83a1f545-c200-4bd2-9f7b-750eee766636)
![text_to_voice](https://github.com/user-attachments/assets/78c74bc5-47c2-4a76-8d66-fb22960e4150)


## ⚡ How to run

```bash
# Clone the repo (or download the code)
git clone <your-repo-url>
cd <your-project-folder>

# (Optional) Create virtual environment
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the app
python app.py
