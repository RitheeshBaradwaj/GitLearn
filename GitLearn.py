# import required pacakges

import os
import win32com.client as wincl
from tkinter import *
import tkinter as tk
from PIL import Image,ImageTk
from tkinter import ttk
import subprocess, sys
import webbrowser
import tkinter.messagebox
from datetime import datetime
import json,requests

# Image Scrollbar
import tkinter
class ScrollableImage(tkinter.Canvas):
    def __init__(self, master=None, **kw):
        self.image = kw.pop('image', None)
        super(ScrollableImage, self).__init__(master=master, **kw)
        self['highlightthickness'] = 0
        self.propagate(0)  # wont let the scrollbars rule the size of Canvas
        self.create_image(0,0, anchor='nw', image=self.image)
        # Vertical and Horizontal scrollbars
        self.v_scroll = tkinter.Scrollbar(self, orient='vertical', width=6)
        self.h_scroll = tkinter.Scrollbar(self, orient='horizontal', width=6)
        self.v_scroll.pack(side='right', fill='y')
        self.h_scroll.pack(side='bottom', fill='x')
        # Set the scrollbars to the canvas
        self.config(xscrollcommand=self.h_scroll.set, 
                yscrollcommand=self.v_scroll.set)
        # Set canvas view to the scrollbars
        self.v_scroll.config(command=self.yview)
        self.h_scroll.config(command=self.xview)
        # Assign the region to be scrolled 
        self.config(scrollregion=self.bbox('all'))

        self.focus_set()
        self.bind_class(self, "<MouseWheel>", self.mouse_scroll)

    def mouse_scroll(self, evt):
        if evt.state == 0 :
            # self.yview_scroll(-1*(evt.delta), 'units') # For MacOS
            self.yview_scroll( int(-1*(evt.delta/120)) , 'units') # For windows
        if evt.state == 1:
            # self.xview_scroll(-1*(evt.delta), 'units') # For MacOS
            self.xview_scroll( int(-1*(evt.delta/120)) , 'units') # For windows

#============================Appending info to logs =======================================

def append(fname,info):
    # current date and time
    now = datetime.now()
    now = str(now)
    now = now[:-7]
    file1 = open("logs/"+fname, "a")  # append mode 
    file1.write(now+" : "+info+"\n") 
    file1.close()
    
#=================================Home Screen===================================
def home():
    
    append("status.txt","Opened HOME tab")
    
    # create a home window
    global home_screen
    home_screen = Toplevel(root)
    home_screen.title("HOME")
    home_screen.geometry(window_size)
    home_screen.configure(background='#2d302d')
    
    # logo 1
    
    logo = tk.PhotoImage(master=home_screen,file="Images/head.png")
    l=Label(home_screen,image=logo,bg='#2d302d')
    l.image=logo
    l.place(x=80,y=30,width=810,height=175)
    Label(home_screen,text="",bg='#2d302d').pack()
    
    # Button with Image for Git Play
    
    imagetest = PhotoImage(master=home_screen,file="Images/gitplay.png")

    button_qwer = tk.Button(home_screen, text="Use GitLearn now",height= 170, image=imagetest,compound="top",font="bold 12",command=gitplay)
    button_qwer.image=imagetest
    button_qwer.place(x=80,y=400)
    
    # Button with Image for Help
    imagehelp = PhotoImage(master=home_screen,file="Images/help.png")
    
    #Label(home_screen,text="",height="8").pack()
    
    button_qwer = tk.Button(home_screen, text="Need Any Help?",height=170, image=imagehelp,compound="top",font="bold 12",command=githelp)
    button_qwer.image=imagehelp
    button_qwer.place(x=580,y=400)
    
    #Label(home_screen,text="Git Learn",fg="black" ,width=50, height="4", font=("Calibri", 18)).pack()
    #Label(home_screen,text="").pack(padx=250)
    
    Button(home_screen, text="Introduction to\nGit", borderwidth=8,width=18, fg="black",height=4, bg="#dce2e6",font="bold 14" ,command = introduction).place(x=80,y=250)
    
    Button(home_screen, text="Set Up\nGit Installation", width=18, fg="black",height=4,borderwidth=8, bg="#dce2e6",font="bold 14" ,command = setup).place(x=380,y=250)

    Button(home_screen, text="Git\nCommands", width=18,borderwidth=6, fg="black",height=4, bg="#dce2e6",font="bold 14" ,command = basics ).place(x=680,y=250)

    #Button(home_screen,image=im, width=60, borderwidth=8,fg="black",height=8, bg="#dce2e6",font="bold 12" ,command = about).place(x=100,y=400)

    #Button(home_screen, text="About", width=20,borderwidth=8, fg="black",height=8, bg="#dce2e6",font="bold 12" ,command = about).place(x=400,y=400)

    #Button(home_screen, text="About", width=20,borderwidth=8, fg="black",height=8, bg="#dce2e6",font="bold 12" ,command = about).place(x=700,y=400)

    Button(home_screen, text="X", width=3,borderwidth=6, fg="white",height=1, bg="red", font="bold 12" ,command = delete_home_screen).place(x=915,y=20)
    

def delete_home_screen():
    append("status.txt","Closed HOME tab")
    home_screen.destroy()
    
#============================================= Home Screen END ==================================================


    
#============================================= Introduction Screen ==============================================

def introduction():
    append("status.txt","Visited Introduction section")
    # create a introduction window
    global intro_screen
    intro_screen = Toplevel(home_screen)
    intro_screen.title("Introduction")
    intro_screen.geometry(window_size)
    intro_screen.configure(background='#2d302d')
    
    # background image
    
    logo = tk.PhotoImage(master=intro_screen,file="Images/Introduction.png")
    l=Label(intro_screen,image=logo)
    l.image=logo
    l.place(x=50,y=30)
    
    #Label(intro_screen,text="").pack()
    
    
    #Label(intro_screen,text="",height="8").pack()
    
    Button(intro_screen, text="Back", width=10,borderwidth=6, fg="white",height=1, bg="red", font="bold 12" ,command = delete_intro_screen).place(x=100,y=600)
    
    Button(intro_screen, text="Next", width=10,borderwidth=6, fg="white",height=1, bg="#4287f5", font="bold 12" ,command = firstslide).place(x=800,y=600)


def delete_intro_screen():
    append("status.txt","Closed Introduction Section")
    intro_screen.destroy()

#=================================Introduction - Slide 1 ================================================

def firstslide():
    
    append("status.txt","Visited Section 1.1")
    
    # create a introduction window
    global firstslide_screen
    firstslide_screen = Toplevel(intro_screen)
    firstslide_screen.title("What is Version Control?")
    firstslide_screen.geometry(window_size)
    firstslide_screen.configure(background='#2d302d')
    
    # background image
    
    logo = tk.PhotoImage(master=firstslide_screen,file="Images/firstslide.png")
    l=Label(firstslide_screen,image=logo)
    l.image=logo
    l.place(x=50,y=70)
    
    # hyperlink for more information
    
    link = Label(firstslide_screen, text="more info...",width=10,height=1,bg="#dce2e6", fg="blue", font="bold 12",cursor="hand2")
    link.place(x=800,y=30)
    link.bind("<Button-1>", lambda e: callback("https://www.atlassian.com/git/tutorials/what-is-version-control"))
    
    #Label(firstslide_screen,text="",height="8").pack()
    
    Button(firstslide_screen, text="Previous",borderwidth=6, width=10, fg="white",height=1, bg="#4287f5", font="bold 12" ,command = delete_firstslide_screen).place(x=100,y=600)
    
    Button(firstslide_screen, text="Home",borderwidth=6, width=10, fg="black",height=1, bg="#dce2e6", font="bold 12" ,command = delete_intro_screen).place(x=100,y=30)

    Button(firstslide_screen, text="Next", borderwidth=6,width=10, fg="white",height=1, bg="#4287f5", font="bold 12" ,command = secondslide).place(x=800,y=600)

