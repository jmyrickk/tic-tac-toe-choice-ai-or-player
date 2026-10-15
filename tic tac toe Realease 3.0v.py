#imports

import customtkinter as ctk
import os, sys
from tkinter import messagebox
import random

#def
def openicon(put):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, put)
    return os.path.join(os.path.abspath("."), put)
def Cs():
    if FirstPWillBe=="player 1: x" and WhoWithWho=="PlAi":
        #prioritets 1. win 2. block 3. centr 4. couriers 5. 1, 3, 5, 7
        #win
        for i,o,p in winingComb:
            buttonText=[butons[i].cget("text"), butons[o].cget("text"), butons[p].cget("text")]
            if buttonText.count("o")==2 and buttonText.count(" ")==1:
                indxOfNothing=[i, o, p][buttonText.index(" ")]
                butons[indxOfNothing].configure(text="o")
                Win()
                return
        #block
        for i,o,p in winingComb:
            buttonText=[butons[i].cget("text"), butons[o].cget("text"), butons[p].cget("text")]
            if buttonText.count("x")==2 and buttonText.count(" ")==1:
                indxOfNothing=[i,o,p][buttonText.index(" ")]
                butons[indxOfNothing].configure(text="o")
                Win()
                return
        #centr
        if butons[4].cget("text")==" ":
            butons[4].configure(text="o", text_color="black")
            Win()
            return
        #couriers
        if butons[0].cget("text")==" " or butons[2].cget("text")==" " or butons[6].cget("text")==" " or butons[8].cget("text")==" ":
            indxOfNothing = []
            for i in [0, 2, 6, 8]:
                if butons[i].cget("text")==" ":
                    indxOfNothing.append(i)
            rcs=random.choice(indxOfNothing)
            butons[rcs].configure(text="o")
            Win()
            return
        #1, 3, 5, 7
        if butons[1].cget("text") == " " or butons[3].cget("text") == " " or butons[5].cget("text") == " " or butons[7].cget("text") == " ":
            indxOfNothing = []
            for i in [1, 3, 5, 7]:
                if butons[i].cget("text")==" ":
                    indxOfNothing.append(i)
            rcs=random.choice(indxOfNothing)
            butons[rcs].configure(text="o")
            Win()
            return
    elif FirstPWillBe=="player 1: o" and WhoWithWho=="PlAi":
        #prioritets 1. win 2. block 3. centr 4. couriers 5. 1, 3, 5, 7
        #win
        for i,o,p in winingComb:
            buttonText=[butons[i].cget("text"), butons[o].cget("text"), butons[p].cget("text")]
            if buttonText.count("x")==2 and buttonText.count(" ")==1:
                indxOfNothing=[i, o, p][buttonText.index(" ")]
                butons[indxOfNothing].configure(text="x")
                Win()
                return
        #block
        for i,o,p in winingComb:
            buttonText=[butons[i].cget("text"), butons[o].cget("text"), butons[p].cget("text")]
            if buttonText.count("o")==2 and buttonText.count(" ")==1:
                indxOfNothing=[i,o,p][buttonText.index(" ")]
                butons[indxOfNothing].configure(text="x")
                Win()
                return
        #centr
        if butons[4].cget("text")==" ":
            butons[4].configure(text="x", text_color="black")
            Win()
            return
        #couriers
        if butons[0].cget("text")==" " or butons[2].cget("text")==" " or butons[6].cget("text")==" " or butons[8].cget("text")==" ":
            indxOfNothing = []
            for i in [0, 2, 6, 8]:
                if butons[i].cget("text")==" ":
                    indxOfNothing.append(i)
            rcs=random.choice(indxOfNothing)
            butons[rcs].configure(text="x")
            Win()
            return
        #1, 3, 5, 7
        if butons[1].cget("text") == " " or butons[3].cget("text") == " " or butons[5].cget("text") == " " or butons[7].cget("text") == " ":
            indxOfNothing = []
            for i in [1, 3, 5, 7]:
                if butons[i].cget("text")==" ":
                    indxOfNothing.append(i)
            rcs=random.choice(indxOfNothing)
            butons[rcs].configure(text="x")
            Win()
            return
    elif FirstPWillBe=="player 1: x" and WhoWithWho=="AiPl":
        #prioritets 1. win 2. block 3. centr 4. couriers 5. 1, 3, 5, 7
        #win
        for i,o,p in winingComb:
            buttonText=[butons[i].cget("text"), butons[o].cget("text"), butons[p].cget("text")]
            if buttonText.count("x")==2 and buttonText.count(" ")==1:
                indxOfNothing=[i, o, p][buttonText.index(" ")]
                butons[indxOfNothing].configure(text="x")
                Win()
                return
        #block
        for i,o,p in winingComb:
            buttonText=[butons[i].cget("text"), butons[o].cget("text"), butons[p].cget("text")]
            if buttonText.count("o")==2 and buttonText.count(" ")==1:
                indxOfNothing=[i,o,p][buttonText.index(" ")]
                butons[indxOfNothing].configure(text="x")
                Win()
                return
        #centr
        if butons[4].cget("text")==" ":
            butons[4].configure(text="x", text_color="black")
            Win()
            return
        #couriers
        if butons[0].cget("text")==" " or butons[2].cget("text")==" " or butons[6].cget("text")==" " or butons[8].cget("text")==" ":
            indxOfNothing = []
            for i in [0, 2, 6, 8]:
                if butons[i].cget("text")==" ":
                    indxOfNothing.append(i)
            rcs=random.choice(indxOfNothing)
            butons[rcs].configure(text="x")
            Win()
            return
        #1, 3, 5, 7
        if butons[1].cget("text") == " " or butons[3].cget("text") == " " or butons[5].cget("text") == " " or butons[7].cget("text") == " ":
            indxOfNothing = []
            for i in [1, 3, 5, 7]:
                if butons[i].cget("text")==" ":
                    indxOfNothing.append(i)
            rcs=random.choice(indxOfNothing)
            butons[rcs].configure(text="x")
            Win()
            return
    elif FirstPWillBe=="player 1: o" and WhoWithWho=="AiPl":
        #prioritets 1. win 2. block 3. centr 4. couriers 5. 1, 3, 5, 7
        #win
        for i,o,p in winingComb:
            buttonText=[butons[i].cget("text"), butons[o].cget("text"), butons[p].cget("text")]
            if buttonText.count("o")==2 and buttonText.count(" ")==1:
                indxOfNothing=[i, o, p][buttonText.index(" ")]
                butons[indxOfNothing].configure(text="o")
                Win()
                return
        #block
        for i,o,p in winingComb:
            buttonText=[butons[i].cget("text"), butons[o].cget("text"), butons[p].cget("text")]
            if buttonText.count("x")==2 and buttonText.count(" ")==1:
                indxOfNothing=[i,o,p][buttonText.index(" ")]
                butons[indxOfNothing].configure(text="o")
                Win()
                return
        #centr
        if butons[4].cget("text")==" ":
            butons[4].configure(text="o", text_color="black")
            Win()
            return
        #couriers
        if butons[0].cget("text")==" " or butons[2].cget("text")==" " or butons[6].cget("text")==" " or butons[8].cget("text")==" ":
            indxOfNothing = []
            for i in [0, 2, 6, 8]:
                if butons[i].cget("text")==" ":
                    indxOfNothing.append(i)
            rcs=random.choice(indxOfNothing)
            butons[rcs].configure(text="o")
            Win()
            return
        #1, 3, 5, 7
        if butons[1].cget("text") == " " or butons[3].cget("text") == " " or butons[5].cget("text") == " " or butons[7].cget("text") == " ":
            indxOfNothing = []
            for i in [1, 3, 5, 7]:
                if butons[i].cget("text")==" ":
                    indxOfNothing.append(i)
            rcs=random.choice(indxOfNothing)
            butons[rcs].configure(text="o")
            Win()
            return
