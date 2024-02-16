import speech_recognition as sr

def audio_to_text(language='en-US'):
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Speak something...")
        audio_data = recognizer.listen(source)
    try:
        text = recognizer.recognize_google(audio_data, language=language)
        return text
    except sr.UnknownValueError:
        return "Could not understand audio"
    except sr.RequestError as e:
        return f"Error: {str(e)}"

if __name__ == "__main__":
    language = input("Enter the language code (e.g., en-US for English, fr-FR for French): ")
    text = audio_to_text(language)
    print("Text:", text)
