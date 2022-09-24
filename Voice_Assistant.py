import datetime
import wikipedia
import webbrowser
from mal import Anime
import os
import random
from friday import Friday

Friday = Friday()
chrome = webbrowser.Chrome(r"C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe")
random_number = random.randint(1, 1000)

if __name__ == "__main__":
    Friday.wish_me()

    #   logic for executing tasks based on query
    while True:

        query = Friday.take_command().lower()

        if 'friday' in query:

            if 'wikipedia' in query:
                Friday.speak("Searching Wikipedia...")
                query = query.replace('wikipedia', '')
                results = wikipedia.summary(query, sentences=3)
                Friday.speak("According to wikipedia ")
                print(results)
                Friday.speak(results)

            elif 'open youtube' in query:
                chrome.open('youtube.com')

            elif 'open google' in query:
                chrome.open('google.com')

            elif 'open stackoverflow' in query:
                chrome.open('stackoverflow.com')

            elif 'play music' in query:
                Friday.speak("Playing music on the device")
                music_dir = 'C:\\Users\\ny111\\Music'
                songs = os.listdir(music_dir)
                len_of_dir = len(songs)
                random_number = random.randint(0, len_of_dir - 1)
                os.startfile(os.path.join(music_dir, songs[random_number]))

            elif 'make file' in query:
                Friday.make_file()

            elif 'music on youtube' in query:
                Friday.speak("Opening playlist on youtube")
                chrome.open('https://www.youtube.com/watch?v=0arvEmH88rU&list=PLsbNCMBZYYIQ-L-mmFN6s_0BkfBlVwN8m')

            elif 'the time' in query:
                str_time = datetime.datetime.now().strftime('%H:%M:%S')
                print(str_time)
                Friday.speak(f"master the time is {str_time}")

            elif 'open code' in query:
                Friday.speak("opening code")
                code_path = "C:\\Users\\ny111\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
                os.startfile(code_path)

            elif 'anime' in query:
                try:
                    anime = Anime(random_number)
                    Friday.speak(anime.title)
                    Friday.speak(anime.genres)
                    Friday.speak(anime.score)
                    print(f"{anime.title}, {anime.genres}, {anime.score}")

                except Exception as ex:
                    # print()
                    Friday.speak("Wait a minute")

            elif 'quit' in query:
                Friday.speak("Shutting down master")
                exit()
