from tkinter import *
from PIL import Image, ImageTk
from random import randint

#window
root = Tk()
root.title("Rock Scissor Paper")
root.configure(background="green")

#gambar
rock_img_user =ImageTk.PhotoImage(Image.open("rock-user.png"))
paper_img_user= ImageTk.PhotoImage(Image.open("paper-user.png"))
scissors_img_user = ImageTk.PhotoImage(Image.open("scissors-user.png"))
rock_img_user_comp = ImageTk.PhotoImage(Image.open("rock.png"))
paper_img_user_comp = ImageTk.PhotoImage(Image.open("paper.png"))
scissors_img_user_comp = ImageTk.PhotoImage(Image.open("scissors.png"))

#penisipan gambar
user_label = Label(root, image=scissors_img_user, bg="green")
comp_label = Label(root, image=scissors_img_user_comp, bg="green")
comp_label.grid(row=1, column= 0)
user_label.grid(row=1, column= 4)

#skor
playerScore = Label(root, text=0, font=100, bg="green", fg="white")
computerScore = Label(root, text=0, font=100, bg="green", fg="white")
computerScore.grid(row=1, column=1)
playerScore.grid(row=1, column=3)

#indikasi
user_indicator= Label(root,font=50,text="USER", bg="green", fg="white")
comp_indicator = Label(root,font=50,text="COMPUTER", bg="green", fg="white")
user_indicator.grid(row=0, column=  3)
comp_indicator.grid(row=0, column=1)

#pesan terbarru
def updateMessage(x):
    msg["text"] = x

#user skor terbaru
def updateUserScore():
    score = int(playerScore["text"])
    score +=1
    playerScore["text"] = str(score)

#komputer skor terbaru
def updateCompScore():
    score = int(computerScore["text"])
    score +=1
    computerScore["text"] = str(score)

#mengecek pemenang
def checkWinner(player, computer):
    if player == computer:
        updateMessage("Seri")
    elif player == "rock":
        if computer == "paper":
            updateMessage("Kamu Kalah")
            updateCompScore()
        else:
            updateMessage("Kamu Menang")
            updateUserScore()
    elif player == "paper" :
        if computer == "scissor":
            updateMessage("Kamu Kalah")
            updateCompScore()
        else:
            updateMessage("Kamu Menang")
            updateUserScore()
    elif player == "scissor":
        if computer == "rock":
            updateMessage("Kamu Kalah")
            updateCompScore()
        else:
            updateMessage("Kamu Menang")
            updateUserScore()
    else:
        pass


#reset
def resetGame():
    point =0
    computerScore["text"] = str(point)
    playerScore["text"]= str(point)
    scoresss = ""
    msg["text"]=str(scoresss)
#pilihan terbaru
choices = ["rock", "paper", "scissor"]
def updateChoice(x):

#untuk komputer
    compChoice = choices[randint(0, 2)]
    if compChoice == "rock":
        comp_label.configure(image=rock_img_user_comp)
    elif compChoice =="paper":
        comp_label.configure(image=paper_img_user_comp)
    else:
        comp_label.configure(image=scissors_img_user_comp)
    checkWinner(x, compChoice)

#untuk user
    if x=="rock":
        user_label.configure(image=rock_img_user)
    elif x=="paper":
        user_label.configure(image=paper_img_user)
    else:
        user_label.configure(image=scissors_img_user)

#isi pesan
msg = Label(root,font=50, bg="green", fg="white")
msg.grid(row= 3, column= 2  )

#tombol
rock = Button(root, width=20, height=2, text="ROCK", bg="#FF3E4D", fg="white", command=lambda:updateChoice("rock")).grid(row= 2, column= 1 )
paper = Button(root, width=20, height=2, text="PAPER", bg="#FAD02E", fg="white", command=lambda:updateChoice("paper")).grid(row= 2, column= 2 )
scissors = Button(root, width=20, height=2, text="SCISSORS", bg="#0ABDE3", fg="white", command=lambda:updateChoice("scissor")).grid(row= 2, column= 3 )
replay = Button(root, width=20, height=2, text="Reset", bg="purple", fg="white", command=lambda:resetGame()).grid(row= 1, column= 2 )
root.mainloop()