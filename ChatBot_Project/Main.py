# Bot PMB
import os

import aiml
from tkinter import *

# # Create the GUI
# # Create tkinter object (represent the parent window)
root = Tk()

#
# # Give the window a title
root.title("PMB UKDW")
#
# # Give the window some dimensions
root.geometry("500x460")
#
# # Create the menu bar
main_menu = Menu(root)
#
# # Create the sub menu
file_menu = Menu(root)
file_menu.add_command(label="New")
file_menu.add_command(label="Save As")
file_menu.add_command(label="Exit")
#
#main_menu.add_cascade(label="File", menu=file_menu)
#root.config(menu=main_menu)
#
# # Create the chat area
chatWindow = Text(root, bd=1, bg="deep sky blue", width=50, height=8, font = "Corbel 11")
chatWindow.place(x=6, y=6, height=385, width=475)
#
# # Create the message window
messageWindow = Text(root, bg="deep sky blue", width=30, height=4, font = "Corbel 11")
messageWindow.place(x=6, y=400, height=50, width=400)
#

#
# # Add the scroll bar
scrollbar = Scrollbar(root, command=chatWindow.yview())
scrollbar.place(x=480, y=5, height=385)
#
#root.mainloop()

# Membuat kernel dan mempelajari berkas aiml
kernel = aiml.Kernel()

# Membuat file brain untuk mempercepat learning
if os.path.isfile("bot_brain.brn"):
    kernel.bootstrap(brainFile="bot_brain.brn")
else:
    kernel.bootstrap(learnFiles="pmb_ukdw.xml", commands="pmb")
    kernel.saveBrain("bot_brain.brn")

#while True:

    #user_input = kernel.respond(input("USER > "))
    #if user_input:
        #print("Chatbot > ", user_input)
    #else:
        #print("PMB > Maaf kakak, saya masih belajar mohon dicoba pertanyaan lainnya")

#txt = Text(root, font = "Corbel 11")
#txt.grid(row=0,column=0, columnspan=2) 
#e = Entry(root, width=100)
#e.grid(row=1, column=0)
chatWindow.insert(END, "Halo selamat datang di chatbot PMB UKDW   (^_^)\nInformasi apa yang ingin kakak ketahui?")

def send():
    send="USER > "+messageWindow.get(1.0,END)
    user_input=kernel.respond(messageWindow.get(1.0,END))
    chatWindow.insert(END, "\n"+send)
    if user_input:
        chatWindow.insert(END,"PMB > "+user_input)
    else:
        chatWindow.insert(END,"PMB > Maaf kakak, saya masih belajar mohon dicoba pertanyaan lainnya")
    messageWindow.delete(1.0,END)
    
#send = Button(root, text="Send", bg="blue", fg="white", activebackground="lightblue", command=send).grid(row=1, column=1)
# # Create the button to send the message
send = Button(root, text="Send", fg="white", bg="blue", activebackground="lightblue", width=12, height=5, font=("Corbel", 12), command=send)
send.place(x=415, y=400, height=50, width=60)

root.mainloop()
