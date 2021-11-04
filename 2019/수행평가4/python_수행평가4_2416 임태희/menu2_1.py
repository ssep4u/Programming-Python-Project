import tkinter
import tkinter.font

import start
import kang2


class Menu2_1:
    def __init__(self, menu2_1):
        self.menu2_1 = menu2_1

        # menu2_1 화면 이미지
        self.kangBackground = tkinter.PhotoImage(file="image/background.gif")
        self.kangBackgroundL = tkinter.Label(image=self.kangBackground)
        self.kangBackgroundL.place(x=-2, y=-2)

        # 꽈트로 튀김 떡볶이 title
        self.titleFont = tkinter.font.Font(size=25, weight="bold")
        self.title = tkinter.Label(self.menu2_1, text=" ♡ 꽈트로 튀김 떡볶이 ♡ ", foreground="#9b95b7", font=self.titleFont)
        self.title.place(x=220, y=40)

#        # 스크롤바
#        self.scrollbar = tkinter.Scrollbar(self.menu2_1)
#        self.scrollbar.pack()
#        self.menuList = tkinter.Listbox(self.menu2_1, yscrollcommand=self.scrollbar.set)
#        self.menuList.insert()

        # 데이터 정보 불러오기
        self.info = open("menu2_1.txt", "r", encoding="utf-8")
        addY = 150
        while True:
            self.infoData = self.info.readlines()
            if not self.infoData:
                break

            # 데이터 정보 사용하기
            for self.line in self.infoData:
                self.title = tkinter.Label(self.menu2_1, text=self.line, foreground="#9b95b7")
                self.title.place(x=150, y=addY)
                addY += 30

        self.info.close()

        # home 버튼
        self.home = tkinter.PhotoImage(file="image/home.gif")
        self.homeButton = tkinter.Button(self.menu2_1, text="home", image=self.home, command=self.moveHomeButton, repeatdelay=20)
        self.homeButton.place(x=50, y=400)

        # back 버튼
        self.back = tkinter.PhotoImage(file="image/back.gif")
        self.backButton = tkinter.Button(self.menu2_1, text="home", image=self.back, command=self.moveBackButton, repeatdelay=20)
        self.backButton.place(x=710, y=400)

    # main=home 페이지로 가기
    def moveHomeButton(self):
        startMove = start.Start(self.menu2_1)

    # back 페이지로 뒤로가기
    def moveBackButton(self):
        backMove = kang2.Kang2(self.menu2_1)