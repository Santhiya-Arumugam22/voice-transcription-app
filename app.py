from flask import Flask, render_template, request, jsonify
import os
from datetime import datetime
import speech_recognition as sr
from pydub import AudioSegment

app = Flask(__name__)
TRANSCRIPTS_DIR = "transcripts"
if not os.path.exists(TRANSCRIPTS_DIR):
    os.makedirs(TRANSCRIPTS_DIR)

@app.route("/")
def home():
    return render_template("voice_to_text.html")

@app.route("/voice-to-text")
def voice_to_text():
    return render_template("voice_to_text.html")

@app.route("/text-to-voice")
def text_to_voice():
    return render_template("text_to_voice.html")

@app.route("/save", methods=["POST"])
def save_transcript():
    data = request.get_json()
    text = data.get("transcript", "").strip()
    if not text:
        return jsonify({"status": "error", "message": "No transcript provided"})
    filename = f"transcript_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
    filepath = os.path.join(TRANSCRIPTS_DIR, filename)
    try:
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(text)
        return jsonify({"status": "success", "filename": filename})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)})

@app.route("/upload-audio", methods=["POST"])
def upload_audio():
    if 'audio' not in request.files:
        return jsonify({"status": "error", "message": "No file uploaded"})
    file = request.files['audio']
    if file.filename == "":
        return jsonify({"status": "error", "message": "Empty filename"})
    filepath = os.path.join(TRANSCRIPTS_DIR, file.filename)
    try:
        file.save(filepath)
        audio = AudioSegment.from_file(filepath)
        wav_path = filepath + ".wav"
        audio.export(wav_path, format="wav")
        recognizer = sr.Recognizer()
        with sr.AudioFile(wav_path) as source:
            audio_data = recognizer.record(source)
        transcript_text = recognizer.recognize_google(audio_data, language="en-IN")
        return jsonify({"status": "success", "transcript": transcript_text})
    except sr.UnknownValueError:
        return jsonify({"status": "error", "message": "Could not understand audio"})
    except sr.RequestError as e:
        return jsonify({"status": "error", "message": f"API error: {e}"})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)})

if __name__ == "__main__":
    app.run(debug=True)
