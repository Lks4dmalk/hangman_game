import tkinter
import re
from tkinter import *
from tkinter import messagebox

valid_word = []
list_with_empty_spaces = []
counter_of_mistakes = 0
valid_bool = False
curr_image = "hang2.png"

def a():
    if valid_bool == False:
        pass
    else:
        if "a" in valid_word:
            for let in range(len(valid_word)):
                if valid_word[let] == "a":
                    list_with_empty_spaces[let] = "a"
            empty_label = tkinter.Label(root, fg="black", font=("Black", 27, "bold"), bg="white",
                                        text=f"{' '.join(list_with_empty_spaces)}")
            empty_label.place(relwidth=0.6, relheight=0.059, rely=0.7)
            if "_" not in list_with_empty_spaces:
                tkinter.messagebox.showinfo(title="Congrats!",
                                             message="You won!")
                root.destroy()
                return
        else:
            global counter_of_mistakes
            global img_start
            global label_start
            counter_of_mistakes += 1
            if counter_of_mistakes == 0:
                pass
            elif counter_of_mistakes == 1:
                img_start = PhotoImage(file="hang5.png")
                label_start = tkinter.Label(image=img_start).place(relwidth=0.4, relheight=0.5, rely=0.3, relx=0.6)
            elif counter_of_mistakes == 2:
                img_start = PhotoImage(file="hang6.png")
                label_start = tkinter.Label(image=img_start).place(relwidth=0.4, relheight=0.5, rely=0.3, relx=0.6)
            elif counter_of_mistakes == 3:
                img_start = PhotoImage(file="hang7.png")
                label_start = tkinter.Label(image=img_start).place(relwidth=0.4, relheight=0.5, rely=0.3, relx=0.6)
            elif counter_of_mistakes == 4:
                img_start = PhotoImage(file="hang8.png")
                label_start = tkinter.Label(image=img_start).place(relwidth=0.4, relheight=0.5, rely=0.3, relx=0.6)
            elif counter_of_mistakes == 5:
                img_start = PhotoImage(file="hang9.png")
                label_start = tkinter.Label(image=img_start).place(relwidth=0.4, relheight=0.5, rely=0.3, relx=0.6)
            elif counter_of_mistakes == 6:
                img_start = PhotoImage(file="hang10.png")
                label_start = tkinter.Label(image=img_start).place(relwidth=0.4, relheight=0.5, rely=0.3, relx=0.6)
            elif counter_of_mistakes == 7:
                img_start = PhotoImage(file="hang11.png")
                label_start = tkinter.Label(image=img_start).place(relwidth=0.4, relheight=0.5, rely=0.3, relx=0.6)
                tkinter.messagebox.showwarning(title="You lost, idiot", message="You lost, bye :)")
                root.destroy()
                return

        word_choice_2.destroy()


def b():
    if valid_bool == False:
        pass
    else:
        if "b" in valid_word:
            for let in range(len(valid_word)):
                if valid_word[let] == "b":
                    list_with_empty_spaces[let] = "b"

            empty_label = tkinter.Label(root, fg="black", font=("Black", 27, "bold"), bg="white",
                                    text=f"{' '.join(list_with_empty_spaces)}")
            empty_label.place(relwidth=0.6, relheight=0.059, rely=0.7)
            if "_" not in list_with_empty_spaces:
                tkinter.messagebox.showinfo(title="Congrats!",
                                             message="You won!")
                root.destroy()
                return

        else:
            global counter_of_mistakes
            global img_start
            global label_start
            counter_of_mistakes += 1
            if counter_of_mistakes == 0:
                pass
            elif counter_of_mistakes == 1:
                img_start = PhotoImage(file="hang5.png")
                label_start = tkinter.Label(image=img_start).place(relwidth=0.4, relheight=0.5, rely=0.3, relx=0.6)
            elif counter_of_mistakes == 2:
                img_start = PhotoImage(file="hang6.png")
                label_start = tkinter.Label(image=img_start).place(relwidth=0.4, relheight=0.5, rely=0.3, relx=0.6)
            elif counter_of_mistakes == 3:
                img_start = PhotoImage(file="hang7.png")
                label_start = tkinter.Label(image=img_start).place(relwidth=0.4, relheight=0.5, rely=0.3, relx=0.6)
            elif counter_of_mistakes == 4:
                img_start = PhotoImage(file="hang8.png")
                label_start = tkinter.Label(image=img_start).place(relwidth=0.4, relheight=0.5, rely=0.3, relx=0.6)
            elif counter_of_mistakes == 5:
                img_start = PhotoImage(file="hang9.png")
                label_start = tkinter.Label(image=img_start).place(relwidth=0.4, relheight=0.5, rely=0.3, relx=0.6)
            elif counter_of_mistakes == 6:
                img_start = PhotoImage(file="hang10.png")
                label_start = tkinter.Label(image=img_start).place(relwidth=0.4, relheight=0.5, rely=0.3, relx=0.6)
            elif counter_of_mistakes == 7:
                img_start = PhotoImage(file="hang11.png")
                label_start = tkinter.Label(image=img_start).place(relwidth=0.4, relheight=0.5, rely=0.3, relx=0.6)
                tkinter.messagebox.showwarning(title="You lost, idiot", message="You lost, bye :)")
                root.destroy()
                return
        word_choice_4.destroy()


def c():
    if valid_bool == False:
        pass
    else:
        if "c" in valid_word:
            for let in range(len(valid_word)):
                if valid_word[let] == "c":
                    list_with_empty_spaces[let] = "c"
            empty_label = tkinter.Label(root, fg="black", font=("Black", 27, "bold"), bg="white",
                                    text=f"{' '.join(list_with_empty_spaces)}")
            empty_label.place(relwidth=0.6, relheight=0.059, rely=0.7)
            if "_" not in list_with_empty_spaces:
                tkinter.messagebox.showinfo(title="Congrats!",
                                             message="You won!")
                root.destroy()
                return

        else:
            global counter_of_mistakes
            global img_start
            global label_start
            counter_of_mistakes += 1
            if counter_of_mistakes == 0:
                pass
            elif counter_of_mistakes == 1:
                img_start = PhotoImage(file="hang5.png")
                label_start = tkinter.Label(image=img_start).place(relwidth=0.4, relheight=0.5, rely=0.3, relx=0.6)
            elif counter_of_mistakes == 2:
                img_start = PhotoImage(file="hang6.png")
                label_start = tkinter.Label(image=img_start).place(relwidth=0.4, relheight=0.5, rely=0.3, relx=0.6)
            elif counter_of_mistakes == 3:
                img_start = PhotoImage(file="hang7.png")
                label_start = tkinter.Label(image=img_start).place(relwidth=0.4, relheight=0.5, rely=0.3, relx=0.6)
            elif counter_of_mistakes == 4:
                img_start = PhotoImage(file="hang8.png")
                label_start = tkinter.Label(image=img_start).place(relwidth=0.4, relheight=0.5, rely=0.3, relx=0.6)
            elif counter_of_mistakes == 5:
                img_start = PhotoImage(file="hang9.png")
                label_start = tkinter.Label(image=img_start).place(relwidth=0.4, relheight=0.5, rely=0.3, relx=0.6)
            elif counter_of_mistakes == 6:
                img_start = PhotoImage(file="hang10.png")
                label_start = tkinter.Label(image=img_start).place(relwidth=0.4, relheight=0.5, rely=0.3, relx=0.6)
            elif counter_of_mistakes == 7:
                img_start = PhotoImage(file="hang11.png")
                label_start = tkinter.Label(image=img_start).place(relwidth=0.4, relheight=0.5, rely=0.3, relx=0.6)
                tkinter.messagebox.showwarning(title="You lost, idiot", message="You lost, bye :)")
                root.destroy()
                return
        word_choice_5.destroy()

def d():
    if valid_bool == False:
        pass
    else:
        if "d" in valid_word:
            for let in range(len(valid_word)):
                if valid_word[let] == "d":
                    list_with_empty_spaces[let] = "d"

            empty_label = tkinter.Label(root, fg="black", font=("Black", 27, "bold"), bg="white",
                                        text=f"{' '.join(list_with_empty_spaces)}")
            empty_label.place(relwidth=0.6, relheight=0.059, rely=0.7)
            if "_" not in list_with_empty_spaces:
                tkinter.messagebox.showinfo(title="Congrats!",
                                             message="You won!")
                root.destroy()
                return

        else:
            global counter_of_mistakes
            global img_start
            global label_start
            counter_of_mistakes += 1
            if counter_of_mistakes == 0:
                pass
            elif counter_of_mistakes == 1:
                img_start = PhotoImage(file="hang5.png")
                label_start = tkinter.Label(image=img_start).place(relwidth=0.4, relheight=0.5, rely=0.3, relx=0.6)
            elif counter_of_mistakes == 2:
                img_start = PhotoImage(file="hang6.png")
                label_start = tkinter.Label(image=img_start).place(relwidth=0.4, relheight=0.5, rely=0.3, relx=0.6)
            elif counter_of_mistakes == 3:
                img_start = PhotoImage(file="hang7.png")
                label_start = tkinter.Label(image=img_start).place(relwidth=0.4, relheight=0.5, rely=0.3, relx=0.6)
            elif counter_of_mistakes == 4:
                img_start = PhotoImage(file="hang8.png")
                label_start = tkinter.Label(image=img_start).place(relwidth=0.4, relheight=0.5, rely=0.3, relx=0.6)
            elif counter_of_mistakes == 5:
                img_start = PhotoImage(file="hang9.png")
                label_start = tkinter.Label(image=img_start).place(relwidth=0.4, relheight=0.5, rely=0.3, relx=0.6)
            elif counter_of_mistakes == 6:
                img_start = PhotoImage(file="hang10.png")
                label_start = tkinter.Label(image=img_start).place(relwidth=0.4, relheight=0.5, rely=0.3, relx=0.6)
            elif counter_of_mistakes == 7:
                img_start = PhotoImage(file="hang11.png")
                label_start = tkinter.Label(image=img_start).place(relwidth=0.4, relheight=0.5, rely=0.3, relx=0.6)
                tkinter.messagebox.showwarning(title="You lost, idiot", message="You lost, bye :)")
                root.destroy()
                return
        word_choice_8.destroy()

