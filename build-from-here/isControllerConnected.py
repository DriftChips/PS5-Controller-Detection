import usb.core
import usb.util
import usb.backend.libusb1
import tkinter as tk
from tkinter import *
import tkinter.messagebox as tkmb
import customtkinter
from PIL import ImageTk, Image
from pystray import MenuItem as item
import pystray
import sys
import os


from win32api import (GetModuleFileName, RegCloseKey, RegDeleteValue,
                    RegOpenKeyEx, RegSetValueEx, RegEnumValue)
from win32con import (HKEY_LOCAL_MACHINE, HKEY_CURRENT_USER, KEY_WRITE,
                    KEY_QUERY_VALUE, REG_SZ)
from winerror import ERROR_NO_MORE_ITEMS
import pywintypes

'''
def run_at_startup_set(appname, path=None, user=False):
    """
    Store the entry in the registry for running the application
    at startup.
    """
    # Open the registry key where applications that run
    # at startup are stored.
    key = RegOpenKeyEx(
        HKEY_CURRENT_USER if user else HKEY_LOCAL_MACHINE,
        STARTUP_KEY_PATH,
        0,
        KEY_WRITE | KEY_QUERY_VALUE
    )
    # Make sure our application is not already in the registry.
    i = 0
    while True:
        try:
            name, _, _ = RegEnumValue(key, i)
        except pywintypes.error as e:
            if e.winerror == ERROR_NO_MORE_ITEMS:
                break
            else:
                raise
        if name == appname:
            RegCloseKey(key)
            return
        i += 1
    # Create a new entry or key.
    RegSetValueEx(key, appname, 0, REG_SZ, path or GetModuleFileName(0))
    # Close the key when no longer used.
    RegCloseKey(key)


run_at_startup_set("isControllerConnected", user=True)
'''


#Setting the window settings
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("green")  # Themes: blue (default), dark-blue, green
window = customtkinter.CTk()
window.title("Controller Detection")
window.geometry("500x400")
#windowIcon = PhotoImage(file = "controllerIcon.png")
#window.iconphoto(False, windowIcon)


isConnected = None

#Function for checking for the controller
def checkForController():

    #Locate the controller device
    dev1 = usb.core.find(idVendor=1356,idProduct=3302)

    #If device is not found, print to console and change the icon to the red_light, else do the opposite
    if dev1 is None:
        print("Device is Disconnected")
        label.configure(text = "Device is Disconnected")
        redLightImage = customtkinter.CTkImage(Image.open(resource_path("Red_Light.png")), size=(100,173))
        imgLabel.configure(image=redLightImage)
        imgLabel.image=redLightImage
        isNotConnectedFunc()


    else:
        print("Device connected")
        label.configure(text = "Device Connected")
        greenLightImage = customtkinter.CTkImage(Image.open(resource_path("Green_Light.png")), size=(100,173))
        imgLabel.configure(image=greenLightImage)
        imgLabel.image=greenLightImage
        isConnected == True
        isConnected
        isConnectedFunc()

    window.after(1000, checkForController)

#Booleans that change the status to True or False depending whether the device is connected and then changes the tray icon accordingly
def isConnectedFunc():
    if isConnected == True:
        pass
    else:
        isConnected == True
        changeIconGreen()
        return

def isNotConnectedFunc():
    if isConnected == False:
        pass
    else:
        isConnected == False
        changeIconRed()
        return

def changeIconRed():
    icon.icon = Image.open(resource_path("controllerIconRed.ico"))

def changeIconGreen():
    icon.icon = Image.open(resource_path("controllerIconGreen.ico"))


#Define the resource path where all images are kept
def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

def quitApplication():
    icon.stop()
    window.quit()


#Locating and creating the image labels for the light system
redLightImage = customtkinter.CTkImage(Image.open(resource_path("Red_Light.png")), size=(100,173))
greenLightImage = customtkinter.CTkImage(Image.open(resource_path("Green_Light.png")), size=(173,173))
imgLabel = customtkinter.CTkLabel(master=window,image = redLightImage, text="",width=120,height=200)
imgLabel.pack(pady=5)


#Simple Label to hold text
label = customtkinter.CTkLabel(window, text="Click the Button to start the controller check")
label.pack(pady=20)
#Button to Start the function
btn1 = customtkinter.CTkButton(window, text="Start", command=checkForController)
btn1.pack(pady=20)
#Quit Button
quitBtn = customtkinter.CTkButton(window, text="Quit & Stop Application", command=quitApplication)
quitBtn.pack(pady=10)


''' 
<-------------------------------------------------------------------------------->
#Function for testing
def testFunction():
    if isConnected == True:
        print("isConnected == True")
    elif isConnected == False:
        print("isConnected == True")
'''

'''
#Test button
testBtn = customtkinter.CTkButton(window, text="Test Button", command=testFunction)
testBtn.pack(pady=20)
<-------------------------------------------------------------------------------->
'''

#Functions for quiting, minimising, and showing the tray icon
def quitWindow(icon, item):
    icon.stop()
    window.quit()

def showWindow(icon, item):
    window.after(0, window.deiconify)

def withdraw_window():  
    window.withdraw()


#Initiation of the tray icon
image = Image.open(resource_path("controllerIconDesktop.ico"))
menu = (item('Quit', quitWindow), item('Open', showWindow))
icon = pystray.Icon("name", image, "title", menu)
icon.run_detached()
window.protocol('WM_DELETE_WINDOW', withdraw_window)

window.mainloop()



