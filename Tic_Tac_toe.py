from tkinter import *
from tkinter import messagebox
root=Tk()
root.title("Mallesh_TIC-TAC-TOE")
# root.geometry(120100)
#-------1.creating buttons for the game----
#-----button clicked function----

def disable_all_buttons():
    b1.config(state=DISABLED)
    b2.config(state=DISABLED)
    b3.config(state=DISABLED)
    b4.config(state=DISABLED)
    b5.config(state=DISABLED)
    b6.config(state=DISABLED)
    b7.config(state=DISABLED)
    b8.config(state=DISABLED)
    b9.config(state=DISABLED)

    
    

def checkwinner():
    global winner
    winner=False
    #----------------check if Player X wins-----------------------
    if b1["text"]=="X" and b2["text"]=="X" and b3["text"]=="X":
        b1.config(bg="green")
        b2.config(bg="green")
        b3.config(bg="green")
        winner=True
        messagebox.showinfo("TIC TAC TOE","Congratulations! player-X wins!")
        disable_all_buttons()
    elif b4["text"]=="X" and b5["text"]=="X" and b6["text"]=="X":
        b4.config(bg="green")
        b5.config(bg="green")
        b6.config(bg="green")
        winner=True
        messagebox.showinfo("TIC TAC TOE","Congratulations! player-X  wins!")
        disable_all_buttons()

    elif b7["text"]=="X" and b8["text"]=="X" and b9["text"]=="X":
        b7.config(bg="green")
        b8.config(bg="green")
        b9.config(bg="green")
        winner=True
        messagebox.showinfo("TIC TAC TOE","Congratulations! player-X wins!")
        disable_all_buttons()
    elif b1["text"]=="X" and b5["text"]=="X" and b9["text"]=="X":
        b1.config(bg="green")
        b5.config(bg="green")
        b9.config(bg="green")
        winner=True
        messagebox.showinfo("TIC TAC TOE","Congratulations! player-X wins!")
        disable_all_buttons()
        Reset()
    elif b1["text"]=="X" and b4["text"]=="X" and b7["text"]=="X":
        b1.config(bg="green")
        b4.config(bg="green")
        b7.config(bg="green")
        winner=True
        messagebox.showinfo("TIC TAC TOE","Congratulations! player-X wins!")
        disable_all_buttons()
        Reset()

    elif b3["text"]=="X" and b6["text"]=="X" and b9["text"]=="X":
        b3.config(bg="green")
        b6.config(bg="green")
        b9.config(bg="green")
        winner=True
        messagebox.showinfo("TIC TAC TOE","Congratulations! player-X wins!")
        disable_all_buttons()
        Reset()
    elif b2["text"] == "X" and b5["text"] == "X" and b8["text"] == "X":
        b2.config(bg="green")
        b5.config(bg="green")
        b8.config(bg="green")
        winner = True
        messagebox.showinfo("TIC TAC TOE", "Congratulations! player-X wins!")
        disable_all_buttons()
        Reset()
    elif b3["text"] == "X" and b5["text"] == "X" and b7["text"] == "X":
        b3.config(bg="green")
        b5.config(bg="green")
        b7.config(bg="green")
        winner = True
        messagebox.showinfo("TIC TAC TOE", "Congratulations! player-X is wins!")
        disable_all_buttons()
        Reset()
 #----------------check if Player O wins-----------------------
    elif b1["text"]=="O" and b2["text"]=="O" and b3["text"]=="O":
        b1.config(bg="green")
        b2.config(bg="green")
        b3.config(bg="green")
        winner=True
        messagebox.showinfo("TIC TAC TOE","Congratulations! player-O wins!")
        disable_all_buttons()
        Reset()
    elif b4["text"]=="O" and b5["text"]=="O" and b6["text"]=="0":
        b4.config(bg="green")
        b5.config(bg="green")
        b6.config(bg="green")
        winner=True
        messagebox.showinfo("TIC TAC TOE","Congratulations! player-O wins!")
        disable_all_buttons()
        Reset()

    elif b7["text"]=="O" and b8["text"]=="O" and b9["text"]=="O":
        b7.config(bg="green")
        b8.config(bg="green")
        b9.config(bg="green")
        winner=True
        messagebox.showinfo("TIC TAC TOE","Congratulations! player-0 wins!")
        disable_all_buttons()
        Reset()
    elif b1["text"]=="O" and b5["text"]=="O" and b9["text"]=="O":
        b1.config(bg="green")
        b5.config(bg="green")
        b9.config(bg="green")
        winner=True
        messagebox.showinfo("TIC TAC TOE","Congratulations! player-O wins!")
        disable_all_buttons()
        Reset()
    elif b1["text"]=="O" and b4["text"]=="O" and b7["text"]=="O":
        b1.config(bg="green")
        b4.config(bg="green")
        b7.config(bg="green")
        winner=True
        messagebox.showinfo("TIC TAC TOE","Congratulations! player-O wins!")
        disable_all_buttons()
        Reset()
    elif b3["text"]=="O" and b6["text"]=="O" and b9["text"]=="O":
        b3.config(bg="green")
        b6.config(bg="green")
        b9.config(bg="green")
        winner=True
        messagebox.showinfo("TIC TAC TOE","Congratulations! player-O wins!")
        disable_all_buttons()
        Reset()
    elif b2["text"] == "O" and b5["text"] == "O" and b8["text"] == "O":
        b2.config(bg="green")
        b5.config(bg="green")
        b8.config(bg="green")
        winner = True
        messagebox.showinfo("TIC TAC TOE", "Congratulations! player-O  wins!")
        disable_all_buttons()
        Reset()
    elif b3["text"] == "O" and b5["text"] == "O" and b7["text"] == "O":
        b3.config(bg="green")
        b5.config(bg="green")
        b7.config(bg="green")
        winner = True
        messagebox.showinfo("TIC TAC TOE", "Congratulations! player-O wins!")
        disable_all_buttons()
        Reset()

    elif count>=9:
        messagebox.showinfo("It's a tie")
        Reset()
   