def Win():
    global FPWins, LabelStats, SPWins, PlayedGames, Tie
    for i,o,p in winingComb:
        if butons[i].cget("text")=="x" and butons[o].cget("text")=="x" and butons[p].cget("text")=="x" and FirstPWillBe=="player 1: x":
            print("win x")
            FPWins+=1
            PlayedGames+=1
            LabelStats.configure(text=f"Wins of player 1: {FPWins}           Wins of player 2: {SPWins}                 Alredy played games: {PlayedGames}              Ties={Tie}", fg_color="white", text_color="black")
            messagebox.showinfo(title="win", message="x has win")
            for bb in butons:
                bb.configure(fg_color="green", text="x win", font=("Courier", 30, "bold"))
            return
        elif butons[i].cget("text")=="o" and butons[o].cget("text")=="o" and butons[p].cget("text")=="o" and FirstPWillBe=="player 1: o":
            print("win o")
            FPWins += 1
            PlayedGames += 1
            LabelStats.configure(text=f"Wins of player 1: {FPWins}           Wins of player 2: {SPWins}                 Alredy played games: {PlayedGames}              Ties={Tie}", fg_color="white", text_color="black")
            messagebox.showinfo(title="win", message="o has win")
            for aa in butons:
                aa.configure(fg_color="green", text="o win", font=("Courier", 30, "bold"))
            return
        elif butons[i].cget("text")=="x" and butons[o].cget("text")=="x" and butons[p].cget("text")=="x" and FirstPWillBe!="player 1: x":
            print("win x")
            SPWins+=1
            PlayedGames+=1
            LabelStats.configure(text=f"Wins of player 1: {FPWins}           Wins of player 2: {SPWins}                 Alredy played games: {PlayedGames}              Ties={Tie}", fg_color="white", text_color="black")
            messagebox.showinfo(title="win", message="x has win")
            for bb in butons:
                bb.configure(fg_color="green", text="x win", font=("Courier", 30, "bold"))
            return
        elif butons[i].cget("text")=="o" and butons[o].cget("text")=="o" and butons[p].cget("text")=="o" and FirstPWillBe!="player 1: o":
            print("win o")
            SPWins += 1
            PlayedGames += 1
            LabelStats.configure(text=f"Wins of player 1: {FPWins}           Wins of player 2: {SPWins}                 Alredy played games: {PlayedGames}              Ties={Tie}", fg_color="white", text_color="black")
            messagebox.showinfo(title="win", message="o has win")
            for aa in butons:
                aa.configure(fg_color="green", text="o win", font=("Courier", 30, "bold"))
            return
    NoneButtons=0
    for Knopcka1 in butons:
        if Knopcka1.cget("text")==" ":
            NoneButtons+=1
    if NoneButtons==0 and butons[0].cget("text")!="o win"  and butons[0].cget("text")!="x win":
        Tie += 1
        PlayedGames += 1
        LabelStats.configure(text=f"Wins of player 1: {FPWins}           Wins of player 2: {SPWins}                 Alredy played games: {PlayedGames}              Ties={Tie}", fg_color="white", text_color="black")
        messagebox.showinfo(title="TIE!", message="Tie!")
        for cc in butons:
            cc.configure(fg_color="black", text="Tie", text_color="white", font=("Courier", 30, "bold"))
