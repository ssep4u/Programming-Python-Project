class tutorial_Wsm_package:
    def show_tutfile(self):
        print('\033[94m'+"========WSM_TUTORIAL=========")
        print("1. 명품 HTML5+CSS3+Javascript 웹 프로그래밍\n"
            +"2. 웹프로그래밍 기초(HTML5+CSS3+JAVASCRIPT)"+'\033[0m')

        import WWWPJ.TUTORIAL.tut_base                  #TUTORIAL 폴더 속 tut_base 파일로 임폴트 하자
        show_menu = WWWPJ.TUTORIAL.tut_base.Base()      #tut_base 파일에 Base 클래스에 들어가자
        show_menu.tutBase()                             #Base 클래스에 tutBase 함수를 보여주자