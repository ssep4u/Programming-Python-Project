# 메뉴창 만들기
# 기능
# 메인 메뉴: pdf, 강의, 자습서, 환경설정
# 디테일 메뉴:
#     Pdf 메뉴:
#         국어 / 수학 / 영어 / 과학 / 자바 / C언어
#     강의 메뉴:
#         DB / Php / Jsp / Java / Python / DS / C / Wsm / Spring
#     자습서 메뉴:
#         DMB / Php / Jsp / Java / Python / DS / C / Wsm/ Spring
#     환경설정메뉴:
#         DB / Php / Jsp / Java / Python / C /
#     내PC지키미:
#         설명서 / 다운로드 / 한글패치 / 비밀번호변경


class Mainmenu:
    def mainmenu(self):
        # MAINMENU: 1.PDF모음, 2.강의추천, 3.자습서추천, 4.환경설정, 5.내PC지키미
        print('\033[96m'+'┌─────────────────┐')
        print('│⌕ 메뉴 선택       │  ')
        print('└─────────────────┘ ')
        print('↳ 1. PDF모음     ')
        print('↳ 2. 강의추천     ')
        print('↳ 3. 자습서추천   ')
        print('↳ 4. 환경설정     ')
        print('↳ 5. 내PC지키미     '+'\033[0m')

        menu = input('메뉴를 선택하세요: ')                    #사용자가 메뉴 선택하게 하자
        menu = int(menu)                                    #인덱스를 위해 문자를 순자로 바꿔주자

        if (menu ==1):
            print("1번 [PDF모음] 메뉴로 이동합니다.")
            import WWWPJ.pdf                                #pdf 파일로 임폴트 하자
            show_menu = WWWPJ.pdf.Pdf_Package()             #pdf 파일에 Pdf_Package 클래스에 들어가자
            show_menu.detailmenu()                          #Pdf_Package 클래스에 detailmenu 함수를 보여주자

        elif (menu ==2):
            print("2번 [강의추천] 메뉴로 이동합니다.")
            import WWWPJ.lecture                            #lecture 파일로 임폴트 하자
            show_menu = WWWPJ.lecture.Lecture_Package()     #lecture 파일에 Lecture_Package 클래스에 들어가자
            show_menu.detailmenu()                          #Pdf_Package 클래스에 detailmenu 함수를 보여주자

        elif (menu ==3):
            print("3번 [자습서추천] 메뉴로 이동합니다.")
            import WWWPJ.tutorial                           #tutorial 파일로 임폴트 하자
            show_menu = WWWPJ.tutorial.Tutorial_Package()   #tutorial 파일에 Tutorial_Package 클래스에 들어가자
            show_menu.detailmenu()                          #Tutorial_Package 클래스에 detailmenu 함수를 보여주자

        elif (menu ==4):
            print("4번 [환경설정] 메뉴로 이동합니다.")
            import WWWPJ.enviroment                         #enviroment 파일로 임폴트 하자
            show_menu = WWWPJ.enviroment.Env_Package()      #enviroment 파일에 Env_Package 클래스에 들어가자
            show_menu.detailmenu()                          #Env_Package 클래스에 detailmenu 함수를 보여주자

        elif (menu ==5):
            print("5번 [내pc지키미] 메뉴로 이동합니다.")
            import WWWPJ.pcKeeper                           #pcKeeper 파일로 임폴트 하자
            show_menu = WWWPJ.pcKeeper.Mypc_Package()       #pcKeeper 파일에 Mypc_Package 클래스에 들어가자
            show_menu.detailmenu()                          #Mypc_Package 클래스에 detailmenu 함수를 보여주자

        else:
            print(" ╭┈┈┈┈╯   ╰┈┈┈╮")
            print("  ╰┳┳╯  ╰┳┳╯")
            print("   💧 　　 💧")
            print("  💧　 　　 💧")
            print(" 💧   ╰┈┈╯   💧  ")
            print(" 💧  ╭━━━━━╮　 💧")
            print("   💧  ┈┈┈┈   1-5을 선택해 주세요ㅠㅠ  ")  # 1번부터 5번까지 고르지 않았을 경우엔 에러메세지를 보내주자
            import WWWPJ.menu                              # menu 파일로 임폴트 하자
            show_file = WWWPJ.menu.Mainmenu()              # menu 파일에 Mainmenu 클래스에 들어가자
            show_file.mainmenu()                           # Mainmenu 클래스에 mainmenu 함수를 보여주자