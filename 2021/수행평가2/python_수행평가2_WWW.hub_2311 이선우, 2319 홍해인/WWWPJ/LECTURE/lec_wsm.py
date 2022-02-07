class lecture_wsm_package:
    def show_lecfile(self):
        print('\033[94m'+"========WSM_LECTURE=========")
        print("1. 자바스크립트 언어 기본 - javascript\n"
              + "2. 기본을 확실히!! HTML 의 모든것\n"
              + "3. HTML,CSS 개발을 위한 핵심 가이드"+'\033[0m')

        import WWWPJ.LECTURE.lec_base               #LECTURE 폴더 속 lec_base 파일로 임폴트 하자
        show_menu = WWWPJ.LECTURE.lec_base.Base()   #lec_base 파일에 Base 클래스에 들어가자
        show_menu.lecBase()                         #Base 클래스에 lecBase 함수를 보여주자