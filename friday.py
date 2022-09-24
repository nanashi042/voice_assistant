import pyttsx3
import datetime
import speech_recognition as sr


class Friday:

    def __init__(self):
        self.engine = pyttsx3.init('sapi5')
        self.voices = self.engine.getProperty("voices")
        # print(voices)
        self.engine.setProperty('voice', self.voices[1].id)

    def speak(self, audio):
        """Helps is speaking """
        self.engine.say(audio)
        self.engine.runAndWait()

    def wish_me(self):
        """wishes the user"""
        hour = int(datetime.datetime.now().hour)
        if 0 <= hour < 12:
            self.speak("Good Morning")
        elif 12 <= hour < 18:
            self.speak("Good Afternoon")
        else:
            self.speak("Good Evening")

        self.speak("Friday is here to help you in anything")

    @staticmethod
    def make_file():
        """creates a file """
        f = open("myfile.txt", "x")
        f.write("This is the file created")
        f.close()

    @staticmethod
    def take_command():
        """It will take  microphone user from input and returns string output"""
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening...")
            r.pause_threshold = 1
            # r.energy_threshold =
            audio = r.listen(source)

        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language='en-in')
            print(f"user said : {query}\n")

        except Exception as e:
            print(e)
            print("say that again")
            return "None"

        return query
