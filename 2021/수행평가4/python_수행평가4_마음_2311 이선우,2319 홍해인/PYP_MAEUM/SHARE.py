import tkinter
from cProfile import label
from tkinter import *  # tkinter 라이브러리에 모든 함수를 사용하겠다.
from functools import partial

import MAEUM_MAIN
# import SHIRTS_DONATE
import THANK_DONATE
import THANK_SHARE


class Share:
    money = []
    total_money = 0
    account_number = ""
    def __init__(self, share):

        self.share =share
        #화면 이미지
        self.shareBack = tkinter.PhotoImage(file = "img/share_back.png")
        self.shareBackL = tkinter.Label(image=self.shareBack)
        self.shareBackL.place(x=-2, y=-2)

        #share 버튼
        self.shareButton = tkinter.Button(self.share, width=210, height=60, borderwidth=0, command=self.T_D_Button)
        self.shareButton.place(x=595, y=500)
        self.shareButtonImg = tkinter.PhotoImage(file='img/share_btn.png')
        self.shareButton.config(image=self.shareButtonImg)


        # 입력
        self.ent1 = tkinter.Entry(share)  # TD라는 창에 입력창 생성
        self.ent1.place(x=350, y=200)

        self.ent2 = tkinter.Entry(share)  # TD라는 창에 입력창 생성
        self.ent2.place(x=350, y=280)

        self.ent3 = tkinter.Entry(share)  # TD라는 창에 입력창 생성
        self.ent3.place(x=350, y=360)

        self.ent4 = tkinter.Entry(share)  # TD라는 창에 입력창 생성
        self.ent4.place(x=350, y=440)

        # back 버튼
        self.backButton = tkinter.Button(self.share, width=120, height=67, borderwidth=0, command=self.BackButton)
        self.backButton.place(x=750, y=9)
        self.backButtonImg = tkinter.PhotoImage(file="img/back_yellow.PNG")
        self.backButton.config(image=self.backButtonImg)


    def T_D_Button(self):

        # wall_label = tkinter.Label(tk, image = label)
        # wall_label.pack()

        self.account_number = self.ent3.get()
        self.money.append(self.account_number)
        for x in self.money:
            self.total_money += int(x)
        print(self.money)
        print(self.total_money)

        THANK_SHARE.Thank_share(self.share)
        #
        # tk = tkinter.Tk()
        # tk.title("your maeums")
        # # tk.place

        wall = PhotoImage(file="img/share_maeumsBack.png")
        wall_label = Label(image=wall)
        wall_label.place(x=-2, y=-2)
        # wall_label.geometry("882x628")
        private_label = tkinter.Label(text=str(self.account_number),bg=('white'), font=("System",50))
        private_label.place(x=480,y=215)
        total_label = tkinter.Label(text=str(self.total_money), bg=('white'),font=("System", 50))
        total_label.place(x=480, y=350)
        # wall_label.mainloop()
        # label.mainloop()

        NextButton = tkinter.Button(width=266, height=65, borderwidth=0, command=self.NextButton)
        NextButton.place(x=580, y=500)
        NextButtonImg = tkinter.PhotoImage(file="img/maenus_nextBtn.png")
        NextButton.config(image=NextButtonImg)
        NextButton.mainloop()

        # label = tkinter.PhotoImage(file="img/your_maeums.png")
        # yourMaumsL = tkinter.Label(image=label)
        # yourMaumsL.place(x=-2, y=-2)
        # tk.label.resizable(False, False)
        # label = tkinter.Label(tk, self.total_money)
        # tk.mainloop()
        # money = []
        # # total_money = 0
        # account_number = self.ent4.get()
        # money.append(int(account_number))
        # total_money += int(account_number)
        # print(money)
    def NextButton(self):
        THANK_SHARE.Thank_share(self.share)
    def BackButton(self):
        MAEUM_MAIN.Maeum_main(self.share)