import tkinter as tk
import tkinter.messagebox
from datetime import datetime
from read_write import Read, Day

class Rice():
    now = datetime.now()
    date = '%s-%s-%s' % (now.year, now.month, now.day)
    breakfast = 0
    lunch = 0
    dinner = 0

    def __init__(self):
        self.breakSum = 0
        self.lunchSum = 0
        self.dinnerSum = 0
        self.start()

    def __str__(self):
        return "현재 날짜 : " + str(self.date) + "\t식사 : " + str(self.breakfast) + "\n"

    def start(self):
        self.start = tk.Tk()
        self.start.title("얼죽아")
        self.start.geometry("850x600")
        self.start.resizable(False, False)
        image1 = tk.PhotoImage(file="Image/얼죽아.png")
        label1 = tk.Label(self.start, image=image1)
        label1.place(x=240, y=40)
        label2 = tk.Label(self.start, text="얼어 죽어도", font=("궁서체", 43))
        label2.place(x=70, y=100)
        image2 = tk.PhotoImage(file="Image/아침밥.png")
        label3 = tk.Label(self.start, image=image2)
        label3.place(x=70, y=180)
        label4 = tk.Label(self.start, text="챙겨야지", font=("궁서체", 43))
        label4.place(x=70, y=260)
        button1 = tk.Button(self.start, width=200, height=100, borderwidth=0, command=self.user)
        button1.place(x=15, y=390)
        btImage1 = tk.PhotoImage(file="Image/시작.png")
        button1.config(image=btImage1)
        button2 = tk.Button(self.start, width=200, height=100, borderwidth=0, command=self.result)
        button2.place(x=15, y=490)
        btImage2 = tk.PhotoImage(file="Image/다음.png")
        button2.config(image=btImage2)
        self.start.mainloop()

    def user(self):
        self.user = tk.Toplevel()
        self.user.title("얼죽아")
        self.user.geometry("660x660")
        self.user.resizable(False, False)
        image1 = tk.PhotoImage(file="Image/영희.png")
        label1 = tk.Label(self.user, image=image1)
        label1.place(x=220, y=110)
        label2 = tk.Label(self.user, text="사용자", font=("궁서체", 27))
        label2.place(x=42, y=380)
        label3 = tk.Label(self.user, text=" 님의 이름을 입력해 주세요.", font=("궁서체", 25))
        label3.place(x=152, y=380)
        textbox = tk.Entry(self.user, width=30, font=("궁서체", 20))
        textbox.place(x=120, y=460)
        startButton = tk.Button(self.user, width=150, height=150, borderwidth=0, command=lambda:self.riceStart(tk.Entry.get(textbox)))
        startButton.place(x=250, y=500)
        btImage = tk.PhotoImage(file="Image/다음버튼.png")
        startButton.config(image=btImage)
        self.user.mainloop()

    def riceStart(self, strName):
        Day(self.date)
        self.start = tk.Toplevel()
        self.start.title("얼죽아")
        self.start.geometry("850x550")
        self.start.resizable(False, False)
        image1 = tk.PhotoImage(file="Image/아침.png")
        label1 = tk.Label(self.start, image=image1)
        label1.place(x=120, y=100)
        image2 = tk.PhotoImage(file="Image/점심.png")
        label2 = tk.Label(self.start, image=image2)
        label2.place(x=335, y=80)
        image3 = tk.PhotoImage(file="Image/저녁.png")
        label3 = tk.Label(self.start, image=image3)
        label3.place(x=575, y=95)
        button1 = tk.Button(self.start, width=250, height=100, borderwidth=0, command=self.bk)
        button1.place(x=57, y=260)
        btImage1 = tk.PhotoImage(file="Image/아침버튼.png")
        button1.config(image=btImage1)
        button2 = tk.Button(self.start, width=250, height=100, borderwidth=0, command=self.lunch)
        button2.place(x=300, y=260)

        btImage2 = tk.PhotoImage(file="Image/점심버튼.png")
        button2.config(image=btImage2)
        button3 = tk.Button(self.start, width=250, height=100, borderwidth=0, command=self.dinner)
        button3.place(x=540, y=260)
        btImage3 = tk.PhotoImage(file="Image/저녁버튼.png")
        button3.config(image=btImage3)

        label1 = tk.Label(self.start, text=strName+" 님은", font=("궁서체", 27))
        label1.place(x=75, y=380)
        label2 = tk.Label(self.start, text=" 아침, 점심, 저녁을 먹었는지", font=("궁서체", 25))
        label2.place(x=280, y=383)
        label2 = tk.Label(self.start, text="아이콘을 눌러서 확인해 주세요.", font=("궁서체", 25))
        label2.place(x=172, y=440)
        self.start.mainloop()

    # 메시지 박스 window 창 수정하기, riceStart의 window 창에서 메시지 박스가 나타나게 하기.
    def bk(self):
        d = Day(self.date)
        self.breakfastQ = tk.messagebox.askquestion("얼죽아", "오늘, 아침밥은 챙기셨나요?")

        if self.breakfastQ == 'yes':
            if d.breakfast == 0:
                d.breakfast += 1
                Read.insert(d)
                self.answerYes()
            else:
                self.attention = tk.messagebox.showwarning("이미 확인하셨습니다. 내일 다시 와 주세요.")
        else:
            self.answerNo()

    def lunch(self):
        d = Day(self.date)
        self.lunchQ = tk.messagebox.askquestion("얼죽아", "오늘, 점심밥은 챙기셨나요?")

        if self.lunchQ == 'yes':
            if d.lunch == 0:
                d.lunch += 1
                Read.insert(d)
                self.answerYes()
            else:
                self.attention = tk.messagebox.showwarning("이미 확인하셨습니다. 내일 다시 와 주세요.")
        else:
            self.answerNo()


    def dinner(self):
        d = Day(self.date)
        self.dinnerQ = tk.messagebox.askquestion("얼죽아", "오늘, 저녁밥은 챙기셨나요?")

        if self.dinnerQ == 'yes':
            if d.dinner == 0:
                d.dinner += 1
                Read.insert(d)
                self.answerYes()
            else:
                self.attention = tk.messagebox.showwarning("이미 확인하셨습니다. 내일 다시 와 주세요.")
        else:
            self.answerNo()

    def answerNo(self):
        self.breakNo = tk.Toplevel()
        self.breakNo.title("얼죽아")
        self.breakNo.geometry("850x450")
        self.breakNo.resizable(False, False)
        image1 = tk.PhotoImage(file="Image/놀랐어.png")
        label1 = tk.Label(self.breakNo, image=image1)
        label1.place(x=550, y=50)
        label2 = tk.Label(self.breakNo, text="오늘 아침에 많이 바쁘셨나요?", font=("궁서체", 20))
        label2.place(x=50, y=100)
        label3 = tk.Label(self.breakNo, text="바쁜 아침 탓에 먹지 못 하였다면,", font=("궁서체", 20))
        label3.place(x=50, y=140)
        label4 = tk.Label(self.breakNo, text="간단한 샌드위치라도 챙겨서 드세요.", font=("궁서체", 20))
        label4.place(x=50, y=180)
        label5 = tk.Label(self.breakNo, text="여유로운 당신의 아침을 응원합니다.", font=("궁서체", 20))
        label5.place(x=50, y=240)
        label6 = tk.Label(self.breakNo, text="※ 특히, 2학년 4반 친구들 잘 챙겨서 먹기.", font=("궁서체", 12))
        label6.place(x=50, y=285)
        button = tk.Button(self.breakNo, width=200, height=100, borderwidth=0, command=self.result)
        button.place(x=300, y=330)
        btImage = tk.PhotoImage(file="Image/시작.png")
        button.config(image=btImage)
        self.breakNo.mainloop()

    def answerYes(self):
        self.breakYes = tk.Toplevel()
        self.breakYes.title("얼죽아")
        self.breakYes.geometry("750x450")
        self.breakYes.resizable(False, False)
        image1 = tk.PhotoImage(file="Image/잘했어.png")
        label1 = tk.Label(self.breakYes, image=image1)
        label1.place(x=550, y=50)
        label2 = tk.Label(self.breakYes, text="여유로운 아침을 만끽하셨군요.", font=("궁서체", 20))
        label2.place(x=50, y=100)
        label3 = tk.Label(self.breakYes, text="바쁜 아침 속에서도,", font=("궁서체", 20))
        label3.place(x=50, y=140)
        label4 = tk.Label(self.breakYes, text="여유를 잃지 않는 모습이 멋있어요.", font=("궁서체", 20))
        label4.place(x=50, y=180)
        label5 = tk.Label(self.breakYes, text="앞으로도 여유로울 당신을 응원합니다.", font=("궁서체", 20))
        label5.place(x=50, y=240)
        label6 = tk.Label(self.breakYes, text="※ 특히, 2학년 4반 친구들을 응원합니다.", font=("궁서체", 12))
        label6.place(x=50, y=285)
        button = tk.Button(self.breakYes, width=200, height=100, borderwidth=0, command=self.result)
        button.place(x=250, y=330)
        btImage = tk.PhotoImage(file="Image/시작.png")
        button.config(image=btImage)
        self.breakYes.mainloop()

    def result(self):
        self.result = tk.Toplevel()
        self.result.title("얼죽아")
        self.result.geometry("750x530")
        self.result.resizable(False, False)
        image1 = tk.PhotoImage(file="Image/결과.png")
        label1 = tk.Label(self.result, image=image1)
        label1.place(x=40, y=40)
        label2 = tk.Label(self.result, text="식사 횟수 평균을", font=("궁서체", 25))
        label2.place(x=280, y=170)
        label3 = tk.Label(self.result, text="보러 가지 않을래, 친구야?", font=("궁서체", 25))
        label3.place(x=280, y=230)
        button = tk.Button(self.result, width=200, height=100, borderwidth=0, command=self.riceFinal)
        button.place(x=400, y=330)
        btImage = tk.PhotoImage(file="Image/가자.png")
        button.config(image=btImage)
        self.result.mainloop()

    def riceFinal(self):
        dateList = Read.get_all()
        for i in dateList:
            self.breakSum += i.breakfast
            self.lunchSum += i.lunch
            self.dinnerSum += i.dinner
        self.avBreak = round((self.breakSum / len(dateList)), 2)
        self.avLunch = round((self.lunchSum / len(dateList)), 2)
        self.avDinner = round((self.dinnerSum / len(dateList)), 2)

        ricefinal = tk.Toplevel()
        ricefinal.title("얼죽아")
        ricefinal.geometry("750x550")
        ricefinal.resizable(False, False)
        image1 = tk.PhotoImage(file="Image/달력.png")
        label1 = tk.Label(ricefinal, image=image1)
        label1.place(x="250", y="50")
        label2 = tk.Label(ricefinal, text="평균적으로 아침은 ", font=("궁서체", 25))
        label2.place(x="80", y="300")
        label3 = tk.Label(ricefinal, text=self.avBreak, font=("궁서체", 25))
        label3.place(x="400", y="300")
        label4 = tk.Label(ricefinal, text=" 회 챙겼고, ", font=("궁서체", 25))
        label4.place(x="470", y="300")
        label5 = tk.Label(ricefinal, text="평균적으로 점심은 ", font=("궁서체", 25))
        label5.place(x="80", y="380")
        label6 = tk.Label(ricefinal, text=self.avLunch, font=("궁서체", 25))
        label6.place(x="400", y="380")
        label7 = tk.Label(ricefinal, text=" 회 챙겼고, ", font=("궁서체", 25))
        label7.place(x="470", y="380")
        label8 = tk.Label(ricefinal, text="평균적으로 저녁은 ", font=("궁서체", 25))
        label8.place(x="80", y="460")
        label9 = tk.Label(ricefinal, text=self.avDinner, font=("궁서체", 25))
        label9.place(x="400", y="460")
        label10 = tk.Label(ricefinal, text=" 회 챙겼습니다. ", font=("궁서체", 25))
        label10.place(x="470", y="460")
        ricefinal.mainloop()

if __name__ == '__main__':
    rice = Rice()