def e():
    if valid_bool == False:
        pass
    else:
        if "e" in valid_word:
            for let in range(len(valid_word)):
                if valid_word[let] == "e":
                    list_with_empty_spaces[let] = "e"

            empty_label = tkinter.Label(root, fg="black", font=("Black", 27, "bold"), bg="white",
                                        text=f"{' '.join(list_with_empty_spaces)}")
            empty_label.place(relwidth=0.6, relheight=0.059, rely=0.7)
            if "_" not in list_with_empty_spaces:
                tkinter.messagebox.showinfo(title="Congrats!",
                                             message="You won!")
                root.destroy()
                return

        else:
            global counter_of_mistakes
            global img_start
            global label_start
            counter_of_mistakes += 1
            if counter_of_mistakes == 0:
                pass
            elif counter_of_mistakes == 1:
                img_start = PhotoImage(file="hang5.png")
                label_start = tkinter.Label(image=img_start).place(relwidth=0.4, relheight=0.5, rely=0.3, relx=0.6)
            elif counter_of_mistakes == 2:
                img_start = PhotoImage(file="hang6.png")
                label_start = tkinter.Label(image=img_start).place(relwidth=0.4, relheight=0.5, rely=0.3, relx=0.6)
            elif counter_of_mistakes == 3:
                img_start = PhotoImage(file="hang7.png")
                label_start = tkinter.Label(image=img_start).place(relwidth=0.4, relheight=0.5, rely=0.3, relx=0.6)
            elif counter_of_mistakes == 4:
                img_start = PhotoImage(file="hang8.png")
                label_start = tkinter.Label(image=img_start).place(relwidth=0.4, relheight=0.5, rely=0.3, relx=0.6)
            elif counter_of_mistakes == 5:
                img_start = PhotoImage(file="hang9.png")
                label_start = tkinter.Label(image=img_start).place(relwidth=0.4, relheight=0.5, rely=0.3, relx=0.6)
            elif counter_of_mistakes == 6:
                img_start = PhotoImage(file="hang10.png")
                label_start = tkinter.Label(image=img_start).place(relwidth=0.4, relheight=0.5, rely=0.3, relx=0.6)
            elif counter_of_mistakes == 7:
                img_start = PhotoImage(file="hang11.png")
                label_start = tkinter.Label(image=img_start).place(relwidth=0.4, relheight=0.5, rely=0.3, relx=0.6)
                tkinter.messagebox.showwarning(title="You lost, idiot", message="You lost, bye :)")
                root.destroy()
                return
        word_choice_10.destroy()

def f():
    if valid_bool == False:
        pass
    else:
        if "f" in valid_word:
            for let in range(len(valid_word)):
                if valid_word[let] == "f":
                    list_with_empty_spaces[let] = "f"

            empty_label = tkinter.Label(root, fg="black", font=("Black", 27, "bold"), bg="white",
                                        text=f"{' '.join(list_with_empty_spaces)}")
            empty_label.place(relwidth=0.6, relheight=0.059, rely=0.7)
            if "_" not in list_with_empty_spaces:
                tkinter.messagebox.showinfo(title="Congrats!",
                                             message="You won!")
                root.destroy()
                return

        else:
            global counter_of_mistakes
            global img_start
            global label_start
            counter_of_mistakes += 1
            if counter_of_mistakes == 0:
                pass
            elif counter_of_mistakes == 1:
                img_start = PhotoImage(file="hang5.png")
                label_start = tkinter.Label(image=img_start).place(relwidth=0.4, relheight=0.5, rely=0.3, relx=0.6)
            elif counter_of_mistakes == 2:
                img_start = PhotoImage(file="hang6.png")
                label_start = tkinter.Label(image=img_start).place(relwidth=0.4, relheight=0.5, rely=0.3, relx=0.6)
            elif counter_of_mistakes == 3:
                img_start = PhotoImage(file="hang7.png")
                label_start = tkinter.Label(image=img_start).place(relwidth=0.4, relheight=0.5, rely=0.3, relx=0.6)
            elif counter_of_mistakes == 4:
                img_start = PhotoImage(file="hang8.png")
                label_start = tkinter.Label(image=img_start).place(relwidth=0.4, relheight=0.5, rely=0.3, relx=0.6)
            elif counter_of_mistakes == 5:
                img_start = PhotoImage(file="hang9.png")
                label_start = tkinter.Label(image=img_start).place(relwidth=0.4, relheight=0.5, rely=0.3, relx=0.6)
            elif counter_of_mistakes == 6:
                img_start = PhotoImage(file="hang10.png")
                label_start = tkinter.Label(image=img_start).place(relwidth=0.4, relheight=0.5, rely=0.3, relx=0.6)
            elif counter_of_mistakes == 7:
                img_start = PhotoImage(file="hang11.png")
                label_start = tkinter.Label(image=img_start).place(relwidth=0.4, relheight=0.5, rely=0.3, relx=0.6)
                tkinter.messagebox.showwarning(title="You lost, idiot", message="You lost, bye :)")
                root.destroy()
                return
        word_choice_12.destroy()

def g():
    if valid_bool == False:
        pass
    else:
        if "g" in valid_word:
            for let in range(len(valid_word)):
                if valid_word[let] == "g":
                    list_with_empty_spaces[let] = "g"
            empty_label = tkinter.Label(root, fg="black", font=("Black", 27, "bold"), bg="white",
                                        text=f"{' '.join(list_with_empty_spaces)}")
            empty_label.place(relwidth=0.6, relheight=0.059, rely=0.7)
            if "_" not in list_with_empty_spaces:
                tkinter.messagebox.showinfo(title="Congrats!",
                                             message="You won!")
                root.destroy()
                return

        else:
            global counter_of_mistakes
            global img_start
            global label_start
            counter_of_mistakes += 1
            if counter_of_mistakes == 0:
                pass
            elif counter_of_mistakes == 1:
                img_start = PhotoImage(file="hang5.png")
                label_start = tkinter.Label(image=img_start).place(relwidth=0.4, relheight=0.5, rely=0.3, relx=0.6)
            elif counter_of_mistakes == 2:
                img_start = PhotoImage(file="hang6.png")
                label_start = tkinter.Label(image=img_start).place(relwidth=0.4, relheight=0.5, rely=0.3, relx=0.6)
            elif counter_of_mistakes == 3:
                img_start = PhotoImage(file="hang7.png")
                label_start = tkinter.Label(image=img_start).place(relwidth=0.4, relheight=0.5, rely=0.3, relx=0.6)
            elif counter_of_mistakes == 4:
                img_start = PhotoImage(file="hang8.png")
                label_start = tkinter.Label(image=img_start).place(relwidth=0.4, relheight=0.5, rely=0.3, relx=0.6)
            elif counter_of_mistakes == 5:
                img_start = PhotoImage(file="hang9.png")
                label_start = tkinter.Label(image=img_start).place(relwidth=0.4, relheight=0.5, rely=0.3, relx=0.6)
            elif counter_of_mistakes == 6:
                img_start = PhotoImage(file="hang10.png")
                label_start = tkinter.Label(image=img_start).place(relwidth=0.4, relheight=0.5, rely=0.3, relx=0.6)
            elif counter_of_mistakes == 7:
                img_start = PhotoImage(file="hang11.png")
                label_start = tkinter.Label(image=img_start).place(relwidth=0.4, relheight=0.5, rely=0.3, relx=0.6)
                tkinter.messagebox.showwarning(title="You lost, idiot", message="You lost, bye :)")
                root.destroy()
                return
        word_choice_14.destroy()

