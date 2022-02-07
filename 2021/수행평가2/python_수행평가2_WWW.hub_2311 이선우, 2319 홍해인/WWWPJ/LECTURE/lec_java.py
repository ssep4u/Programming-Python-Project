class lecture_java_package:
    def show_lecfile(self):
        print('\033[94m'+"========JAVA_LECTURE=========")
        print("1. 자바(JAVA) 언어 기본 강좌\n"
              + "2. Do it! 자바 프로그래밍 입문\n"
              + "3. 웹개발 코스 [JAVA 개발언어]"+'\033[0m')

        import WWWPJ.LECTURE.lec_base               #LECTURE 폴더 속 lec_base 파일로 임폴트 하자
        show_menu = WWWPJ.LECTURE.lec_base.Base()   #lec_base 파일에 Base 클래스에 들어가자
        show_menu.lecBase()                         #Base 클래스에 lecBase 함수를 보여주자