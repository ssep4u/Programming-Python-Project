class lecture_spring_package:
    def show_lecfile(self):
        print('\033[94m'+"========SPRING_LECTURE=========")
        print("1. 자바 스프링 프레임워크(renew ver.) - 신입 프로그래머를 위한 강좌\n"
              + "2. 스프링 입문 - 코드로 배우는 스프링 부트, 웹 MVC, DB 접근 기술\n"
              + "3. 예제로 배우는 스프링 입문 (개정판)"+'\033[0m')

        import WWWPJ.LECTURE.lec_base               #LECTURE 폴더 속 lec_base 파일로 임폴트 하자
        show_menu = WWWPJ.LECTURE.lec_base.Base()   #lec_base 파일에 Base 클래스에 들어가자
        show_menu.lecBase()                         #Base 클래스에 lecBase 함수를 보여주자