def h():
    if valid_bool == False:
        pass
    else:
        if "h" in valid_word:
            for let in range(len(valid_word)):
                if valid_word[let] == "h":
                    list_with_empty_spaces[let] = "h"
            empty_label = tkinter.Label(root, fg="black", font=("Black", 27, "bold"), bg="white",
                                        text=f"{' '.join(list_with_empty_spaces)}")
            empty_label.place(relwidth=0.6, relheight=0.059, rely=0.7)
            if "_" not in list_with_empty_spaces:
                tkinter.messagebox.showinfo(title="Congrats!",
                                             message="You won!")
                root.destroy()
                return

        else:
            global counter_of_mistakes
            global img_start
            global label_start
            counter_of_mistakes += 1
            if counter_of_mistakes == 0:
                pass
            elif counter_of_mistakes == 1:
                img_start = PhotoImage(file="hang5.png")
                label_start = tkinter.Label(image=img_start).place(relwidth=0.4, relheight=0.5, rely=0.3, relx=0.6)
            elif counter_of_mistakes == 2:
                img_start = PhotoImage(file="hang6.png")
                label_start = tkinter.Label(image=img_start).place(relwidth=0.4, relheight=0.5, rely=0.3, relx=0.6)
            elif counter_of_mistakes == 3:
                img_start = PhotoImage(file="hang7.png")
                label_start = tkinter.Label(image=img_start).place(relwidth=0.4, relheight=0.5, rely=0.3, relx=0.6)
            elif counter_of_mistakes == 4:
                img_start = PhotoImage(file="hang8.png")
                label_start = tkinter.Label(image=img_start).place(relwidth=0.4, relheight=0.5, rely=0.3, relx=0.6)
            elif counter_of_mistakes == 5:
                img_start = PhotoImage(file="hang9.png")
                label_start = tkinter.Label(image=img_start).place(relwidth=0.4, relheight=0.5, rely=0.3, relx=0.6)
            elif counter_of_mistakes == 6:
                img_start = PhotoImage(file="hang10.png")
                label_start = tkinter.Label(image=img_start).place(relwidth=0.4, relheight=0.5, rely=0.3, relx=0.6)
            elif counter_of_mistakes == 7:
                img_start = PhotoImage(file="hang11.png")
                label_start = tkinter.Label(image=img_start).place(relwidth=0.4, relheight=0.5, rely=0.3, relx=0.6)
                tkinter.messagebox.showwarning(title="You lost, idiot", message="You lost, bye :)")
                root.destroy()
                return
        word_choice_16.destroy()

def i():
    if valid_bool == False:
        pass
    else:
        if "i" in valid_word:
            for let in range(len(valid_word)):
                if valid_word[let] == "i":
                    list_with_empty_spaces[let] = "i"
            empty_label = tkinter.Label(root, fg="black", font=("Black", 27, "bold"), bg="white",
                                        text=f"{' '.join(list_with_empty_spaces)}")
            empty_label.place(relwidth=0.6, relheight=0.059, rely=0.7)
            if "_" not in list_with_empty_spaces:
                tkinter.messagebox.showinfo(title="Congrats!",
                                             message="You won!")
                root.destroy()
                return
        else:
            global counter_of_mistakes
            global img_start
            global label_start
            counter_of_mistakes += 1
            if counter_of_mistakes == 0:
                pass
            elif counter_of_mistakes == 1:
                img_start = PhotoImage(file="hang5.png")
                label_start = tkinter.Label(image=img_start).place(relwidth=0.4, relheight=0.5, rely=0.3, relx=0.6)
            elif counter_of_mistakes == 2:
                img_start = PhotoImage(file="hang6.png")
                label_start = tkinter.Label(image=img_start).place(relwidth=0.4, relheight=0.5, rely=0.3, relx=0.6)
            elif counter_of_mistakes == 3:
                img_start = PhotoImage(file="hang7.png")
                label_start = tkinter.Label(image=img_start).place(relwidth=0.4, relheight=0.5, rely=0.3, relx=0.6)
            elif counter_of_mistakes == 4:
                img_start = PhotoImage(file="hang8.png")
                label_start = tkinter.Label(image=img_start).place(relwidth=0.4, relheight=0.5, rely=0.3, relx=0.6)
            elif counter_of_mistakes == 5:
                img_start = PhotoImage(file="hang9.png")
                label_start = tkinter.Label(image=img_start).place(relwidth=0.4, relheight=0.5, rely=0.3, relx=0.6)
            elif counter_of_mistakes == 6:
                img_start = PhotoImage(file="hang10.png")
                label_start = tkinter.Label(image=img_start).place(relwidth=0.4, relheight=0.5, rely=0.3, relx=0.6)
            elif counter_of_mistakes == 7:
                img_start = PhotoImage(file="hang11.png")
                label_start = tkinter.Label(image=img_start).place(relwidth=0.4, relheight=0.5, rely=0.3, relx=0.6)
                tkinter.messagebox.showwarning(title="You lost, idiot", message="You lost, bye :)")
                root.destroy()
                return
        word_choice_18.destroy()
def j():
    if valid_bool == False:
        pass
    else:
        if "j" in valid_word:
            for let in range(len(valid_word)):
                if valid_word[let] == "j":
                    list_with_empty_spaces[let] = "j"
            empty_label = tkinter.Label(root, fg="black", font=("Black", 27, "bold"), bg="white",
                                        text=f"{' '.join(list_with_empty_spaces)}")
            empty_label.place(relwidth=0.6, relheight=0.059, rely=0.7)
            if "_" not in list_with_empty_spaces:
                tkinter.messagebox.showinfo(title="Congrats!",
                                             message="You won!")
                root.destroy()
                return

        else:
            global counter_of_mistakes
            global img_start
            global label_start
            counter_of_mistakes += 1
            if counter_of_mistakes == 0:
                pass
            elif counter_of_mistakes == 1:
                img_start = PhotoImage(file="hang5.png")
                label_start = tkinter.Label(image=img_start).place(relwidth=0.4, relheight=0.5, rely=0.3, relx=0.6)
            elif counter_of_mistakes == 2:
                img_start = PhotoImage(file="hang6.png")
                label_start = tkinter.Label(image=img_start).place(relwidth=0.4, relheight=0.5, rely=0.3, relx=0.6)
            elif counter_of_mistakes == 3:
                img_start = PhotoImage(file="hang7.png")
                label_start = tkinter.Label(image=img_start).place(relwidth=0.4, relheight=0.5, rely=0.3, relx=0.6)
            elif counter_of_mistakes == 4:
                img_start = PhotoImage(file="hang8.png")
                label_start = tkinter.Label(image=img_start).place(relwidth=0.4, relheight=0.5, rely=0.3, relx=0.6)
            elif counter_of_mistakes == 5:
                img_start = PhotoImage(file="hang9.png")
                label_start = tkinter.Label(image=img_start).place(relwidth=0.4, relheight=0.5, rely=0.3, relx=0.6)
            elif counter_of_mistakes == 6:
                img_start = PhotoImage(file="hang10.png")
                label_start = tkinter.Label(image=img_start).place(relwidth=0.4, relheight=0.5, rely=0.3, relx=0.6)
            elif counter_of_mistakes == 7:
                img_start = PhotoImage(file="hang11.png")
                label_start = tkinter.Label(image=img_start).place(relwidth=0.4, relheight=0.5, rely=0.3, relx=0.6)
                tkinter.messagebox.showwarning(title="You lost, idiot", message="You lost, bye :)")
                root.destroy()
                return
        word_choice_20.destroy()


def k():
    if valid_bool == False:
        pass
    else:
        if "k" in valid_word:
            for let in range(len(valid_word)):
                if valid_word[let] == "k":
                    list_with_empty_spaces[let] = "k"
            empty_label = tkinter.Label(root, fg="black", font=("Black", 27, "bold"), bg="white",
                                        text=f"{' '.join(list_with_empty_spaces)}")
            empty_label.place(relwidth=0.6, relheight=0.059, rely=0.7)
            if "_" not in list_with_empty_spaces:
                tkinter.messagebox.showinfo(title="Congrats!",
                                             message="You won!")
                root.destroy()
                return

        else:
            global counter_of_mistakes
            global img_start
            global label_start
            counter_of_mistakes += 1
            if counter_of_mistakes == 0:
                pass
            elif counter_of_mistakes == 1:
                img_start = PhotoImage(file="hang5.png")
                label_start = tkinter.Label(image=img_start).place(relwidth=0.4, relheight=0.5, rely=0.3, relx=0.6)
            elif counter_of_mistakes == 2:
                img_start = PhotoImage(file="hang6.png")
                label_start = tkinter.Label(image=img_start).place(relwidth=0.4, relheight=0.5, rely=0.3, relx=0.6)
            elif counter_of_mistakes == 3:
                img_start = PhotoImage(file="hang7.png")
                label_start = tkinter.Label(image=img_start).place(relwidth=0.4, relheight=0.5, rely=0.3, relx=0.6)
            elif counter_of_mistakes == 4:
                img_start = PhotoImage(file="hang8.png")
                label_start = tkinter.Label(image=img_start).place(relwidth=0.4, relheight=0.5, rely=0.3, relx=0.6)
            elif counter_of_mistakes == 5:
                img_start = PhotoImage(file="hang9.png")
                label_start = tkinter.Label(image=img_start).place(relwidth=0.4, relheight=0.5, rely=0.3, relx=0.6)
            elif counter_of_mistakes == 6:
                img_start = PhotoImage(file="hang10.png")
                label_start = tkinter.Label(image=img_start).place(relwidth=0.4, relheight=0.5, rely=0.3, relx=0.6)
            elif counter_of_mistakes == 7:
                img_start = PhotoImage(file="hang11.png")
                label_start = tkinter.Label(image=img_start).place(relwidth=0.4, relheight=0.5, rely=0.3, relx=0.6)
                tkinter.messagebox.showwarning(title="You lost, idiot", message="You lost, bye :)")
                root.destroy()
                return
        word_choice_22.destroy()

