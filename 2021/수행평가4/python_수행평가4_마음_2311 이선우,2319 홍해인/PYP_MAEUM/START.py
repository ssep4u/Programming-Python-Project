
import tkinter

import MAEUM_MAIN

class Start:
    def __init__(self, start):
        self.start = start

        #화면 이미지
        self.startBack = tkinter.PhotoImage(file ="img/StartBack.PNG")
        self.startBackL = tkinter.Label(image=self.startBack)
        self.startBackL.place(x=-2, y=-2)

        # start 버튼
        self.startButton = tkinter.Button(self.start, width=250, height=70, borderwidth=0, command=self.move)
        self.startButton.place(x=320, y=430)
        self.startButtonImg = tkinter.PhotoImage(file="img/start.png")
        self.startButton.config(image=self.startButtonImg)

    def move(self):
        MAEUM_MAIN.Maeum_main(self.start)

    def play(self):
        self.start.mainloop()

if __name__ == '__main__':
    start = tkinter.Tk()
    start.title("마음을 나눠요")
    start.geometry("882x628+400+100")
    start.resizable(False, False)


    start = Start(start)
    start.play()