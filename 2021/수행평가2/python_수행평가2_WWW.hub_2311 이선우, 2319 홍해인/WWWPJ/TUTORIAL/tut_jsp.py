class tutorial_Jsp_package:
    def show_tutfile(self):
        print('\033[94m'+"========JSP_TUTORIAL=========")
        print("1. 최범균의 JSP 2.3 웹 프로그래밍 기초부터 중급까지\n"
            +"2. 처음 해보는 Servlet & JSP 웹 프로그래밍-나의 첫 번째 웹 프로그래밍 스파링 파트너"+'\033[0m')

        import WWWPJ.TUTORIAL.tut_base                  #TUTORIAL 폴더 속 tut_base 파일로 임폴트 하자
        show_menu = WWWPJ.TUTORIAL.tut_base.Base()      #tut_base 파일에 Base 클래스에 들어가자
        show_menu.tutBase()                             #Base 클래스에 tutBase 함수를 보여주자
