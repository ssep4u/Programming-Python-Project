class Base:
    def mypcBase(self):
        # BACKMENU: 1.MAINMENU, 2.MYPCMENU, 3.FINISH
        print('￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣')
        print('| 　BACKMENU!　　　　　　　　　　　　　　　   　　[－][口][×] |')
        print('| ￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣ |')
        print('| 　　　　＿＿＿＿＿＿　　　　＿＿＿＿＿＿　　　　＿＿＿＿＿　　　 |')
        print('| 　　　｜1.메인메뉴 | 　　｜2.PC지키미｜ 　  |3.끝내기 | 　  |')
        print('| 　　　　￣￣￣￣￣￣　　　　￣￣￣￣￣￣　　　　￣￣￣￣￣　　　 |')
        print('￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣')

        menu = input('메뉴를 선택하세요: ')            #사용자가 메뉴 선택하게 하자
        menu = int(menu)                            #인덱스를 위해 문자를 순자로 바꿔주자

        if (menu == 1):
            print("MAINMENU로 이동합니다.")
            import WWWPJ.menu                       #menu 파일로 임폴트 하자
            show_file = WWWPJ.menu.Mainmenu()       #menu 파일에 Mainmenu 클래스에 들어가자
            show_file.mainmenu()                    #Mainmenu 클래스에 mainmenu 함수를 보여주자

        elif (menu == 2):
            print("MYPCKEEPER로 이동합니다.")
            import WWWPJ.pcKeeper                   #pckeeper 파일로 임폴트 하자
            show_file = WWWPJ.pcKeeper.Mypc_Package #pckeeper 파일에 Mypc_Package 클래스에 들어가자
            show_file.detailmenu(self)              #Mypc_Package 클래스에 detailmenu 함수를 보여주자

        elif (menu == 3):
            print('。 •　 .  ﾟ　　。　  •    。   .　')  # 프로그램을 종료하는 메세지를 보내주자
            print(' 　.　　。　•　 .　 。  .　 •　  ﾟ　')
            print('　.　 。 •  。 　 ඞ   。　.  •  。')
            print('•  .  。 프로그램을 종료합니다 。 •  ')
            print('。 • 　 .  ﾟ　　。　  •     。   .　')
            print(' .   ﾟ　　。 다음에 또 와 !  。 •  .')
            print(' 。 •　 .  ﾟ　　。　  •    。   .　')

        else:
            print(" ╭┈┈┈┈╯   ╰┈┈┈╮")
            print("  ╰┳┳╯  ╰┳┳╯")
            print("   💧 　　 💧")
            print("  💧　 　　 💧")
            print(" 💧   ╰┈┈╯   💧  ")
            print(" 💧  ╭━━━━━╮　 💧")
            print("   💧  ┈┈┈┈   1-3을 선택해 주세요ㅠㅠ  ") # 1번부터 3번까지 고르지 않았을 경우엔 에러메세지를 보내주자

            import WWWPJ.MYPCKEEPER.mypc_base              # MYPCKEEPER 폴더 속 mypc_base 파일로 임폴트 하자
            show_menu = WWWPJ.MYPCKEEPER.mypc_base.Base()  # mypc_base 파일에 Base 클래스에 들어가자
            show_menu.mypcBase()                           # Base 클래스에 mypcBase 함수를 보여주자