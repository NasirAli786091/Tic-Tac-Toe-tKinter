from tkinter import *
from tkinter import messagebox

win = Tk()
win.title("TIC TAC TOE")


def disableB():
    b1.config(state=DISABLED)
    b2.config(state=DISABLED)
    b3.config(state=DISABLED)
    b4.config(state=DISABLED)
    b5.config(state=DISABLED)
    b6.config(state=DISABLED)
    b7.config(state=DISABLED)
    b8.config(state=DISABLED)
    b9.config(state=DISABLED)


clicked = True
count = 0

def checkIfWon():
    global winner
    winner = False
    winingCom = [
        (b1, b2, b3), (b4, b5, b6), (b7, b8, b9),  # Horizontal
        (b1, b4, b7), (b2, b5, b8), (b3, b6, b9),  # Vertical
        (b1, b5, b9), (b3, b5, b7) #diagonal
        ]
    for combo in winingCom:
        if combo[0]["text"] == combo[1]["text"] == combo[2]["text"] != " ":
            for b in combo:
                b.config(bg="Red")
            winner = True
            messagebox.showinfo("Tic Tac Toe", f"Congratulations {combo[0]['text']} won!!!")
            disableB()
            break
        elif count == 9:
            messagebox.showinfo("Tic Tac Toe", f"DRAW!!")
            break

def buttonClicked(b):
    global clicked, count
    if b["text"] == " " and clicked == True:
        b["text"] = "X"
        clicked = False
        count += 1
        checkIfWon()
    elif b["text"] == " " and clicked == False:
        b["text"] = "O"
        clicked = True
        count += 1
        checkIfWon()
    else:
        messagebox.showerror("Tic Tac Toe! Hey that place has been selected")

def createButtons():
    global b1, b2, b3, b4, b5, b6, b7, b8, b9
    but = [b1, b2, b3, b4, b5, b6, b7, b8, b9]
    #create buttons

    r = 0
    c = 0
    for i in but:
        i = Button(win, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda:buttonClicked(b1))
        i.grid(row=r, column=c)
        if r == 4 or c == 4:
            if r == 4:
                r = 0
            if c == 4:
                c = 0
        else:
            pass            

    # b1 = Button(win, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda:buttonClicked(b1))
    # b2 = Button(win, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda:buttonClicked(b2))
    # b3 = Button(win, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda:buttonClicked(b3))
    
    # b4 = Button(win, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda:buttonClicked(b4))
    # b5 = Button(win, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda:buttonClicked(b5))
    # b6 = Button(win, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda:buttonClicked(b6))

    # b7 = Button(win, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda:buttonClicked(b7))
    # b8 = Button(win, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda:buttonClicked(b8))
    # b9 = Button(win, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda:buttonClicked(b9))

    #grid out the buttons on the screen
    i = 0
    j = 0


    b1.grid(row=0, column=0)
    b2.grid(row=0, column=1)
    b3.grid(row=0, column=2)

    b4.grid(row=1, column=0)
    b5.grid(row=1, column=1)
    b6.grid(row=1, column=2)

    b7.grid(row=2, column=0)
    b8.grid(row=2, column=1)
    b9.grid(row=2, column=2)

createButtons()


win.mainloop()