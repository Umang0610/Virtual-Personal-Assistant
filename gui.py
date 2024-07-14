import sys
from tkinter import *
from PIL import Image, ImageTk
import action
import speech_to_text
import vpa
def User_send():
    send = entry1.get()
    bot = action.Action(send)
    text.insert(END, "Me --> " + send + "\n")
    if bot != None:
        text.insert(END, "Bot <-- " + str(bot) + "\n")
    if bot == "ok sir":
        root.destroy()
def ask():
    ask_val = speech_to_text.takeCommand()
    bot_val = action.Action(ask_val)
    print (bot_val)
    text.insert(END, "Me --> " + ask_val + "\n")
    if bot_val != None:
        text.insert(END, "Bot <-- " + str(bot_val) + "\n")
    if bot_val == "ok sir":
        root.destroy()
def clear_text():
    text.delete("1.0", "end")
def exit():
    sys.exit()
root = Tk()
root.geometry("900x850")
root.title("Virtual Personal Assistant")
root.config(bg="#6F8FAF")

# Main Frame
Main_frame = LabelFrame(root, padx=100, pady=7, borderwidth=3, relief="raised")
Main_frame.config(bg="#6F8FAF")
Main_frame.grid(row=0, column=1, padx=55, pady=10)

# Text Lable
Text_lable = Label(Main_frame, text="Virtual Personal Assistant", font=("comic Sans ms", 14, "bold"), bg="#356696")
Text_lable.grid(row=0, column=0, padx=20, pady=10)

# Image
Display_Image = ImageTk.PhotoImage(Image.open(r"C:\Users\hp\PycharmProjects\pythonProject\.idea\gui.png"))
Image_Lable = Label(Main_frame, image=Display_Image)
Image_Lable.grid(row=1, column=0, pady=20)

# Add a text widget

text = Text(root, font=('Courier 10 bold'), bg="#356696")
text.grid(row=2, column=0)
text.place(x=120, y=500, width=600, height=100)

# Add a entry widget
entry1 = Entry(root, justify=CENTER)
entry1.place(x=250, y=625, width=350, height=30)

# Add a text button1
button1 = Button(root, text="Ask", bg="#356696", pady=16, padx=40, borderwidth=3, relief=SOLID, command=ask)
button1.place(x=90, y=720)

# Add a text button2
button2 = Button(root, text="Send", bg="#356696", pady=16, padx=40, borderwidth=3, relief=SOLID, command=User_send)
button2.place(x=465, y=720)

# Add a text button3
button3 = Button(root, text="Clear", bg="#356696", pady=16, padx=40, borderwidth=3, relief=SOLID, command=clear_text)
button3.place(x=270, y=720)

button4 = Button(root, text="Exit", bg="#356696", pady=16, padx=40, borderwidth=3, relief=SOLID, command=exit)
button4.place(x=655, y=720)
root.mainloop()