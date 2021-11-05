#2318 장유경
#'만다르트 기법'을 배경으로 한 책 추천 프로그램. 장르별로 책을 분류하고, 흥미가 가는 책을 골라 누르면 명대사를 출력해주고 명대사를 저장 할 수 있습니다
#checkmain.py(현재 파일) 에서 실행한 후, 버튼을 하나씩 클릭하면 됩니다

from tkinter import *
# from tkinter as tk
import tkinter as tk
from tkinter import messagebox as msg
import webbrowser
import sys

class checkmain:
    def __init__(self): #메인 화면 구성 함수
        self.mmWindow = tk.Tk()
        self.mmWindow.title("책크리스트")
        # 메인 목차
        button_mult = tk.Button(self.mmWindow, height=4, width=10, text="SF", command = self.sbutton)   #버튼 만들기/command=self.sbutton-> sbutton으로 이동함
        button_mult.grid(row=1, column=0)  #버튼 위치 조정
        button_mult = tk.Button(self.mmWindow, height=4, width=10, text="한국소설", command = self.kbutton)
        button_mult.grid(row=1, column=1)
        button_mult = tk.Button(self.mmWindow, height=4, width=10, text="고전소설",  command = self.gbutton)
        button_mult.grid(row=1, column=2)

        button_mult = tk.Button(self.mmWindow, height=4, width=10, text="외국소설", command = self.ebutton)
        button_mult.grid(row=2, column=0)
        button_mult = tk.Button(self.mmWindow, height=4, width=10, text="책",
                                background='#ff0000')  #버튼 배경색 지정
        button_mult.grid(row=2, column=1)
        button_mult = tk.Button(self.mmWindow, height=4, width=10, text="작성한 명대사", command = self.fbutton)
        button_mult.grid(row=2, column=2)

        button_mult = tk.Button(self.mmWindow, height=4, width=10, text="사용방법", command=self.useinfo)
        button_mult.grid(row=3, column=0)
        button_mult = tk.Button(self.mmWindow, height=4, width=10,
                                text="책 사러가기",  command = self.OpenUrl)
        button_mult.grid(row=3, column=1)
        button_mult = tk.Button(self.mmWindow, height=4, width=10, text="파일저장",command = self.mychart)
        button_mult.grid(row=3, column=2)
        self.mmWindow.mainloop()

    def show(self,num,num1): #누르면 책 명대사 보여주는 함수
        textList  = []
        sf = ['세상이 어떤 식으로 바뀌는 것을 보고 싶다면\n너 자신이 그런 쪽으로 변해야 한다.\n베르나르 베르베르 지음',
               '미래는 이미 와 있다.\n단지 널리 퍼지지 않았을 뿐이다\n윌리엄 깁슨 지음',
               '나는 처음부터 나의 목적지가 어디인지 알고 있었고\n그것에 상응하는 경로를 골랐어\n테드창 지음',
               '자유의지가 있는 것처럼 행동하라.\n설령 사실이 아님을 알고 있어도,\n스스로 내리는 선택에 의미가 있는 듯이 행동하는 것이 가장 중요하다.\n테드창 지음',
               '나는 내 우울을 쓰다듬고 손 위에 두길 원해.\n그게 찍어 맛 볼수 있고 단단히 만져지는 것이면 좋겠어.\n김초엽 지음',
               '명대사 준비중입니다.\n아이작 아시모프 지음',
               '그에게 정말 간절한 소원이 있다면,\n그건 바로 말 한마리를 갖는 것 이다.\n필립 K.딕 지음',
               '전쟁은 평화, 자유는 예속, 무지는 힘.\n조지 오웰 지음']

        korea = ['흥미로운 사실은, 군중을 이루는 개개인의 도덕적 수준과 별개로\n특정한 윤리적 파동이 현장에서 발생된다는 것이다.\n한강 지음',
                 '어떤 연애는 우정 같고,\n어떤 우정은 연애 같다.\n쇼코를 생각하면 그 애가 나를 더 이상 좋아하지 않을까봐 두려웠었다.',
                 '사람들은 곤이가 대체 어떤 앤지 모르겠다고 했지만,\n나는 그말에 동의하지 않았다.\n단지 아무도 곤이를 들여다보지 않았을 뿐이다.\n손원평 지음',
                 '아무도 교사가 매력을 활용하는 직업이라고\n얘기해 주지 않았으므로 너무 뒤늦게 깨달았다.\n정세랑 지음',
                 '사람들이 나보고\n맘충이래\n조남주 지음','그것은 사람의 몸이라기 보단 잘 세공된 보석 같았으며\n곤이 세상의 어느 누구와도 같지 않은\n특별한 생명체임을 증명하는 표지였다.\n구병모지음',
                 '한 사람이라도 당신을 닮았기를\n당신의 목소리로 말하길 빕니다.\n정세랑 지음','어떤놈이 그랬는지\n찾아서 똑같이 갚어줘야지!\n정유정 지음']

        english = ['새는 알에서 빠져나오려고 몸부림친다. 알은 세계이다. 태어나려는 자는 누구든 한 개의 세계를 부숴야 한다.\n헤르만 헤세 지음',
                   '그가 말하는 세상이란 대체 뭘까요,\n인간의 복수형일까요?\n다자이 오사무 지음',
                   '너무 계산적으로 살지 말아요 우리\nF.스콧 제럴드 지음',
                   '편견은 내가 다른 사람을 사랑할 수 없게 하고\n 오만은 다른 사람이 나를 사랑하지 못하게 한다.\n제인 오스틴 지음',
                   '인간은 패배하기 위해 태어난게 아니야\n인간은 파멸 당할 수 있을지 언정 패배하진 않아.\n어니스트 해밍웨이 지음',
                   '행복한 가정은 모두 비슷한 이유로 행복하지만\n 불행한 가정은 저마다의 이유로 불행하다.\n레프 톨스토이 지음',
                   '히스클리프는 나야.\n에밀리 브론테 지음',
                   '암흑 없이는 빛이 없고, 타인 없이는 내가 없듯이\n슬픔과 두려움과 질병과 고통없이는\n즐거움도 느끼지 못하리라.\n헤르만 헤세 지음']
        fore = [
            '가장 어두운 시간에도 행복은 존재해.\n조앤 케이 롤링',
             '사랑을 한다는 건 그런거야\n숨이 멎을 만큼 황홀한 기분을 느끼는 것도 네 몫이고,\n깊은 어둠 속에서 방황하는 것도 네 몫이지.\n넌 자신의 몸과 마음으로 그것을 견뎌야만 해\n무라카미 하루키 지음',
             '사람이 자유로워 진다는 건 어떤 것일까...그녀는 곧잘 자문했다.\n하나의 감옷에서 멋지게 빠져나온다 해도, 그곳 역시 또다른 좀더 큰 감옥에 지나지 않는 것일까?\n무라카미 하루키 지음',
             '다른 사람들의 결정에 자신의 행복을 의지하는 사람은 불행해지기 마련이란다.\n어느 누구에게도 종속되면 안 돼\n베르나르 베르베르 지음',
             '만약 네가 말해준다면, \n제이 아셰르 지음','미래에 대해 생각해 봤자 소용없다.\n 일어날 일은 어짜피 일어난다.\n요나스 요나손 지음.',
            '때로는 뒤에 남긴 삶의 자취가 앞에 놓인 길보다 더 중요한 법이라는 거다. \n바바라 오코너 지음',
            '이 세상은 일부의 인간들만으로 움직여지는 것이 아니다.\n얼핏 보기에 아무 재능도 없고 가치도 없어 보이는 사람들이야말로 중요한 구성 요소다.\n히가시노 게이고 지음'
        ]

        textList.append(sf)
        textList.append(korea)
        textList.append(english)
        textList.append(fore)
        self.window1 = tk.Toplevel()
        self.la = tk.Label(self.window1, text = textList[num-1][num1-1])
        self.la.pack()

    def sbutton(self): #sf 소설 책 페이지 함수
        self.window = tk.Toplevel()
        button_mult = tk.Button(self.window, height=4, width=10, text="제 3인류", command = lambda : self.show(1,1))
        button_mult.grid(row=1, column=0)
        button_mult = tk.Button(self.window, height=4, width=10, text="뉴로맨서", command = lambda : self.show(1,2))
        button_mult.grid(row=1, column=1)
        button_mult = tk.Button(self.window, height=4, width=10,
                                text="당신\n인생의\n이야기", command = lambda : self.show(1,3))
        button_mult.grid(row=1, column=2)

        button_mult = tk.Button(self.window, height=4, width=10, text="숨", command = lambda : self.show(1,4))
        button_mult.grid(row=2, column=0)
        button_mult = tk.Button(self.window, height=4, width=10, text="sf",
                                background='#ff0000')
        button_mult.grid(row=2, column=1)
        button_mult = tk.Button(self.window, height=4, width=10,
                                text="우리가\n빛의속도로\n갈수없다면", command = lambda : self.show(1,5))
        button_mult.grid(row=2, column=2)

        button_mult = tk.Button(self.window, height=4, width=10, text="파운데이션", command = lambda : self.show(1,6))
        button_mult.grid(row=3, column=0)
        button_mult = tk.Button(self.window, height=4, width=10,
                                text="안드로이드는\n전기양을\n꿈꾸는가?", command = lambda : self.show(1,7))
        button_mult.grid(row=3, column=1)
        button_mult = tk.Button(self.window, height=4, width=10, text="1984↖", command = lambda : self.show(1,8))
        button_mult.grid(row=3, column=2)
        
    def kbutton(self): #한국 소설 목차 페이지 함수
            self.window = tk.Toplevel()
            button_mult = tk.Button(self.window, height=4, width=10,
                                    text="소년이 온다", command = lambda : self.show(2,1))
            button_mult.grid(row=1, column=0)
            button_mult = tk.Button(self.window, height=4, width=10,
                                    text="쇼코의 미소", command = lambda : self.show(2,2))
            button_mult.grid(row=1, column=1)
            button_mult = tk.Button(self.window, height=4, width=10,
                                    text="아몬드", command = lambda : self.show(2,3))
            button_mult.grid(row=1, column=2)

            button_mult = tk.Button(self.window, height=4, width=10,
                                    text="보건교사\n안은영", command = lambda : self.show(2,4))
            button_mult.grid(row=2, column=0)
            button_mult = tk.Button(self.window, height=4, width=10, text="한국소설",
                                    background='#ff0000')
            button_mult.grid(row=2, column=1)
            button_mult = tk.Button(self.window, height=4, width=10,
                                    text="82년생\n김지영", command = lambda : self.show(2,5))
            button_mult.grid(row=2, column=2)

            button_mult = tk.Button(self.window, height=4, width=10,
                                    text="아가미", command = lambda : self.show(2,6))
            button_mult.grid(row=3, column=0)
            button_mult = tk.Button(self.window, height=4, width=10,
                                    text="피프티 피플", command = lambda : self.show(2,7))
            button_mult.grid(row=3, column=1)
            button_mult = tk.Button(self.window, height=4, width=10,
                                    text="7년의 밤↖", command = lambda : self.show(2,8))
            button_mult.grid(row=3, column=2)

    def gbutton(self):  # 고전 소설 목차 페이지 함수
            self.window = tk.Toplevel()
            button_mult = tk.Button(self.window, height=4, width=10,
                                        text="데미안" ,command = lambda : self.show(3,1))
            button_mult.grid(row=1, column=0)
            button_mult = tk.Button(self.window, height=4, width=10,
                                        text="인간실격",command = lambda : self.show(3,2))
            button_mult.grid(row=1, column=1)
            button_mult = tk.Button(self.window, height=4, width=10,
                                        text="위대한 개츠비",command = lambda : self.show(3,3))
            button_mult.grid(row=1, column=2)

            button_mult = tk.Button(self.window, height=4, width=10,
                                        text="오만과\n편견",command = lambda : self.show(3,4))
            button_mult.grid(row=2, column=0)
            button_mult = tk.Button(self.window, height=4, width=10, text="고전소설",
                                        background='#ff0000')
            button_mult.grid(row=2, column=1)
            button_mult = tk.Button(self.window, height=4, width=10,
                                        text="노인과\n바다",command = lambda : self.show(3,5))
            button_mult.grid(row=2, column=2)

            button_mult = tk.Button(self.window, height=4, width=10,
                                        text="안나\n카레니나",command = lambda : self.show(3,6))
            button_mult.grid(row=3, column=0)
            button_mult = tk.Button(self.window, height=4, width=10,
                                        text="폭풍의\n언덕",command = lambda : self.show(3,7))
            button_mult.grid(row=3, column=1)
            button_mult = tk.Button(self.window, height=4, width=10,
                                        text="크눌프↖",command = lambda : self.show(3,8))
            button_mult.grid(row=3, column=2)

    def ebutton(self):  # 외국소설 소설 목차 페이지 함수
            self.window = tk.Toplevel()
            button_mult = tk.Button(self.window, height=4, width=10, text="해리포터\n시리즈", command = lambda : self.show(4,1))
            button_mult.grid(row=1, column=0)
            button_mult = tk.Button(self.window, height=4, width=10, text="해변의\n카프카", command = lambda : self.show(4,2))
            button_mult.grid(row=1, column=1)
            button_mult = tk.Button(self.window, height=4, width=10, text="1Q84", command = lambda : self.show(4,3))
            button_mult.grid(row=1, column=2)
            button_mult = tk.Button(self.window, height=4, width=10,text="죽음", command = lambda : self.show(4,4))
            button_mult.grid(row=2, column=0)
            button_mult = tk.Button(self.window, height=4, width=10, text="외국소설", background='#ff0000')
            button_mult.grid(row=2, column=1)
            button_mult = tk.Button(self.window, height=4, width=10, text="루머의\n루머의\n루머", command = lambda : self.show(4,5))
            button_mult.grid(row=2, column=2)
            button_mult = tk.Button(self.window, height=4, width=10, text="창문을 넘어서\n도망친\n100세 노인", command = lambda : self.show(4,6))
            button_mult.grid(row=3, column=0)
            button_mult = tk.Button(self.window, height=4, width=10, text="개를 훔치는\n완벽한 방법", command = lambda : self.show(4,7))
            button_mult.grid(row=3, column=1)
            button_mult = tk.Button(self.window, height=4, width=10, text="마력의\n태동", command = lambda : self.show(4,8))
            button_mult.grid(row=3, column=2)\

    def fbutton(self): #작성한 명대사 파일 불러오는 함수
        self.window = tk.Toplevel()
        f = open ("output.txt","r")
        text=f.read()
        label = tk.Label(self.window, text = text)
        label.pack()


    def useinfo(self): #사용 방법 알려주는 함수, 새창 띄움
        self.window = tk.Toplevel()
        self.window.resizable(width=TRUE, height=TRUE);
        label1 = tk.Label(self.window, text="1. 보고싶으신 책의 장르를 선택해주세요.\n"
                                            "2. 이중 읽고싶은 책의 장르를 고르시고, 명대사를 확인해주세요\n"
                                            "3. 마음에 드는 명대사가 있다면, 초기 화면의 파일 저장 버튼을 클릭해 명대사를 저장해주세요.\n"
                                            "4. 내가 마음에 들어한 명대사는, 다음에 다시 실행했을때도 확인할 수 있습니다.")
        label1.pack()

    def saved(self, text): #파일 저장하는 함수
        f = open('output.txt','a')
        f.write(text+"\n")
        msg.showwarning('저장완료', '저장되었습니다') #메세지 박스 출력
        self.window.destroy() #화면 창 끄기

    def mychart(self): #명대사 저장하기 위해 입력하는 창
            self.window = tk.Toplevel()
            self.window.geometry("800x400")

            label1 = Label(self.window, text = "인상 깊게 본 명대사를 써주세요!")
            str = StringVar()
            textbox = Entry(self.window, width=20, textvariable=str)
            label1.pack()
            textbox.pack()
            button_sa = tk.Button(self.window, height=6, width=10, text="저장", command=lambda:self.saved(str.get()))
            button_sa.pack()
            self.window.mainloop()

    def OpenUrl(self): #알라딘 웹사이트로 으로 이동하는 함수
        url = 'https://www.aladin.co.kr/home/welcome.aspx'
        webbrowser.open_new(url)


if __name__ == '__main__':
    checkmain=checkmain()