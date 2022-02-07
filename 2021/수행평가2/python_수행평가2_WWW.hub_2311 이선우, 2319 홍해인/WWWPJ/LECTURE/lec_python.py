class lecture_python_package:
    def show_lecfile(self):
        print('\033[94m'+"========PYTHON_LECTURE=========")
        print("1. 파이썬 무료 강의 (기본편) - 6시간 뒤면 나도 개발자\n"
              + "2. 프로그래밍 시작하기 : 파이썬 입문 (Inflearn Original)(유료)\n"+'\033[0m')

        import WWWPJ.LECTURE.lec_base               #LECTURE 폴더 속 lec_base 파일로 임폴트 하자
        show_menu = WWWPJ.LECTURE.lec_base.Base()   #lec_base 파일에 Base 클래스에 들어가자
        show_menu.lecBase()                         #Base 클래스에 lecBase 함수를 보여주자