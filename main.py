import tkinter as tk
import customtkinter as ctk

from tkinter import messagebox
from customtkinter import CTkImage

from PIL import Image, ImageTk
import backend
from time import sleep

import os
import sys
from plyer import notification
import winsound

ctk.set_appearance_mode('System')
ctk.set_default_color_theme('blue')

def resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.abspath(relative_path)


updating1 = False
updating2 = False
popmenu = None
notifmenu = None
notifoptionsmenu = None
choice2 = None
notifentry = None
notifset = False
check_time_run = 'STOP'
goalmenu = None
timegoal=['h', 1]
beeped = False
updprog = False
accept = False

def menu_command():   

    root_x = root.winfo_x()
    root_y = root.winfo_y()

    global popmenu, notifentry
    popmenu = ctk.CTkToplevel(root)
    popmenu.title('Choose option')
    popmenu.geometry(f'387x120+{root_x+8}+{root_y+8}')
    popmenu.configure(fg_color='#1f1d1d')
    popmenu.attributes('-alpha' , 0.95)
    popmenu.attributes('-topmost', True)

    sltbutton = ctk.CTkButton(master=popmenu,
                              text='Set initial learning time',
                              font=('Calibri', 15, 'bold'),
                              command=settime,
                              hover_color='black',
                              text_color='white',
                              fg_color='#1f1d1d',
                              width=260
                                )
    sltbutton.pack(pady=(4,0))

    sbtbutton = ctk.CTkButton(master=popmenu,
                              text=' Set initial break time ',
                              font=('Calibri', 15, 'bold'),
                              command=setbreaktime,
                              hover_color='black',
                              text_color='white',
                              fg_color='#1f1d1d',
                              width=260
                                )
    sbtbutton.pack()

    slabbutton = ctk.CTkButton(master=popmenu,
                              text=' Set label names ',
                              font=('Calibri', 15, 'bold'),
                              command=setlabels,
                              hover_color='black',
                              text_color='white',
                              fg_color='#1f1d1d',
                              width=260
                                )
    slabbutton.pack()

    stgbutton = ctk.CTkButton(master=popmenu,
                              text=' Set a time goal ',
                              font=('Calibri', 15, 'bold'),
                              command=setgoal,
                              hover_color='black',
                              text_color='white',
                              fg_color='#1f1d1d',
                              width=260
                                )
    stgbutton.pack()







# MENU - FUNKCJE 
def settime():
    popmenu.destroy()
    def submit():
        global time1, updating1, beeped
        try:
            b = entry.get().split(':')
            h = int(b[0])
            m = int(b[1])
            s = int(b[2])
            ms = int(b[3])
            if int(m) < 60 and int(s) <60:
                updating1 = False
                backend.running = False
                backend.start_time = 0
                backend.elapsed = (3600*h + 60*m + s + ms/1000)
                time1.configure(text= f'{h:02d}:{m:02d}:{s:02d},{(ms // 10):02d}')
                beeped = False
                sleep(0.25)
                popup.destroy()
                if startbutton.cget('image') == pauseicon:
                    startbutton.configure(image=starticon)
            else:
                messagebox.showinfo(title='Wrong format',message='You entered number of minutes/seconds greater than 59.')
        except Exception as e:
            messagebox.showerror(title='Wrong format error',message='You entered letters or numbers in wrong format. \n' \
                                 'The correct format is XX:XX:XX:XXX')
            entry.delete(0, ctk.END)

    root_x = root.winfo_x()
    root_y = root.winfo_y()

    popup = ctk.CTkToplevel(root)
    popup.title('Set initial learning time')
    popup.geometry(f'387x140+{root_x+8}+{root_y+8}')
    popup.configure(fg_color='#1f1d1d')
    popup.attributes('-alpha', 0.95)
    popup.attributes('-topmost', True)


    poplabel = ctk.CTkLabel(master=popup,
                        text='Enter the initial learning time:\n[ Hours : Minutes : Seconds : Miliseconds ]',
                        text_color='white',
                        font=('Calibri',15, 'bold'),
                        fg_color='#1f1d1d'
                        )
    poplabel.pack(pady=(10,0))

    entry = ctk.CTkEntry(master=popup,
                    fg_color='#1f1d1d',
                    text_color='white',
                    font=('Britannic Bold', 20),
                    placeholder_text_color='red')
    entry.pack(pady=(10,10))

    submitbutton = ctk.CTkButton(master=popup,
                             text='Submit',
                             command=submit,
                             text_color='white',
                             hover_color='#0f0e0e',
                             font=('Calibri', 13),
                             fg_color='black')
    submitbutton.pack()


