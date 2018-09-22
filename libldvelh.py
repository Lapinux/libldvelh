"""A Library for Text adventure games"""
from Tix import *
from ttk import *
import csv
import pydoc
import os
#Please don't modify the dependencies!

#INSTALL INSTRUCTION (if you have just that file):
#To install the library, make a folder named scenes and another named setting in the directory of the .py.
#Then, make that var true. Start the script, close the shell and make that var back to false.
INSTALL = False
#If you already have the folders and files inside, then you SHOULD NOT MODIFY THAT VAR!!!


#'''Vars for customizing the library'''!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

#Enable Debug
DEBUG = 0

#start menu when starting the library
menuu = False

#start from last save
play = True

#Enable game developing mode
create = False

#Delete the save when gameover
strongameover = False
#'''End of the vars for customizing the library'''!!!!!!!!!!!!!!!!!!!!!!!!!!!!!


#Please don't modify!!!
class Settings:
    """The class with all the settings"""
    #define every settings
    title = "Zombie game"
    description = "A basical Text Adventure game with zombies"
    h = 220
    w = 650
    gameover_message = "You are dead."
    gameover_title = "You are dead."
    youwon_message = "Wow! You beaten the game!"
    youwon_title = "You Won!"
def settingret():
    """Returns the settings"""
    print(Settings.title)
    print(Settings.description)
    print(Settings.h)
    print(Settings.w)
    print(Settings.gameover_message)
    print(Settings.gameover_title)
    print(Settings.youwon_title)
    print(Settings.youwon_message)
def settingwizard():
        """Wizard for setting-up all vars."""
        #function for setting-up everything
        global title
        global description
        global gameover_message
        global w
        global h
        global gameover_title
        global youwon_message
        global youwon_title
        print "Welcome to the Set up wizard for libldvelh!"
        Settings.title = raw_input("What should be the name of your game?")
        Settings.description = raw_input("Give a short description that should be displayed on the menu.")
        Settings.gameover_message = raw_input("What gameover message must be displayed when you die?")
        Settings.gameover_title = raw_input("What should be the title of your gameover Window?")
        Settings.youwon_message = raw_input("What should be the message of the 'You Won' dialog?")
        Settings.youwon_title = raw_input("What should be the name of the 'You Won' Window?")
        temp = raw_input("Would you add width or height to the current width or height? y/n (for default press n)")
        if(temp == "yes" or temp == "y" or temp == "YES" or temp == "Y"):
            try:
                Settings.h = int(raw_input("Set new height (min 220 default 220)."))
                Settings.w = int(raw_input("Set new width (min 650 default 650)."))
            except:
                print "you didn't entered a valid number"
        else: print("Ok. I don't change anything.")
        del temp
        savesettings()
        return("End of the wizard. Thank you!")
def savesettings():
    """Save all actual settings in a file."""
    if(Settings.h < 220):
        Settings.h = 220
    if(Settings.w < 650):
        Settings.w = 650
    with open('setting/settings.dat', 'w') as setting:
        fieldnames = ['setting']
        writer = csv.DictWriter(setting, fieldnames=fieldnames)

        writer.writeheader()
        writer.writerow({'setting': Settings.title})
        writer.writerow({'setting': Settings.description})
        writer.writerow({'setting': Settings.h})
        writer.writerow({'setting': Settings.w})
        writer.writerow({'setting': Settings.gameover_message})
        writer.writerow({'setting': Settings.gameover_title})
        writer.writerow({'setting': Settings.youwon_message})
        writer.writerow({'setting': Settings.youwon_title})
def loadsettings():
    """Load all settings that have been saved by savesetting()"""
    with open('setting/settings.dat') as setting:
        reader = csv.DictReader(setting)
        temp = list()
        for row in reader:
            temp.append(row['setting'])
        Settings.title = str(temp[0])
        Settings.description = str(temp[1])
        Settings.h = temp[2]
        Settings.w = temp[3]
        Settings.gameover_message = str(temp[4])
        Settings.gameover_title = str(temp[5])
        Settings.youwon_message = str(temp[6])
        Settings.youwon_title = str(temp[7])
        if(Settings.h < 220):
            Settings.h = 220
        if(Settings.w < 650):
            Settings.w = 650
