#importing
import tkinter
from tkinter import filedialog
import customtkinter
from PIL import Image
from mss import mss

#Creates the window with the right settings.
customtkinter.set_appearance_mode("dark")       # Modes: system (default), light, dark
customtkinter.set_default_color_theme("blue")   # Themes: blue (default), dark-blue, green

root_tk = customtkinter.CTk()       # create CTk window
root_tk.geometry("400x480")         #The Window Size
root_tk.title("Simple screenshot")  #The window title

#Variables:

screensetting = -1          #This variable holds if the app should make a screenhot of all screens or only the main screen. (-1 is all screens | 0 is only the main screen.)
screenshotamount = 0        #This variable holds the amount of screenshots the user has made.

#Definitions:

def take_screenshot(): #This definitions occurs when the user presses the "Take screenshot!" button.
    global screenshotamount                     #Get the variable into the definition

    path = filedialog.asksaveasfilename()       #Asks the user to select where to save the file.

    if(path!=""): #checks if user has selected a path.
        with mss() as sct:
            root_tk.iconify()                                                                      #Removes window from screen, preventing the app is in the screenshot

            filename = sct.shot(mon=screensetting, output=path+".jpg")                             #Take the screenshot
            
            screenshotamount += 1                                                                  #Adds one to the screenshot variable.
            screenshot_label.configure(text="Screeshot is saved (" + str(screenshotamount) + "x)") #Updates the text label
            root_tk.deiconify()                                                                    #Makes it so the window reappears

def checkbox_event(): #This definitions occurs when user presses the "Take screenshot of all screens?" checkbox
    global screensetting         #Get the variable into the definition

    if(check_var.get() == "on"): #Checks if the checkbox is on or off
        screensetting = -1       #Changes the variable so it makes a screenshot of both screens
    else:
        screensetting = 0        #Changes the variable so it makes a screenshot of both screens

# Create buttons, checkbox, frame and images

banner_img = customtkinter.CTkImage(Image.open("Simplebanner.png"), size=(375, 200))
banner_label = customtkinter.CTkLabel(master=root_tk, text="", image = banner_img)
banner_label.place(relx=0.5, rely=0.25, anchor=tkinter.CENTER)

screenshot_button = customtkinter.CTkButton(master=root_tk, text="Take screenshot!", command=take_screenshot)
screenshot_button.place(relx=0.5, rely=0.7, anchor=tkinter.CENTER)

screenshot_label = customtkinter.CTkLabel(master=root_tk, text="")
screenshot_label.place(relx=0.5, rely=0.8, anchor=tkinter.CENTER)

check_var = tkinter.StringVar(value="on")

checkbox = customtkinter.CTkCheckBox(master=root_tk, text="Take screenshot of all screens?", command=checkbox_event,
                                     variable=check_var, onvalue="on", offvalue="off")
checkbox.place(relx=0.5, rely=0.575, anchor=tkinter.CENTER)

frame = customtkinter.CTkFrame(master=root_tk, width=200, height=200)

root_tk.mainloop()