def callback(url):
    append("status.txt","Opened the url : "+url)
    webbrowser.open_new(url)

def delete_firstslide_screen():
    append("status.txt","Closed Section 1.1")
    firstslide_screen.destroy()

    
#=================================Introduction - Slide 2 ================================================
def secondslide():
    append("status.txt","Visited Section 1.2")
    # create a introduction window
    global secondslide_screen
    secondslide_screen = Toplevel(firstslide_screen)
    secondslide_screen.title("Centralized Version Control")
    secondslide_screen.geometry(window_size)
    secondslide_screen.configure(background='#2d302d')
    
    # background image
    
    logo = tk.PhotoImage(master=secondslide_screen,file="Images/secondslide.png")
    l=Label(secondslide_screen,image=logo)
    l.image=logo
    l.place(x=50,y=70)
    
    # hyperlink for more information
    
    link = Label(secondslide_screen, text="more info...",width=10,height=1,bg="#dce2e6", fg="blue", font="bold 12",cursor="hand2")
    link.place(x=800,y=30)
    link.bind("<Button-1>", lambda e: callback("https://www.atlassian.com/blog/software-teams/version-control-centralized-dvcs"))
    
    #Label(secondslide_screen,text="").pack()
    
    
    #Label(secondslide_screen,text="",height="8").pack()
    
    Button(secondslide_screen, text="Previous",borderwidth=6, width=10, fg="white",height=1, bg="#4287f5", font="bold 12" ,command = delete_secondslide_screen).place(x=100,y=600)
    
    Button(secondslide_screen, text="Home", width=10,borderwidth=6, fg="black",height=1, bg="#dce2e6", font="bold 12" ,command = delete_intro_screen).place(x=100,y=30)

    Button(secondslide_screen, text="Next", width=10, borderwidth=6,fg="white",height=1, bg="#4287f5", font="bold 12" ,command = thirdslide).place(x=800,y=600)



def delete_secondslide_screen():
    append("status.txt","Closed Section 1.2")
    secondslide_screen.destroy()
    
#=================================== Introduction - Slide 3 ========================================   

def thirdslide():
    append("status.txt","Visited Section 1.3")
     # create a introduction window
    global thirdslide_screen
    thirdslide_screen = Toplevel(secondslide_screen)
    thirdslide_screen.title("Distributed Version Control")
    thirdslide_screen.geometry(window_size)
    thirdslide_screen.configure(background='#2d302d')
    
    # background image
    
    logo = tk.PhotoImage(master=thirdslide_screen,file="Images/thirdslide.png")
    l=Label(thirdslide_screen,image=logo)
    l.image=logo
    l.place(x=50,y=70)
    
    # hyperlink for more information
    
    link = Label(thirdslide_screen, text="more info...",width=10,height=1,bg="#dce2e6", fg="blue", font="bold 12",cursor="hand2")
    link.place(x=800,y=30)
    link.bind("<Button-1>", lambda e: callback("https://en.wikipedia.org/wiki/Distributed_version_control"))
    
    #Label(thirdslide_screen,text="").pack()
    
    
    #Label(thirdslide_screen,text="",height="8").pack()
    
    Button(thirdslide_screen, text="Previous", width=10,borderwidth=6, fg="white",height=1, bg="#4287f5", font="bold 12" ,command = delete_thirdslide_screen).place(x=100,y=600)
    
    Button(thirdslide_screen, text="Home", width=10, borderwidth=6,fg="black",height=1, bg="#dce2e6", font="bold 12" ,command = delete_intro_screen).place(x=100,y=30)

    Button(thirdslide_screen, text="Next", width=10, borderwidth=6,fg="white",height=1, bg="#4287f5", font="bold 12" ,command = fourthslide).place(x=800,y=600)



def delete_thirdslide_screen():
    append("status.txt","Closed Section 1.3")
    thirdslide_screen.destroy()
    
#=================================== Introduction - Slide 4 ========================================   

def fourthslide():
    
    append("status.txt","Visited Section 1.4")
     # create a introduction window
    global fourthslide_screen
    fourthslide_screen = Toplevel(thirdslide_screen)
    fourthslide_screen.title("Centralized vs Distributed Version Control")
    fourthslide_screen.geometry(window_size)
    fourthslide_screen.configure(background='#2d302d')
    
    # background image
    
    logo = tk.PhotoImage(master=fourthslide_screen,file="Images/fourthslide.png")
    l=Label(fourthslide_screen,image=logo)
    l.image=logo
    l.place(x=50,y=70)
    
    # hyperlink for more information

    link = Label(fourthslide_screen, text="more info...",width=10,height=1,bg="#dce2e6", fg="blue", font="bold 12",cursor="hand2")
    link.place(x=800,y=30)
    link.bind("<Button-1>", lambda e: callback("https://www.teamstudio.com/blog/distributed-vs-centralized-version-control-systems-for-lotus-notes"))
    
    #Label(fourthslide_screen,text="").pack()
    
    
    #Label(fourthslide_screen,text="",height="8").pack()
    
    Button(fourthslide_screen, text="Previous", width=10,borderwidth=6, fg="white",height=1, bg="#4287f5", font="bold 12" ,command = delete_fourthslide_screen).place(x=100,y=600)
    
    Button(fourthslide_screen, text="Home", width=10,borderwidth=6, fg="black",height=1, bg="#dce2e6", font="bold 12" ,command = delete_intro_screen).place(x=100,y=30)

    Button(fourthslide_screen, text="Next", width=10,borderwidth=6, fg="white",height=1, bg="#4287f5", font="bold 12" ,command = fifthslide).place(x=800,y=600)


def delete_fourthslide_screen():
    append("status.txt","Closed Section 1.4")
    fourthslide_screen.destroy()


#=================================== Introduction - Slide 5 ========================================   

def fifthslide():
    append("status.txt","Visited Section 1.5")
     # create a introduction window
    global fifthslide_screen
    fifthslide_screen = Toplevel(fourthslide_screen)
    fifthslide_screen.title("What is Git?")
    fifthslide_screen.geometry(window_size)
    fifthslide_screen.configure(background='#2d302d')
    
    # background image
    
    logo = tk.PhotoImage(master=fifthslide_screen,file="Images/fifthslide.png")
    l=Label(fifthslide_screen,image=logo)
    l.image=logo
    l.place(x=50,y=70)
    
    # hyperlink for more information
    
    link = Label(fifthslide_screen, text="more info...",width=10,height=1,bg="#dce2e6", fg="blue", font="bold 12",cursor="hand2")
    link.place(x=800,y=30)
    link.bind("<Button-1>", lambda e: callback("https://git-scm.com/book/en/v2/Getting-Started-A-Short-History-of-Git"))
    
    #Label(fifthslide_screen,text="").pack()
    
    
    #Label(fifthslide_screen,text="",height="8").pack()
    
    Button(fifthslide_screen, text="Previous", width=10, borderwidth=6,fg="white",height=1, bg="#4287f5", font="bold 12" ,command = delete_fifthslide_screen).place(x=100,y=600)
    
    Button(fifthslide_screen, text="Home", width=10,borderwidth=6, fg="black",height=1, bg="#dce2e6", font="bold 12" ,command = delete_intro_screen).place(x=100,y=30)

    Button(fifthslide_screen, text="Next", width=10,borderwidth=6, fg="white",height=1, bg="#4287f5", font="bold 12" ,command = sixthslide).place(x=800,y=600)