def menu():
    """Default start function with menu"""
    #minimal height and weight to avoid break
    if(Settings.h < 220):
        Settings.h = 220
    if(Settings.w < 650):
        Settings.w = 650
    #command definition for buttons
    def sav():
        try:
            f = open("data.sav","r")
            savv = int(f.read())
            f.close()
            root.destroy()
            loadscene(savv)
        except:
            print("You don't have any save!")
    def startt():
        root.destroy()
        loadscene(1)
    #gui configuration
    root = Tk()
    root.title(str(Settings.title))

    mainframe = Frame(root, height = int(Settings.h), width = int(Settings.w))
    mainframe.pack_propagate(0)
    mainframe.pack(padx = 5, pady = 5)

    intro = Label(mainframe, text = "Welcome to "+str(Settings.title)+", the text adventure where YOU decide almost everything.")
    intro.pack(side = TOP)

    start = Button(mainframe, text = "Start!", command = startt)
    start.pack(side = RIGHT)

    sav = Button(mainframe, text = "Return to savepoint", command = sav)
    sav.pack(side = RIGHT)

    QUIT = Button(mainframe, text = "QUIT", command = root.destroy)
    QUIT.pack(side = LEFT)

    descript = Label(mainframe, text = str(Settings.description))
    descript.pack(side = BOTTOM)

    cop = Label(mainframe, text = "Game Engine copyright by Lapinux, all right reserved.")
    cop.pack()

    #start gui
    root.mainloop()

def loadscene(scenenumber):
    """Function for starting any scene."""
    if(scenenumber == "death"):
        gameover()
        return("death...")
    if(scenenumber == "death"):
        Youwon()
        return("Yeah!")
    with open('scenes/scene'+str(scenenumber)+'.csv') as csvfile:
        reader = csv.DictReader(csvfile)
        scene = list()
        for row in reader:
            scene.append(row['scene'])
            if(DEBUG):
                print(row['scene'])
    choices = int(scene[1])
    labelll = str(scene[0])
    #minimal height and weight to avoid break
    if(Settings.h < 220):
        Settings.h = 220
    if(Settings.w < 650):
        Settings.w = 650
    #define gui
    def one():
        root.destroy()
        loadscene(scene[3])
    def two():
        root.destroy()
        loadscene(scene[5])
    def three():
        root.destroy()
        loadscene(scene[7])
    def savq():
        root.destroy()
        f = open("data.sav","w")
        f.write(str(scenenumber))
        f.close()
        return("Saved!")
    if(choices == 0):
        return("Choices can't be 0!")
    if(choices == 1):
        #programm 1 question
        root = Tk()
        root.title(str(Settings.title))
        
        mainframe = Frame(root, height = int(Settings.h), width = int(Settings.w))
        mainframe.pack_propagate(0)
        mainframe.pack(padx = 5, pady = 5)

        text = Label(mainframe, text = labelll)
        text.pack(side = TOP)

        btq = Button(mainframe, text = "Save and quit.", command = savq)
        btq.pack(side = RIGHT)

        bt = Button(mainframe, text = scene[2], command = one)
        bt.pack(side = BOTTOM)
    elif(choices == 2 and scene[4] != 0):
        if(scene[4] == 0):
            return("Define question2!")
        #programm 2 questions
        root = Tk()
        root.title(str(Settings.title))
        
        mainframe = Frame(root, height = 220, width = 650)
        mainframe.pack_propagate(0)
        mainframe.pack(padx = 5, pady = 5)

        text = Label(mainframe, text = labelll)
        text.pack(side = TOP)
        
        btq = Button(mainframe, text = "Save and quit.", command = savq)
        btq.pack(side = RIGHT)

        bt1 = Button(mainframe, text = scene[2], command = one)
        bt1.pack(side = BOTTOM)

        bt2 = Button(mainframe, text = scene[4], command = two)
        bt2.pack(side = BOTTOM)
        
    elif(choices == 3 and scene[4] != 0 and scene[6] != 0):
        #programm 3 questions
        if(scene[4] != 0 or scene[6] != 0):
            return("Define question2 or define question3!")
        root = Tk()
        root.title(str(Settings.title))
        
        mainframe = Frame(root, height = 220, width = 650)
        mainframe.pack_propagate(0)
        mainframe.pack(padx = 5, pady = 5)

        text = Label(mainframe, text = labelll)
        text.pack(side = TOP)

        btq = Button(mainframe, text = "Save and quit.", command = savq)
        btq.pack(side = RIGHT)

        bt1 = Button(mainframe, text = scene[2], command = one)
        bt1.pack(side = BOTTOM)
        
        bt2 = Button(mainframe, text = scene[4], command = two)
        bt2.pack(side = BOTTOM)

        bt3 = Button(mainframe, text = scene[6], command = three)
        bt3.pack(side = BOTTOM)
    else:
        return("Not a valid number of question/choices.")
    root.mainloop()
