import tarfile
from tkinter import *
# import tkinter.messagebox
import tkinter

import MAEUM_MAIN

class Top3:
    def __init__(self, top3):
        self.top3 = top3

        #화면 이미지
        self.top3Back = tkinter.PhotoImage(file = "img/top3_back.png")
        self.top3BackL = tkinter.Label(image=self.top3Back)
        self.top3BackL.place(x=-2, y=-2)

        self.c_d = dict()
        file = open('미림마이스터고.txt', 'r', encoding="UTF-8")
        m_lines = file.readlines()
        m_lines = ' '.join(m_lines)
        m_lines = int(m_lines)
        self.c_d['미림마이스터고'] = m_lines  # m_line

        file = open('선린인터넷고.txt', 'r', encoding="UTF-8")
        s_lines = file.readlines()
        s_lines = ' '.join(s_lines)
        s_lines = int(s_lines)
        self.c_d['선린인터넷고'] = s_lines  # s_line

        file = open('디지털미디어고.txt', 'r', encoding="UTF-8")
        d_lines = file.readlines()
        d_lines = ' '.join(d_lines)
        d_lines = int(d_lines)
        self.c_d['디지털미디어고'] = d_lines  # d_line

        count_dic = sorted(self.c_d.items(), key=lambda x: x[1], reverse = True)
        print(count_dic[0][0])
        print(count_dic[1][0])
        print(count_dic[2][0])

        t1 = tkinter.Label(top3)
        t1.config(text=count_dic[0][0], bg='white', font='Times 32 bold italic')
        t1.place(x= 300, y=190)

        t2 = tkinter.Label(top3)
        t2.config(text=count_dic[1][0], bg='white', font='Times 32 bold italic')
        t2.place(x= 300, y=325)

        t3 = tkinter.Label(top3)  # 레이블 텍스트
        t3.config(text=count_dic[2][0], bg='white', font='Times 32 bold italic')
        t3.place(x= 300, y=462)  # 레이블 배치

        #back 버튼
        self.backButton = tkinter.Button(self.top3, width=120, height=67, borderwidth=0, command=self.BackButton)
        self.backButton.place(x=750, y=27)
        self.backButtonImg = tkinter.PhotoImage(file="img/back_yellow.PNG")
        self.backButton.config(image=self.backButtonImg)

    def BackButton(self):
        MAEUM_MAIN.Maeum_main(self.top3)