def delete_fifthslide_screen():
    append("status.txt","Closed Section 1.5")
    fifthslide_screen.destroy()

    
#=================================== Introduction - Slide 6 ========================================   

def sixthslide():
    append("status.txt","Visited Section 1.6")
     # create a introduction window
    global sixthslide_screen
    sixthslide_screen = Toplevel(fifthslide_screen)
    sixthslide_screen.title("Git - Life Cycle")
    sixthslide_screen.geometry(window_size)
    sixthslide_screen.configure(background='#2d302d')
    
    # background image
    
    logo = tk.PhotoImage(master=sixthslide_screen,file="Images/sixthslide.png")
    l=Label(sixthslide_screen,image=logo)
    l.image=logo
    l.place(x=50,y=70)
    
    # hyperlink for more information
    
    link = Label(sixthslide_screen, text="more info...",width=10,height=1,bg="#dce2e6", fg="blue", font="bold 12",cursor="hand2")
    link.place(x=800,y=30)
    link.bind("<Button-1>", lambda e: callback("https://www.toolsqa.com/git/git-life-cycle/"))
    #Label(sixthslide_screen,text="").pack()
    
    
    #Label(sixthslide_screen,text="",height="8").pack()
    
    Button(sixthslide_screen, text="Previous", borderwidth=6,width=10, fg="white",height=1, bg="#4287f5", font="bold 12" ,command = delete_sixthslide_screen).place(x=100,y=600)
    
    Button(sixthslide_screen, text="Home", width=10,borderwidth=6, fg="black",height=1, bg="#dce2e6", font="bold 12" ,command = delete_intro_screen).place(x=100,y=30)

    Button(sixthslide_screen, text="Cheat Sheet", borderwidth=6,width=10, fg="white",height=1, bg="green", font="bold 12" ,command = open_cheatsheet).place(x=800,y=600)

def open_cheatsheet():
    append("status.txt","Opened CheatSheet")
    webbrowser.open('Cheatsheet.pdf')

def delete_sixthslide_screen():
    append("status.txt","Closed Section 1.6")
    sixthslide_screen.destroy()

#==================================== Introduction Screen END ==========================================================
    
def about():
    pass

#root.destroy()
def delete_root():
    append("status.txt","********************Closed the application*************************")
    root.destroy()



#===================================== SetUp Screen =======================================================

def setup():
    append("status.txt","Opened SetUp Section")
    # create a introduction window
    global setup_screen
    setup_screen = Toplevel(home_screen)
    setup_screen.title("SetUp Git")
    setup_screen.geometry(window_size)
    setup_screen.configure(background='#2d302d')
    
    # background image
    
    logo = tk.PhotoImage(master=setup_screen,file="Images/setup.png")
    l=Label(setup_screen,image=logo)
    l.image=logo
    l.place(x=50,y=70)
    
    #Label(setup_screen,text="").pack()
    
    
    #Label(setup_screen,text="",height="8").pack()
    
    Button(setup_screen, text="Back", width=10, fg="white",height=1,borderwidth=6, bg="red", font="bold 12" ,command = delete_setup_screen).place(x=100,y=600)
    
    Button(setup_screen, text="Next", width=10, fg="white",height=1,borderwidth=6, bg="#4287f5", font="bold 12" ,command = git).place(x=800,y=600)

    Button(setup_screen, text="Home", width=10, fg="black",height=1,borderwidth=6, bg="#dce2e6", font="bold 12" ,command = delete_setup_screen).place(x=100,y=30)


def delete_setup_screen():
    append("status.txt","Closed SetUp Section")
    setup_screen.destroy()
    
#================================== Installation of Git Screen ===================================================

def git():
    append("status.txt","Visited Installation of Git tab")
     # create a introduction window
    global git_screen
    git_screen = Toplevel(setup_screen)
    git_screen.title("Installation of Git on Windows")
    git_screen.geometry(window_size)
    git_screen.configure(background='#2d302d')
    
    # background image
    
    logo = tk.PhotoImage(master=git_screen,file="Images/install.png")
    l=Label(git_screen,image=logo)
    l.image=logo
    l.place(x=50,y=70)
    
    # hyperlink for more information
    
    link = Label(git_screen, text="On Linux & Mac",width=15,height=1,bg="#dce2e6", fg="blue", font="bold 12",cursor="hand2")
    link.place(x=830,y=30)
    link.bind("<Button-1>", lambda e: callback("https://git-scm.com/book/en/v2/Getting-Started-Installing-Git"))
    #Label(git_screen,text="").pack()
    
    
    #Label(git_screen,text="",height="8").pack()
    
    Button(git_screen, text="Previous", width=10, fg="white",borderwidth=6,height=1, bg="#4287f5", font="bold 12" ,command = delete_git_screen).place(x=100,y=600)
    
    Button(git_screen, text="Home", width=10, fg="black",height=1, borderwidth=6,bg="#dce2e6", font="bold 12" ,command = delete_setup_screen).place(x=100,y=30)

    Button(git_screen, text="Next", width=10, fg="white",height=1,borderwidth=6, bg="#4287f5", font="bold 12" ,command = account).place(x=800,y=600)

    Button(git_screen, text="Install", width=10, fg="white",height=1,borderwidth=6, bg="green", font="bold 12" ,command = install).place(x=250,y=600)

    Button(git_screen, text="Git Bash", width=10, fg="white",height=1,borderwidth=6, bg="green", font="bold 12" ,command = gitbash).place(x=650,y=600)

def gitbash():
    append("status.txt","Trying to open GitBash")
    cwd=os.getcwd()
    f=open("scripts/path.txt",'w')
    f.write(cwd)
    f.close()

    try:
        p = subprocess.Popen(["powershell.exe","-ExecutionPolicy","Unrestricted","./scripts/gitbash.ps1",cwd],stdout=subprocess.PIPE,stderr=subprocess.PIPE)
        p.communicate()
        append("status.txt","GitBash Opened!")

    except Exception as e:
        append("gitbash.txt",str(e))
        append("status.txt",str(e))
        tkinter.messagebox.showerror("Error","Something went wrong.Check logs/gitbash.txt",parent=git_screen)

def install():
    append("status.txt","Installing Git")
    cwd=os.getcwd()
    f=open("scripts/path.txt",'w')
    f.write(cwd)
    f.close()

    try:
        p = subprocess.Popen(["powershell.exe","-ExecutionPolicy","Unrestricted","./scripts/setup.ps1",cwd],stdout=subprocess.PIPE,stderr=subprocess.PIPE)
        p.communicate()
        tkinter.messagebox.showinfo("Info","You can use Git Bash now!",parent=git_screen)
        append("status.txt","Git Installed")

    except Exception as e:
        append("setup.txt",str(e))
        append("status.txt",str(e))

        tkinter.messagebox.showerror("Error","Something went wrong.Check logs/setup.txt",parent=git_screen)
    
        