clicked=True
count=0
def b_click(b):
    global clicked,count
    if b["text"]==" " and clicked==True:
        b["text"]="X"
        clicked=False
        count+=1
        checkwinner()
    elif b["text"]==" " and clicked==False:
        b["text"]="O"
        clicked=True
        count+=1
        checkwinner()
    else:
        messagebox.showerror("TIC-TAC_TOE","This box has already been clicked.\n click another one")


def Reset():
    global clicked,count
    global b1,b2,b3,b4,b5,b6,b7,b8,b9
    clicked=True
    count=0
#------------------1st row------------------------------
    b1=Button(root,text=" ",font=("Helvetica",20),height=3,width=6,bg="SystemButtonFace",command=lambda:b_click(b1))
    b2=Button(root,text=" ",font=("Helvetica",20),height=3,width=6,bg="SystemButtonFace",command=lambda:b_click(b2))
    b3=Button(root,text=" ",font=("Helvetica",20),height=3,width=6,bg="SystemButtonFace",command=lambda:b_click(b3))
    #------------------2nd row--------------------------------
    b4=Button(root,text=" ",font=("Helvetica",20),height=3,width=6,bg="SystemButtonFace",command=lambda:b_click(b4))
    b5=Button(root,text=" ",font=("Helvetica",20),height=3,width=6,bg="SystemButtonFace",command=lambda:b_click(b5))
    b6=Button(root,text=" ",font=("Helvetica",20),height=3,width=6,bg="SystemButtonFace",command=lambda:b_click(b6))
    #------------------3rd row-------------------------------
    b7=Button(root,text=" ",font=("Helvetica",20),height=3,width=6,bg="SystemButtonFace",command=lambda:b_click(b7))
    b8=Button(root,text=" ",font=("Helvetica",20),height=3,width=6,bg="SystemButtonFace",command=lambda:b_click(b8))
    b9=Button(root,text=" ",font=("Helvetica",20),height=3,width=6,bg="SystemButtonFace",command=lambda:b_click(b9))
    #-----lets grid our buttons on the screeen---
    b1.grid(row=0,column=0)
    b2.grid(row=0,column=1)
    b3.grid(row=0,column=2)

    b4.grid(row=1,column=0)
    b5.grid(row=1,column=1)
    b6.grid(row=1,column=2)

    b7.grid(row=2,column=0)
    b8.grid(row=2,column=1)
    b9.grid(row=2,column=2)

#-------------create menu------------
my_menu=Menu(root)
root.config(menu=my_menu)
#-----creating options menu----
options_menu=Menu(my_menu,tearoff=False)
my_menu.add_cascade(label="options",menu=options_menu)
options_menu.add_command(label="Reset Game",command=Reset)
Reset()
root.mainloop()
