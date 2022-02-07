class tutorial_Db_package:
    def show_tutfile(self):
        print('\033[94m'+"========DB_TUTORIAL=========")
        print("1. Head First SQL : 효율적인 DB 관리를 위한 SQL 학습법\n"
            +"2. 실전 DB 모델링과 SQL for ORACLE"+'\033[0m')

        import WWWPJ.TUTORIAL.tut_base                  #TUTORIAL 폴더 속 tut_base 파일로 임폴트 하자
        show_menu = WWWPJ.TUTORIAL.tut_base.Base()      #tut_base 파일에 Base 클래스에 들어가자
        show_menu.tutBase()                             #Base 클래스에 tutBase 함수를 보여주자