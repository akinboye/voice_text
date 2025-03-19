# pip install SpeechRecognition
# pip install pyttsx3
# pip install pyaudio
import speech_recognition as sr
import pyttsx3

# Initialize the recognizer
recognizer = sr.Recognizer()

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Function to convert voice to text
def voice_to_text():
    # Use the microphone as the audio source
    with sr.Microphone() as source:
        print("Please say something...")
        
        # Adjust recognizer sensitivity to ambient noise
        recognizer.adjust_for_ambient_noise(source)
        
        # Listen for the first phrase
        audio = recognizer.listen(source)
        
        try:
            # Recognize the speech using Google's speech recognition
            print("Recognizing...")
            text = recognizer.recognize_google(audio)
            print("You said: " + text)
            
            # Convert text to speech
            text_to_speech(text)
        
        except sr.UnknownValueError:
            print("Sorry, I could not understand the audio.")
        except sr.RequestError:
            print("Could not request results from Google Speech Recognition service.")

# Function to convert text to speech
def text_to_speech(text):
    print("Converting text to speech...")
    engine.say(text)
    engine.runAndWait()

# Run the voice-to-text function
if __name__ == "__main__":
    #text_to_speech("testing something")
    voice_to_text()
