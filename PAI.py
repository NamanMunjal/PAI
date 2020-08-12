import pyttsx3      #sound library
import speech_recognition as sr     #speech recognition library
import wikipedia        #for wikipedia search
import tkinter as tk        #gui
from tkinter import mainloop
from tkinter import filedialog
import webbrowser       #opening web browser
import os
m=tk.Tk()       #GUI
m.geometry("500x500")
m.title("Proxima")
m.configure(background='#000000')
engine=pyttsx3.init('sapi5')        #sapi5 microsoft voice box
voices=engine.getProperty('voices')
#print(voices[0].id)
engine.setProperty('voice',voices[1].id)        #setting up voice
def speak(audio):       #audio function with sapi5
    engine.say(audio)
    engine.runAndWait()
speak("hello i am   ``proxima")
speak("I am your personal task manager")
class todoist:      #for special todo list
    def addtask(self):
        speak('tell the five precious tasks you want to accomplish today')
        self.i=input(speak("task 1"))       #task 1
        o=input(speak('if any, select the file you would need for this work. answer with yes or no'))
        if 'yes' in o:
            self.filefortask=filedialog.askopenfilename(initialdir='/',title='File needed for task',filetypes=(('executable','*.exe'),('all files','*.*')))
            print(self.filefortask+'is needed for the task')
        elif 'no' in o:
            speak('no worries lets move on to the next task')
        print(self.i)
        fil=open('todoist.txt','w')
        fil.write(self.i)
        self.a=input(speak("task 2"))       #task 2
        k=input(speak('if any, select the file you would need for this work. answer with yes or no'))
        if 'yes' in k:
            self.filefortask1=filedialog.askopenfilename(initialdir='/',title='File needed for task',filetypes=(('executable','*.exe'),('all files','*.*')))
            print(self.filefortask1+'is needed for the task')
        elif 'no' in k:
            speak('lets continue with the next task')
        print(self.a)
        fil.write(self.a)
        self.b=input(speak("task 3"))       #task 3
        l=input(speak('if any, select the file you would need for this work. answer with yes or no'))
        if 'yes' in l:
            self.filefortask2=filedialog.askopenfilename(initialdir='/',title='File needed for task',filetypes=(('executable','*.exe'),('all files','*.*')))
            print(self.filefortask2+'is needed for the task')
        elif 'no' in l:
            speak('here we go to the next task')
        print(self.b)
        fil.write(self.b)
        self.c=input(speak("task 4"))       #task 4
        p=input(speak('if any, select the file you would need for this work. answer with yes or no'))
        if 'yes' in p:
            self.filefortask3=filedialog.askopenfilename(initialdir='/',title='File needed for task',filetypes=(('executable','*.exe'),('all files','*.*')))
            print(self.filefortask3+'is needed for the task')
        elif 'no' in p:
            speak('no problem')
        print(self.c)
        fil.write(self.c)
        self.d=input(speak("task 5"))       #task 5
        q=input(speak('if any, select the file you would need for this work. answer with yes or no'))
        if 'yes' in q:
            self.filefortask4=filedialog.askopenfilename(initialdir='/',title='File needed for task',filetypes=(('executable','*.exe'),('all files','*.*')))
            print(self.filefortask4+'is needed for the task')
            speak('thats fine you reached the limit of tasks')
        elif 'no' in q:
            speak('thats fine you reached the limit of tasks')
        print(self.d)
        fil.write(self.d)
        fil.close()
    def readTodo(self):     #simply reads the todo
        speak(self.i)
        speak(self.a)
        speak(self.b)
        speak(self.c)
        speak(self.d)
    def openTfiles(self):       #opens file needed for the task
        task=input(speak('task to be accomplished'))
        if self.i in task:
            os.startfile(self.filefortask)
        elif self.a in task:
            os.startfile(self.filefortask1)
        elif self.b in task:
            os.startfile(self.filefortask2)
        elif self.c in task:
            os.startfile(self.filefortask3)
        elif self.d in task:
            os.startfile(self.filefortask4)
    def taskDone(self):     #deletes and asks for new task instead
        done=input(speak('great to know you accomplished a task may i know which one was it'))
        if self.i in done:
            q=input(speak('any new task'))
            if 'yes' in q:
                self.i=input(speak('move on tell the new task'))
            elif 'no' in q:
                speak('stay motivated')
        elif self.a in done:
            q=input(speak('any new task'))
            if 'yes' in q:
                self.a=input(speak('move on tell the new task'))
            elif 'no' in q:
                speak('stay motivated')
        elif self.b in done:
            q=input(speak('any new task'))
            if 'yes' in q:
                self.b=input(speak('move on tell the new task'))
            elif 'no' in q:
                speak('stay motivated')
        elif self.c in done:
            q=input(speak('any new task'))
            if 'yes' in q:
                self.c=input(speak('move on tell the new task'))
            elif 'no' in q:
                speak('stay motivated')
        elif self.d in done:
            q=input(speak('any new task'))
            if 'yes' in q:
                self.d=input(speak('move on tell the new task'))
            elif 'no' in q:
                speak('stay motivated')
