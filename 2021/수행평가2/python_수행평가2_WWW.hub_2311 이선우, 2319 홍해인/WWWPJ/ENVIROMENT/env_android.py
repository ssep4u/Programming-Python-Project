class env_Android_package:
    def show_envfile(self):
        print('\033[94m' + "========ANDROID_ENVIROMENT=========")
        print("1. Window+R키(실행 단축키)누르기")
        print("2. sysdm.cpl 입력하기")
        print("3. 시스템 속성창-> 고급-> 환경변수-> Path-> 편집-> 새로만들기")
        print("4. C:\Program Files\Android\Android Studio\jre\bin -> 복사 후 넣기" +  '\033[0m')

        import WWWPJ.ENVIROMENT.env_base                #LECTURE 폴더 속 lec_base 파일로 임폴트 하자
        show_menu = WWWPJ.ENVIROMENT.env_base.Base()    #lec_base 파일에 Base 클래스에 들어가자
        show_menu.envBase()                             #Base 클래스에 lecBase 함수를 보여주자