def createscene(scenenumber):
    """Wizard for creating a new scene for your project"""
    print("Hello! Let's create a new scene!")
    temp = 0
    num = scenenumber
    labell = raw_input("What should be the label/text/story?")
    while(temp != 1):
        try:
            questions = int(raw_input("How many questions?(1-3)"))
        except:
            print("Enter a valid number!")
        if(questions == 0):
            print("Choices can't be 0!")
        elif(questions > 3):
            print("Choices must be 3 or smaller")
        else:
            print("Valid number.")
            temp = 1
    root = Tk()
    root.title(str(Settings.title))

    mainframe = Frame(root, height = 220, width = 650)
    mainframe.pack_propagate(0)
    mainframe.pack(padx = 5, pady = 5)

    text = Label(mainframe, text = labell)
    text.pack(side = TOP)

    temp = 0
    while(temp != 1):
        temp = 1
        try:
            bt1txt = str(raw_input("Text for button 1?"))
            bt1command = int(raw_input("Wich scene number must be loaded by Button 1?"))
        except:
            print("Not a valid value.")
            temp = 0
    del temp

    bt1 = Button(mainframe, text = bt1txt)
    bt1.pack(side = BOTTOM)

    if(questions > 1):
        temp = 0
        while(temp != 1):
            temp = 1
            try:
                bt2txt = str(raw_input("Text for button 2?"))
                bt2command = int(raw_input("Wich scene must be loaded by Button 2?"))
            except:
                print("Not a valid value.")
                temp = 0
        del temp
        
        bt2 = Button(mainframe, text = bt1txt)
        bt2.pack(side = BOTTOM)
        
        if(questions == 3):
            temp = 0
            while(temp != 1):
                temp = 1
                try:
                    bt3txt = str(raw_input("Text for button 3?"))
                    bt3command = int(raw_input("Wich scene must be loaded by Button 3?"))
                except:
                    print("Not a valid value.")
                    temp = 0
            del temp
            
            bt3 = Button(mainframe, text = bt3txt)
            bt3.pack(side = BOTTOM)
        else:
            bt3txt = 0
            bt3command = 0
    else:
        bt2txt = 0
        bt2command = 0
        bt3txt = 0
        bt3command = 0
    temp = raw_input("Now, I will display the result. (!!!The buttons aren't working in preview mode!!!)")
    del temp
    root.mainloop()
    temp = raw_input("Should I save it? (y/n) (default=y)")
    if(temp == "yes" or temp == "YES" or temp == "y" or temp == "Y" or temp == "Yes"):
        try:
            with open('scenes/scene'+str(num)+'.csv', 'w') as scene:
                fieldnames = ['scene']
                writer = csv.DictWriter(scene, fieldnames=fieldnames)

                writer.writeheader()
                writer.writerow({'scene': labell})
                writer.writerow({'scene': questions})
                writer.writerow({'scene': bt1txt})
                writer.writerow({'scene': bt1command})
                writer.writerow({'scene': bt2txt})
                writer.writerow({'scene': bt2command})
                writer.writerow({'scene': bt3txt})
                writer.writerow({'scene': bt3command})
            print("File writen successfull!")
        except:
            return("Error writing File.")
    else:
        return("Aborted.")
    del temp
    return("End of the wizard.")