def GameOver():
    return butons[0].cget("text") in ("x win", "o win", "Tie")
def step(indx):
    global wstep, butons
    if WhoWithWho == "PlPl":
        if butons[indx].cget("text") == " ":
            butons[indx].configure(text=wstep)
            wstep = "o" if wstep == "x" else "x"
        Win()
    elif WhoWithWho=="PlAi" or WhoWithWho=="AiPl":
        if butons[indx].cget("text") == " " and not GameOver():
            butons[indx].configure(text=wstep)
            Win()
            if not GameOver():
                Cs()
def StartGame():
    global WhoWithWho, wstep, WillBePlF, WillBePlS, WillGoF, FirstPWillBe
    for e in range(9):
        butons[e].configure(fg_color="white", font=("Courier", 100, "bold"), text=" ", text_color="black")
    WillBePlF = ChoicePlayerF.get()
    WillBePlS = ChoicePlayerS.get()
    WillGoF = ChoiceStepF.get()
    FirstPWillBe = ChoiceWhoWBFP.get()
    if WillBePlF == "player 1" and WillBePlS == "player 2":
        WhoWithWho = "PlPl"
    elif WillBePlF == "player 1" and WillBePlS == "AI":
        WhoWithWho = "PlAi"
    elif WillBePlF == "AI" and WillBePlS == "player 2":
        WhoWithWho = "AiPl"
    p1 = "x" if FirstPWillBe == "player 1: x" else "o"
    p2 = "o" if p1 == "x" else "x"
    if WhoWithWho == "PlAi":
        wstep = p1
    elif WhoWithWho == "AiPl":
        wstep = p2
    else:
        wstep = p1 if WillGoF == "player 1" else p2
    if (WhoWithWho == "AiPl" and WillGoF == "player 1") or \
       (WhoWithWho == "PlAi" and WillGoF == "player 2"):
        Cs()
