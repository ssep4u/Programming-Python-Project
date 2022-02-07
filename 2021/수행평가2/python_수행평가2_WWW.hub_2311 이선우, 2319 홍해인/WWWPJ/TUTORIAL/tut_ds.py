class tutorial_Ds_package:
    def show_tutfile(self):
        print('\033[94m'+"========DS_TUTORIAL=========")
        print("1. 인프런 - C로 배우는 자료구조 및 여러가지 예제 실습\n"
            +"2. 프로그래머스(유료)-어서와! 자료구조와 알고리즘은 처음이지?"+'\033[0m')

        import WWWPJ.TUTORIAL.tut_base                  #TUTORIAL 폴더 속 tut_base 파일로 임폴트 하자
        show_menu = WWWPJ.TUTORIAL.tut_base.Base()      #tut_base 파일에 Base 클래스에 들어가자
        show_menu.tutBase()                             #Base 클래스에 tutBase 함수를 보여주자