def setbreaktime():
    popmenu.destroy()
    def submitbreaktime():
        global time2, updating2
        try:
            initialbtime = entry2.get().split(':')
            h = int(initialbtime[0])
            m = int(initialbtime[1])
            s = int(initialbtime[2])
            ms = int(initialbtime[3])
            if int(m) < 60 and int(s) <60:
                updating2 = False
                backend.running2 = False
                backend.start_time2 = 0
                backend.elapsed2 = (3600*h + 60*m + s + ms/1000)
                time2.configure(text= f'{h:02d}:{m:02d}:{s:02d},{(ms // 10):02d}')
                if startbutton.cget('image') == pauseicon:
                    startbutton.configure(image=starticon)
                sleep(0.25)
                popup2.destroy()
            else:
                messagebox.showinfo(title='Wrong format',message='You entered number of minutes/seconds greater than 59.')
        except Exception as e:
            messagebox.showerror(title='Wrong format error',message='You entered letters or numbers in wrong format.')
            entry2.delete(0, ctk.END)

    root_x = root.winfo_x()
    root_y = root.winfo_y()

    popup2 = ctk.CTkToplevel(root)
    popup2.title('Set initial break time')
    popup2.geometry(f'387x140+{root_x+8}+{root_y+8}')
    popup2.attributes('-alpha', 0.95)
    popup2.attributes('-topmost', True)


    poplabel2 = ctk.CTkLabel(master=popup2,
                        text='Enter the initial break time:\n[ Hours : Minutes : Seconds : Miliseconds ]',
                        font=('Calibri',15, 'bold'),
                        fg_color='#1f1d1d',
                        text_color='white'
                        )
    poplabel2.pack(pady=(10,0))

    entry2 = ctk.CTkEntry(master=popup2,
                    fg_color='#1f1d1d',
                    text_color='white',
                    font=('Britannic Bold', 20),
                    placeholder_text_color='red')
    entry2.pack(pady=(10,10))

    submitbutton2 = ctk.CTkButton(master=popup2,
                             text='Submit',
                             command=submitbreaktime,
                             text_color='white',
                             hover_color='#0f0e0e',
                             font=('Calibri', 13),
                             fg_color='black')
    submitbutton2.pack()

def setlabels():
    def savelabelspressed():
        newlabel1 = setlabel1entry.get()
        if newlabel1 != '':
            label1.configure(text=newlabel1)

        newlabel2 = setlabel2entry.get()
        if newlabel2 != '':
            label2.configure(text=newlabel2)
            label3.configure(text=f'Single {newlabel2}')
            sleep(0.25)
        setlabelsmenu.destroy()
        

    def restorelabelspressed():
         label1.configure(text='Learning time')
         label2.configure(text='Break time')
         label3.configure(text='Single break time')
         sleep(0.25)
         setlabelsmenu.destroy()


    popmenu.destroy()

    root_x = root.winfo_x()
    root_y = root.winfo_y()

    setlabelsmenu = ctk.CTkToplevel(root)
    setlabelsmenu.title('Set label names')
    setlabelsmenu.attributes('-alpha', 0.95)
    setlabelsmenu.attributes('-topmost', True)
    setlabelsmenu.geometry(f'387x190+{root_x+8}+{root_y+8}')

    setlabel1 = ctk.CTkLabel(master=setlabelsmenu,
                             text='Enter main label name:',
                             font=('Calibri', 15, 'bold'),
                             text_color='white'

                             )
    setlabel1.pack(pady=(5,0))

    setlabel1entry = ctk.CTkEntry(master=setlabelsmenu,
                                  fg_color='#1f1d1d',
                                  text_color='white',
                                  font=('Britannic Bold', 20))
    setlabel1entry.pack(pady=(0,2))

    setlabel2 = ctk.CTkLabel(master=setlabelsmenu,
                             text='Enter second label name:',
                             font=('Calibri', 15, 'bold'),
                             text_color='white'

                             )
    setlabel2.pack(pady=(0,0))

    setlabel2entry = ctk.CTkEntry(master=setlabelsmenu,
                                  fg_color='#1f1d1d',
                                  text_color='white',
                                  font=('Britannic Bold', 20))
    setlabel2entry.pack(pady=(0,2))

    setlabelsavebutton = ctk.CTkButton(master=setlabelsmenu,
                                       text='Save',
                                       command=savelabelspressed,
                                       fg_color='black',
                                       hover_color='#0f0e0e',
                                       font=('Calibri', 13),
                                       text_color='white')
    setlabelsavebutton.pack(pady=(2,3))

    restorelabelsbutton = ctk.CTkButton(master=setlabelsmenu,
                                       text='Restore labels',
                                       command=restorelabelspressed,
                                       fg_color='black',
                                       hover_color='#0f0e0e',
                                       font=('Calibri', 13),
                                       text_color='white')
    restorelabelsbutton.pack(pady=(0,7))