def delete_git_screen():
    append("status.txt","Closed Installation of Git tab")
    git_screen.destroy()
    
#=============================================== Github Account Creating ==========================================

def account():
    append("status.txt","Visited the Why Github? screen")
     # create a introduction window
    global account_screen
    account_screen = Toplevel(git_screen)
    account_screen.title("Why GitHub Account?")
    account_screen.geometry(window_size)
    account_screen.configure(background='#2d302d')
    
    # background image
    
    logo = tk.PhotoImage(master=account_screen,file="Images/gitaccount.png")
    l=Label(account_screen,image=logo)
    l.image=logo
    l.place(x=50,y=70)
    
    # hyperlink for more information
    
    link = Label(account_screen, text="GitHub About",width=10,height=1,bg="#dce2e6", fg="blue", font="bold 12",cursor="hand2")
    link.place(x=830,y=30)
    link.bind("<Button-1>", lambda e: callback("https://github.com/about"))
    #Label(account_screen,text="").pack()
    
    
    #Label(account_screen,text="",height="8").pack()
    
    Button(account_screen, text="Previous", width=10, fg="white",height=1,borderwidth=6, bg="#4287f5", font="bold 12" ,command = delete_account_screen).place(x=100,y=600)
    
    Button(account_screen, text="Home", width=10, fg="black",height=1,borderwidth=6, bg="#dce2e6", font="bold 12" ,command = delete_setup_screen).place(x=100,y=30)

    Button(account_screen, text="Video", width=10, fg="white",height=1,borderwidth=6, bg="#8c3526", font="bold 12" ,command = setupvideo).place(x=800,y=600)

    Button(account_screen, text="Create Account", width=15, fg="white",borderwidth=6,height=1, bg="green", font="bold 12" ,command = githubaccount).place(x=250,y=600)

    Button(account_screen, text="Git Bash", width=10, fg="white",height=1,borderwidth=6, bg="green", font="bold 12" ,command = gitbash).place(x=650,y=600)

# video for creating account
def setupvideo():
    append("status.txt","Playing Video for SetUp GitHub Account")
    callback("https://www.youtube.com/watch?v=6U7_Om4zffM")

# creating Github account
def githubaccount():
    append("status.txt","Visited Github Sign Up page")
    callback("https://github.com/join?source=login")

def delete_account_screen():
    append("status.txt","Closed why GitHub? screen")
    account_screen.destroy()
    
#============================================ SetUp Screen END ================================================


#============================================== Basic Concepts ============================================

def basics():
    append("status.txt","Opened Basics Git Commands section")
    # create a introduction window
    global content_screen
    content_screen = Toplevel(home_screen)
    content_screen.title("Basic Concepts of Git")
    content_screen.geometry(window_size)
    content_screen.configure(background='#2d302d')
    
    # background image
    
    logo = tk.PhotoImage(master=content_screen,file="Images/basics.png")
    l=Label(content_screen,image=logo)
    l.image=logo
    l.place(x=50,y=70)
    
    Label(content_screen,text="").pack()
    
    
    Label(content_screen,text="",height="8").pack()
    
    Button(content_screen, text="Back", width=10, fg="white",height=1,borderwidth=6, bg="red", font="bold 12" ,command = delete_content_screen).place(x=100,y=600)
    
    Button(content_screen, text="Next", width=10, fg="white",height=1,borderwidth=6, bg="#4287f5", font="bold 12" ,command = firstconcept).place(x=800,y=600)

    Button(content_screen, text="Home", width=10, fg="black",height=1,borderwidth=6, bg="#dce2e6", font="bold 12" ,command = delete_content_screen).place(x=100,y=30)

def delete_content_screen():
    append("status.txt","Closed Git Commands section")
    content_screen.destroy()

    
    
#============================================ First Page =====================================================================
def firstconcept():
    append("status.txt","Visited Section 3.1")
    # create a introduction window
    global firstconcept_screen
    firstconcept_screen = Toplevel(content_screen)
    firstconcept_screen.title("Basic Git Commands")
    firstconcept_screen.geometry(window_size)
    firstconcept_screen.configure(background='#2d302d')
    
    # background image
    
    img = Image.open('Images/basics1.png')
    img = ImageTk.PhotoImage(img)
    ScrollableImage(firstconcept_screen, image=img, width=980, height=650).pack()
    
    Label(firstconcept_screen,text="").pack()
    
    
    Label(firstconcept_screen,text="",height="8").pack()
    
    Button(firstconcept_screen, text="Previous", width=12, fg="white",height=1,borderwidth=6, bg="#4287f5", font="bold 12" ,command = delete_firstconcept_screen).place(x=800,y=500)
    
    Button(firstconcept_screen, text="Next", width=12, fg="white",height=1,borderwidth=6, bg="#4287f5", font="bold 12" ,command = secondconcept).place(x=800,y=600)

    Button(firstconcept_screen, text="Home", width=12, fg="black",height=1,borderwidth=6, bg="#dce2e6", font="bold 12" ,command = delete_content_screen).place(x=800,y=30)
    
    Button(firstconcept_screen, text="Tutorial", width=12, fg="white",height=8,borderwidth=6, bg="black", font="bold 12" ,command=basicsvideo).place(x=800,y=300)

def basicsvideo():
    append("status.txt","Playing video for Git Commands")
    callback("https://www.youtube.com/watch?v=HVsySz-h9r4")

def delete_firstconcept_screen():
    append("status.txt","Closed Section 3.1")
    firstconcept_screen.destroy()

#========================================== Second Page ============================================================

def secondconcept():
    append("status.txt","Visited Section 3.2")
    # create a introduction window
    global secondconcept_screen
    secondconcept_screen = Toplevel(firstconcept_screen)
    secondconcept_screen.title("Basic Git Commands")
    secondconcept_screen.geometry(window_size)
    secondconcept_screen.configure(background='#2d302d')
    
    # background image
    
    img = Image.open('Images/basics2.png')
    img = ImageTk.PhotoImage(img)
    ScrollableImage(secondconcept_screen, image=img, width=980, height=650).pack()
    
    Label(secondconcept_screen,text="").pack()
    
    
    Label(secondconcept_screen,text="",height="8").pack()
    
    Button(secondconcept_screen, text="Previous", width=12, fg="white",height=1,borderwidth=6, bg="#4287f5", font="bold 12" ,command = delete_secondconcept_screen).place(x=800,y=500)
    
    Button(secondconcept_screen, text="Next", width=12, fg="white",height=1,borderwidth=6, bg="#4287f5", font="bold 12" ,command = thirdconcept).place(x=800,y=600)

    Button(secondconcept_screen, text="Home", width=12, fg="black",height=1,borderwidth=6, bg="#dce2e6", font="bold 12" ,command = delete_content_screen).place(x=800,y=30)
    
    Button(secondconcept_screen, text="Tutorial", width=12, fg="white",height=8,borderwidth=6, bg="black", font="bold 12" ,command = basicsvideo).place(x=800,y=300)

