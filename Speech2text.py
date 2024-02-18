import speech_recognition as sr
import pyttsx3

# Initialize recognizer class (for recognizing the speech)
r = sr.Recognizer()

# Function to convert text to speech
def SpeakText(command):
    # Initialize the speech generation library
    engine = pyttsx3.init()
    # Making the machine speak the command
    engine.say(command)
    # Play the speech
    engine.runAndWait()

# Infinite loop to continuously recognize speech
while(1):    
    try:  
        # Use the microphone as source for input
        with sr.Microphone() as source2:
            # Wait for a second to let the recognizer adjust the energy threshold based on the surrounding noise level
            r.adjust_for_ambient_noise(source2, duration=0.2)
            # Listens for the user's input
            audio2 = r.listen(source2)
            # Using Google to recognize audio
            MyText = r.recognize_google(audio2)
            MyText = MyText.lower()
            print("Did you say ?",MyText)
            SpeakText(MyText)
    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))
    except sr.UnknownValueError:
        print("unknown error occurred")
