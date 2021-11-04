#2407 남정윤
#gui를 통해 음식 레시피를 작성하고 보고, 퀴즈를 풀 수 있는 프로그램.
#GUI.py에서 실행해주세요.

import tkinter as ttk
from fast_recipe import Recipe
from read_write import read
import tkinter.messagebox
import random
import sys
import os
from time import sleep

class GUI:
    def __init__(self):
        self.recipe = []
        self.material = []
        self.label = []
        self.entry = []
        self.label1 = []
        self.entry1 = []
        self.root = ttk.Tk()
        self.root.title("Fast Recipe")
        self.root.geometry("200x200")
        self.root.resizable(False,True)
        label = ttk.Label(self.root, text="Fast recipe")
        label.pack()
        button1 = ttk.Button(self.root, text="레시피 보기", command=self.show_recipe)
        button1.pack()
        label1 = ttk.Label(self.root, text = "")
        label1.pack()
        button2 = ttk.Button(self.root, text="레시피 작성하기", command=self.create_recipe)
        button2.pack()
        label2 = ttk.Label(self.root, text = "")
        label2.pack()
        button3 = ttk.Button(self.root, text="퀴즈 풀기", command=self.create_quiz)
        button3.pack()
        label3 = ttk.Label(self.root, text = "")
        label3.pack()
        button4 = ttk.Button(self.root, text="그만하기", command=self.finish)
        button4.pack()
        self.root.mainloop()

    def create_recipe(self):
        self.window = ttk.Toplevel()
        self.window.title("레시피 작성하기-카테고리")
        self.window.geometry("340x200")
        self.title = ttk.Label(self.window, text="작성할 레시피의 카테고리를 선택해주세요")
        self.title.grid(row=0, column = 1, columnspan =2)
        self.blank = ttk.Label(self.window, text=" ")
        self.blank.grid(row=1)
        self.img1 = ttk.PhotoImage(file = "img/soup.gif")
        self.soup = ttk.Label(self.window,image = self.img1, width=50,height=50)
        self.soup.grid(row = 2,column = 0)
        self.img2 = ttk.PhotoImage(file = "img/bread.gif")
        self.bread = ttk.Label(self.window,image = self.img2, width=50, height=50)
        self.bread.grid(row = 2, column = 1)
        self.img3 = ttk.PhotoImage(file = "img/noodle.gif")
        self.noodle = ttk.Label(self.window,image = self.img3, width=50, height=50)
        self.noodle.grid(row = 2, column = 2)
        self.img4 = ttk.PhotoImage(file = "img/meat.gif")
        self.meat = ttk.Label(self.window, image = self.img4, width=50, height=50)
        self.meat.grid(row = 2, column = 3)
        self.button1 = ttk.Button(self.window, text="국류", command=lambda : self.create_recipe1(0))
        self.button1.grid(row=3, column=0)
        self.button2 = ttk.Button(self.window, text="빵류", command=lambda : self.create_recipe1(1))
        self.button2.grid(row=3, column=1)
        self.button3 = ttk.Button(self.window, text="면류", command=lambda : self.create_recipe1(2))
        self.button3.grid(row=3, column=2)
        self.button4 = ttk.Button(self.window, text="육류", command=lambda : self.create_recipe1(3))
        self.button4.grid(row=3, column=3)
        self.window.mainloop()

    def show_recipe(self):
        self.window2 = ttk.Toplevel()
        self.window2.title("레시피 보기-카테고리")
        self.window2.geometry("340x200")
        self.title = ttk.Label(self.window2, text="보고싶은 레시피의 카테고리를 선택해주세요")
        self.title.grid(row=0, column = 1, columnspan =2)
        self.blank = ttk.Label(self.window2, text=" ")
        self.blank.grid(row=1)
        self.img1 = ttk.PhotoImage(file = "img/soup.gif")
        self.soup = ttk.Label(self.window2,image = self.img1, width=50,height=50)
        self.soup.grid(row = 2,column = 0)
        self.img2 = ttk.PhotoImage(file = "img/bread.gif")
        self.bread = ttk.Label(self.window2,image = self.img2, width=50, height=50)
        self.bread.grid(row = 2, column = 1)
        self.img3 = ttk.PhotoImage(file = "img/noodle.gif")
        self.noodle = ttk.Label(self.window2,image = self.img3, width=50, height=50)
        self.noodle.grid(row = 2, column = 2)
        self.img4 = ttk.PhotoImage(file = "img/meat.gif")
        self.meat = ttk.Label(self.window2, image = self.img4, width=50, height=50)
        self.meat.grid(row = 2, column = 3)
        self.button1 = ttk.Button(self.window2, text="국류", command=lambda : self.show_recipe1(0))
        self.button1.grid(row=3, column=0)
        self.button2 = ttk.Button(self.window2, text="빵류", command=lambda : self.show_recipe1(1))
        self.button2.grid(row=3, column=1)
        self.button3 = ttk.Button(self.window2, text="면류", command=lambda : self.show_recipe1(2))
        self.button3.grid(row=3, column=2)
        self.button4 = ttk.Button(self.window2, text="육류", command=lambda : self.show_recipe1(3))
        self.button4.grid(row=3, column=3)
        self.window2.mainloop()
        
        
    def show_recipe1(self, category):
        self.window2.destroy()
        List = read.get_all()
        soup = []
        bread = []
        noodle = []
        meat = []
        for item in List:
            print(item.category)
            if item.category == 0:
               soup.append(item)
            elif item.category == 1:
                bread.append(item)
            elif item.category == 2:
                noodle.append(item)
            elif item.category == 3:
                meat.append(item)
        if category ==0 :
            self.show_recipe2(soup)
        elif category == 1 :
            self.show_recipe2(bread)
        elif category ==2 :
            self.show_recipe2(noodle)
        elif category == 3 :
            self.show_recipe2(meat)

    def show_recipe2(self, f_list):
        self.window3 = ttk.Toplevel()
        self.window3.title("레시피 보기 - 리스트")
        self.window3.geometry("180x450")
        self.radio = []
        self.label = []

        j=0
        self.var = ttk.IntVar()
        self.show = ttk.Label(self.window3, text = "요리를 선택해주세요")
        self.show.grid(row=0, columnspan=2)
        for i in f_list:
            self.label.append(ttk.Label(self.window3, text = str(j+1)+" . "+i.name))
            self.label[j].grid(row=j+1, column =0)
            self.radio.append(ttk.Radiobutton(self.window3, value=j, variable=self.var))
            self.radio[j].grid(row=j+1, column=1)
            j += 1
        self.summitB = ttk.Button(self.window3, text = "선택", command = lambda : self.show1(f_list[self.var.get()]))
        self.summitB.grid(row=j+1, column =0, columnspan=2)

    def show1(self, no):
        self.window3.destroy()
        self.window7 = ttk.Toplevel()
        self.window7.title("레시피 보기")
        self.window7.geometry("550x230")
        self.recipe = "요리 : " + no.name +"\n소요 시간 : "+str(no.time)+"분\n재료 : "+no.meterial[0]
        for i in range(0,len(no.meterial)-1):
            self.recipe+=", "+no.meterial[i+1]
        self.recipe+="\n레시피 : "
        for i in range(0,len(no.recipe)):
            self.recipe+="\n"+no.recipe[i]
        print(self.recipe)
        self.show_re = ttk.Label(self.window7, text =self.recipe)
        self.show_re.grid(row = 0)
    
    def show2(self, no):
        self.recipe = "요리 : " + no.name +"\n소요 시간 : "+str(no.time)+"분\n재료 : "+no.meterial[0]
        for i in range(0,len(no.meterial)-1):
            self.recipe+=", "+no.meterial[i+1]
        self.recipe+="\n레시피 : "
        for i in range(0,len(no.recipe)):
            self.recipe+="\n"+no.recipe[i]
        return self.recipe

  
    def create_recipe1(self, category):
        self.category = category
        self.window1 = ttk.Toplevel()
        self.window1.title("레시피 작성하기 - 요리 이름")
        self.window1.geometry("340x600")
        self.title = ttk.Label(self.window1, text="요리 : ")
        self.title.grid(row=0, column=0)
        self.name = ttk.Entry(self.window1, width=20)
        self.name.grid(row=0, column = 1)
        self.time = ttk.Label(self.window1, text="시간 : ")
        self.time.grid(row=1, column=0)
        self.timeinput = ttk.Entry(self.window1, width=20)
        self.timeinput.grid(row=1, column =1)
        self.minute = ttk.Label(self.window1, text = "분")
        self.minute.grid(row=1, column =2)
        self.mat_su = ttk.Label(self.window1, text="재료 : ")
        self.mat_su.grid(row=2, column =0)
        self.mat_input = ttk.Entry(self.window1, width=20)
        self.mat_input.grid(row=2, column =1)
        self.mat_su = ttk.Label(self.window1, text = "개")
        self.mat_su.grid(row=2, column =2)
        self.mat_button = ttk.Button(self.window1, text="확인", command=lambda : self.check_mat(ttk.Entry.get(self.mat_input)))
        self.mat_button.grid(row=2, column=3)
        self.window1.mainloop()

    def check_mat(self, mat_su):
        if int(mat_su)<5:
            tkinter.messagebox.showinfo("경고","재료는 5개 이상 입력해 주세요")
        else:
            for i in range(1, int(mat_su)+1):
                text = "재료 "+str(i)+" : "
                self.label.append(ttk.Label(self.window1, text = text))
                self.label[i-1].grid(row = i+2, column =0)
                self.entry.append(ttk.Entry(self.window1, width=20))
                self.entry[i-1].grid(row = i+2, column = 1)
            self.re_su = ttk.Label(self.window1, text="레시피 : ")
            self.re_su.grid(row=i+3, column =0)
            self.re_input = ttk.Entry(self.window1, width=20)
            self.re_input.grid(row=i+3, column =1)
            self.re_su = ttk.Label(self.window1, text = "개")
            self.re_su.grid(row=i+3, column =2)
            self.re_button = ttk.Button(self.window1, text="확인", command=lambda : self.check_re(ttk.Entry.get(self.re_input),mat_su))
            self.re_button.grid(row=i+3, column=3)

    def check_re(self, re_su, mat_su):
        mat_su = int(mat_su)
        if int(re_su)<5:
            tkinter.messagebox.showinfo("경고","레시피는 5개 이상 입력해 주세요")
        else:
            for i in range(1, int(re_su)+1):
                text = "레시피 "+str(i)+" : "
                self.label1.append(ttk.Label(self.window1, text = text))
                self.label1[i-1].grid(row = i+3+mat_su, column =0)
                self.entry1.append(ttk.Entry(self.window1, width=20))
                self.entry1[i-1].grid(row = i+3+mat_su, column = 1)
            self.ok = ttk.Button(self.window1, text = "확인", command = self.insert_food)
            self.ok.grid(row = i+4+mat_su, columnspan = 3)
        
    def insert_food(self):
        for i in range(0,len(self.entry)):
            self.material.append(ttk.Entry.get(self.entry[i]))
        for i in range(0,len(self.entry1)):
            self.recipe.append(ttk.Entry.get(self.entry1[i]))
        self.name=ttk.Entry.get(self.re_input)
        self.time = int(ttk.Entry.get(self.timeinput))
        print(self.category)
        r = Recipe(self.name, self.material, self.time, self.recipe, self.category )
        read.create(r)
        tkinter.messagebox.showinfo("레시피 완성","레시피 작성이 완료되었습니다.")
        self.window1.destroy()
        self.window.destroy()
    
    def create_quiz(self):
        self.window5 = ttk.Toplevel()
        self.window5.title("퀴즈 풀기-카테고리")
        self.window5.geometry("340x200")
        self.title = ttk.Label(self.window5, text="원하는 카테고리를 선택해 주세요")
        self.title.grid(row=0, column = 1, columnspan =2)
        self.blank = ttk.Label(self.window5, text=" ")
        self.blank.grid(row=1)
        self.img1 = ttk.PhotoImage(file = "img/soup.gif")
        self.soup = ttk.Label(self.window5,image = self.img1, width=50,height=50)
        self.soup.grid(row = 2,column = 0)
        self.img2 = ttk.PhotoImage(file = "img/bread.gif")
        self.bread = ttk.Label(self.window5,image = self.img2, width=50, height=50)
        self.bread.grid(row = 2, column = 1)
        self.img3 = ttk.PhotoImage(file = "img/noodle.gif")
        self.noodle = ttk.Label(self.window5,image = self.img3, width=50, height=50)
        self.noodle.grid(row = 2, column = 2)
        self.img4 = ttk.PhotoImage(file = "img/meat.gif")
        self.meat = ttk.Label(self.window5, image = self.img4, width=50, height=50)
        self.meat.grid(row = 2, column = 3)
        self.button1 = ttk.Button(self.window5, text="국류", command=lambda : self.create_quiz1(0))
        self.button1.grid(row=3, column=0)
        self.button2 = ttk.Button(self.window5, text="빵류", command=lambda : self.create_quiz1(1))
        self.button2.grid(row=3, column=1)
        self.button3 = ttk.Button(self.window5, text="면류", command=lambda : self.create_quiz1(2))
        self.button3.grid(row=3, column=2)
        self.button4 = ttk.Button(self.window5, text="육류", command=lambda : self.create_quiz1(3))
        self.button4.grid(row=3, column=3)
        self.window5.mainloop()

    def create_quiz1(self, category):
        List = read.get_all()
        soup = []
        bread = []
        noodle = []
        meat = []
        for item in List:
            if item.category == 0:
                soup.append(item)
            elif item.category == 1:
                bread.append(item)
            elif item.category == 2:
                noodle.append(item)
            elif item.category == 3:
                meat.append(item)
        if category == 0:
            self.select_randomQ(category,soup)
        elif category == 1:
            self.select_randomQ(category,bread)
        elif category ==2:
            self.select_randomQ(category,noodle)
        elif category ==3:
            self.select_randomQ(category, meat)

    def select_randomQ(self, cate, List):#문제를 선택하고 보여줌
        self.score = 0
        rannum = random.randrange(0, len(List)) #랜덤 요리 선택
        ran = random.randrange(0, len(List)) # 오답 카테고리 중에서 오답재료선택
        self.recipeT = ttk.Toplevel()
        self.recipeT.title("레시피 보기")
        self.recipeT.geometry("340x200")
        self.show_re = ttk.Label(self.recipeT, text=self.show2(List[rannum]))
        self.show_re.grid(row = 0)
        self.window5.destroy()
        tkinter.messagebox.showinfo("QUIZ!","20초 후에 레시피가 사라집니다.\n빨리 외워 주세요!")
        #랜덤값으로 레시피 보여주기
        sleep(20)
        self.recipeT.destroy()
        self.ifran = random.randrange(0,5)#오답을 몇번째에 낼 건지
        self.quiz = ttk.Toplevel()
        self.quiz.title("퀴즈")
        self.quiz.geometry("340x200")
        self.label = []
        self.radio = []
        self.var = ttk.IntVar()
        for i in List[rannum].meterial:
            print(i)
        for j in range(0, 5):#4개의 정답과 1개의 오답 내는
            if j == self.ifran:
                self.label.append(ttk.Label(self.quiz, text = (j+1, ". "+List[ran].meterial[j]))) #1개의 오답
                self.label[j].grid(row=j, column=0)
                self.radio.append(ttk.Radiobutton(self.quiz,value=j, variable=self.var))
                self.radio[j].grid(row=j, column=1)
                continue
            self.label.append(ttk.Label(self.quiz, text = (j+1, ". "+List[rannum].meterial[j])))#나머지 정답
            self.label[j].grid(row=j, column=0)
            self.radio.append(ttk.Radiobutton(self.quiz,value=j, variable=self.var))
            self.radio[j].grid(row=j, column=1)
        self.ansButton = ttk.Button(self.quiz, text = "선택", command = lambda: self.ans(self.var.get()))
        self.ansButton.grid(row = j+1)

        tkinter.messagebox.showinfo("QUIZ!","레시피의 재료로 옳지 않은 것은?") 
        print(self.ifran+1)
    def ans(self, su):
        tkinter.messagebox.showinfo("QUIZ!","정답은 "+str(self.ifran+1)+"번 입니다.")
        if(su == self.ifran):
            tkinter.messagebox.showinfo("QUIZ!","정답입니다!")
        else:
            tkinter.messagebox.showinfo("QUIZ!","틀렸습니다!")

        self.quiz.destroy()

    def finish(self):
        self.root.destroy()

if __name__ == '__main__':
    gui = GUI()