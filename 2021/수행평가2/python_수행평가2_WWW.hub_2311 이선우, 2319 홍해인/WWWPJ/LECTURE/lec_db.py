class lecture_db_package:
    def show_lecfile(self):
        print('\033[94m' + "========DB_LECTURE=========")
        print("1. 생애 첫 SQL With 제코베\n"
            +"2. [백문이불여일타] 데이터 분석을 위한 고급 SQL\n"+'\033[0m')

        import WWWPJ.LECTURE.lec_base               #LECTURE 폴더 속 lec_base 파일로 임폴트 하자
        show_menu = WWWPJ.LECTURE.lec_base.Base()   #lec_base 파일에 Base 클래스에 들어가자
        show_menu.lecBase()                         #Base 클래스에 lecBase 함수를 보여주자