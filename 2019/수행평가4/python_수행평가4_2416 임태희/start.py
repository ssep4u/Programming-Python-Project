# 2416 임태희
# TV 인기예능 강식당(1/2/3)의 음식 레시피를 간단하면서도 확실하게 살펴볼 수 있는 프로그램
# 실행방법 : start.py에서 실행하시면 됩니다.
import tkinter

import main


class Start:
    def __init__(self, start):
        self.start = start

        # start 화면 이미지
        self.startBack = tkinter.PhotoImage(file="image/start.gif")
        self.startBackL = tkinter.Label(image=self.startBack)
        self.startBackL.place(x=-2, y=-2)

        # start 버튼
        self.startFont = tkinter.font.Font(size=11, weight="bold")
        self.startButton = tkinter.Button(self.start, text="START", command=self.move, foreground="#9b95b7", width=10, repeatdelay=20, font=self.startFont)
        self.startButton.place(x=350, y=310)

    def move(self):
        startMove = main.Main(self.start)

    def play(self):
        self.start.mainloop()


if __name__ == '__main__':
    # start 화면 만들기
    start = tkinter.Tk()
    start.title("나도! 강식당")
    start.geometry("800x500+250+50")  # 너비 x 높이 + x좌표 + y좌표
    start.resizable(False, False)

    kang = Start(start)
    kang.play()
