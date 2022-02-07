class Mypc_Package:
    def detailmenu(self):
        print('￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣')
        print('| 　MYPCKEEPER!　　　　　　　　　　　　　　　   　　     [－][口][×]   |')
        print('| ￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣ |')
        print('| 　＿＿＿＿＿＿＿　　＿＿＿＿＿＿　　＿＿＿＿＿＿　　 ＿＿＿＿＿＿＿      |')
        print('| ｜1.기본설명서 | ｜2.다운로드 ｜ |3.한글패치 |  |4.비밀번호변경 |    |')
        print('| 　￣￣￣￣￣￣￣　　￣￣￣￣￣￣　　￣￣￣￣￣￣　　 ￣￣￣￣￣￣￣　     |')
        print('￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣')

        menu = input('메뉴를 선택하세요: ')                                         #사용자가 메뉴 선택하게 하자
        menu = int(menu)                                                         #인덱스를 위해 문자를 순자로 바꿔주자

        if (menu == 1):
            print("1번 [기본설명서] 로 이동합니다.")
            import WWWPJ.MYPCKEEPER.mypc_vaccine                                 #MYPCKEEPER 폴더 속 mypc_vacine 파일로 임폴트 하자
            show_file = WWWPJ.MYPCKEEPER.mypc_vaccine.mypc_vaccine_package()        #mypc_vacine 파일에 mypc_vaccine_package 클래스에 들어가자
            show_file.show_mypcfile()                                            #mypc_vaccine_package 클래스에 show_mypcfile 함수를 보여주자

        elif (menu == 2):
            print("2번 [다운로드] 로 이동합니다.")
            import WWWPJ.MYPCKEEPER.mypc_download                                #MYPCKEEPER 폴더 속 mypc_download 파일로 임폴트 하자
            show_file = WWWPJ.MYPCKEEPER.mypc_download.mypc_download_package()       #mypc_download 파일에 mypc_download_package 클래스에 들어가자
            show_file.show_mypcfile()                                            #mypc_download_package 클래스에 show_mypcfile 함수를 보여주자

        elif (menu == 3):
            print("3번 [한글패치] 로 이동합니다.")
            import WWWPJ.MYPCKEEPER.mypc_korean                                  #MYPCKEEPER 폴더 속 mypc_korean 파일로 임폴트 하자
            show_file = WWWPJ.MYPCKEEPER.mypc_korean.mypc_korean_package()         #mypc_korean 파일에 mypc_korean_package 클래스에 들어가자
            show_file.show_mypcfile()                                            #mypc_korean_package 클래스에 show_mypcfile 함수를 보여주자

        elif (menu == 4):
            print("4번 [비밀번호변경] 로 이동합니다.")
            import WWWPJ.MYPCKEEPER.mypc_pwchange                                #MYPCKEEPER 폴더 속 mypc_pwchange 파일로 임폴트 하자
            show_file = WWWPJ.MYPCKEEPER.mypc_pwchange.mypc_pwchange_package()       #mypc_pwchange 파일에 mypc_pwchange_package 클래스에 들어가자
            show_file.show_mypcfile()                                            #mypc_pwchange_package 클래스에 show_mypcfile 함수를 보여주자

        else:
            print(" ╭┈┈┈┈╯   ╰┈┈┈╮")
            print("  ╰┳┳╯  ╰┳┳╯")
            print("   💧 　　 💧")
            print("  💧　 　　 💧")
            print(" 💧   ╰┈┈╯   💧  ")
            print(" 💧  ╭━━━━━╮　 💧")
            print("   💧  ┈┈┈┈   1-4을 선택해 주세요ㅠㅠ  ")  # 1번부터 4번까지 고르지 않았을 경우엔 에러메세지를 보내주자
            print("MYPCKEEPER로 이동합니다.")
            import WWWPJ.pcKeeper                          # pckeeper 파일로 임폴트 하자
            show_file = WWWPJ.pcKeeper.Mypc_Package        # pckeeper 파일에 Mypc_Package 클래스에 들어가자
            show_file.detailmenu(self)                     # Mypc_Package 클래스에 detailmenu 함수를 보여주자