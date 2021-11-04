import tkinter
import tkinter.font

import start
import main

import menu1_1
import menu1_2
import menu1_3
import menu1_4
import menu1_5


class Kang1:
    def __init__(self, kang1):
        self.kang1 = kang1

        # kang1 화면 이미지
        self.kangBackground = tkinter.PhotoImage(file="image/background.gif")
        self.kangBackgroundL = tkinter.Label(image=self.kangBackground)
        self.kangBackgroundL.place(x=-2, y=-2)

        # menu title
        self.menuFont = tkinter.font.Font(size=25, weight="bold")
        self.menu = tkinter.Label(self.kang1, text=" << MENU >> ", foreground="#9b95b7", font=self.menuFont)
        self.menu.place(x=290, y=40)

        # 강호동까스 버튼
        self.food1_1 = tkinter.Button(self.kang1, text="강호동까스", command=self.moveFood1_1, foreground="#9b95b7", width=18, repeatdelay=20)
        self.food1_1.place(x=160, y=150)

        # 이수근까스 버튼
        self.food1_2 = tkinter.Button(self.kang1, text="이수근까스", command=self.moveFood1_2, foreground="#9b95b7", width=18, repeatdelay=20)
        self.food1_2.place(x=330, y=150)

        # 오므라이스 버튼
        self.food1_3 = tkinter.Button(self.kang1, text="오므라이스", command=self.moveFood1_3, foreground="#9b95b7", width=18, repeatdelay=20)
        self.food1_3.place(x=160, y=210)

        # 제주많은 돼지라면 버튼
        self.food1_4 = tkinter.Button(self.kang1, text="제주많은 돼지라면", command=self.moveFood1_4, foreground="#9b95b7", width=18, repeatdelay=20)
        self.food1_4.place(x=330, y=210)

        # 삼겹살 김밥 버튼
        self.food1_5 = tkinter.Button(self.kang1, text="삼겹살 김밥", command=self.moveFood1_5, foreground="#9b95b7", width=18, repeatdelay=20)
        self.food1_5.place(x=500, y=210)

      # home 버튼
        self.home = tkinter.PhotoImage(file="image/home.gif")
        self.homeButton = tkinter.Button(self.kang1, text="home", image=self.home, command=self.moveHomeButton, repeatdelay=20)
        self.homeButton.place(x=50, y=400)

        # back 버튼
        self.back = tkinter.PhotoImage(file="image/back.gif")
        self.backButton = tkinter.Button(self.kang1, text="home", image=self.back, command=self.moveBackButton, repeatdelay=20)
        self.backButton.place(x=710, y=400)

    # menu1_1 레시피 소개 페이지로 이동
    def moveFood1_1(self):
        menuMoveButton1_1 = menu1_1.Menu1_1(self.kang1)

    # menu1_2 레시피 소개 페이지로 이동
    def moveFood1_2(self):
        menuMoveButton1_2 = menu1_2.Menu1_2(self.kang1)

    # menu1_3 레시피 소개 페이지로 이동
    def moveFood1_3(self):
        menuMoveButton1_3 = menu1_3.Menu1_3(self.kang1)

    # menu1_4 레시피 소개 페이지로 이동
    def moveFood1_4(self):
        menuMoveButton1_4 = menu1_4.Menu1_4(self.kang1)

    # menu2_5 레시피 소개 페이지로 이동
    def moveFood1_5(self):
        menuMoveButton1_5 = menu1_5.Menu1_5(self.kang1)

    # main=home 페이지로 가기
    def moveHomeButton(self):
        startMove = start.Start(self.kang1)

    # back 페이지로 뒤로가기
    def moveBackButton(self):
        backMove = main.Main(self.kang1)