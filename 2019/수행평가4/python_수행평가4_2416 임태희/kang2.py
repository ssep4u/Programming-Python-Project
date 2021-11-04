import tkinter
import tkinter.font

import start
import main

import menu2_1
import menu2_2
import menu2_3
import menu2_4
import menu2_5
import menu2_6
import menu2_7


class Kang2:
    def __init__(self, kang2):
        self.kang2 = kang2

        # kang1 화면 이미지
        self.kangBackground = tkinter.PhotoImage(file="image/background.gif")
        self.kangBackgroundL = tkinter.Label(image=self.kangBackground)
        self.kangBackgroundL.place(x=-2, y=-2)

        # menu title
        self.menuFont = tkinter.font.Font(size=25, weight="bold")
        self.menu = tkinter.Label(self.kang2, text=" << MENU >> ", foreground="#9b95b7", font=self.menuFont)
        self.menu.place(x=290, y=40)

        # 꽈트로 튀김 떡볶이 버튼
        self.food2_1 = tkinter.Button(self.kang2, text="꽈트로 튀김 떡볶이", command=self.moveFood2_1, foreground="#9b95b7", width=18, repeatdelay=20)
        self.food2_1.place(x=160, y=150)

        # 짜장 떡볶이 버튼
        self.food2_2 = tkinter.Button(self.kang2, text="웃기는 짜장 떡볶이", command=self.moveFood2_2, foreground="#9b95b7", width=18, repeatdelay=20)
        self.food2_2.place(x=330, y=150)

        # 니가가락 국수 버튼
        self.food2_3 = tkinter.Button(self.kang2, text="니가가락 국수", command=self.moveFood2_3, foreground="#9b95b7", width=18, repeatdelay=20)
        self.food2_3.place(x=160, y=210)

        # 니가가락 냉국수 버튼
        self.food2_4 = tkinter.Button(self.kang2, text="니가가락 냉국수", command=self.moveFood2_4, foreground="#9b95b7", width=18, repeatdelay=20)
        self.food2_4.place(x=330, y=210)

        # 니가 비비바락 국수 버튼
        self.food2_5 = tkinter.Button(self.kang2, text="니가 비비바락 국수", command=self.moveFood2_5, foreground="#9b95b7", width=18, repeatdelay=20)
        self.food2_5.place(x=500, y=210)

        # 김치밥이 피오씁니다 버튼
        self.food2_6 = tkinter.Button(self.kang2, text="김치밥이 피오씁니다", command=self.moveFood2_6, foreground="#9b95b7", width=18, repeatdelay=20)
        self.food2_6.place(x=160, y=270)

        # 아기 짜자장밥
        self.food2_7 = tkinter.Button(self.kang2, text="아기 짜자장밥", command=self.moveFood2_7, foreground="#9b95b7", width=18, repeatdelay=20)
        self.food2_7.place(x=330, y=270)

      # home 버튼
        self.home = tkinter.PhotoImage(file="image/home.gif")
        self.homeButton = tkinter.Button(self.kang2, text="home", image=self.home, command=self.moveHomeButton, repeatdelay=20)
        self.homeButton.place(x=50, y=400)

        # back 버튼
        self.back = tkinter.PhotoImage(file="image/back.gif")
        self.backButton = tkinter.Button(self.kang2, text="home", image=self.back, command=self.moveBackButton, repeatdelay=20)
        self.backButton.place(x=710, y=400)

    # menu2_1 레시피 소개 페이지로 이동
    def moveFood2_1(self):
        menuMoveButton2_1 = menu2_1.Menu2_1(self.kang2)

    # menu2_2 레시피 소개 페이지로 이동
    def moveFood2_2(self):
        menuMoveButton2_2 = menu2_2.Menu2_2(self.kang2)

    # menu2_3 레시피 소개 페이지로 이동
    def moveFood2_3(self):
        menuMoveButton2_3 = menu2_3.Menu2_3(self.kang2)

    # menu2_4 레시피 소개 페이지로 이동
    def moveFood2_4(self):
        menuMoveButton2_4 = menu2_4.Menu2_4(self.kang2)

    # menu2_5 레시피 소개 페이지로 이동
    def moveFood2_5(self):
        menuMoveButton2_5 = menu2_5.Menu2_5(self.kang2)

    # menu2_6 레시피 소개 페이지로 이동
    def moveFood2_6(self):
        menuMoveButton2_6 = menu2_6.Menu2_6(self.kang2)

    # menu2_7 레시피 소개 페이지로 이동
    def moveFood2_7(self):
        menuMoveButton2_7 = menu2_7.Menu2_7(self.kang2)

    # main=home 페이지로 가기
    def moveHomeButton(self):
        startMove = start.Start(self.kang2)

    # back 페이지로 뒤로가기
    def moveBackButton(self):
        backMove = main.Main(self.kang2)