def delete_secondconcept_screen():
    append("status.txt","Closed Section 3.2")
    secondconcept_screen.destroy()

#============================================ Third Page =====================================================================
def thirdconcept():
    append("status.txt","Visited Section 3.3")
    # create a introduction window
    global thirdconcept_screen
    thirdconcept_screen = Toplevel(secondconcept_screen)
    thirdconcept_screen.title("Basic Git Commands")
    thirdconcept_screen.geometry(window_size)
    thirdconcept_screen.configure(background='#2d302d')
    
    # background image
    
    img = Image.open('Images/basics3.png')
    img = ImageTk.PhotoImage(img)
    ScrollableImage(thirdconcept_screen, image=img, width=980, height=650).pack()
    
    Label(thirdconcept_screen,text="").pack()
    
    
    Label(thirdconcept_screen,text="",height="8").pack()
    
    Button(thirdconcept_screen, text="Previous", width=12, fg="white",height=1,borderwidth=6, bg="#4287f5", font="bold 12" ,command = delete_thirdconcept_screen).place(x=800,y=500)
    
    Button(thirdconcept_screen, text="Next", width=12, fg="white",height=1,borderwidth=6, bg="#4287f5", font="bold 12" ,command = fourthconcept).place(x=800,y=600)

    Button(thirdconcept_screen, text="Home", width=12, fg="black",height=1,borderwidth=6, bg="#dce2e6", font="bold 12" ,command = delete_content_screen).place(x=800,y=30)
    
    Button(thirdconcept_screen, text="Tutorial", width=12, fg="white",height=8,borderwidth=6, bg="black", font="bold 12" ,command = basicsvideo).place(x=800,y=300)

def delete_thirdconcept_screen():
    append("status.txt","Closed Section 3.3")
    thirdconcept_screen.destroy()


#============================================ Fourth Page =====================================================================
def fourthconcept():
    append("status.txt","Visited Section 3.4")
    # create a introduction window
    global fourthconcept_screen
    fourthconcept_screen = Toplevel(thirdconcept_screen)
    fourthconcept_screen.title("Basic Git Commands")
    fourthconcept_screen.geometry(window_size)
    fourthconcept_screen.configure(background='#2d302d')
    
    # background image
    
    img = Image.open('Images/basics4.png')
    img = ImageTk.PhotoImage(img)
    ScrollableImage(fourthconcept_screen, image=img, width=980, height=650).pack()
    
    Label(fourthconcept_screen,text="").pack()
    
    
    Label(fourthconcept_screen,text="",height="8").pack()
    
    Button(fourthconcept_screen, text="Previous", width=12, fg="white",height=1,borderwidth=6, bg="#4287f5", font="bold 12" ,command = delete_fourthconcept_screen).place(x=800,y=500)
    
    Button(fourthconcept_screen, text="Next", width=12, fg="white",height=1,borderwidth=6, bg="#4287f5", font="bold 12" ,command = fifthconcept).place(x=800,y=600)

    Button(fourthconcept_screen, text="Home", width=12, fg="black",height=1,borderwidth=6, bg="#dce2e6", font="bold 12" ,command = delete_content_screen).place(x=800,y=30)
    
    Button(fourthconcept_screen, text="Tutorial", width=12, fg="white",height=8,borderwidth=6, bg="black", font="bold 12" ,command = basicsvideo).place(x=800,y=300)

def delete_fourthconcept_screen():
    append("status.txt","Closed Section 3.4")
    fourthconcept_screen.destroy()


#============================================ Fifth Page =====================================================================

def fifthconcept():
    append("status.txt","Visited Section 3.5")
    # create a introduction window
    global fifthconcept_screen
    fifthconcept_screen = Toplevel(thirdconcept_screen)
    fifthconcept_screen.title("Basic Git Commands")
    fifthconcept_screen.geometry(window_size)
    fifthconcept_screen.configure(background='#2d302d')
    
    # background image
    
    img = Image.open('Images/basics5.png')
    img = ImageTk.PhotoImage(img)
    ScrollableImage(fifthconcept_screen, image=img, width=980, height=650).pack()
    
    Label(fifthconcept_screen,text="").pack()
    
    
    Label(fifthconcept_screen,text="",height="8").pack()
    
    Button(fifthconcept_screen, text="Previous", width=12, fg="white",height=1,borderwidth=6, bg="#4287f5", font="bold 12" ,command = delete_fifthconcept_screen).place(x=800,y=500)
    
    Button(fifthconcept_screen, text="Cheat Sheet", width=12, fg="black",height=1,borderwidth=6, bg="#49eb34", font="bold 12" ,command = open_cheatsheet).place(x=800,y=600)

    Button(fifthconcept_screen, text="Home", width=12, fg="black",height=1,borderwidth=6, bg="#dce2e6", font="bold 12" ,command = delete_content_screen).place(x=800,y=30)
    
    Button(fifthconcept_screen, text="Tutorial", width=12, fg="white",height=8,borderwidth=6, bg="black", font="bold 12" ,command = basicsvideo).place(x=800,y=300)

def delete_fifthconcept_screen():
    append("status.txt","Closed Section 3.5")
    fifthconcept_screen.destroy()

    
    
    

#================================================ Basics Concepts for Git - END ====================================================


#============================================== Git Play ===============================================

def gitplay():
    append("status.txt","Opened the GitPlay section")
    # create a introduction window
    global gitplay_screen
    gitplay_screen = Toplevel(home_screen)
    gitplay_screen.title("Git Play")
    gitplay_screen.geometry(window_size)
    gitplay_screen.configure(background='#2d302d')
    
    
    
    Label(gitplay_screen,text="",bg="#2d302d").pack()
    
    Label(gitplay_screen,text="Use this automated tool to create your own repositories",font=("Calibri", 26),bg="#2d302d",fg="white").place(x=100,y=100)

    
    Label(gitplay_screen,text="Let's have fun!",font=("Calibri", 26),bg="#2d302d",fg="white").place(x=400,y=200)
    
    Label(gitplay_screen,text="",bg="#2d302d",height="8").pack()
    
    Label(gitplay_screen,text="Note : Make sure you have installed Git. If not go to SetUp section - Slide 2 and\n click on install button.Also you need to have a GitHub account.\nBy using this tool you can push your files into remote repository",bg="#2d302d",fg="white",height=3,width=100,font="bold 11").place(x=80,y=450)

    
    Button(gitplay_screen, text="Create New \nRepository & Push files", width=20, fg="white",height=5,borderwidth=6, bg="#32a852", font="bold 12" ,command = createrepo).place(x=100,y=300)
    
    Button(gitplay_screen, text="Push files to\nExisiting Repositroy", width=20, fg="white",height=5,borderwidth=6, bg="#f5424b", font="bold 12" ,command = existingrepo).place(x=400,y=300)

    Button(gitplay_screen, text="Clone a\n Repository", width=20, fg="white",height=5,borderwidth=6, bg="#428af5", font="bold 12" ,command = clonerepo).place(x=700,y=300)

    Button(gitplay_screen, text="X", width=3,borderwidth=6, fg="white",height=1, bg="red", font="bold 12" ,command = delete_gitplay_screen).place(x=915,y=20)


def delete_gitplay_screen():
    append("status.txt","Closed GitPlay scetion")
    gitplay_screen.destroy()
    
