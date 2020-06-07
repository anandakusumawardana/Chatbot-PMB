# Bot PMB
import os

import aiml

# Membuat kernel dan mempelajari berkas aiml
kernel = aiml.Kernel()

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
        print("Chatbot > Maaf, saya masih tidak mengerti kata yang diucapkan, bisa diulangi lagi?")
