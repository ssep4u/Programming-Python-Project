class tutorial_Python_package:
    def show_tutfile(self):
        print('\033[94m'+"========PYTHON_TUTORIAL=========")
        print("1. Do It! 점프 투 파이썬\n"
            +"2. 혼자 공부하는 파이썬(개정판)"+'\033[0m')

        import WWWPJ.TUTORIAL.tut_base                  #TUTORIAL 폴더 속 tut_base 파일로 임폴트 하자
        show_menu = WWWPJ.TUTORIAL.tut_base.Base()      #tut_base 파일에 Base 클래스에 들어가자
        show_menu.tutBase()                             #Base 클래스에 tutBase 함수를 보여주자