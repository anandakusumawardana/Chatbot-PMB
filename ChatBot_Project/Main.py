# Bot PMB
import aiml

# Membuat kernel dan mempelajari berkas aiml
kernel = aiml.Kernel()
kernel.learn("pmb_ukdw.xml")
kernel.respond("pmb")
while True:
    user_input = kernel.respond(input("USER > "))
    if user_input:
        print("Chatbot > ", user_input)
    else:
        print("Chatbot > Maaf, saya masih tidak mengerti kata yang diucapkan, bisa diulangi lagi?")