def Youwon():
    def bt():
        root.destroy()
        menu()
    root = Tk()
    root.title(str(Settings.youwon_title))

    mainframe = Frame(root, height = 100, width = 250)
    mainframe.pack_propagate(0)
    mainframe.pack(padx = 5, pady = 5)

    labell = Label(mainframe, text = Settings.youwon_message)
    labell.pack(side = TOP)

    bt1 = Button(mainframe, text = "Return to menu", command = bt)
    bt1.pack(side = BOTTOM)

    root.mainloop()
def gameover():
    def bt():
        global strongameover
        if(strongameover):
            os.remove("data.sav")
        root.destroy()
        menu()
    root = Tk()
    root.title(str(Settings.gameover_title))

    mainframe = Frame(root, height = 100, width = 250)
    mainframe.pack_propagate(0)
    mainframe.pack(padx = 5, pady = 5)

    labell = Label(mainframe, text = Settings.gameover_message)
    labell.pack(side = TOP)

    bt1 = Button(mainframe, text = "Return to menu", command = bt)
    bt1.pack(side = BOTTOM)

    root.mainloop()

try:
    loadsettings()
except:
    savesettings()
if(INSTALL):
    try:
        f = open("scenes/scene1","r")
        f.close
    except:
        f = open("scenes/scene1.csv", "w")
        f.close()
        with open('scenes/scene1.csv', 'w') as scene:
            fieldnames = ['scene']
            writer = csv.DictWriter(scene, fieldnames=fieldnames)

            writer.writeheader()
            writer.writerow({'scene': 'You walk in the woods. Suddely, you see a zombie.'})
            writer.writerow({'scene': '2'})
            writer.writerow({'scene': 'Bye, zombie!'})
            writer.writerow({'scene': '4'})
            writer.writerow({'scene': 'I wanna die.'})
            writer.writerow({'scene': '5'})
            writer.writerow({'scene': '0'})
            writer.writerow({'scene': '0'})
            
    try:
        f = open("scenes/scene2","r")
        f.close
    except:
        f = open("scenes/scene2.csv", "w")
        f.close()
        with open('scenes/scene2.csv', 'w') as scene:
            fieldnames = ['scene']
            writer = csv.DictWriter(scene, fieldnames=fieldnames)

            writer.writeheader()
            writer.writerow({'scene': 'You walk in the city. Suddely, you see a zombie.'})
            writer.writerow({'scene': '2'})
            writer.writerow({'scene': 'Bye, zombie!'})
            writer.writerow({'scene': '4'})
            writer.writerow({'scene': 'I wanna die.'})
            writer.writerow({'scene': '5'})
            writer.writerow({'scene': '0'})
            writer.writerow({'scene': '0'})

    try:
        f = open("scenes/scene3","r")
        f.close
    except:
        f = open('scenes/scene3.csv', "w")
        f.close() 
        with open('scenes/scene3.csv', 'w') as scene:
            fieldnames = ['scene']
            writer = csv.DictWriter(scene, fieldnames=fieldnames)

            writer.writeheader()
            writer.writerow({'scene': 'You swim in the lake. Suddely, you see a zombie.'})
            writer.writerow({'scene': '2'})
            writer.writerow({'scene': 'Bye, zombie!'})
            writer.writerow({'scene': '4'})
            writer.writerow({'scene': 'I wanna die.'})
            writer.writerow({'scene': '5'})
            writer.writerow({'scene': '0'})
            writer.writerow({'scene': '0'})
    settingswizard()
            
if(DEBUG):
    settingret()
if(create):
    i = False
    caca = False
    while(i == False):
        try:
            x = int(raw_input("Wich scene number?"))
            caca = True
        except:
            print("Enter an integer!")
            caca = False
        if(caca):
            createscene(x)
            prompt = str(raw_input("do you want to continue creating scenes? (y/n) (default = y)"))
            if(prompt == "yes" or prompt == "YES" or prompt == "y" or prompt == "Y" or prompt == "Yes"):
                i = False
            else:
                i = True      
if(play):
    try:
        f = open("data.sav","r")
        savv = int(f.read())
        f.close()
        loadscene(savv)
    except:
        print("You don't have any save!")
if(menuu):
    menu()
