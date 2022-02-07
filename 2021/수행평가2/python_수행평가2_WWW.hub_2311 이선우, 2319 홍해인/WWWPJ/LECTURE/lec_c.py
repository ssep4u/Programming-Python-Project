class lecture_c_package:
    def show_lecfile(self):
        print('\033[94m'+"========C_LECTURE=========")
        print("1. C 프로그래밍 - 입문부터 게임 개발까지\n"
            +"2. C 와 C++ 을 동시에 배워보자-두들낙서의 C/C++\n"
            +"3. 혼자 공부하는 C 언어 저자에게 배우는 C 언어의 모든 것"+'\033[0m')

        import WWWPJ.LECTURE.lec_base               #LECTURE 폴더 속 lec_base 파일로 임폴트 하자
        show_menu = WWWPJ.LECTURE.lec_base.Base()   #lec_base 파일에 Base 클래스에 들어가자
        show_menu.lecBase()                         #Base 클래스에 lecBase 함수를 보여주자
