#---------------------------------ZEUS - ASSITANT---------------------------------
'''NECESSARY MODULES PLEASE INSTALL THEM USING (pip install module_name)'''

import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install SpeechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import random
import time
from playsound import playsound #pip install playsound
import PIL.Image #pip install Pillow
import ctypes
from tkinter import *
from art import* #pip install art
import pywhatkit as kit #pip install pywhatkit
import subprocess

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[0].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def zeus():
    tprint('ZEUS',font='block')
    playsound('C:\\Users\\divya\\OneDrive\\Desktop\\CLG\\191270\\Project\\ZEUS\\sound\\zeus-1.wav')
    time.sleep(0.2)
    playsound('C:\\Users\\divya\\OneDrive\\Desktop\\CLG\\191270\\Project\\ZEUS\\sound\\lightning_sms.mp3')
    #set current wallpaper to zeus
    ctypes.windll.user32.SystemParametersInfoW(20, 0, "C:\\Users\\divya\\OneDrive\\Desktop\\CLG\\191270\\Project\\ZEUS\\pictures\\zeus.png" , 0)
    time.sleep(0.3)
    playsound('C:\\Users\\divya\\OneDrive\\Desktop\\CLG\\191270\\Project\\ZEUS\\sound\\zeus_wrath_divine.mp3')
    time.sleep(0.3)
def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("   Morning!")

    elif hour>=12 and hour<14:
        speak("   Afternoon!")   

    elif hour>=14 and hour<20:
        speak("   Evening!")
    else:
        speak("   Night!")
    speak("Mortal human. I am Zeus . I am the god of sky and thunder in ancient Greek religion.   Now what do u want from me?")       

def take_command():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        playsound('C:\\Users\\divya\\OneDrive\\Desktop\\CLG\\191270\\Project\\ZEUS\\sound\\google_now_voice.mp3')
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"You said: {query}\n")

    except Exception:
        speak("You are wasting my time...")
        print("Say that again please...")  
        return "None"
    except sr.RequestError:
            speak('the service is down')
    return query

