import tkinter
import tkinter.font

import kang1
import kang2
import kang3


class Main:
    def __init__(self, main):
        self.main = main

        # main 화면 이미지
        self.mainBack = tkinter.PhotoImage(file="image/background.gif")
        self.mainBackL = tkinter.Label(image=self.mainBack)
        self.mainBackL.place(x=-2, y=-2)

        # title
        self.titleFont = tkinter.font.Font(size=15, weight="bold")
        self.title = tkinter.Label(self.main, text=" ※ 보고 싶은 강식당 시즌 메뉴를 선택해주세요 ※ ", foreground="#9b95b7", font=self.titleFont)
        self.title.place(x=170, y=40)

        # kang1 이미지
        self.kang1 = tkinter.PhotoImage(file="image/kang1.gif")
        self.kang1L = tkinter.Label(image=self.kang1)
        self.kang1L.place(x=100, y=100)

        # kang2 이미지
        self.kang2 = tkinter.PhotoImage(file="image/kang2.gif")
        self.kang2L = tkinter.Label(image=self.kang2)
        self.kang2L.place(x=310, y=100)

        # kang3 이미지
        self.kang3 = tkinter.PhotoImage(file="image/kang3.gif")
        self.kang3L = tkinter.Label(image=self.kang3)
        self.kang3L.place(x=520, y=100)

        # kmenu1 버튼
        self.kangMenuButton1 = tkinter.Button(self.main, text="강식당1", command=self.moveButton1, foreground="#9b95b7",
                                              width=10, repeatdelay=20)
        self.kangMenuButton1.place(x=150, y=380)

        # kmenu2 버튼
        self.kangMenuButton2 = tkinter.Button(self.main, text="강식당2", command=self.moveButton2, foreground="#9b95b7",
                                              width=10, repeatdelay=20)
        self.kangMenuButton2.place(x=360, y=380)

        # kmenu3 버튼
        self.kangMenuButton3 = tkinter.Button(self.main, text="강식당3", command=self.moveButton3, foreground="#9b95b7",
                                              width=10, repeatdelay=20)
        self.kangMenuButton3.place(x=570, y=380)

    # kmenu1 페이지로 넘기기
    def moveButton1(self):
        mainMoveButton1 = kang1.Kang1(self.main)

    # kmenu2 페이지로 넘기기
    def moveButton2(self):
        mainMoveButton2 = kang2.Kang2(self.main)

    # kmenu3 페이지로 넘기기
    def moveButton3(self):
        mainMoveButton3 = kang3.Kang3(self.main)