def l():
    if valid_bool == False:
        pass
    else:
        if "l" in valid_word:
            for let in range(len(valid_word)):
                if valid_word[let] == "l":
                    list_with_empty_spaces[let] = "l"
            empty_label = tkinter.Label(root, fg="black", font=("Black", 27, "bold"), bg="white",
                                        text=f"{' '.join(list_with_empty_spaces)}")
            empty_label.place(relwidth=0.6, relheight=0.059, rely=0.7)
            if "_" not in list_with_empty_spaces:
                tkinter.messagebox.showinfo(title="Congrats!",
                                             message="You won!")
                root.destroy()
                return

        else:
            global counter_of_mistakes
            global img_start
            global label_start
            counter_of_mistakes += 1
            if counter_of_mistakes == 0:
                pass
            elif counter_of_mistakes == 1:
                img_start = PhotoImage(file="hang5.png")
                label_start = tkinter.Label(image=img_start).place(relwidth=0.4, relheight=0.5, rely=0.3, relx=0.6)
            elif counter_of_mistakes == 2:
                img_start = PhotoImage(file="hang6.png")
                label_start = tkinter.Label(image=img_start).place(relwidth=0.4, relheight=0.5, rely=0.3, relx=0.6)
            elif counter_of_mistakes == 3:
                img_start = PhotoImage(file="hang7.png")
                label_start = tkinter.Label(image=img_start).place(relwidth=0.4, relheight=0.5, rely=0.3, relx=0.6)
            elif counter_of_mistakes == 4:
                img_start = PhotoImage(file="hang8.png")
                label_start = tkinter.Label(image=img_start).place(relwidth=0.4, relheight=0.5, rely=0.3, relx=0.6)
            elif counter_of_mistakes == 5:
                img_start = PhotoImage(file="hang9.png")
                label_start = tkinter.Label(image=img_start).place(relwidth=0.4, relheight=0.5, rely=0.3, relx=0.6)
            elif counter_of_mistakes == 6:
                img_start = PhotoImage(file="hang10.png")
                label_start = tkinter.Label(image=img_start).place(relwidth=0.4, relheight=0.5, rely=0.3, relx=0.6)
            elif counter_of_mistakes == 7:
                img_start = PhotoImage(file="hang11.png")
                label_start = tkinter.Label(image=img_start).place(relwidth=0.4, relheight=0.5, rely=0.3, relx=0.6)
                tkinter.messagebox.showwarning(title="You lost, idiot", message="You lost, bye :)")
                root.destroy()
                return
        word_choice_24.destroy()

def m():
    if valid_bool == False:
        pass
    else:
        if "m" in valid_word:
            for let in range(len(valid_word)):
                if valid_word[let] == "m":
                    list_with_empty_spaces[let] = "m"
            empty_label = tkinter.Label(root, fg="black", font=("Black", 27, "bold"), bg="white",
                                        text=f"{' '.join(list_with_empty_spaces)}")
            empty_label.place(relwidth=0.6, relheight=0.059, rely=0.7)
            if "_" not in list_with_empty_spaces:
                tkinter.messagebox.showinfo(title="Congrats!",
                                             message="You won!")
                root.destroy()
                return

        else:
            global counter_of_mistakes
            global img_start
            global label_start
            counter_of_mistakes += 1
            if counter_of_mistakes == 0:
                pass
            elif counter_of_mistakes == 1:
                img_start = PhotoImage(file="hang5.png")
                label_start = tkinter.Label(image=img_start).place(relwidth=0.4, relheight=0.5, rely=0.3, relx=0.6)
            elif counter_of_mistakes == 2:
                img_start = PhotoImage(file="hang6.png")
                label_start = tkinter.Label(image=img_start).place(relwidth=0.4, relheight=0.5, rely=0.3, relx=0.6)
            elif counter_of_mistakes == 3:
                img_start = PhotoImage(file="hang7.png")
                label_start = tkinter.Label(image=img_start).place(relwidth=0.4, relheight=0.5, rely=0.3, relx=0.6)
            elif counter_of_mistakes == 4:
                img_start = PhotoImage(file="hang8.png")
                label_start = tkinter.Label(image=img_start).place(relwidth=0.4, relheight=0.5, rely=0.3, relx=0.6)
            elif counter_of_mistakes == 5:
                img_start = PhotoImage(file="hang9.png")
                label_start = tkinter.Label(image=img_start).place(relwidth=0.4, relheight=0.5, rely=0.3, relx=0.6)
            elif counter_of_mistakes == 6:
                img_start = PhotoImage(file="hang10.png")
                label_start = tkinter.Label(image=img_start).place(relwidth=0.4, relheight=0.5, rely=0.3, relx=0.6)
            elif counter_of_mistakes == 7:
                img_start = PhotoImage(file="hang11.png")
                label_start = tkinter.Label(image=img_start).place(relwidth=0.4, relheight=0.5, rely=0.3, relx=0.6)
                tkinter.messagebox.showwarning(title="You lost, idiot", message="You lost, bye :)")
                root.destroy()
                return
        word_choice_26.destroy()

def n():
    if valid_bool == False:
        pass
    else:
        if "n" in valid_word:
            for let in range(len(valid_word)):
                if valid_word[let] == "n":
                    list_with_empty_spaces[let] = "n"

            empty_label = tkinter.Label(root, fg="black", font=("Black", 27, "bold"), bg="white",
                                        text=f"{' '.join(list_with_empty_spaces)}")
            empty_label.place(relwidth=0.6, relheight=0.059, rely=0.7)
            if "_" not in list_with_empty_spaces:
                tkinter.messagebox.showinfo(title="Congrats!",
                                             message="You won!")
                root.destroy()
                return

        else:
            global counter_of_mistakes
            global img_start
            global label_start
            counter_of_mistakes += 1
            if counter_of_mistakes == 0:
                pass
            elif counter_of_mistakes == 1:
                img_start = PhotoImage(file="hang5.png")
                label_start = tkinter.Label(image=img_start).place(relwidth=0.4, relheight=0.5, rely=0.3, relx=0.6)
            elif counter_of_mistakes == 2:
                img_start = PhotoImage(file="hang6.png")
                label_start = tkinter.Label(image=img_start).place(relwidth=0.4, relheight=0.5, rely=0.3, relx=0.6)
            elif counter_of_mistakes == 3:
                img_start = PhotoImage(file="hang7.png")
                label_start = tkinter.Label(image=img_start).place(relwidth=0.4, relheight=0.5, rely=0.3, relx=0.6)
            elif counter_of_mistakes == 4:
                img_start = PhotoImage(file="hang8.png")
                label_start = tkinter.Label(image=img_start).place(relwidth=0.4, relheight=0.5, rely=0.3, relx=0.6)
            elif counter_of_mistakes == 5:
                img_start = PhotoImage(file="hang9.png")
                label_start = tkinter.Label(image=img_start).place(relwidth=0.4, relheight=0.5, rely=0.3, relx=0.6)
            elif counter_of_mistakes == 6:
                img_start = PhotoImage(file="hang10.png")
                label_start = tkinter.Label(image=img_start).place(relwidth=0.4, relheight=0.5, rely=0.3, relx=0.6)
            elif counter_of_mistakes == 7:
                img_start = PhotoImage(file="hang11.png")
                label_start = tkinter.Label(image=img_start).place(relwidth=0.4, relheight=0.5, rely=0.3, relx=0.6)
                tkinter.messagebox.showwarning(title="You lost, idiot", message="You lost, bye :)")
                root.destroy()
                return
        word_choice.destroy()


def o():
    if valid_bool == False:
        pass
    else:
        if "o" in valid_word:
            for let in range(len(valid_word)):
                if valid_word[let] == "o":
                    list_with_empty_spaces[let] = "o"
            empty_label = tkinter.Label(root, fg="black", font=("Black", 27, "bold"), bg="white",
                                        text=f"{' '.join(list_with_empty_spaces)}")
            empty_label.place(relwidth=0.6, relheight=0.059, rely=0.7)
            if "_" not in list_with_empty_spaces:
                tkinter.messagebox.showinfo(title="Congrats!",
                                             message="You won!")
                root.destroy()
                return

        else:
            global counter_of_mistakes
            global img_start
            global label_start
            counter_of_mistakes += 1
            if counter_of_mistakes == 0:
                pass
            elif counter_of_mistakes == 1:
                img_start = PhotoImage(file="hang5.png")
                label_start = tkinter.Label(image=img_start).place(relwidth=0.4, relheight=0.5, rely=0.3, relx=0.6)
            elif counter_of_mistakes == 2:
                img_start = PhotoImage(file="hang6.png")
                label_start = tkinter.Label(image=img_start).place(relwidth=0.4, relheight=0.5, rely=0.3, relx=0.6)
            elif counter_of_mistakes == 3:
                img_start = PhotoImage(file="hang7.png")
                label_start = tkinter.Label(image=img_start).place(relwidth=0.4, relheight=0.5, rely=0.3, relx=0.6)
            elif counter_of_mistakes == 4:
                img_start = PhotoImage(file="hang8.png")
                label_start = tkinter.Label(image=img_start).place(relwidth=0.4, relheight=0.5, rely=0.3, relx=0.6)
            elif counter_of_mistakes == 5:
                img_start = PhotoImage(file="hang9.png")
                label_start = tkinter.Label(image=img_start).place(relwidth=0.4, relheight=0.5, rely=0.3, relx=0.6)
            elif counter_of_mistakes == 6:
                img_start = PhotoImage(file="hang10.png")
                label_start = tkinter.Label(image=img_start).place(relwidth=0.4, relheight=0.5, rely=0.3, relx=0.6)
            elif counter_of_mistakes == 7:
                img_start = PhotoImage(file="hang11.png")
                label_start = tkinter.Label(image=img_start).place(relwidth=0.4, relheight=0.5, rely=0.3, relx=0.6)
                tkinter.messagebox.showwarning(title="You lost, idiot", message="You lost, bye :)")
                root.destroy()
                return
        word_choice_3.destroy()
