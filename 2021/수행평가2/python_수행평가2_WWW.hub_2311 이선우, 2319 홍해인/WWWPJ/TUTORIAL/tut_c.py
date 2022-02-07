class tutorial_C_package:
    def show_tutfile(self):
        print('\033[94m'+"========C_TUTORIAL=========")
        print("1. 윤성우 열혈 C 프로그래밍(개정판)\n"
            +"2. 언어 코딩 도장"+'\033[0m')

        import WWWPJ.TUTORIAL.tut_base                  #TUTORIAL 폴더 속 tut_base 파일로 임폴트 하자
        show_menu = WWWPJ.TUTORIAL.tut_base.Base()      #tut_base 파일에 Base 클래스에 들어가자
        show_menu.tutBase()                             #Base 클래스에 tutBase 함수를 보여주자
