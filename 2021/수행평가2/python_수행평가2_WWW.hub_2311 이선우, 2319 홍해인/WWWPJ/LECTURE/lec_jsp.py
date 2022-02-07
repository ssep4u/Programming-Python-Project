class lecture_jsp_package:
    def show_lecfile(self):
        print('\033[94m'+"========JSP_LECTURE=========")
        print("1. 실전 JSP (renew ver.) - 신입 프로그래머를 위한 강좌\n"
              + "2. 누구나 따라하면서 배우는 JSP 커뮤니티 게시판 만들기\n"+'\033[0m')

        import WWWPJ.LECTURE.lec_base               #LECTURE 폴더 속 lec_base 파일로 임폴트 하자
        show_menu = WWWPJ.LECTURE.lec_base.Base()   #lec_base 파일에 Base 클래스에 들어가자
        show_menu.lecBase()                         #Base 클래스에 lecBase 함수를 보여주자