def p():
    if valid_bool == False:
        pass
    else:
        if "p" in valid_word:
            for let in range(len(valid_word)):
                if valid_word[let] == "p":
                    list_with_empty_spaces[let] = "p"
            empty_label = tkinter.Label(root, fg="black", font=("Black", 27, "bold"), bg="white",
                                        text=f"{' '.join(list_with_empty_spaces)}")
            empty_label.place(relwidth=0.6, relheight=0.059, rely=0.7)
            if "_" not in list_with_empty_spaces:
                tkinter.messagebox.showinfo(title="Congrats!",
                                             message="You won!")
                root.destroy()
                return

        else:
            global counter_of_mistakes
            global img_start
            global label_start
            counter_of_mistakes += 1
            if counter_of_mistakes == 0:
                pass
            elif counter_of_mistakes == 1:
                img_start = PhotoImage(file="hang5.png")
                label_start = tkinter.Label(image=img_start).place(relwidth=0.4, relheight=0.5, rely=0.3, relx=0.6)
            elif counter_of_mistakes == 2:
                img_start = PhotoImage(file="hang6.png")
                label_start = tkinter.Label(image=img_start).place(relwidth=0.4, relheight=0.5, rely=0.3, relx=0.6)
            elif counter_of_mistakes == 3:
                img_start = PhotoImage(file="hang7.png")
                label_start = tkinter.Label(image=img_start).place(relwidth=0.4, relheight=0.5, rely=0.3, relx=0.6)
            elif counter_of_mistakes == 4:
                img_start = PhotoImage(file="hang8.png")
                label_start = tkinter.Label(image=img_start).place(relwidth=0.4, relheight=0.5, rely=0.3, relx=0.6)
            elif counter_of_mistakes == 5:
                img_start = PhotoImage(file="hang9.png")
                label_start = tkinter.Label(image=img_start).place(relwidth=0.4, relheight=0.5, rely=0.3, relx=0.6)
            elif counter_of_mistakes == 6:
                img_start = PhotoImage(file="hang10.png")
                label_start = tkinter.Label(image=img_start).place(relwidth=0.4, relheight=0.5, rely=0.3, relx=0.6)
            elif counter_of_mistakes == 7:
                img_start = PhotoImage(file="hang11.png")
                label_start = tkinter.Label(image=img_start).place(relwidth=0.4, relheight=0.5, rely=0.3, relx=0.6)
                tkinter.messagebox.showwarning(title="You lost, idiot", message="You lost, bye :)")
                root.destroy()
                return
        word_choice_6.destroy()

def q():
    if valid_bool == False:
        pass
    else:
        if "q" in valid_word:
            for let in range(len(valid_word)):
                if valid_word[let] == "q":
                    list_with_empty_spaces[let] = "q"
            empty_label = tkinter.Label(root, fg="black", font=("Black", 27, "bold"), bg="white",
                                        text=f"{' '.join(list_with_empty_spaces)}")
            empty_label.place(relwidth=0.6, relheight=0.059, rely=0.7)
            if "_" not in list_with_empty_spaces:
                tkinter.messagebox.showinfo(title="Congrats!",
                                             message="You won!")
                root.destroy()
                return

        else:
            global counter_of_mistakes
            global img_start
            global label_start
            counter_of_mistakes += 1
            if counter_of_mistakes == 0:
                pass
            elif counter_of_mistakes == 1:
                img_start = PhotoImage(file="hang5.png")
                label_start = tkinter.Label(image=img_start).place(relwidth=0.4, relheight=0.5, rely=0.3, relx=0.6)
            elif counter_of_mistakes == 2:
                img_start = PhotoImage(file="hang6.png")
                label_start = tkinter.Label(image=img_start).place(relwidth=0.4, relheight=0.5, rely=0.3, relx=0.6)
            elif counter_of_mistakes == 3:
                img_start = PhotoImage(file="hang7.png")
                label_start = tkinter.Label(image=img_start).place(relwidth=0.4, relheight=0.5, rely=0.3, relx=0.6)
            elif counter_of_mistakes == 4:
                img_start = PhotoImage(file="hang8.png")
                label_start = tkinter.Label(image=img_start).place(relwidth=0.4, relheight=0.5, rely=0.3, relx=0.6)
            elif counter_of_mistakes == 5:
                img_start = PhotoImage(file="hang9.png")
                label_start = tkinter.Label(image=img_start).place(relwidth=0.4, relheight=0.5, rely=0.3, relx=0.6)
            elif counter_of_mistakes == 6:
                img_start = PhotoImage(file="hang10.png")
                label_start = tkinter.Label(image=img_start).place(relwidth=0.4, relheight=0.5, rely=0.3, relx=0.6)
            elif counter_of_mistakes == 7:
                img_start = PhotoImage(file="hang11.png")
                label_start = tkinter.Label(image=img_start).place(relwidth=0.4, relheight=0.5, rely=0.3, relx=0.6)
                tkinter.messagebox.showwarning(title="You lost, idiot", message="You lost, bye :)")
                root.destroy()
                return
        word_choice_7.destroy()


def r():
    if valid_bool == False:
        pass
    else:
        if "r" in valid_word:
            for let in range(len(valid_word)):
                if valid_word[let] == "r":
                    list_with_empty_spaces[let] = "r"
            empty_label = tkinter.Label(root, fg="black", font=("Black", 27, "bold"), bg="white",
                                        text=f"{' '.join(list_with_empty_spaces)}")
            empty_label.place(relwidth=0.6, relheight=0.059, rely=0.7)
            if "_" not in list_with_empty_spaces:
                tkinter.messagebox.showinfo(title="Congrats!",
                                             message="You won!")
                root.destroy()
                return
        else:
            global counter_of_mistakes
            global img_start
            global label_start
            counter_of_mistakes += 1
            if counter_of_mistakes == 0:
                pass
            elif counter_of_mistakes == 1:
                img_start = PhotoImage(file="hang5.png")
                label_start = tkinter.Label(image=img_start).place(relwidth=0.4, relheight=0.5, rely=0.3, relx=0.6)
            elif counter_of_mistakes == 2:
                img_start = PhotoImage(file="hang6.png")
                label_start = tkinter.Label(image=img_start).place(relwidth=0.4, relheight=0.5, rely=0.3, relx=0.6)
            elif counter_of_mistakes == 3:
                img_start = PhotoImage(file="hang7.png")
                label_start = tkinter.Label(image=img_start).place(relwidth=0.4, relheight=0.5, rely=0.3, relx=0.6)
            elif counter_of_mistakes == 4:
                img_start = PhotoImage(file="hang8.png")
                label_start = tkinter.Label(image=img_start).place(relwidth=0.4, relheight=0.5, rely=0.3, relx=0.6)
            elif counter_of_mistakes == 5:
                img_start = PhotoImage(file="hang9.png")
                label_start = tkinter.Label(image=img_start).place(relwidth=0.4, relheight=0.5, rely=0.3, relx=0.6)
            elif counter_of_mistakes == 6:
                img_start = PhotoImage(file="hang10.png")
                label_start = tkinter.Label(image=img_start).place(relwidth=0.4, relheight=0.5, rely=0.3, relx=0.6)
            elif counter_of_mistakes == 7:
                img_start = PhotoImage(file="hang11.png")
                label_start = tkinter.Label(image=img_start).place(relwidth=0.4, relheight=0.5, rely=0.3, relx=0.6)
                tkinter.messagebox.showwarning(title="You lost, idiot", message="You lost, bye :)")
                root.destroy()
                return
    word_choice_9.destroy()

