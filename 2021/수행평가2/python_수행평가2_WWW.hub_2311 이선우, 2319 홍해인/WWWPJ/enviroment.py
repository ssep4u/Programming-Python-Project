class Env_Package:
    def detailmenu(self):
        print('￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣')
        print('| 　ENVIROMENTMENU!　　　　　　　　　　　　　　　   　　  [－][口][×]  |')
        print('| ￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣ |')
        print('| 　＿＿＿　　＿＿＿＿　　＿＿＿＿　　 ＿＿＿＿    ＿＿＿　  ＿＿＿＿＿＿  |')
        print('| ｜1.DB | ｜2.PHP ｜ |3.Jsp |  |4.Java |  |5.C |  |6.Android | |')
        print('| 　￣￣￣　　￣￣￣￣　　￣￣￣￣　　 ￣￣￣￣　   ￣￣    ￣￣￣￣￣￣   |')
        print('￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣')

        menu = input('메뉴를 선택하세요: ')                                         #사용자가 메뉴 선택하게 하자
        menu = int(menu)                                                        #인덱스를 위해 문자를 순자로 바꿔주자

        if (menu == 1):
            print("1번 [DB] 로 이동합니다.")
            import WWWPJ.ENVIROMENT.env_db                                      #ENVIROMENT 폴더 속 env_db 파일로 임폴트 하자
            show_file = WWWPJ.ENVIROMENT.env_db.env_Db_package()                #env_db 파일에 env_Db_package 클래스에 들어가자
            show_file.show_envfile()                                            #env_Db_package 클래스에 show_envfile 함수를 보여주자

        elif (menu == 2):
            print("2번 [Php] 로 이동합니다.")
            import WWWPJ.ENVIROMENT.env_php                                     #ENVIROMENT 폴더 속 env_php 파일로 임폴트 하자
            show_file = WWWPJ.ENVIROMENT.env_php.env_Php_package()              #env_php 파일에 env_Php_package 클래스에 들어가자
            show_file.show_envfile()                                            #env_Php_package 클래스에 show_envfile 함수를 보여주자

        elif (menu == 3):
            print("3번 [Jsp] 로 이동합니다.")
            import WWWPJ.ENVIROMENT.env_jsp                                     #ENVIROMENT 폴더 속 env_jsp 파일로 임폴트 하자
            show_file = WWWPJ.ENVIROMENT.env_jsp.env_Jsp_package()              #env_jsp 파일에 env_Jsp_package 클래스에 들어가자
            show_file.show_envfile()                                            #env_Jsp_package 클래스에 show_envfile 함수를 보여주자

        elif (menu == 4):
            print("4번 [Java] 로 이동합니다.")
            import WWWPJ.ENVIROMENT.env_java                                    #ENVIROMENT 폴더 속 env_java 파일로 임폴트 하자
            show_file = WWWPJ.ENVIROMENT.env_java.env_Java_package()            #env_java 파일에 env_Java_package 클래스에 들어가자
            show_file.show_envfile()                                            #env_Java_package 클래스에 show_envfile 함수를 보여주자

        elif (menu == 5):
            print("5번 [C] 로 이동합니다.")
            import WWWPJ.ENVIROMENT.env_c                                       #ENVIROMENT 폴더 속 env_c 파일로 임폴트 하자
            show_file = WWWPJ.ENVIROMENT.env_c.env_C_package()                  #env_c 파일에 env_C_package 클래스에 들어가자
            show_file.show_envfile()                                            #env_C_package 클래스에 show_envfile 함수를 보여주자

        elif (menu == 6):
            print("6번 [Android] 로 이동합니다.")
            import WWWPJ.ENVIROMENT.env_android                                 #ENVIROMENT 폴더 속 env_android 파일로 임폴트 하자
            show_file = WWWPJ.ENVIROMENT.env_android.env_Android_package()      #env_android 파일에 env_Android_package 클래스에 들어가자
            show_file.show_envfile()                                            #env_Android_package 클래스에 show_envfile 함수를 보여주자

        else:
            print(" ╭┈┈┈┈╯   ╰┈┈┈╮")
            print("  ╰┳┳╯  ╰┳┳╯")
            print("   💧 　　 💧")
            print("  💧　 　　 💧")
            print(" 💧   ╰┈┈╯   💧  ")
            print(" 💧  ╭━━━━━╮　 💧")
            print("   💧  ┈┈┈┈   1-6을 선택해 주세요ㅠㅠ  ")                        # 1번부터 6번까지 고르지 않았을 경우엔 에러메세지를 보내주자
            import WWWPJ.enviroment                                             # enviroment 파일로 임폴트 하자
            show_file = WWWPJ.enviroment.Env_Package()                          # enviroment 파일에 Env_Package 클래스에 들어가자
            show_file.detailmenu()                                              # Env_Package 클래스에 detailmenu 함수를 보여주자