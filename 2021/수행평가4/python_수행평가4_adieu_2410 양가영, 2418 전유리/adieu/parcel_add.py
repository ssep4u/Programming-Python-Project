from tkinter import *
from tkinter import messagebox

from adieu_main import adieuMain
from _Adoption_book import Adoption_book

class ParceAdieuAdd():
    def __init__(self,title):
        self.engien = Adoption_book()
        self.parcelEditGUI(title)

    def parcelEditGUI(self, title):
        bg_color = '#FFC978'  # 배경색
        self.root = Tk()
        self.root.title(title)
        self.root.geometry('745x580+400+100')
        self.root.configure(bg=bg_color)
        self.root.resizable(0, 0)

        # 프레임 설정
        self.mainFrame = Frame(self.root, bg=bg_color)
        self.mainFrame.pack(expand=True)

        # input 박스 타이틀
        info1 = ['이름', '성별', '나이', '장소']
        info2 = ['세부설명', '게시물 작성자', '종류']

        # logo 설정
        logo_img = PhotoImage(file='img/Adieu.png', width=200, height=87)
        logo = Label(self.root, bg=bg_color, image=logo_img)
        logo.bind('<Button-1>',self.cancelbtnEvent)

        photo_img = PhotoImage(file='img/animal_img.png')
        photo = Label(self.root, image=photo_img, bg=bg_color, anchor="w")  # 이미지 넣기 왼쪽 정렬
        # button 설정
        btn_edit = Button(self.root, width=10, text='등록', bg='#F0AD48', command=self.subscriptionEvent, relief='flat', bd=10, fg='#B96F00')
        btn_back = Button(self.root, width=10, text='취소', bg='#F0AD48', command=self.cancelbtnEvent, relief='flat', bd=10, fg='#B96F00')

        # 입력받기
        infoFrame1 = Frame(self.root, bg=bg_color, width=350, height=400)
        infoFrame2 = Frame(self.root, bg=bg_color, width=100, height=200)
        inputFrame1 = Frame(self.root, bg=bg_color, width=430, height=400)
        inputFrame2 = Frame(self.root, bg=bg_color, width=100, height=200)
        name = Entry(inputFrame1, width=15, relief="flat", bd=13, fg="gray")
        age = Entry(inputFrame1, width=15, relief="flat", bd=13, fg="gray")
        place = Entry(inputFrame1, width=15, relief="flat", bd=13, fg="gray")
        add_infor = Entry(inputFrame2, width=52, relief="flat", bd=13, fg="gray")
        self.gender_ani = IntVar()  # 여기에 int 형으로 값을 저장한다
        gender_w = Radiobutton(self.root, text="암컷", value=1, variable=self.gender_ani, bg=bg_color)
        gender_m = Radiobutton(self.root, text="수컷", value=2, variable=self.gender_ani, bg=bg_color)
        gender_w.select()  # 기본적으로 여자 선택
        self.species_var = IntVar()
        species_0 = Radiobutton(self.root, text="고양이", value=0, variable=self.species_var, bg=bg_color)
        species_1 = Radiobutton(self.root, text="강아지", value=1, variable=self.species_var, bg=bg_color)
        species_2 = Radiobutton(self.root, text="새", value=2, variable=self.species_var, bg=bg_color)
        species_3 = Radiobutton(self.root, text="기타", value=3, variable=self.species_var, bg=bg_color)
        species_0.select()
        self.inputList = [name, age, place, add_infor]  # 입력 받을 리스트

        # hint
        self.inputList[0].insert(0, '이름')
        self.inputList[1].insert(0, '나이')
        self.inputList[2].insert(0, '장소')
        self.inputList[3].insert(0, '추가설명')

        # hint 이벤트
        self.inputList[0].bind('<Button-1>', lambda x: self.hintEvent(event=name))
        self.inputList[1].bind('<Button-1>', lambda x: self.hintEvent(event=age))
        self.inputList[2].bind('<Button-1>', lambda x: self.hintEvent(event=place))
        self.inputList[3].bind('<Button-1>', lambda x: self.hintEvent(event=add_infor))

        # tab 이벤트
        self.inputList[0].bind('<FocusIn>', lambda x: self.hintEvent(event=name))
        self.inputList[1].bind('<FocusIn>', lambda x: self.hintEvent(event=age))
        self.inputList[2].bind('<FocusIn>', lambda x: self.hintEvent(event=place))
        self.inputList[3].bind('<FocusIn>', lambda x: self.hintEvent(event=add_infor))

        # 화면에 출력    ----------------------
        infoFrame1.place(x=380, y=80)
        inputFrame1.place(x=460, y=80)
        infoFrame2.place(x=50, y=340)
        inputFrame2.place(x=150, y=340)
        logo.place(x=10, y=5)
        photo.place(x=100, y=90)
        btn_edit.place(x=470, y=500)
        btn_back.place(x=590, y=500)
        # input 박스 타이틀
        info1 = ['이름', '나이', '장소', '성별']
        info2 = ['세부설명','종류']

        for i, d in enumerate(info1):  # 왼쪽 수직 타이틀 텍스트 보여주기
            text = Label(infoFrame1, bg=bg_color, width=10, text=d, fg='#333')
            text.pack(padx=10, pady=20)

        for i, d in enumerate(info2):  # 하단 수평 타이틀 텍스트 보여주기
            text = Label(infoFrame2, bg=bg_color, width=10, text=d, fg='#333')
            text.pack(padx=10, pady=15)

        name.pack(padx=15, pady=10, anchor='w')
        gender_w.place(x=470, y=295, anchor='w')
        gender_m.place(x=535, y=295, anchor='w')
        age.pack(padx=15, pady=10, anchor='w')
        place.pack(padx=15, pady=5, anchor='w')
        add_infor.pack(padx=10, pady=5, anchor='w')
        species_0.place(x=150, y=420, anchor='w')
        species_1.place(x=220, y=420, anchor='w')
        species_2.place(x=290, y=420, anchor='w')
        species_3.place(x=340, y=420, anchor='w')
        self.play()

    def cancelbtnEvent(self):   # 취소
        self.root.destroy()
        adieuMain("메인")

    def subscriptionEvent(self):    # 등록후 메인
        for info in self.inputList:
            if info['foreground']!='black': # 입력 안되엇을경우
                messagebox.showinfo("입력오류",info.get()+" 입력하시오.")
                return
        message = self.engien.up_animal(self.inputList, self.gender_ani,self.species_var)
        if message != 'ok':
            messagebox.showinfo("오류", message)  # 등록이 성공적으로 안되면 이유 리턴
            return
        messagebox.showinfo("안내","게시물 등록 완료!!")
        self.root.destroy()
        adieuMain("메인")

    # 클릭 시 입력
    def hintEvent(self,event):  # 눌렀을때 글자 넣을수 있게
        event.config(fg='black')
        event.delete(0,END)

    def play(self):
        self.root.mainloop()


if __name__ == '__main__':
    ParceAdieuAdd('분양게시물등록')