def s():
    if valid_bool == False:
        pass
    else:
        if "s" in valid_word:
            for let in range(len(valid_word)):
                if valid_word[let] == "s":
                    list_with_empty_spaces[let] = "s"

            empty_label = tkinter.Label(root, fg="black", font=("Black", 27, "bold"), bg="white",
                                        text=f"{' '.join(list_with_empty_spaces)}")
            empty_label.place(relwidth=0.6, relheight=0.059, rely=0.7)
            if "_" not in list_with_empty_spaces:
                tkinter.messagebox.showinfo(title="Congrats!",
                                             message="You won!")
                root.destroy()
                return

        else:
            global counter_of_mistakes
            global img_start
            global label_start
            counter_of_mistakes += 1
            if counter_of_mistakes == 0:
                pass
            elif counter_of_mistakes == 1:
                img_start = PhotoImage(file="hang5.png")
                label_start = tkinter.Label(image=img_start).place(relwidth=0.4, relheight=0.5, rely=0.3, relx=0.6)
            elif counter_of_mistakes == 2:
                img_start = PhotoImage(file="hang6.png")
                label_start = tkinter.Label(image=img_start).place(relwidth=0.4, relheight=0.5, rely=0.3, relx=0.6)
            elif counter_of_mistakes == 3:
                img_start = PhotoImage(file="hang7.png")
                label_start = tkinter.Label(image=img_start).place(relwidth=0.4, relheight=0.5, rely=0.3, relx=0.6)
            elif counter_of_mistakes == 4:
                img_start = PhotoImage(file="hang8.png")
                label_start = tkinter.Label(image=img_start).place(relwidth=0.4, relheight=0.5, rely=0.3, relx=0.6)
            elif counter_of_mistakes == 5:
                img_start = PhotoImage(file="hang9.png")
                label_start = tkinter.Label(image=img_start).place(relwidth=0.4, relheight=0.5, rely=0.3, relx=0.6)
            elif counter_of_mistakes == 6:
                img_start = PhotoImage(file="hang10.png")
                label_start = tkinter.Label(image=img_start).place(relwidth=0.4, relheight=0.5, rely=0.3, relx=0.6)
            elif counter_of_mistakes == 7:
                img_start = PhotoImage(file="hang11.png")
                label_start = tkinter.Label(image=img_start).place(relwidth=0.4, relheight=0.5, rely=0.3, relx=0.6)
                tkinter.messagebox.showwarning(title="You lost, idiot", message="You lost, bye :)")
                root.destroy()
                return
        word_choice_11.destroy()

def t():
    if valid_bool == False:
        pass
    else:
        if "t" in valid_word:
            for let in range(len(valid_word)):
                if valid_word[let] == "t":
                    list_with_empty_spaces[let] = "t"
            empty_label = tkinter.Label(root, fg="black", font=("Black", 27, "bold"), bg="white",
                                        text=f"{' '.join(list_with_empty_spaces)}")
            empty_label.place(relwidth=0.6, relheight=0.059, rely=0.7)
            if "_" not in list_with_empty_spaces:
                tkinter.messagebox.showinfo(title="Congrats!",
                                             message="You won!")
                root.destroy()
                return

        else:
            global counter_of_mistakes
            global img_start
            global label_start
            counter_of_mistakes += 1
            if counter_of_mistakes == 0:
                pass
            elif counter_of_mistakes == 1:
                img_start = PhotoImage(file="hang5.png")
                label_start = tkinter.Label(image=img_start).place(relwidth=0.4, relheight=0.5, rely=0.3, relx=0.6)
            elif counter_of_mistakes == 2:
                img_start = PhotoImage(file="hang6.png")
                label_start = tkinter.Label(image=img_start).place(relwidth=0.4, relheight=0.5, rely=0.3, relx=0.6)
            elif counter_of_mistakes == 3:
                img_start = PhotoImage(file="hang7.png")
                label_start = tkinter.Label(image=img_start).place(relwidth=0.4, relheight=0.5, rely=0.3, relx=0.6)
            elif counter_of_mistakes == 4:
                img_start = PhotoImage(file="hang8.png")
                label_start = tkinter.Label(image=img_start).place(relwidth=0.4, relheight=0.5, rely=0.3, relx=0.6)
            elif counter_of_mistakes == 5:
                img_start = PhotoImage(file="hang9.png")
                label_start = tkinter.Label(image=img_start).place(relwidth=0.4, relheight=0.5, rely=0.3, relx=0.6)
            elif counter_of_mistakes == 6:
                img_start = PhotoImage(file="hang10.png")
                label_start = tkinter.Label(image=img_start).place(relwidth=0.4, relheight=0.5, rely=0.3, relx=0.6)
            elif counter_of_mistakes == 7:
                img_start = PhotoImage(file="hang11.png")
                label_start = tkinter.Label(image=img_start).place(relwidth=0.4, relheight=0.5, rely=0.3, relx=0.6)
                tkinter.messagebox.showwarning(title="You lost, idiot", message="You lost, bye :)")
                root.destroy()
                return
        word_choice_13.destroy()

def u():
    if valid_bool == False:
        pass
    else:
        if "u" in valid_word:
            for let in range(len(valid_word)):
                if valid_word[let] == "u":
                    list_with_empty_spaces[let] = "u"
            empty_label = tkinter.Label(root, fg="black", font=("Black", 27, "bold"), bg="white",
                                        text=f"{' '.join(list_with_empty_spaces)}")
            empty_label.place(relwidth=0.6, relheight=0.059, rely=0.7)
            if "_" not in list_with_empty_spaces:
                tkinter.messagebox.showinfo(title="Congrats!",
                                             message="You won!")
                root.destroy()
                return

        else:
            global counter_of_mistakes
            global img_start
            global label_start
            counter_of_mistakes += 1
            if counter_of_mistakes == 0:
                pass
            elif counter_of_mistakes == 1:
                img_start = PhotoImage(file="hang5.png")
                label_start = tkinter.Label(image=img_start).place(relwidth=0.4, relheight=0.5, rely=0.3, relx=0.6)
            elif counter_of_mistakes == 2:
                img_start = PhotoImage(file="hang6.png")
                label_start = tkinter.Label(image=img_start).place(relwidth=0.4, relheight=0.5, rely=0.3, relx=0.6)
            elif counter_of_mistakes == 3:
                img_start = PhotoImage(file="hang7.png")
                label_start = tkinter.Label(image=img_start).place(relwidth=0.4, relheight=0.5, rely=0.3, relx=0.6)
            elif counter_of_mistakes == 4:
                img_start = PhotoImage(file="hang8.png")
                label_start = tkinter.Label(image=img_start).place(relwidth=0.4, relheight=0.5, rely=0.3, relx=0.6)
            elif counter_of_mistakes == 5:
                img_start = PhotoImage(file="hang9.png")
                label_start = tkinter.Label(image=img_start).place(relwidth=0.4, relheight=0.5, rely=0.3, relx=0.6)
            elif counter_of_mistakes == 6:
                img_start = PhotoImage(file="hang10.png")
                label_start = tkinter.Label(image=img_start).place(relwidth=0.4, relheight=0.5, rely=0.3, relx=0.6)
            elif counter_of_mistakes == 7:
                img_start = PhotoImage(file="hang11.png")
                label_start = tkinter.Label(image=img_start).place(relwidth=0.4, relheight=0.5, rely=0.3, relx=0.6)
                tkinter.messagebox.showwarning(title="You lost, idiot", message="You lost, bye :)")
                root.destroy()
                return
        word_choice_15.destroy()


def v():
    if valid_bool == False:
        pass
    else:
        if "v" in valid_word:
            for let in range(len(valid_word)):
                if valid_word[let] == "v":
                    list_with_empty_spaces[let] = "v"
            empty_label = tkinter.Label(root, fg="black", font=("Black", 27, "bold"), bg="white",
                                        text=f"{' '.join(list_with_empty_spaces)}")
            empty_label.place(relwidth=0.6, relheight=0.059, rely=0.7)
            if "_" not in list_with_empty_spaces:
                tkinter.messagebox.showinfo(title="Congrats!",
                                             message="You won!")
                root.destroy()
                return

        else:
            global counter_of_mistakes
            global img_start
            global label_start
            counter_of_mistakes += 1
            if counter_of_mistakes == 0:
                pass
            elif counter_of_mistakes == 1:
                img_start = PhotoImage(file="hang5.png")
                label_start = tkinter.Label(image=img_start).place(relwidth=0.4, relheight=0.5, rely=0.3, relx=0.6)
            elif counter_of_mistakes == 2:
                img_start = PhotoImage(file="hang6.png")
                label_start = tkinter.Label(image=img_start).place(relwidth=0.4, relheight=0.5, rely=0.3, relx=0.6)
            elif counter_of_mistakes == 3:
                img_start = PhotoImage(file="hang7.png")
                label_start = tkinter.Label(image=img_start).place(relwidth=0.4, relheight=0.5, rely=0.3, relx=0.6)
            elif counter_of_mistakes == 4:
                img_start = PhotoImage(file="hang8.png")
                label_start = tkinter.Label(image=img_start).place(relwidth=0.4, relheight=0.5, rely=0.3, relx=0.6)
            elif counter_of_mistakes == 5:
                img_start = PhotoImage(file="hang9.png")
                label_start = tkinter.Label(image=img_start).place(relwidth=0.4, relheight=0.5, rely=0.3, relx=0.6)
            elif counter_of_mistakes == 6:
                img_start = PhotoImage(file="hang10.png")
                label_start = tkinter.Label(image=img_start).place(relwidth=0.4, relheight=0.5, rely=0.3, relx=0.6)
            elif counter_of_mistakes == 7:
                img_start = PhotoImage(file="hang11.png")
                label_start = tkinter.Label(image=img_start).place(relwidth=0.4, relheight=0.5, rely=0.3, relx=0.6)
                tkinter.messagebox.showwarning(title="You lost, idiot", message="You lost, bye :)")
                root.destroy()
                return
        word_choice_17.destroy()


