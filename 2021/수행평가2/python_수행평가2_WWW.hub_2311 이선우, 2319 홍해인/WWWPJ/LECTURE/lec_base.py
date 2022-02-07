class Base:
    def lecBase(self):
        # BACKMENU: 1.MAINMENU, 2.LECTUREMENU, 3.FINISH
        print('￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣')
        print('| 　BACKMENU!　　　　　　　　　　　　　　　   　　[－][口][×] |')
        print('| ￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣ |')
        print('| 　　　　＿＿＿＿＿＿　　　　＿＿＿＿＿＿　　　　＿＿＿＿＿　　　 |')
        print('| 　　　｜1.메인메뉴 | 　　｜2.강의메뉴 ｜ 　  |3.끝내기 | 　  |')
        print('| 　　　　￣￣￣￣￣￣　　　　￣￣￣￣￣￣　　　　￣￣￣￣￣　　　 |')
        print('￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣')

        menu = input('메뉴를 선택하세요: ')  # 사용자가 메뉴 선택하게 하자
        menu = int(menu)  # 인덱스를 위해 문자를 순자로 바꿔주자

        if (menu == 1):
            print("MAINMENU로 이동합니다.")
            import WWWPJ.menu  # menu 파일로 임폴트 하자
            show_file = WWWPJ.menu.Mainmenu()  # menu 파일로 임폴트 하자
            show_file.mainmenu()  # Mainmenu 클래스에 mainmenu 함수를 보여주자

        elif (menu == 2):
            print("LECTURE로 이동합니다.")
            import WWWPJ.lecture  # enviroment 파일로 임폴트 하자
            show_file = WWWPJ.lecture.Lecture_Package()  # enviroment 파일에 Env_Package 클래스에 들어가자
            show_file.detailmenu()  # Env_Package 클래스에 detailmenu 함수를 보여주자

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
            print("   💧  ┈┈┈┈   1-3을 선택해 주세요ㅠㅠ  ")# 1번부터 3번까지 고르지 않았을 경우엔 에러메세지를 보내주자

            import WWWPJ.LECTURE.lec_base              # LECTURE 폴더 속 lec_base 파일로 임폴트 하자
            show_menu = WWWPJ.LECTURE.lec_base.Base()  # lec_base 파일에 Base 클래스에 들어가자
            show_menu.lecBase()                        # Base 클래스에 lecBase 함수를 보여주자