if __name__ == "__main__":
    zeus()
    time.sleep(1)
    wishme()
    while True:
        query = take_command().lower()

        #1:WIKIPEDIA
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
            
        #2:YOUTUBE
        elif 'open youtube' in query:
            url = f"https://www.youtube.com"
            speak("Opening Youtube!")
            webbrowser.open(url)
        elif 'youtube' in query:
            speak('Searching Youtube...')
            query = query.replace("youtube", "")
            url = f"https://www.youtube.com/results?search_query={query}"
            webbrowser.get().open(url)
            speak(f'Here is what I found for {query} on youtube')

        #3:GOOGLE
        elif 'open google' in query:
            url = f"https://google.com/search?q="
            speak("Opening Google!")
            webbrowser.open(url)
        elif 'google' in query:
            speak('Searching Google...')
            query = query.replace("google", "")
            url = f"https://google.com/search?q={query}"
            webbrowser.get().open(url)
            speak(f'Here is what I found for {query} on google')

        #4:TIME TABLE
        elif 'time table' in query:
            im = PIL.Image.open(r"C:\Users\divya\OneDrive\Desktop\CLG\191270\Project\ZEUS\pictures\timetable_sem_3.jpg")
            im.show()
            playsound('C:\\Users\\divya\\OneDrive\\Desktop\\CLG\\191270\\Project\\ZEUS\\sound\\zeus-2.wav')

        #5:STUDY
        elif 'study' in query:
            url="https://classroom.google.com/u/1/h"
            webbrowser.get().open(url)

        #6:STACK OVERFLOW
        elif 'open stack overflow' in query:
            url = f"https://stackoverflow.com"
            webbrowser.get().open(url)
            
        #7:DATA CAMP   
        elif 'open data camp' in query:
            url=f"https://learn.datacamp.com/#"
            webbrowser.get().open(url)

        #8:HACKERANK
        elif 'open hackerrank' in query:
            url=f"https://https://hackerrank.com/dashboard"
            webbrowser.get().open(url)
            
        #9:MUSIC
        elif 'music' in query:
            music_dir = 'F:\\Divyansh'
            songs = os.listdir(music_dir)
            n= random.randint(1,60)
            os.startfile(os.path.join(music_dir, songs[n]))

       
        #10:TIME
        elif 'tell me the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"the time is {strTime}")
            print(f"the time is {strTime}")
            playsound('C:\\Users\\divya\\OneDrive\\Desktop\\CLG\\191270\\Project\\ZEUS\\sound\\zeus-2.wav')

        #11:CODE
        elif 'open code' in query:
            codePath = "C:\\Users\\divya\\OneDrive\\Desktop\\CLG\\191270\\sem3"
            os.startfile(codePath)

        #12:MAIL
        elif 'email' in query:
            speak('Opening Mail...')
            url = f"https://www.gmail.com/"
            webbrowser.get().open(url)

        #13:ROCK PAPER SCISSORS
        elif 'game' in query:
            root = Tk()
            root.configure(bg="#000000")
            root.geometry('+0+0')
            root.iconbitmap("C:\\Users\\divya\\OneDrive\\Desktop\\CLG\\191270\\Project\\ZEUS\\pictures\\rps.ico")
            root.title("Rock-Paper-Scissor")
            root.resizable(width=False,height=False)

            #SOUND
            roar = 'C:\\Users\\divya\\OneDrive\\Desktop\\CLG\\191270\\Project\\ZEUS\\sound\\roar.mp3'
            laugh ='C:\\Users\\divya\\OneDrive\\Desktop\\CLG\\191270\\Project\\ZEUS\\sound\\laugh.mp3'

            #IMAGES
            rock= PhotoImage(file="C:\\Users\\divya\\OneDrive\\Desktop\\CLG\\191270\\Project\\ZEUS\\pictures\\Rock.png")
            paper= PhotoImage(file="C:\\Users\\divya\\OneDrive\\Desktop\\CLG\\191270\\Project\\ZEUS\\pictures\\Paper.png")
            scissor= PhotoImage(file="C:\\Users\\divya\\OneDrive\\Desktop\\CLG\\191270\\Project\\ZEUS\\pictures\\Scissor.png")
            win= PhotoImage(file="C:\\Users\\divya\\OneDrive\\Desktop\\CLG\\191270\\Project\\ZEUS\\pictures\\WIN.png")
            lose = PhotoImage(file="C:\\Users\\divya\\OneDrive\\Desktop\\CLG\\191270\\Project\\ZEUS\\pictures\\LOST.png")
            tie= PhotoImage(file="C:\\Users\\divya\\OneDrive\\Desktop\\CLG\\191270\\Project\\ZEUS\\pictures\\DRAW.png")
            startgame = PhotoImage(file="C:\\Users\\divya\\OneDrive\\Desktop\\CLG\\191270\\Project\\ZEUS\\pictures\\game.png")

            rockHandButton = " "
            paperHandButton = " "
            scissorHandButton = " "
            resultButton = Button(root,image=startgame)

            click = True

            def play():
                global rockHandButton,paperHandButton,scissorHandButton    
                #Set images and commands for buttons :
                rockHandButton = Button(root,image = rock, command=lambda:you_pick("Rock"))
                paperHandButton = Button(root,image = paper, command=lambda:you_pick("Paper"))
                scissorHandButton = Button(root,image = scissor, command=lambda:you_pick("Scissor"))
   
    
                #Place the buttons on window :
                rockHandButton.grid(row=0,column=0)
                paperHandButton.grid(row=0,column=1)
                scissorHandButton.grid(row=0,column=2)
    
                #Add space :
                root.grid_rowconfigure(1, minsize=50) 
    
                #Place result button on window : 
                resultButton.grid(row=2,column=0,columnspan=5)
   
            def computerPick():
                choice = random.choice(["Rock","Paper","Scissor"])
                return choice
            speak("choose among rock paper or scissor")
            def you_pick(yourChoice):
                global click
    
                compPick = computerPick()
                if click==True:
                    if yourChoice == "Rock":
                        rockHandButton.configure(image=rock)
            
                        if compPick == "Rock":
                            paperHandButton.configure(image=rock)
                            resultButton.configure(image=tie)
                            scissorHandButton.grid_forget()
                            click = False
                            speak(" i will see you next time")
            
                        elif compPick == "Paper":
                            paperHandButton.configure(image=paper)
                            scissorHandButton.grid_forget()
                            resultButton.configure(image=lose)
                            click = False
                            speak("  you lowly human,you dare to defeat me")
                            playsound(laugh)
            
                        else:
                            paperHandButton.configure(image=scissor)
                            scissorHandButton.grid_forget()
                            resultButton.configure(image=win)
                            click = False
                            speak("I lost")
                            playsound(roar)
                
                
                    elif yourChoice == "Paper":
                        rockHandButton.configure(image=paper)
            
                        if compPick == "Rock":
                            paperHandButton.configure(image=rock)
                            resultButton.configure(image=win)
                            scissorHandButton.grid_forget()
                            click = False
                            speak("I lost")
                            playsound(roar)
        
                        elif compPick == "Paper":
                            paperHandButton.configure(image=paper)
                            resultButton.configure(image=tie)
                            scissorHandButton.grid_forget()
                            click = False
                            speak(" i will see you next time")
            
                        else:
                            paperHandButton.configure(image=scissor)
                            resultButton.configure(image=lose)
                            scissorHandButton.grid_forget()
                            click = False
                            speak("  you lowly human,you dare to defeat me")
                            playsound(laugh)

                    elif yourChoice=="Scissor":
                        rockHandButton.configure(image=scissor)

                        if compPick == "Rock":
                            paperHandButton.configure(image=rock)
                            resultButton.configure(image=lose)
                            scissorHandButton.grid_forget()
                            click = False
                            speak("  you lowly human,you dare to defeat me")
                            playsound(laugh)
            
                        elif compPick == "Paper":
                            paperHandButton.configure(image=paper)
                            resultButton.configure(image=win)
                            scissorHandButton.grid_forget()
                            click = False
                            speak("I lost")
                            playsound(roar)

                        else:
                            paperHandButton.configure(image=scissor)
                            resultButton.configure(image=tie)
                            scissorHandButton.grid_forget()
                            click = False
                            speak(" i will see you next time")               
                else:
                    #To reset the game :
                    if yourChoice=="Rock" or yourChoice=="Paper" or yourChoice=="Scissor" or yourChoice=="Lizard" or yourChoice=="Spock":
                        rockHandButton.configure(image=rock)
                        paperHandButton.configure(image=paper)
                        scissorHandButton.configure(image=scissor)
                        resultButton.configure(image=startgame)
                        
                        #Get back the deleted buttons
                        scissorHandButton.grid(row=0,column=2)
                        click=True



            play()
            root.mainloop()
        #14.TOSS A COIN
        elif 'coin' in query:
            moves=["head", "tails"]   

            cmove=random.choice(moves)
            speak("I chose " + cmove)
            
        #15.WHATSAPP
        elif 'open whatsapp'in query:
            subprocess.Popen('C:\\Users\\divya\\AppData\\Local\\WhatsApp\\WhatsApp.exe')

        elif 'whatsapp'in query:
            speak("Whom do you want to disturb?")
            phone_no = input()
            speak("What message?")
            message = str(input())
            kit.sendwhatmsg(phone_no,message,int(datetime.datetime.now().hour),int(datetime.datetime.now().minute+2))
            
        #16:SOME FACTS
        elif 'tell me about yourself'in query:
            facts = {
            'Fact1' : 'I became the ruler of heaven and earth after a revolt against my father, Kronos. In his position as king of the gods, I had to play mediator when other the immortals were mad at each other.',
            'Fact2' : 'I am the father of Athena, who is said to have sprung from her head. She was my favorite child, with whom I shared the thunderbolt and aegis.',
            'Fact3' : 'I was raised by Gaia, Adamanthea, and a goat named Amalthea after my mother saved his life and sent him away to protect him.',
            'Fact4' : 'My siblings are Hades, Poseidon, Demeter, Hera and Hestia.',
            'Fact5' : 'I am able to shape shift, which means I am able to transform myself to look like an animal or another person.',
            'Fact6' : 'I have twin children named Apollo and Artemis with Leto.',
            'Fact7' : 'I, more recently known for causing thunder and lightning, was once a rain-god. I am always associated with the weather in some form.',
            'Fact8' : 'I let the other Gods lend aid to their respective sides in the war',
            'Fact9' : 'I am considered the youngest as well as eldest in my siblings ',
            'Fact10' : 'I am a Greek god and could not die because I am immortal.'}
            val = random.choice(list(facts.values()))
            print(val)
            speak(val)
            
            
        #17:EXIT
        elif 'go away' in query:
            playsound('C:\\Users\\divya\\OneDrive\\Desktop\\CLG\\191270\\Project\\ZEUS\\sound\\zeus-3.wav')
            playsound('C:\\Users\\divya\\OneDrive\\Desktop\\CLG\\191270\\Project\\ZEUS\\sound\\lightning_sms.mp3')
            time.sleep(1)
            print(
            '''
            ´´´´´´´´´´´´´´´´´´´ ¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶´´´´´´´´´´´´´´´´´´´`
            ´´´´´´´´´´´´´´´´´¶¶¶¶¶¶´´´´´´´´´´´´´¶¶¶¶¶¶¶´´´´´´´´´´´´´´´´
            ´´´´´´´´´´´´´´¶¶¶¶´´´´´´´´´´´´´´´´´´´´´´´¶¶¶¶´´´´´´´´´´´´´´
            ´´´´´´´´´´´´´¶¶¶´´´´´´´´´´´´´´´´´´´´´´´´´´´´´¶¶´´´´´´´´´´´´
            ´´´´´´´´´´´´¶¶´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´¶¶´´´´´´´´´´´
            ´´´´´´´´´´´¶¶´´´´´´´´´´´´´´´´´´´´´`´´´´´´´´´´´¶¶´´´´´´´´´´`
            ´´´´´´´´´´¶¶´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´¶¶´´´´´´´´´´
            ´´´´´´´´´´¶¶´¶¶´´´´´´´´´´´´´´´´´´´´´´´´´´´´´¶¶´¶¶´´´´´´´´´´
            ´´´´´´´´´´¶¶´¶¶´´´´´´´´´´´´´´´´´´´´´´´´´´´´´¶¶´´¶´´´´´´´´´´
            ´´´´´´´´´´¶¶´¶¶´´´´´´´´´´´´´´´´´´´´´´´´´´´´´¶¶´´¶´´´´´´´´´´
            ´´´´´´´´´´¶¶´´¶¶´´´´´´´´´´´´´´´´´´´´´´´´´´´´¶¶´¶¶´´´´´´´´´´
            ´´´´´´´´´´¶¶´´¶¶´´´´´´´´´´´´´´´´´´´´´´´´´´´¶¶´´¶¶´´´´´´´´´´
            ´´´´´´´´´´´¶¶´¶¶´´´¶¶¶¶¶¶¶¶´´´´´¶¶¶¶¶¶¶¶´´´¶¶´¶¶´´´´´´´´´´´
            ´´´´´´´´´´´´¶¶¶¶´¶¶¶¶¶¶¶¶¶¶´´´´´¶¶¶¶¶¶¶¶¶¶´¶¶¶¶¶´´´´´´´´´´´
            ´´´´´´´´´´´´´¶¶¶´¶¶¶¶¶¶¶¶¶¶´´´´´¶¶¶¶¶¶¶¶¶¶´¶¶¶´´´´´´´´´´´´´
            ´´´´¶¶¶´´´´´´´¶¶´´¶¶¶¶¶¶¶¶´´´´´´´¶¶¶¶¶¶¶¶¶´´¶¶´´´´´´¶¶¶¶´´´
            ´´´¶¶¶¶¶´´´´´¶¶´´´¶¶¶¶¶¶¶´´´¶¶¶´´´¶¶¶¶¶¶¶´´´¶¶´´´´´¶¶¶¶¶¶´´
            ´´¶¶´´´¶¶´´´´¶¶´´´´´¶¶¶´´´´¶¶¶¶¶´´´´¶¶¶´´´´´¶¶´´´´¶¶´´´¶¶´´
            ´¶¶¶´´´´¶¶¶¶´´¶¶´´´´´´´´´´¶¶¶¶¶¶¶´´´´´´´´´´¶¶´´¶¶¶¶´´´´¶¶¶´
            ¶¶´´´´´´´´´¶¶¶¶¶¶¶¶´´´´´´´¶¶¶¶¶¶¶´´´´´´´¶¶¶¶¶¶¶¶¶´´´´´´´´¶¶
            ¶¶¶¶¶¶¶¶¶´´´´´¶¶¶¶¶¶¶¶´´´´¶¶¶¶¶¶¶´´´´¶¶¶¶¶¶¶¶´´´´´´¶¶¶¶¶¶¶¶
            ´´¶¶¶¶´¶¶¶¶¶´´´´´´¶¶¶¶¶´´´´´´´´´´´´´´¶¶¶´¶¶´´´´´¶¶¶¶¶¶´¶¶¶´
            ´´´´´´´´´´¶¶¶¶¶¶´´¶¶¶´´¶¶´´´´´´´´´´´¶¶´´¶¶¶´´¶¶¶¶¶¶´´´´´´´´
            ´´´´´´´´´´´´´´¶¶¶¶¶¶´¶¶´¶¶¶¶¶¶¶¶¶¶¶´¶¶´¶¶¶¶¶¶´´´´´´´´´´´´´´
            ´´´´´´´´´´´´´´´´´´¶¶´¶¶´¶´¶´¶´¶´¶´¶´¶´¶´¶¶´´´´´´´´´´´´´´´´´
            ´´´´´´´´´´´´´´´´¶¶¶¶´´¶´¶´¶´¶´¶´¶´¶´¶´´´¶¶¶¶¶´´´´´´´´´´´´´´
            ´´´´´´´´´´´´¶¶¶¶¶´¶¶´´´¶¶¶¶¶¶¶¶¶¶¶¶¶´´´¶¶´¶¶¶¶¶´´´´´´´´´´´´
            ´´´´¶¶¶¶¶¶¶¶¶¶´´´´´¶¶´´´´´´´´´´´´´´´´´¶¶´´´´´´¶¶¶¶¶¶¶¶¶´´´´
            ´´´¶¶´´´´´´´´´´´¶¶¶¶¶¶¶´´´´´´´´´´´´´¶¶¶¶¶¶¶¶´´´´´´´´´´¶¶´´´
            ´´´´¶¶¶´´´´´¶¶¶¶¶´´´´´¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶´´´´´¶¶¶¶¶´´´´´¶¶¶´´´´
            ´´´´´´¶¶´´´¶¶¶´´´´´´´´´´´¶¶¶¶¶¶¶¶¶´´´´´´´´´´´¶¶¶´´´¶¶´´´´´´
            ´´´´´´¶¶´´¶¶´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´¶¶´´¶¶´´´´´´
            ´´´´´´´¶¶¶¶´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´¶¶¶¶´´´´´´´
            ''')
            speak("I am the GOD , I do not obey anyone")
            exit()