def w():
    if valid_bool == False:
        pass
    else:
        if "w" in valid_word:
            for let in range(len(valid_word)):
                if valid_word[let] == "w":
                    list_with_empty_spaces[let] = "w"
            empty_label = tkinter.Label(root, fg="black", font=("Black", 27, "bold"), bg="white",
                                        text=f"{' '.join(list_with_empty_spaces)}")
            empty_label.place(relwidth=0.6, relheight=0.059, rely=0.7)
            if "_" not in list_with_empty_spaces:
                tkinter.messagebox.showinfo(title="Congrats!",
                                             message="You won!")
                root.destroy()
                return

        else:
            global counter_of_mistakes
            global img_start
            global label_start
            counter_of_mistakes += 1
            if counter_of_mistakes == 0:
                pass
            elif counter_of_mistakes == 1:
                img_start = PhotoImage(file="hang5.png")
                label_start = tkinter.Label(image=img_start).place(relwidth=0.4, relheight=0.5, rely=0.3, relx=0.6)
            elif counter_of_mistakes == 2:
                img_start = PhotoImage(file="hang6.png")
                label_start = tkinter.Label(image=img_start).place(relwidth=0.4, relheight=0.5, rely=0.3, relx=0.6)
            elif counter_of_mistakes == 3:
                img_start = PhotoImage(file="hang7.png")
                label_start = tkinter.Label(image=img_start).place(relwidth=0.4, relheight=0.5, rely=0.3, relx=0.6)
            elif counter_of_mistakes == 4:
                img_start = PhotoImage(file="hang8.png")
                label_start = tkinter.Label(image=img_start).place(relwidth=0.4, relheight=0.5, rely=0.3, relx=0.6)
            elif counter_of_mistakes == 5:
                img_start = PhotoImage(file="hang9.png")
                label_start = tkinter.Label(image=img_start).place(relwidth=0.4, relheight=0.5, rely=0.3, relx=0.6)
            elif counter_of_mistakes == 6:
                img_start = PhotoImage(file="hang10.png")
                label_start = tkinter.Label(image=img_start).place(relwidth=0.4, relheight=0.5, rely=0.3, relx=0.6)
            elif counter_of_mistakes == 7:
                img_start = PhotoImage(file="hang11.png")
                label_start = tkinter.Label(image=img_start).place(relwidth=0.4, relheight=0.5, rely=0.3, relx=0.6)
                tkinter.messagebox.showwarning(title="You lost, idiot", message="You lost, bye :)")
                root.destroy()
                return
        word_choice_19.destroy()

def x():
    if valid_bool == False:
        pass
    else:
        if "x" in valid_word:
            for let in range(len(valid_word)):
                if valid_word[let] == "x":
                    list_with_empty_spaces[let] = "x"
            empty_label = tkinter.Label(root, fg="black", font=("Black", 27, "bold"), bg="white",
                                        text=f"{' '.join(list_with_empty_spaces)}")
            empty_label.place(relwidth=0.6, relheight=0.059, rely=0.7)
            if "_" not in list_with_empty_spaces:
                tkinter.messagebox.showinfo(title="Congrats!",
                                             message="You won!")
                root.destroy()
                return

        else:
            global counter_of_mistakes
            global img_start
            global label_start
            counter_of_mistakes += 1
            if counter_of_mistakes == 0:
                pass
            elif counter_of_mistakes == 1:
                img_start = PhotoImage(file="hang5.png")
                label_start = tkinter.Label(image=img_start).place(relwidth=0.4, relheight=0.5, rely=0.3, relx=0.6)
            elif counter_of_mistakes == 2:
                img_start = PhotoImage(file="hang6.png")
                label_start = tkinter.Label(image=img_start).place(relwidth=0.4, relheight=0.5, rely=0.3, relx=0.6)
            elif counter_of_mistakes == 3:
                img_start = PhotoImage(file="hang7.png")
                label_start = tkinter.Label(image=img_start).place(relwidth=0.4, relheight=0.5, rely=0.3, relx=0.6)
            elif counter_of_mistakes == 4:
                img_start = PhotoImage(file="hang8.png")
                label_start = tkinter.Label(image=img_start).place(relwidth=0.4, relheight=0.5, rely=0.3, relx=0.6)
            elif counter_of_mistakes == 5:
                img_start = PhotoImage(file="hang9.png")
                label_start = tkinter.Label(image=img_start).place(relwidth=0.4, relheight=0.5, rely=0.3, relx=0.6)
            elif counter_of_mistakes == 6:
                img_start = PhotoImage(file="hang10.png")
                label_start = tkinter.Label(image=img_start).place(relwidth=0.4, relheight=0.5, rely=0.3, relx=0.6)
            elif counter_of_mistakes == 7:
                img_start = PhotoImage(file="hang11.png")
                label_start = tkinter.Label(image=img_start).place(relwidth=0.4, relheight=0.5, rely=0.3, relx=0.6)
                tkinter.messagebox.showwarning(title="You lost, idiot", message="You lost, bye :)")
                root.destroy()
                return
    word_choice_21.destroy()


def y():
    if valid_bool == False:
        pass
    else:
        if "y" in valid_word:
            for let in range(len(valid_word)):
                if valid_word[let] == "y":
                    list_with_empty_spaces[let] = "y"
            empty_label = tkinter.Label(root, fg="black", font=("Black", 27, "bold"), bg="white",
                                        text=f"{' '.join(list_with_empty_spaces)}")
            empty_label.place(relwidth=0.6, relheight=0.059, rely=0.7)
            if "_" not in list_with_empty_spaces:
                tkinter.messagebox.showinfo(title="Congrats!",
                                             message="You won!")
                root.destroy()
                return

        else:
            global counter_of_mistakes
            global img_start
            global label_start
            counter_of_mistakes += 1
            if counter_of_mistakes == 0:
                pass
            elif counter_of_mistakes == 1:
                img_start = PhotoImage(file="hang5.png")
                label_start = tkinter.Label(image=img_start).place(relwidth=0.4, relheight=0.5, rely=0.3, relx=0.6)
            elif counter_of_mistakes == 2:
                img_start = PhotoImage(file="hang6.png")
                label_start = tkinter.Label(image=img_start).place(relwidth=0.4, relheight=0.5, rely=0.3, relx=0.6)
            elif counter_of_mistakes == 3:
                img_start = PhotoImage(file="hang7.png")
                label_start = tkinter.Label(image=img_start).place(relwidth=0.4, relheight=0.5, rely=0.3, relx=0.6)
            elif counter_of_mistakes == 4:
                img_start = PhotoImage(file="hang8.png")
                label_start = tkinter.Label(image=img_start).place(relwidth=0.4, relheight=0.5, rely=0.3, relx=0.6)
            elif counter_of_mistakes == 5:
                img_start = PhotoImage(file="hang9.png")
                label_start = tkinter.Label(image=img_start).place(relwidth=0.4, relheight=0.5, rely=0.3, relx=0.6)
            elif counter_of_mistakes == 6:
                img_start = PhotoImage(file="hang10.png")
                label_start = tkinter.Label(image=img_start).place(relwidth=0.4, relheight=0.5, rely=0.3, relx=0.6)
            elif counter_of_mistakes == 7:
                img_start = PhotoImage(file="hang11.png")
                label_start = tkinter.Label(image=img_start).place(relwidth=0.4, relheight=0.5, rely=0.3, relx=0.6)
                tkinter.messagebox.showwarning(title="You lost, idiot", message="You lost, bye :)")
                root.destroy()
                return
        word_choice_23.destroy()