def setgoal():

    def unitchosen(choice):
        global timegoal, accept
        timegoal = []
        if choice == 'Enter hours':
            timegoal.append('h')
        elif choice == 'Enter minutes':
            timegoal.append('m')
        accept = True

    def savegoalpressed():
        global timegoal, beeped, updprog, accept
        if accept == True:
            if len(timegoal) > 1:
                timegoal.pop(1)
            gorm = goalentry.get()
            if gorm.isdigit() and int(gorm) < 60:
                timegoal.append(gorm)
                goallabel.configure(text='changing goal in process...')
                # print(timegoal)
                updprog = True
                beeped = False
                update_progress()
                sleep(0.25)
                setgoalmenu.destroy()
            else:
                messagebox.showinfo(title='Not allowed entry type', message='You cannot enter any letters or special' \
                                    ' characters and numbers greater than 59.')
            accept = False
        else:
            messagebox.showinfo(title='Option not selected', message='You must choose an option.')

    def removegoalpressed():
        global timegoal, updprog
        timegoal = []
        progressbar.set(0)
        updprog = False
        goallabel.configure(text='No time goal')
        sleep(0.25)
        setgoalmenu.destroy()


    popmenu.destroy()

    root_x = root.winfo_x()
    root_y = root.winfo_y()

    setgoalmenu = ctk.CTkToplevel(root)
    setgoalmenu.title('Set a time goal')
    setgoalmenu.attributes('-alpha', 0.95)
    setgoalmenu.attributes('-topmost', True)
    setgoalmenu.geometry(f'387x170+{root_x+8}+{root_y+8}')

    setlabel1 = ctk.CTkLabel(master=setgoalmenu,
                             text='Enter a time goal:',
                             font=('Calibri', 15, 'bold'),
                             text_color='white'

                             )
    setlabel1.pack(pady=(5,0))

    choosegoalunit = ['Enter hours', 'Enter minutes']

    global goalmenu
    goalmenu = ctk.CTkOptionMenu(master=setgoalmenu,
                                      values=choosegoalunit,
                                      command=unitchosen,
                                      fg_color='black',
                                      button_color='black',
                                      button_hover_color='dark red',
                                      text_color='white'
                                    )
    goalmenu.pack()
    goalmenu.set('Choose option')

    goalentry = ctk.CTkEntry(master=setgoalmenu,
                              fg_color='#1f1d1d',
                              text_color='white',
                              font=('Britannic Bold', 20)
                              )
    goalentry.pack(pady=(5,5))

    goalsubmitbutton = ctk.CTkButton(master=setgoalmenu,
                                      text='Save',
                                      command=savegoalpressed,
                                      fg_color='black',
                                      hover_color='#0f0e0e',
                                      font=('Calibri', 13),
                                      text_color='white')
    goalsubmitbutton.pack(pady=(2,3))

    goalremovebutton = ctk.CTkButton(master=setgoalmenu,
                                      text='Remove time goal',
                                      command=removegoalpressed,
                                      fg_color='black',
                                      hover_color='#0f0e0e',
                                      font=('Calibri', 13),
                                      text_color='white')
    goalremovebutton.pack(pady=(2,5))



# MENU - WYGLĄD 
root = ctk.CTk()
root.title('Timer')
root.geometry('400x430')
root.attributes('-alpha', 0.85)
root.configure(fg_color='#181818')