#===================================================Creating new repository================================

def createrepo():
    append("status.txt","Getting ready to create a repository")
    # create a introduction window
    global create_screen
    create_screen = Toplevel(gitplay_screen)
    create_screen.title("Create New Repository")
    create_screen.geometry(window_size)
    create_screen.configure(background='#2d302d')
    
    Label(create_screen,text="Mandatory sections are marked with ** ",bg="white",fg="red",height=1,width=30,font="bold 12").place(x=100,y=20)

    # UserName
    global entry1
    Label(create_screen,text="Enter GitHub Username** : ",bg="#2d302d",fg="white",height=1,width=25,font="bold 15").place(x=100,y=60)
    entry1 = Entry(create_screen,fg="black",bg="#dce2e6",width=30,font="bold 12")
    entry1.place(x=400,y=60,height=30)
    
    # RepoName
    global entry2
    Label(create_screen,text="Enter new Repository name** : ",bg="#2d302d",fg="white",height=1,width=25,font="bold 15").place(x=100,y=160)
    entry2 = Entry(create_screen,fg="black",bg="#dce2e6",width=30,font="bold 12")
    entry2.place(x=400,y=160,height=30)
    
    # Description
    global entry3
    Label(create_screen,text="Enter Description : ",bg="#2d302d",fg="white",height=1,width=25,font="bold 15").place(x=100,y=260)
    entry3 = Entry(create_screen,fg="black",bg="#dce2e6",width=50,font="bold 12")
    entry3.place(x=400,y=260,height=30)
    
    # RepoPath
    global entry4
    Label(create_screen,text="Enter the path : \n( deafult: current directory) ",bg="#2d302d",fg="white",height=2,width=25,font="bold 15").place(x=100,y=360)
    entry4 = Entry(create_screen,fg="black",bg="#dce2e6",width=50,font="bold 12")
    entry4.place(x=400,y=360,height=30)
    
    Label(create_screen,text="Note : On clciking Submit button your files in the specified path will\n be pushed to your GitHub with Repositor name given ",bg="#2d302d",fg="white",height=3,width=100,font="bold 11").place(x=80,y=450)

    
    Button(create_screen,text='Submit',font="bold 12",borderwidth=6,height=1,width=20,bg="#32a852",fg="white" ,command=actionCreateRepo).place(x=400,y=550)
    Button(create_screen, text="X", width=3,borderwidth=6, fg="white",height=1, bg="red", font="bold 12" ,command = delete_create_screen).place(x=915,y=20)

    
    
# Github UserName Validation

def UserExist(UserName):
    
    
    if UserName == "":
        return False
    
    api_url = "https://api.github.com/users/" + UserName
    r=requests.get(api_url)
    
    if r.status_code == 200:
        d =json.loads(r.content.decode('utf-8'))
        try:
            if d['login']==UserName:
                return True
            else:
                return False
        except:
            return False
    else:
        return False  
    
# Check if the RepoName exists

def RepoExist(UserName,RepoName):
    
    if RepoName == "" or len(RepoName.split())>1:
        return "bad"
    
    api_url = "https://api.github.com/users/" + UserName +"/repos"
    r=requests.get(api_url)
    if r.status_code == 200:
        d =json.loads(r.content.decode('utf-8'))
        try:
            for i in d:
                if RepoName == i['name']:
                    return "good"
        except:
            return "no"
    return "no"  
    
