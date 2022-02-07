class tutorial_Spring_package:
    def show_tutfile(self):
        print('\033[94m'+"========SPRING_TUTORIAL=========")
        print("1. Spring 4.0 프로그래밍(웹 개발자를 위한)\n"
            +"2. 웹 개발자를 위한 Spring 3.0 프로그래밍\n"
            +"3. 스타트 스프링 부트-초급 개발자들을 위한 가볍고 넓은 스프링 부트"+'\033[0m')

        import WWWPJ.TUTORIAL.tut_base                  #TUTORIAL 폴더 속 tut_base 파일로 임폴트 하자
        show_menu = WWWPJ.TUTORIAL.tut_base.Base()      #tut_base 파일에 Base 클래스에 들어가자
        show_menu.tutBase()                             #Base 클래스에 tutBase 함수를 보여주자