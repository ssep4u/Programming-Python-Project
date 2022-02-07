class env_Jsp_package:
    def show_envfile(self):
        print('\033[94m'+"========JSP_ENVIROMENT=========")
        print("1. JDK(Java SE Development Kit) 설치하기\n"
            +"(자바 기반의 프로그램을 작성하기 위해서는 컴파일러 및 실행환경이 필요함)\n"
            +"Jsp를 사용하기 위해 필수적으로 설치하기")
        print("2. JDK를 설치하기 위해", "https://www.oracle.com/java/technologies/javase/javase-jdk8-downloads.html\n"
            +"링크에 접속 후 자신이 사용하는 운영체제에 맞는 버전을 다운 받기")
        print("3. 다운 받은 파일 실행 후 설치를 진행하기(별다른 설정 필요없이 Next 만 눌러도 설치 완료)")
        print("4. 내 컴퓨터-> 속성-> 시스템에서 고급시스템 설정-> 시스템 속성의 고급-> 환경변수\n"
            +"JDK를 사용하기 위한 환경 변수를 설정하기")
        print("5. 변수 Path 에서 편집을 눌러 변수 값 C:/Program Files/Java/jsk1.8.0_101/bin 내용을 추가하기\n"
            +"(자바 버전에 따라 설치된 경로명은 바뀔 수 있음)")
        print("6. 확인을 눌러 저장 후 정상적으로 설치가 되었는지 확인해보려면 명령 프롬프트를 실행해\n"
            +"java와 javas 를 입력해보기"+'\033[0m')

        import WWWPJ.ENVIROMENT.env_base                #LECTURE 폴더 속 lec_base 파일로 임폴트 하자
        show_menu = WWWPJ.ENVIROMENT.env_base.Base()    #lec_base 파일에 Base 클래스에 들어가자
        show_menu.envBase()                             #Base 클래스에 lecBase 함수를 보여주자