def actionCreateRepo():
    
    append("gitplay.txt","=========Creating new repository============")
    append("status.txt","Submitted the details")
    
    # UserName 
    
    UserName = entry1.get()
    append("status.txt","Checking if the UserName :"+UserName+" exists")
    
    if not UserExist(UserName):
        msg = "User is not Found!"
        append("gitplay.txt",msg)
        append("status.txt",msg)
        tkinter.messagebox.showwarning("Warning",msg+"Check logs/gitplay.txt",parent=create_screen)
        return
    
    append("gitplay.txt","GitHub User Found")
    append("status.txt","GitHub User Found")

    
    # RepoName
        
    RepoName = entry2.get()
    append("status.txt","Checking if a repository with name "+RepoName+" exists")

    result = RepoExist(UserName,RepoName)
    
    if result=="bad":
        msg = "Repository name is invalid"
        append("gitplay.txt",msg)
        append("status.txt",msg)

        tkinter.messagebox.showwarning("Warning",msg+"\nCheck logs/gitplay.txt",parent=create_screen)
        return
    elif result=="good":
        msg = "Repo already exists!"
        append("gitplay.txt",msg)
        append("status.txt",msg)

        tkinter.messagebox.showwarning("Warning",msg+"\nCheck logs/gitplay.txt",parent=create_screen)
        return
    
    # Description
    
    Description = entry3.get()
    
    if Description == "":
        Description = "This repository was made with GitLearn"
        msg = "A default description was added to your repo"
        append("gitplay.txt",msg)
        append("status.txt",msg)
        
    f = open("logs/description.txt", "w")
    f.write(Description)
    f.close()
    # RepoPath
    
    RepoPath = entry4.get()
    append("status.txt","Checking if the path is valid")
    if RepoPath == "":
        RepoPath = os.getcwd()
    
    if not os.path.exists(RepoPath):
        msg = "Given Path not found!!"
        append("gitplay.txt",msg)
        append("status.txt",msg)
        tkinter.messagebox.showwarning("Error",msg+"\nCheck logs/gitplay.txt",parent=create_screen)
        return
    
    msg = "Path Found -- "+RepoPath
    append("gitplay.txt",msg)
    append("status.txt",msg)

    f=open("scripts/path.txt",'w')
    f.write(RepoPath)
    f.close()
    
    # Github API
    
    append("status.txt","GitHub API fetched to create repo")
    
    command = 'start /wait cmd /c curl -u '+UserName+' https://api.github.com/user/repos -d "{\\"name\\":\\"'+RepoName+'\\",\\"description\\":\\"'+Description+'\\"}"'
    
    try:
        l=os.system(command)
    except:
        msg = "Something went wrong! Check your Internet Connection"
        append("gitplay.txt",msg)
        append("status.txt",msg)
        tkinter.messagebox.showwarning("Error",msg+"\nCheck logs/gitplay.txt",parent=create_screen)
        return
    
    '''result = RepoExist(UserName,RepoName)
    
    if result=="bad" or result=="no":
        msg = "Invalid Password!"
        append("gitplay.txt",msg)
        tkinter.messagebox.showerror("Error",msg+"\nCheck logs/gitplay.txt")
        return
    elif result=="good":
        msg = "Repository is created Succesfully!"
        append("gitplay.txt",msg)'''
    
    
    newrepo = "1"    
    
    cwd =os.getcwd()
    
    p = subprocess.Popen(["powershell.exe","-ExecutionPolicy","Unrestricted","./scripts/gitplay.ps1",UserName,RepoName,newrepo,RepoPath],stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    p.communicate()
    
    result = RepoExist(UserName,RepoName)
    
    if result=="bad" or result=="no":
        msg = "Check your GitHub account\nrepo will not be created\n if you entered wrong password"
        append("gitplay.txt",msg)
        append("status.txt",msg)
        tkinter.messagebox.showerror("Error",msg+"\nCheck logs/gitplay.txt",parent=create_screen)
        return
    elif result=="good":
        msg = "Repository is created Succesfully!"
        append("gitplay.txt",msg)
        append("status.txt",msg)
    
    msg = "Task Finished!"
    append("gitplay.txt",msg)
    append("status.txt",msg)
    tkinter.messagebox.showinfo("Info",msg+"\nCheck logs/gitplay.txt",parent=create_screen)
    
    
def delete_create_screen():
    append("status.txt","Closed Create repo tab")
    create_screen.destroy()

#===========================================Pushing content to existing repository===============================


def existingrepo():
    append("status.txt","Opened Existing repo section")
    # create a introduction window
    global existing_screen
    existing_screen = Toplevel(gitplay_screen)
    existing_screen.title("Existing Repository")
    existing_screen.geometry(window_size)
    existing_screen.configure(background='#2d302d')
    
    Label(existing_screen,text="Mandatory sections are marked with ** ",bg="white",fg="red",height=1,width=30,font="bold 12").place(x=100,y=20)

    # UserName
    global entry5
    Label(existing_screen,text="Enter GitHub Username** : ",bg="#2d302d",fg="white",height=1,width=25,font="bold 15").place(x=100,y=100)
    entry5 = Entry(existing_screen,fg="black",bg="#dce2e6",width=30,font="bold 12")
    entry5.place(x=400,y=100,height=30)
    
    # RepoName
    global entry6
    Label(existing_screen,text="Existing Repository name** : ",bg="#2d302d",fg="white",height=1,width=25,font="bold 15").place(x=100,y=200)
    entry6 = Entry(existing_screen,fg="black",bg="#dce2e6",width=30,font="bold 12")
    entry6.place(x=400,y=200,height=30)
    
    # RepoPath
    global entry7
    Label(existing_screen,text="Enter the path : \n( default: current directory) ",bg="#2d302d",fg="white",height=2,width=25,font="bold 15").place(x=100,y=300)
    entry7 = Entry(existing_screen,fg="black",bg="#dce2e6",width=50,font="bold 12")
    entry7.place(x=400,y=300,height=30)
    
    Label(existing_screen,text="Note : On clciking Submit button your files in the specified path will\n be pushed to your GitHub with Repository name given ",bg="#2d302d",fg="white",height=3,width=100,font="bold 11").place(x=80,y=450)
    
    Button(existing_screen,text='Submit',font="bold 12",borderwidth=6,height=1,width=20,bg="#32a852",fg="white" ,command=actionExistRepo).place(x=400,y=550)
    Button(existing_screen, text="X", width=3,borderwidth=6, fg="white",height=1, bg="red", font="bold 12" ,command = delete_existing_screen).place(x=915,y=20)

    
    
def actionExistRepo():
    append("status.txt","Getting ready to push files to remote repo")
    append("gitplay.txt","============Existing Repository===========")

    
    # UserName 
    
    UserName = entry5.get()
    append("status.txt","Checking if the UserName :"+UserName+" exists")
    if not UserExist(UserName):
        msg = "User is not Found!"
        append("gitplay.txt",msg)
        append("status.txt",msg)
        tkinter.messagebox.showwarning("Warning",msg+"Check logs/gitplay.txt",parent=existing_screen)
        return
    
    append("gitplay.txt","GitHub User Found")
    append("status.txt","GitHub User Found")
    # RepoName
    
    RepoName = entry6.get()
    append("status.txt","Checking if the Repository exists")
    
    result = RepoExist(UserName,RepoName)
    
    if result=="bad" or result=="no":
        msg = "Repo doesn't exist with given name"
        append("gitplay.txt",msg)
        append("status.txt",msg)
        tkinter.messagebox.showerror("Error",msg+"\nCheck logs/gitplay.txt",parent=existing_screen)
        return
    elif result=="good":
        msg = "Repository is found!"
        append("gitplay.txt",msg)
        append("status.txt",msg)
    
    # RepoPath
    
    RepoPath = entry7.get()
    append("status.txt","Checking it the given RepoPath exists")
    
    if RepoPath == "":
        RepoPath = os.getcwd()
        
    if not os.path.exists(RepoPath):
        msg = "Path not found!!"
        append("gitplay.txt",msg)
        append("status.txt",msg)
        tkinter.messagebox.showwarning("Error",msg+"\nCheck logs/gitplay.txt",parent=existing_screen)
        return
    
    msg = "Path Found -- "+RepoPath
    append("gitplay.txt",msg)
    append("status.txt",msg)

    f=open("scripts/path.txt",'w')
    f.write(RepoPath)
    f.close()
    
    newrepo ="0"
    
    p = subprocess.Popen(["powershell.exe","-ExecutionPolicy","Unrestricted","./scripts/gitplay.ps1",UserName,RepoName,newrepo,RepoPath],stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    p.communicate()
    
    msg = "Task Finished! Check your Repo.\n NOTE: Existing files can't be pushed"
    append("gitplay.txt",msg)
    append("status.txt",msg)
    tkinter.messagebox.showinfo("Info",msg+"\nCheck logs/gitplay.txt",parent=existing_screen)
    
    
def delete_existing_screen():
    append("status.txt","Closed Existing Repo Section")
    existing_screen.destroy()    

#===============================================Cloning a Repository =============================================

def clonerepo():
    append("status.txt","Opened Clone Repository Section")
    # create a introduction window
    global clone_screen
    clone_screen = Toplevel(gitplay_screen)
    clone_screen.title("Clone Repository")
    clone_screen.geometry(window_size)
    clone_screen.configure(background='#2d302d')
    
    Label(clone_screen,text="Mandatory sections are marked with ** ",bg="white",fg="red",height=1,width=30,font="bold 12").place(x=100,y=20)

    # UserName
    global entry8
    Label(clone_screen,text="Enter the link to repo** : ",bg="#2d302d",fg="white",height=1,width=25,font="bold 15").place(x=100,y=140)
    entry8 = Entry(clone_screen,fg="black",bg="#dce2e6",width=50,font="bold 12")
    entry8.place(x=400,y=140,height=30)
    
    # RepoPath
    global entry9
    Label(clone_screen,text="Enter the path : \n( default: current directory) ",bg="#2d302d",fg="white",height=2,width=25,font="bold 15").place(x=100,y=290)
    entry9 = Entry(clone_screen,fg="black",bg="#dce2e6",width=50,font="bold 12")
    entry9.place(x=400,y=290,height=30)
    
    Label(clone_screen,text="Note : On clciking Submit button the repository will be downloaded to your given path ",bg="#2d302d",fg="white",height=3,width=100,font="bold 11").place(x=80,y=450)

    
    Button(clone_screen,text='Submit',font="bold 12",borderwidth=6,height=1,width=20,bg="#32a852",fg="white" ,command=actionCloneRepo).place(x=400,y=550)
    Button(clone_screen, text="X", width=3,borderwidth=6, fg="white",height=1, bg="red", font="bold 12" ,command = delete_clone_screen).place(x=915,y=20)

    
def actionCloneRepo():
    append("status.txt","Getting ready to clone a remote repository")
    append("gitplay.txt","============Cloning Repository===========")
    
    # RepoUrl
    
    RepoUrl = entry8.get()
    append("status.txt","Checking if the URL is valid")
    if RepoUrl =="":
        msg = "URL not found!"
        append("gitplay.txt",msg)
        append("status.txt",msg)
        tkinter.messagebox.showwarning("Warning",msg+"\nCheck logs/gitplay.txt",parent=clone_screen)
        return
    try:
        words = RepoUrl.split("/")
        UserName = words[3]
        RepoName = words[-1]
        if RepoName[-4:-1]==".gi":
            RepoName = RepoName[:-4]
    except:
        msg = "URL not found!"
        append("gitplay.txt",msg)
        append("status.txt",msg)
        tkinter.messagebox.showwarning("Warning",msg+"\nCheck logs/gitplay.txt",parent=clone_screen)
        return
    
    if RepoExist(UserName,RepoName)!="good":
        msg = "URL not found!"
        append("gitplay.txt",msg)
        append("status.txt",msg)
        tkinter.messagebox.showwarning("Warning",msg+"\nCheck logs/gitplay.txt",parent=clone_screen)
        return
        
    
    append("status.txt","URL FOUND!")
    # Repo Path
    
    RepoPath = entry9.get()
    append("status.txt","Checking if the given path is valid")
    if RepoPath == "":
        RepoPath = os.getcwd()
        
    if not os.path.exists(RepoPath):
        msg = "Path not found!!"
        append("gitplay.txt",msg)
        append("status.txt",msg)
        tkinter.messagebox.showwarning("Error",msg+"\nCheck logs/gitplay.txt",parent=clone_screen)
        return
    
    msg = "Path Found -- "+RepoPath
    append("gitplay.txt",msg)
    append("status.txt",msg)

    f=open("scripts/path.txt",'w')
    f.write(RepoPath)
    f.close()
    
    p = subprocess.Popen(["powershell.exe","-ExecutionPolicy","Unrestricted","./scripts/clonerepo.ps1",RepoUrl],stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    p.communicate()
    
    msg = "Task Finished!"
    append("gitplay.txt",msg)
    append("status.txt",msg)
    tkinter.messagebox.showinfo("Info",msg+"\nCheck logs/gitplay.txt",parent=clone_screen)
    
    
    
def delete_clone_screen():
    
    append("status.txt","Closed Clone Section")
    clone_screen.destroy()


#============================================== Git Assitant ==============================================

def githelp():
    append("status.txt","Opened Git Assitant")
    
    # create a introduction window
    global help_screen
    help_screen = Toplevel(home_screen)
    help_screen.title("Need Any help?")
    help_screen.geometry("550x350+320+180")
    help_screen.configure(background='#2d302d')
    
    #Label(help_screen,text="Mandatory sections are marked with ** ",bg="white",fg="red",height=1,width=30,font="bold 12").place(x=100,y=20)

    # command
    global entry10
    Label(help_screen,text="Enter the git command",bg="#2d302d",fg="white",height=1,width=25,font="bold 15").place(x=30,y=50)
    entry10 = Entry(help_screen,fg="black",bg="#dce2e6",width=25,font="bold 12")
    entry10.place(x=70,y=100,height=35)
    
    # query
    global entry11
    Label(help_screen,text="Enter your query : ",bg="#2d302d",fg="white",height=1,width=22,font="bold 15").place(x=30,y=150)
    entry11 = Entry(help_screen,fg="black",bg="#dce2e6",width=25,font="bold 12")
    entry11.place(x=70,y=200,height=35)
    
    
    Button(help_screen,text='HELP',font="bold 11",borderwidth=6,height=1,width=8,bg="#32a852",fg="white" ,command = gitcommand).place(x=350,y=100)
    Button(help_screen, text="SEARCH", width=8,borderwidth=6, fg="white",height=1, bg="#32a852", font="bold 11" ,command = gitsearch).place(x=350,y=200)

def gitcommand():
    append("status.txt","Trying to search for a git command")
    
    command = entry10.get()
    os.system("git --help "+command)
    if command == "":
        tkinter.messagebox.showinfo("Info","Please enter a command",parent=help_screen)
        append("status.txt","Git Command Search Failed!")
        append("githelp.txt","Git Command Search Failed!")
        return
    append("githelp.txt","searched for git "+command+" command")
    append("status.txt","searched for git "+command+" command")
    help_screen.destroy()

def gitsearch():
    append("status.txt","Trying to search for a Query")
    
    query = entry11.get()
    if query == "":
        tkinter.messagebox.showinfo("Info","Please enter your query",parent=help_screen)
        append("status.txt","Query Search Failed!")
        append("githelp.txt","Query Search Failed!")
        return
    webbrowser.open_new_tab('https://google.com//search?btnG=1&q=%s' % query)
    webbrowser.open_new_tab('https://stackoverflow.com//search?btnG=1&q=%s' % query)
    append("githelp.txt","searched for : "+query)
    append("status.txt","searched for : "+query)
    help_screen.destroy()
    
#======================================= Git Assitant END ================================

def ritheeshprofile():
    append("status.txt","Opened Ritheesh Portfolio")
    callback("https://ritheeshbaradwaj.github.io/")

# Main Code

if __name__ == "__main__":
    
    # declaring global variables which are needed through the application
    append("status.txt","************************Started GitLearn***************************")
    
    global main_screen
    global root
    global current_id
    #"980x650+100+50"
    # create a GUI window 
    root = Tk()
    window_size = "980x650+100+50"
    root.geometry(window_size)
    root.title("Git Learn") 
    
    # set the background for GUI window
    root.configure(background='#2d302d')
    cwd = os.getcwd() #current directory
    
    # background image-button
    
    imagetest = PhotoImage(file="Images/root.png")
    button_qwer = tk.Button(image=imagetest,command=ritheeshprofile)
    button_qwer.image=imagetest
    button_qwer.place(x=70,y=30)
    
    '''img1  = Image.open(cwd+'\\Images\\github.png') 
    img = img1.resize((700, 250), Image.ANTIALIAS)
    photo=ImageTk.PhotoImage(img)
    lab=Label(image=photo).pack()#.place(x=200,y=30)'''
    
    
    Label(bg="#2d302d",height=25).pack()
    
    #Label(text="").pack()
    Label(text="Hey mate! This tool is designed to gain basic knowledge on Git and its commands.", bg="#2d302d",fg="white", width="300", height="2", font=("Calibri", 15)).pack()
    
    Label(text="For any queries/to provide feedback : bunnyrb4@gmail.com\nTo visit my profile Click on the above image!", bg="#2d302d",fg="white", width="300", height="2", font=("Calibri", 15)).pack()
    
    #Label(text="").pack()
    #Label(text="", bg="#2d302d",fg="white", width="300", height="1", font=("Calibri", 13)).pack()
    #Label(text="").pack()
    Button(text="Let's Get Started!!", height="2",borderwidth=7, width="30",font="bold 12", command = home).place(x=340,y=520)
    #Label(text="").pack()
    #Button(text="Close", height="2",borderwidth=7, width="30",bg="black",fg="white",font="bold 10",command=delete_root).pack()
    #Label(text="").pack()
    Button(root, text="X", width=3,borderwidth=6, fg="white",height=1, bg="red", font="bold 12" ,command = delete_root).place(x=915,y=20)

    #Button(text="My Profile", width=10,borderwidth=6, fg="black",height=1, bg="#3498eb", font="bold 12" ,command = ritheeshprofile).place(x=800,y=550)

    root.mainloop()