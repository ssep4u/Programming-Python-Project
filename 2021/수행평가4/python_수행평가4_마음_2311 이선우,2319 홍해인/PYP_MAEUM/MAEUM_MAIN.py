
import tkinter

import SHARE
import DONATE
import START
import TOP3

class Maeum_main:
    def __init__(self, main):
        self.main = main

        # Maeum_main 화면 이미지
        self.Maeum_mainBack = tkinter.PhotoImage(file="img/background.gif")
        self.Maeum_mainBackL = tkinter.Label(image=self.Maeum_mainBack)
        self.Maeum_mainBackL.place(x=-2, y=-2)

        # share 버튼
        self.shareButton = tkinter.Button(self.main, width=435, height=131, borderwidth=0, command=self.ShareButton)
        self.shareButton.place(x=210, y=100)
        self.shareButtonImg = tkinter.PhotoImage(file="img/share.png")
        self.shareButton.config(image=self.shareButtonImg)

        # donate 버튼
        self.donateButton = tkinter.Button(self.main,  width=435, height=131,  borderwidth=0, command=self.DonateButton)
        self.donateButton.place(x=210, y=270)
        self.donateButtonImg = tkinter.PhotoImage(file="img/donate.png")
        self.donateButton.config(image=self.donateButtonImg)

        # top3 버튼
        self.top3Button = tkinter.Button(self.main,  width=435, height=131, borderwidth=0, command=self.Top3Button)
        self.top3Button.place(x=210, y=440)
        self.top3ButtonImg = tkinter.PhotoImage(file="img/top3.png")
        self.top3Button.config(image=self.top3ButtonImg)

        # home 버튼
        self.homeButton = tkinter.Button(self.main, width=72, height=72, borderwidth=0, command=self.HomeButton)
        self.homeButton.place(x=755, y=30)
        self.homeButtonImg = tkinter.PhotoImage(file="img/home_y.png")
        self.homeButton.config(image=self.homeButtonImg)

    # SHARE 페이지로 넘기기
    def ShareButton(self):
        SHARE.Share(self.main)

    # DONATE 페이지로 넘기기
    def DonateButton(self):
        DONATE.Donate(self.main)

    # TOP3 페이지로 넘기기
    def Top3Button(self):

        TOP3.Top3(self.main)

    # home 페이지로 가기
    def HomeButton(self):
        START.Start(self.main)
