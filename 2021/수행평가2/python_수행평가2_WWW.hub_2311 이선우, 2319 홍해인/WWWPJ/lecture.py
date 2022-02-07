class Lecture_Package:
    def detailmenu(self):
        print('￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣')
        print('| 　LECTUREMENU!　　   　　　　　　　　　　　　　   　　             [－][口][×]  |')
        print('| ￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣   |')
        print('| 　＿＿＿　　＿＿＿＿　　＿＿＿＿　　 ＿＿＿＿＿＿    ＿＿　   ＿＿＿＿    ＿＿＿＿＿  |')
        print('| ｜1.DB | ｜2.Jsp ｜ |3.Java |  |4.Python |  |5.C |  |6.Wsm |  |7.Spring | |')
        print('| 　￣￣￣　　￣￣￣￣　　￣￣￣￣　　  ￣￣￣￣￣　   ￣￣    ￣￣￣￣    ￣￣￣￣￣   |')
        print('￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣')

        menu = input('메뉴를 선택하세요: ')                                         #사용자가 메뉴 선택하게 하자
        menu = int(menu)                                                         #인덱스를 위해 문자를 순자로 바꿔주자

        if (menu == 1):
            print("1번 [DB 강의] 로 이동합니다.")
            import WWWPJ.LECTURE.lec_db                                         #LECTURE 폴더 속 lec_db 파일로 임폴트 하자
            show_file = WWWPJ.LECTURE.lec_db.lecture_db_package()               #lec_db 파일에 lecture_db_package 클래스에 들어가자
            show_file.show_lecfile()                                            #lecture_db_package 클래스에 show_lecfile 함수를 보여주자

        elif (menu == 2):
            print("2번 [JSP 강의] 로 이동합니다.")
            import WWWPJ.LECTURE.lec_jsp                                        #LECTURE 폴더 속 lec_jsp 파일로 임폴트 하자
            show_file = WWWPJ.LECTURE.lec_jsp.lecture_jsp_package()             #lec_jsp 파일에 lecture_jsp_package 클래스에 들어가자
            show_file.show_lecfile()                                            #lecture_jsp_package 클래스에 show_lecfile 함수를 보여주자

        elif (menu == 3):
            print("3번 [JAVA 강의] 로 이동합니다.")
            import WWWPJ.LECTURE.lec_java                                       #LECTURE 폴더 속 lec_java 파일로 임폴트 하자
            show_file = WWWPJ.LECTURE.lec_java.lecture_java_package()           #lec_java 파일에 lecture_java_package 클래스에 들어가자
            show_file.show_lecfile()                                            #lecture_java_package 클래스에 show_lecfile 함수를 보여주자

        elif (menu == 4):
            print("4번 [Python 강의] 로 이동합니다.")
            import WWWPJ.LECTURE.lec_python                                     #LECTURE 폴더 속 lec_python 파일로 임폴트 하자
            show_file = WWWPJ.LECTURE.lec_python.lecture_python_package()       #lec_python 파일에 lecture_python_package 클래스에 들어가자
            show_file.show_lecfile()                                            #lecture_python_package 클래스에 show_lecfile 함수를 보여주자

        elif (menu == 5):
            print("5번 [C 강의] 로 이동합니다.")
            import WWWPJ.LECTURE.lec_c                                          #LECTURE 폴더 속 lec_c 파일로 임폴트 하자
            show_file = WWWPJ.LECTURE.lec_c.lecture_c_package()                 #lec_c 파일에 lecture_c_package 클래스에 들어가자
            show_file.show_lecfile()                                            #lecture_c_package 클래스에 show_lecfile 함수를 보여주자

        elif (menu == 6):
            print("6번 [WSM 강의] 로 이동합니다.")
            import WWWPJ.LECTURE.lec_wsm                                        #LECTURE 폴더 속 lec_wsm 파일로 임폴트 하자
            show_file = WWWPJ.LECTURE.lec_wsm.lecture_wsm_package()             #lec_wsm 파일에 lecture_wsm_package 클래스에 들어가자
            show_file.show_lecfile()                                            #lecture_wsm_package 클래스에 show_lecfile 함수를 보여주자

        elif (menu == 7):
            print("7번 [Spring 강의] 로 이동합니다.")
            import WWWPJ.LECTURE.lec_spring                                     #LECTURE 폴더 속 lec_spring 파일로 임폴트 하자
            show_file = WWWPJ.LECTURE.lec_spring.lecture_spring_package()       #lec_spring 파일에 lecture_spring_package 클래스에 들어가자
            show_file.show_lecfile()                                            #lecture_spring_package 클래스에 show_lecfile 함수를 보여주자

        else:
            print(" ╭┈┈┈┈╯   ╰┈┈┈╮")
            print("  ╰┳┳╯  ╰┳┳╯")
            print("   💧 　　 💧")
            print("  💧　 　　 💧")
            print(" 💧   ╰┈┈╯   💧  ")
            print(" 💧  ╭━━━━━╮　 💧")
            print("   💧  ┈┈┈┈   1-7을 선택해 주세요ㅠㅠ  ")  # 1번부터 7번까지 고르지 않았을 경우엔 에러메세지를 보내주자
            import WWWPJ.lecture                          # enviroment 파일로 임폴트 하자
            show_file = WWWPJ.lecture.Lecture_Package()   # enviroment 파일에 Env_Package 클래스에 들어가자
            show_file.detailmenu()                        # Env_Package 클래스에 detailmenu 함수를 보여주자