t=todoist()
class functions:        #general functions of Proxima
    def addCommand1(self):      #for new commands
        speak('please enter the query,      and then the answer,       you want for the following query')
        self.a1=input('whats the query?')
        self.b1=input('answer')
        file=open('pai.txt','w')
        file.write(self.a1)
        file.write(self.b1)
        file.close()
    def ask(self):      #for asking PAI
        self.d=input(speak("how may i help you"))
        if self.d==self.a1:
            speak(self.b1)
    def wiki():
        query=input(speak('say the question or an action please'))
        if 'wikipedia' in query:
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        elif 'open web' in query:
            web=input(speak('website name with extension please'))
            webbrowser.open(web)
        elif 'search' in query:
            webbrowser.open('google.com')
        elif 'open file' in query:
            file=input(speak('please tell the file path'))
            os.startfile(file)
        elif 'play song' in query:
            n=input(speak('song name please'))
            webbrowser.open('youtube.com/'+n)
f=functions()
class files:        #file save open function
    def addFile(self):      #file system
        self.selectFile=filedialog.askopenfilename(initialdir='/',title='Select a file',filetypes=(('executables','*.exe'),('all files','*.*')))
        print(self.selectFile)
        self.selectFile1=filedialog.askopenfilename(initialdir='/',title='Select a file',filetypes=(('executables','*.exe'),('all files','*.*')))
        print(self.selectFile1)
        self.selectFile2=filedialog.askopenfilename(initialdir='/',title='Select a file',filetypes=(('executables','*.exe'),('all files','*.*')))
        print(self.selectFile2)
        self.selectFile3=filedialog.askopenfilename(initialdir='/',title='Select a file',filetypes=(('executables','*.exe'),('all files','*.*')))
        print(self.selectFile3)
        self.selectFile4=filedialog.askopenfilename(initialdir='/',title='Select a file',filetypes=(('executables','*.exe'),('all files','*.*')))
        print(self.selectFile4)
        fil=open('files.txt','w')
        fil.write(self.selectFile)
        fil.write(self.selectFile1)
        fil.write(self.selectFile2)
        fil.write(self.selectFile3)
        fil.write(self.selectFile4)
        fil.close()
    def createNewWindowForSelectAFile(self):
        self.w=tk.Toplevel(m)
        self.w.title('Files Selected')
        self.w.geometry('200x200')
        btn4=tk.Button(self.w,text='Select a file',bg='#5173ad',command=fi.addFile).pack()
        w.mainloop()
    def openFile(self):
        os.startfile(self.selectFile)
        os.startfile(self.selectFile1)
        os.startfile(self.selectFile2)
        os.startfile(self.selectFile3)
        os.startfile(self.selectFile4)
    def createWindowForNewCommand(self):
        self.n=tk.Toplevel(m)
        self.n.title('NewCommand')
        self.n.geometry('200x200')
        btn1=tk.Button(self.n,bg='#5173ad',command=f.addCommand1,text='NewCommand').pack()
        self.n.mainloop()
fi=files()
class routine:
    def takeFiles(self):
        self.fe1=filedialog.askopenfilename(initialdir='/',filetypes=(('executables','*.exe'),('all files','*.*')))
    def openFiles(self):
        os.startfile(self.fe1)
btn1=tk.Button(m,bg='#5173ad',command=fi.createWindowForNewCommand,text='NewCommand').pack()
btn2=tk.Button(m,bg='#5173ad',command=f.ask,text='Ask').pack()
btn3=tk.Button(m,text='open files/search wiki/open web',bg='#5173ad',command=functions.wiki).pack()
btn4=tk.Button(m,text='Select Files',bg="#5173ad",command=fi.createNewWindowForSelectAFile).pack()
btn5=tk.Button(m,text='Open files',bg='#5173ad',command=fi.openFile).pack()
btn6=tk.Button(m,text='TODO',bg='#5173ad',command=t.addtask).pack()
btn7=tk.Button(m,text="Read TODO",bg='#5173ad',command=t.readTodo).pack()
btn8=tk.Button(m,text="Task files",bg='#5173ad',command=t.openTfiles).pack()
btn9=tk.Button(m,text="Task done",bg='#5173ad',command=t.taskDone).pack()
m.mainloop()