def z():
    if valid_bool == False:
        pass
    else:
        if "z" in valid_word:
            for let in range(len(valid_word)):
                if valid_word[let] == "z":
                    list_with_empty_spaces[let] = "z"
            empty_label = tkinter.Label(root, fg="black", font=("Black", 27, "bold"), bg="white",
                                        text=f"{' '.join(list_with_empty_spaces)}")
            empty_label.place(relwidth=0.6, relheight=0.059, rely=0.7)
            if "_" not in list_with_empty_spaces:
                tkinter.messagebox.showinfo(title="Congrats!",
                                             message="You won!")
                root.destroy()
                return

        else:
            global counter_of_mistakes
            global img_start
            global label_start
            counter_of_mistakes += 1
            if counter_of_mistakes == 0:
                pass
            elif counter_of_mistakes == 1:
                img_start = PhotoImage(file="hang5.png")
                label_start = tkinter.Label(image=img_start).place(relwidth=0.4, relheight=0.5, rely=0.3, relx=0.6)
            elif counter_of_mistakes == 2:
                img_start = PhotoImage(file="hang6.png")
                label_start = tkinter.Label(image=img_start).place(relwidth=0.4, relheight=0.5, rely=0.3, relx=0.6)
            elif counter_of_mistakes == 3:
                img_start = PhotoImage(file="hang7.png")
                label_start = tkinter.Label(image=img_start).place(relwidth=0.4, relheight=0.5, rely=0.3, relx=0.6)
            elif counter_of_mistakes == 4:
                img_start = PhotoImage(file="hang8.png")
                label_start = tkinter.Label(image=img_start).place(relwidth=0.4, relheight=0.5, rely=0.3, relx=0.6)
            elif counter_of_mistakes == 5:
                img_start = PhotoImage(file="hang9.png")
                label_start = tkinter.Label(image=img_start).place(relwidth=0.4, relheight=0.5, rely=0.3, relx=0.6)
            elif counter_of_mistakes == 6:
                img_start = PhotoImage(file="hang10.png")
                label_start = tkinter.Label(image=img_start).place(relwidth=0.4, relheight=0.5, rely=0.3, relx=0.6)
            elif counter_of_mistakes == 7:
                img_start = PhotoImage(file="hang11.png")
                label_start = tkinter.Label(image=img_start).place(relwidth=0.4, relheight=0.5, rely=0.3, relx=0.6)
                tkinter.messagebox.showwarning(title="You lost, idiot", message="You lost, bye :)")
                root.destroy()
                return
        word_choice_25.destroy()


def on_click_button_play():
    text = entry_player.get()
    if len(text) == 0:
        return
    else:
        pattern = fr"\b^[a-z]+$"
        match = re.findall(pattern, text)
        if match:
            global valid_word
            valid_word_1 = match[0]
            valid_word_2 = [w for w in valid_word_1]
            valid_word = valid_word_2
            entry_player.delete(0, len(text))
            label_entry.destroy()
            play_button.destroy()
            entry_player.destroy()
            global list_with_empty_spaces
            list_with_empty_spaces = ['_' for a in valid_word_1]
            global valid_bool
            valid_bool = True
            empty_label_1 = tkinter.Label(root, fg="black", font=("Black", 27, "bold"), bg="white",
                                         text=f"{len(list_with_empty_spaces) * '_ '}")
            empty_label_1.place(relwidth=0.6, relheight=0.059, rely=0.7)
            global image_start
            global img_label
            image_start = tkinter.PhotoImage(file="hang2.png")
            img_label = tkinter.Label(image=image_start).place(relwidth=0.4, relheight=0.5, rely=0.3, relx=0.6)

        elif len(match) == 0:
            tkinter.messagebox.showerror(title="Invalid input",
                                         message="Word cannot contain numbers, symbols, space or capital letters!")
            entry_player.delete(0, len(text))


root = tkinter.Tk()
title = root.title("Hangman game")
root.geometry("1000x600+50+50")

image_start = tkinter.PhotoImage(file="hang2.png")
img_label = tkinter.Label(image=image_start).place(relwidth=0.4, relheight=0.5, rely=0.3, relx=0.6)

my_canvas = tkinter.Canvas(root, bg="white", height=600, width=1000)
my_canvas.pack()

label_welcome = tkinter.Label(root, font=('White', 45, 'bold'), fg="Black", text="Welcome to Hangman!", bg="white")
label_welcome.place(relwidth=0.7, relheight=0.12, rely=0.1, relx=0.12)

label_entry = tkinter.Label(root, font=('White', 17,
                                        'bold'), fg="Black", text=f"Enter your chosen word below:", bg="white")
label_entry.place(relwidth=0.35, relheight=0.059, rely=0.4)

entry_player = tkinter.Entry(root, bg="Black", fg='white')
entry_player.place(relwidth=0.31, relheight=0.059, rely=0.5)

play_button = tkinter.Button(root, font=('Black', 17, 'bold'), fg="White", bg="BLack", text="Play",
                             command=on_click_button_play)
play_button.place(relwidth=0.17, relheight=0.059, rely=0.5, relx=0.32)

word_choice = tkinter.Button(root, bg="Black", fg="White", text="N", command=n)
word_choice.place(relwidth=0.05, relheight=0.05, rely=0.9, relx=0.01)

word_choice_2 = tkinter.Button(root, bg="Black", fg="White", text="A", command=a)
word_choice_2.place(relwidth=0.05, relheight=0.05, rely=0.84, relx=0.01)

word_choice_3 = tkinter.Button(root, bg="Black", fg="White", text="O", command=o)
word_choice_3.place(relwidth=0.05, relheight=0.05, rely=0.9, relx=0.07)

word_choice_4 = tkinter.Button(root, bg="Black", fg="White", text="B", command=b)
word_choice_4.place(relwidth=0.05, relheight=0.05, rely=0.84, relx=0.07)

word_choice_5 = tkinter.Button(root, bg="Black", fg="White", text="C", command=c)
word_choice_5.place(relwidth=0.05, relheight=0.05, rely=0.84, relx=0.13)

word_choice_6 = tkinter.Button(root, bg="Black", fg="White", text="P", command=p)
word_choice_6.place(relwidth=0.05, relheight=0.05, rely=0.9, relx=0.13)

word_choice_7 = tkinter.Button(root, bg="Black", fg="White", text="Q", command=q)
word_choice_7.place(relwidth=0.05, relheight=0.05, rely=0.9, relx=0.19)

word_choice_8 = tkinter.Button(root, bg="Black", fg="White", text="D", command=d)
word_choice_8.place(relwidth=0.05, relheight=0.05, rely=0.84, relx=0.19)

word_choice_9 = tkinter.Button(root, bg="Black", fg="White", text="R", command=r)
word_choice_9.place(relwidth=0.05, relheight=0.05, rely=0.9, relx=0.25)

word_choice_10 = tkinter.Button(root, bg="Black", fg="White", text="E", command=e)
word_choice_10.place(relwidth=0.05, relheight=0.05, rely=0.84, relx=0.25)

word_choice_11 = tkinter.Button(root, bg="Black", fg="White", text="S", command=s)
word_choice_11.place(relwidth=0.05, relheight=0.05, rely=0.9, relx=0.31)

word_choice_12 = tkinter.Button(root, bg="Black", fg="White", text="F", command=f)
word_choice_12.place(relwidth=0.05, relheight=0.05, rely=0.84, relx=0.31)

word_choice_13 = tkinter.Button(root, bg="Black", fg="White", text="T", command=t)
word_choice_13.place(relwidth=0.05, relheight=0.05, rely=0.9, relx=0.37)

word_choice_14 = tkinter.Button(root, bg="Black", fg="White", text="G", command=g)
word_choice_14.place(relwidth=0.05, relheight=0.05, rely=0.84, relx=0.37)

word_choice_15 = tkinter.Button(root, bg="Black", fg="White", text="U", command=u)
word_choice_15.place(relwidth=0.05, relheight=0.05, rely=0.9, relx=0.43)

word_choice_16 = tkinter.Button(root, bg="Black", fg="White", text="H", command=h)
word_choice_16.place(relwidth=0.05, relheight=0.05, rely=0.84, relx=0.43)

word_choice_17 = tkinter.Button(root, bg="Black", fg="White", text="V", command=v)
word_choice_17.place(relwidth=0.05, relheight=0.05, rely=0.9, relx=0.49)

word_choice_18 = tkinter.Button(root, bg="Black", fg="White", text="I", command=i)
word_choice_18.place(relwidth=0.05, relheight=0.05, rely=0.84, relx=0.49)

word_choice_19 = tkinter.Button(root, bg="Black", fg="White", text="W", command=w)
word_choice_19.place(relwidth=0.05, relheight=0.05, rely=0.9, relx=0.55)

word_choice_20 = tkinter.Button(root, bg="Black", fg="White", text="J", command=j)
word_choice_20.place(relwidth=0.05, relheight=0.05, rely=0.84, relx=0.55)

word_choice_21 = tkinter.Button(root, bg="Black", fg="White", text="X", command=x)
word_choice_21.place(relwidth=0.05, relheight=0.05, rely=0.9, relx=0.61)

word_choice_22 = tkinter.Button(root, bg="Black", fg="White", text="K", command=k)
word_choice_22.place(relwidth=0.05, relheight=0.05, rely=0.84, relx=0.61)

word_choice_23 = tkinter.Button(root, bg="Black", fg="White", text="Y", command=y)
word_choice_23.place(relwidth=0.05, relheight=0.05, rely=0.9, relx=0.67)

word_choice_24 = tkinter.Button(root, bg="Black", fg="White", text="L", command=l)
word_choice_24.place(relwidth=0.05, relheight=0.05, rely=0.84, relx=0.67)

word_choice_25 = tkinter.Button(root, bg="Black", fg="White", text="Z", command=z)
word_choice_25.place(relwidth=0.05, relheight=0.05, rely=0.9, relx=0.73)

word_choice_26 = tkinter.Button(root, bg="Black", fg="White", text="M", command=m)
word_choice_26.place(relwidth=0.05, relheight=0.05, rely=0.84, relx=0.73)

play_again_but = tkinter.Button(root, bg="Black", font=("White", 20, 'bold'), fg='White', text="Play again")
play_again_but.place(relwidth=0.15, relheight=0.11, rely=0.84, relx=0.8)
root.mainloop()