window=ctk.CTk("black")
window.geometry("890x755+380+0")
window.title("jmyrickk tic tac toes")
window.wm_iconbitmap("imag.ico")
FPWins=0
SPWins=0
PlayedGames=0
Tie=0
WhoWithWho=""
wstep="x"
butons=[]
winingComb=((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 4, 8), (2, 4, 6), (0, 3, 6), (1, 4, 7), (2, 5, 8))
WillBePlF=None
WillBePlS=None
WillGoF=None
FirstPWillBe=None
textForFStep=ctk.CTkLabel(window, text="Who goes first?")
ChoiceStepF=ctk.CTkSegmentedButton(window, values=["player 1", "player 2"], fg_color="white", selected_color="black", unselected_color="gray")
ChoiceStepF.set("player 1")
textForFPlayer=ctk.CTkLabel(window, text="Who will be player 1?")
ChoicePlayerF=ctk.CTkSegmentedButton(window, values=["player 1", "AI"], fg_color="white", selected_color="black", unselected_color="gray")
ChoicePlayerF.set("player 1")
textForSPlayer=ctk.CTkLabel(window, text="Who will be player 2?")
ChoicePlayerS=ctk.CTkSegmentedButton(window, values=["player 2", "AI"], fg_color="white", selected_color="black", unselected_color="gray")
ChoicePlayerS.set("player 2")
textForWhoWBFP=ctk.CTkLabel(window, text="Who will be player 1?")
ChoiceWhoWBFP=ctk.CTkSegmentedButton(window, values=["player 1: x", "player 1: o"], fg_color="white", selected_color="black", unselected_color="gray")
ChoiceWhoWBFP.set("player 1: x")
ButtonStartPlay=ctk.CTkButton(window, text="play", fg_color="#44DB04", text_color="black", hover_color="green", font=("Courier", 20, "bold"), command=StartGame)
LabelStats=ctk.CTkLabel(window, text=f"Wins of player 1: {FPWins}           Wins of player 2: {SPWins}                 Alredy played games: {PlayedGames}              Ties={Tie}", fg_color="white", text_color="black")


for u in range(1, 10):
    buton=ctk.CTkButton(window, text=" ", font=("Courier", 100, "bold"), text_color="black", border_color="black", border_width=1, fg_color="white", hover_color="gray", command=lambda nam=u: step(nam-1))
    if u==1 or u==4 or u==7:
        buton.grid(column=(u-1)%3, row=(u-1)//3+3, columnspan=2, sticky="wesn")
    elif u==2 or u==5 or u==8:
        buton.grid(column=(u - 1) % 3 + 1, row=(u - 1) // 3 + 3, columnspan=2, sticky="wesn")
    elif u==3 or u==6 or u==9:
        buton.grid(column=(u - 1) % 3 + 2, row=(u - 1) // 3 + 3, columnspan=2, sticky="wesn")
    butons.append(buton)
textForFStep.grid(column=0, row=0, sticky="wesn")
ChoiceStepF.grid(column=0, row=1, sticky="wesn")
textForFPlayer.grid(column=1, row=0, sticky="wesn")
ChoicePlayerF.grid(column=1, row=1, sticky="wesn")
textForSPlayer.grid(column=2, row=0, sticky="wesn")
ChoicePlayerS.grid(column=2, row=1, sticky="wesn")
textForWhoWBFP.grid(column=3, row=0, sticky="wesn")
ChoiceWhoWBFP.grid(column=3, row=1, sticky="wesn")
ButtonStartPlay.grid(column=4, row=0, sticky="wesn", rowspan=2, columnspan=3)
LabelStats.grid(column=0, row=2, sticky="wesn", columnspan=6)
window.rowconfigure(3, minsize=280)
window.rowconfigure(4, minsize=280)
window.rowconfigure(5, minsize=280)
for i in range(6):
    window.grid_columnconfigure(i, minsize=185)
window.mainloop()