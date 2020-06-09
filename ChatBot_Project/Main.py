# Bot PMB
import os

import aiml

# from tkinter import *
#
# # Create the GUI
# # Create tkinter object (represent the parent window)
# root = Tk()
#
# # Give the window a title
# root.title("PMB UKDW")
#
# # Give the window some dimensions
# root.geometry("500x500")
#
# # Create the menu bar
# main_menu = Menu(root)
#
# # Create the sub menu
# file_menu = Menu(root)
# file_menu.add_command(label="New")
# file_menu.add_command(label="Save As")
# file_menu.add_command(label="Exit")
#
# main_menu.add_cascade(label="File", menu=file_menu)
# root.config(menu=main_menu)
#
# # Create the chat area
# chatWindow = Text(root, bd=1, bg="black", width=50, height=8)
# chatWindow.place(x=6, y=6, height=385, width=475)
#
# # Create the message window
# messageWindow = Text(root, bg="black", width=30, height=4)
# messageWindow.place(x=6, y=400, height=88, width=400)
#
# # Create the button to send the message
# Button = Button(root, text="Send", bg="blue", activebackground="lightblue", width=12, height=5, font=("Arial", 12))
# Button.place(x=420, y=440, height=50, width=60)
#
# # Add the scroll bar
# scrollbar = Scrollbar(root, command=chatWindow.yview())
# scrollbar.place(x=475, y=5, height=385)
#
# root.mainloop()

# Membuat kernel dan mempelajari berkas aiml
kernel = aiml.Kernel()

# Membuat file brain untuk mempercepat learning
if os.path.isfile("bot_brain.brn"):
    kernel.bootstrap(brainFile="bot_brain.brn")
else:
    kernel.bootstrap(learnFiles="pmb_ukdw.xml", commands="pmb")
    kernel.saveBrain("bot_brain.brn")

while True:

    user_input = kernel.respond(input("USER > "))
    if user_input:
        print("Chatbot > ", user_input)
    else:
        print("PMB > Maaf kakak, saya masih belajar mohon dicoba pertanyaan lainnya")