root.wm_iconbitmap(resource_path('clock.ico'))

options = ctk.CTkButton(master=root,
                        text='Options', 
                        font=('Calibri', 15, 'bold'),
                        fg_color='transparent',
                        text_color='white',
                        width=25,
                        height=8,
                        hover_color='black',
                        command=menu_command)
options.place(x=0,y=0)


# FUNKCJE
def format_time(seconds):
    if seconds:
        h = int(seconds//3600)
        m = int((seconds % 3600) // 60)
        s = int(seconds % 60)
        ms = int((seconds*1000) - (int(seconds)*1000))
        return f'{h:02d}:{m:02d}:{s:02d},{(ms // 10):02d}'
    else:
        return '00:00:00,00'

def update_timer():
    global updating1
    if updating1:
        seconds = backend.get_time()
        formatted = format_time(seconds)
        time1.configure(text=formatted)
        root.after(50, update_timer)

def when_clicked():
    global updprog
    if startbutton.cget('image') == starticon:
        startbutton.configure(image=pauseicon)
        updprog = True
        update_progress()
    else:
        startbutton.configure(image=starticon)
        updprog = False
    global updating1
    updating1 = True
    result = backend.start_stop()
    update_timer()

def reset_timer():
    startbutton.configure(image=starticon)
    resetbutton.configure(image=stopiconL)
    root.after(200, resetbuttonconfigure)
    global updating1
    updating1 = False
    backend.running = False
    backend.start_time = 0
    backend.elapsed = 0 
    time1.configure(text='00:00:00,00')

def resetbuttonconfigure():
    resetbutton.configure(image=stopicon)

def resetbuttonconfigure2():
    resetbutton2.configure(image=stopicon)

def update_timer2():
    if updating2:
        seconds = backend.get_time2()
        formatted = format_time(seconds)
        time2.configure(text=formatted)
        root.after(50, update_timer2)

def when_clicked2():
    if startbutton2.cget('image') == starticon:
        startbutton2.configure(image=pauseicon)
    else:
        startbutton2.configure(image=starticon)
    global updating2
    updating2 = True
    result = backend.start_stop2()
    update_timer2()
    update_timer3()

def update_timer3():
    seconds = backend.get_time3()
    formatted = format_time(seconds)
    time3.configure(text=formatted)
    root.after(50, update_timer3)

def reset_timer23():
    startbutton2.configure(image=starticon)
    resetbutton2.configure(image=stopiconL)
    root.after(200, resetbuttonconfigure2)
    global updating2
    updating2 = False
    backend.running2 = False
    backend.elapsed2 = 0
    backend.start_time2 = 0
    time2.configure(text='00:00:00,00')
    time3.configure(text='00:00:00,00')




# NAPIS 1 - LEARNING TIME
label1 = ctk.CTkLabel(master=root,
                    text='Learning time',
                    font=('Britannic Bold', 20),
                    text_color='white',
                    fg_color='transparent',)
label1.pack(pady=(30,0))

# CZAS 1
time1 = ctk.CTkLabel(master=root,
                    text='00:00:00,00',
                    font=('Britannic Bold', 60),
                    text_color='#fffec4',
                    fg_color='transparent')
time1.pack()

# PASEK CELU 1
progressbar = ctk.CTkProgressBar(root, width=200)
progressbar.pack(pady=(15,0))
progressbar.set(0)
progressbar.configure(progress_color='dark red')

def update_progress():
    fromlabel = time1.cget('text')
    seconds = int(fromlabel[0:2])*3600 + int(fromlabel[3:5])*60 + int(fromlabel[6:8])
    if backend.running:
        global beeped
        try:
            if timegoal[0] == 'h':
                goalseconds = int(timegoal[1])*3600
                goallabel.configure(text=f'{timegoal[1]}h')
            elif timegoal[0] == 'm':
                goalseconds = int(timegoal[1])*60
                goallabel.configure(text=f'{timegoal[1]}min')
            progr = seconds / goalseconds
            if progr <= 1:
                progressbar.set(progr)
                # print('aktualizacja paska')
            else:
                progressbar.set(1)
                if not beeped:
                    winsound.Beep(1000,500)
                    beeped = True
        except IndexError:
            # print('indexerror')
            pass
    else:
        # print('not running')
        pass
    
    if updprog:
        root.after(5000, update_progress)

# update_progress()

#NAPIS 0 - CEL

goallabel = ctk.CTkLabel(master=root,
                         text='1h',
                         text_color='white',
                         font=('Calibri', 12),
                         fg_color='transparent')
goallabel.pack(pady=(0,0))

# PRZYCISK 1 - START LEARNING TIME

image_path = resource_path("play.png")
original_image = Image.open(image_path)
resized_image = original_image.resize((40, 40), Image.Resampling.LANCZOS)
starticon = CTkImage(light_image=resized_image, dark_image=resized_image, size=(40, 40))

image_path1 = resource_path("pause.png")
original_image1 = Image.open(image_path1)
resized_image1 = original_image1.resize((40, 40), Image.Resampling.LANCZOS)
pauseicon = CTkImage(light_image=resized_image1, dark_image=resized_image1, size=(38, 38))




startbutton = ctk.CTkButton(master=root,
                        image=starticon,
                        border_width=0,
                        fg_color='transparent',
                        hover_color='#1f1d1d',
                        text='',
                        command=when_clicked,
                        width=35,
                        height=35)
startbutton.place(x=144, y=175)


# PRZYCISK 1.2 - STOP LEARNING TIME

image_path = resource_path("stop.png")
original_image = Image.open(image_path)
resized_image = original_image.resize((40, 40), Image.Resampling.LANCZOS)
stopicon = CTkImage(light_image=resized_image, dark_image=resized_image, size=(40, 40))

image_path4 = resource_path("stopl.png")
original_image4 = Image.open(image_path4)
resized_image4 = original_image4.resize((40, 40), Image.Resampling.LANCZOS)
stopiconL = CTkImage(light_image=resized_image4, dark_image=resized_image4, size=(40, 40))


resetbutton = ctk.CTkButton(master=root,
                        image=stopicon,
                        border_width=0,
                        fg_color='transparent',
                        hover_color='#1f1d1d',
                        text='',
                        command=reset_timer,
                        width=35,
                        height=35
                        )
resetbutton.place(x=199, y=175)





# NAPIS 2 - BREAK TIME
label2 = ctk.CTkLabel(master=root,
                    text='Break time',
                    font=('Britannic Bold', 15),
                    text_color='white',
                    fg_color='transparent'
                    )
label2.pack(pady=(50,0))

# CZAS 2
time2 = ctk.CTkLabel(master=root,
                    text='00:00:00,00',
                    font=('Britannic Bold', 40),
                    text_color='#fffec4',
                    fg_color='transparent')
time2.pack()


# PRZYCISK 2 - START BREAK TIME

startbutton2 = ctk.CTkButton(root,
                        image=starticon,
                        border_width=0,
                        fg_color='transparent',
                        hover_color='#1f1d1d',
                        text='',
                        command=when_clicked2,
                        width=35,
                        height=35)
startbutton2.place(x=144, y=300)

# PRZYCISK 2.2 - STOP BREAK TIME

resetbutton2 = ctk.CTkButton(master=root,
                        image=stopicon,
                        border_width=0,
                        fg_color='transparent',
                        hover_color='#1f1d1d',
                        text='',
                        command=reset_timer23,
                        width=35,
                        height=35
                        )
resetbutton2.place(x=199, y=300)





# NAPIS 3 - SINGLE BREAK TIME
label3 = ctk.CTkLabel(master=root,
                    text='Single break time',
                    font=('Britannic Bold', 15),
                    text_color='white',
                    fg_color='transparent',
                    )
label3.pack(pady=(48,0))

# CZAS 3
time3 = ctk.CTkLabel(master=root,
                    text='00:00:00,00',
                    font=('Britannic Bold', 40),
                    text_color='#fffec4',
                    fg_color='transparent')
time3.pack()


def menu_notif():


    def notifselected(choice):
        global choice2, notifset
        if not notifset:
            if choice == 'Enter hours':
                choice2 = 'hour'
                
            elif choice == 'Enter minutes':
                choice2 = 'minute'
        else:
            messagebox.showinfo(title='Information', message='You cannot set more than one notification. ' \
                                'Remove already set notification in order to set another.')
            notifmenu.destroy()

    def notifsubmitpressed():
        global check_time_run
        check_time_run = ''
        notifnumber = notifentry.get()
        if notifnumber.isdigit() and int(notifnumber) < 60:
            global choice2
            if choice2 == 'hour' or choice2 == 'minute':
                messagebox.showinfo(title='Notification successfully set', message=f'You will receive notification after every {notifnumber} {choice2}(s) passed.')
                notifmenu.destroy()
            else:
                messagebox.showinfo(title='Option not selected', message='You must choose an option.')

            def check_time():
                global check_time_run
                if check_time_run == 'STOP':
                    return 0
                global choice2
                if choice2 == 'hour' or choice2 == 'minute':
                    curtime = time1.cget('text')
                    hours = int(curtime[0:2])
                    minutes = int(curtime[3:5])
                    if choice2 == 'hour' and hours != 0 and hours % int(notifnumber) == 0 and curtime[3:7] == '00:0':
                        notification.notify(title='Time passed',
                                            message=f' Another {notifnumber} {choice2}(s) passed!',
                                            timeout=5)
                        
                    elif choice2 == 'minute' and minutes != 0 and minutes % int(notifnumber) == 0 and curtime[6] =='0':
                        notification.notify(title='Time passed',
                                            message=f'Another {notifnumber} {choice2}(s) passed!',
                                            timeout=5)
                    
                    root.after(9000, check_time)
                    # print('checking again')
            if choice2 == 'hour' or choice2 == 'minute':
                check_time()
                global notifset
                notifset = True
        else: 
            messagebox.showinfo(title='Not allowed entry type', message='You cannot enter any letters or special' \
                                ' characters and numbers greater than 59.')
            
    def notifremovepressed():
        global notifset, check_time_run
        notifset = False
        check_time_run = 'STOP'
        messagebox.showinfo(title='Notification successfully removed', message=f'You will no longer receive notifications.')



    root_x = root.winfo_x()
    root_y = root.winfo_y()

    global notifmenu
    notifmenu = ctk.CTkToplevel(root)
    notifmenu.title('Notification settings')
    notifmenu.configure(fg_color='#1f1d1d')
    notifmenu.attributes('-alpha' , 0.95)
    notifmenu.attributes('-topmost', True)
    notifmenu.geometry(f'+{root_x+8}+{root_y+8}')

    notiflabel = ctk.CTkLabel(master=notifmenu,
                              text=' Enter the period after which the notification should be sent. ',
                              text_color='white',
                              font=('Calibri',15, 'bold'),
                              fg_color='#1f1d1d'
                              )
    notiflabel.pack(pady=(10,10))

    notiflist = ['Enter hours', 'Enter minutes']

    global notifoptionsmenu
    notifoptionsmenu = ctk.CTkOptionMenu(master=notifmenu,
                                      values=notiflist,
                                      command=notifselected,
                                      fg_color='black',
                                      button_color='black',
                                      button_hover_color='dark red',
                                      text_color='white'
                                    )
    notifoptionsmenu.pack()
    notifoptionsmenu.set('Choose option')

    notifentry = ctk.CTkEntry(master=notifmenu,
                              fg_color='#1f1d1d',
                              text_color='white',
                              font=('Britannic Bold', 20)
                              )
    notifentry.pack(pady=(5,5))

    notifsubmitbutton = ctk.CTkButton(master=notifmenu,
                                      text='Submit',
                                      command=notifsubmitpressed,
                                      fg_color='black',
                                      hover_color='#0f0e0e',
                                      font=('Calibri', 13),
                                      text_color='white')
    notifsubmitbutton.pack(pady=(2,5))


    notifremovebutton = ctk.CTkButton(master=notifmenu,
                                      text='Remove notification',
                                      command=notifremovepressed,
                                      fg_color='black',
                                      hover_color='#0f0e0e',
                                      font=('Calibri', 13),
                                      text_color='white')
    notifremovebutton.pack(pady=(0,5))




notif = ctk.CTkButton(master=root,
                        text='Notifications', 
                        font=('Calibri', 15, 'bold'),
                        fg_color='transparent',
                        text_color='white',
                        width=25,
                        height=8,
                        hover_color='black',
                        command=menu_notif)
notif.place(x=60,y=0)

root.mainloop()