import tkinter
import tkinter.font

import start
import main

import menu3_1
import menu3_2
import menu3_3
import menu3_4
import menu3_5
import menu3_6


class Kang3:
    def __init__(self, kang3):
        self.kang3 = kang3

        # kang3 화면 이미지
        self.kangBackground = tkinter.PhotoImage(file="image/background.gif")
        self.kangBackgroundL = tkinter.Label(image=self.kangBackground)
        self.kangBackgroundL.place(x=-2, y=-2)

        # menu title
        self.menuFont = tkinter.font.Font(size=25, weight="bold")
        self.menu = tkinter.Label(self.kang3, text=" << MENU >> ", foreground="#9b95b7", font=self.menuFont)
        self.menu.place(x=290, y=40)

        # 강호동 불고기 파스타 버튼
        self.food3_1 = tkinter.Button(self.kang3, text="강호동 불고기 파스타", command=self.moveFood3_1, foreground="#9b95b7", width=18, repeatdelay=20)
        self.food3_1.place(x=160, y=150)

        # 강호동 돼지고기 파스타 버튼
        self.food3_2 = tkinter.Button(self.kang3, text="강호동 돼지고기 파스타", command=self.moveFood3_2, foreground="#9b95b7", width=18, repeatdelay=20)
        self.food3_2.place(x=330, y=150)

        # 강호동 조각 피자 버튼
        self.food3_3 = tkinter.Button(self.kang3, text="강호동 조각 피자", command=self.moveFood3_3, foreground="#9b95b7", width=18, repeatdelay=20)
        self.food3_3.place(x=160, y=210)

        # 이수근 한판 피자 버튼
        self.food3_4 = tkinter.Button(self.kang3, text="이수근 한판 피자", command=self.moveFood3_4, foreground="#9b95b7", width=18, repeatdelay=20)
        self.food3_4.place(x=330, y=210)

        # 수근이 몇살? 부챗살! 피자 버튼
        self.food3_5 = tkinter.Button(self.kang3, text="수근이 몇살? 부챗살!", command=self.moveFood3_5, foreground="#9b95b7", width=18, repeatdelay=20)
        self.food3_5.place(x=500, y=210)

        # 김치밥이 피오씁니다 버튼
        self.food3_6 = tkinter.Button(self.kang3, text="김치밥이 피오씁니다", command=self.moveFood3_6, foreground="#9b95b7", width=18, repeatdelay=20)
        self.food3_6.place(x=160, y=270)

      # home 버튼
        self.home = tkinter.PhotoImage(file="image/home.gif")
        self.homeButton = tkinter.Button(self.kang3, text="home", image=self.home, command=self.moveHomeButton, repeatdelay=20)
        self.homeButton.place(x=50, y=400)

        # back 버튼
        self.back = tkinter.PhotoImage(file="image/back.gif")
        self.backButton = tkinter.Button(self.kang3, text="home", image=self.back, command=self.moveBackButton, repeatdelay=20)
        self.backButton.place(x=710, y=400)

    # menu3_1 레시피 소개 페이지로 이동
    def moveFood3_1(self):
        menuMoveButton3_1 = menu3_1.Menu3_1(self.kang3)

    # menu3_2 레시피 소개 페이지로 이동
    def moveFood3_2(self):
        menuMoveButton3_2 = menu3_2.Menu3_2(self.kang3)

    # menu3_3 레시피 소개 페이지로 이동
    def moveFood3_3(self):
        menuMoveButton3_3 = menu3_3.Menu3_3(self.kang3)

    # menu3_4 레시피 소개 페이지로 이동
    def moveFood3_4(self):
        menuMoveButton3_4 = menu3_4.Menu3_4(self.kang3)

    # menu3_5 레시피 소개 페이지로 이동
    def moveFood3_5(self):
        menuMoveButton3_5 = menu3_5.Menu3_5(self.kang3)

    # menu3_6 레시피 소개 페이지로 이동
    def moveFood3_6(self):
        menuMoveButton3_6 = menu3_6.Menu3_6(self.kang3)

    # main=home 페이지로 가기
    def moveHomeButton(self):
        startMove = start.Start(self.kang3)

    # back 페이지로 뒤로가기
    def moveBackButton(self):
        backMove = main.Main(self.kang3)