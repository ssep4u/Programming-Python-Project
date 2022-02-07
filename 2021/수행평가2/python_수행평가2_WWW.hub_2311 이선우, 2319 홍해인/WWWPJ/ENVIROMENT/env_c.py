class env_C_package:
    def show_envfile(self):
        print('\033[94m' +"========C_ENVIROMENT=========")
        print("1. 비주얼 스튜디오 내려받아 설치하기")
        print("2. 인터넷 브라우저에", "http://visualstudio.microsoft.com/ko/downloads/\n"
              +"주소를 입력하고 커뮤니티 항목에 있는 [무료다운로드] 클릭하기\n"
              +" 단축주소 ", "bit.ly/VSdown")
        print("3. 화면 아래에서 메시지 박스가 올라오면 [실행] 버튼 클릭하기")
        print("4. [계속] 버튼을 클릭해서 설치 진행하기\n"
              +"(바로 다운로드 받아 설치하면 네트워크 속도에 따라 설치 시간이 걸릴 수 있음")
        print("[설치 후 시작]박스는 체크한 상태로 진행하기")
        print("5. 설치가 모두 끝나면 온라인으로 지원되는 개발자 서비스를 위해 마이크로소프트 계정으로 로그인하는 창 열기\n"
              +"[나중에 로그인] 링크를 누르고 새로운 창을 연다\n"
              +"이 창에서 [개발 설정]을 Viusal C++ 선택하고 원하는 색 테마 선택하기")
        print("[Visual Studio 시작] 버튼 누르기"+'\033[0m')

        import WWWPJ.ENVIROMENT.env_base                #LECTURE 폴더 속 lec_base 파일로 임폴트 하자
        show_menu = WWWPJ.ENVIROMENT.env_base.Base()    #lec_base 파일에 Base 클래스에 들어가자
        show_menu.envBase()                             #Base 클래스에 lecBase 함수를 보여주자