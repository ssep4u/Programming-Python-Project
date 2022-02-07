class mypc_pwchange_package:
    def show_mypcfile(self):
        print('\033[94m' + "========PWCHANGE_MYPC=========")
        print('1.윈도우 키를 누르고 계정관리를 검색하여 선택')
        print('2.대신 로컬 계정으로 로그인 클릭')
        print('3.다음과 같은 화면이 나오는 경우 PC지키미 조건에 맞는 암호를 설정한 후 다음을 클릭. 이후 윈도우 운영체제의 로그오프가 시작됨')
        print('4.PC지키미를 재검사 하여 안전상태로 나왔는지 확인'+ '\033[0m')

        import WWWPJ.MYPCKEEPER.mypc_base                  #MYPCKEEPER 폴더 속 mypc_base 파일로 임폴트 하자
        show_menu = WWWPJ.MYPCKEEPER.mypc_base.Base()      #mypc_base 파일에 Base 클래스에 들어가자
        show_menu.mypcBase()                               #Base 클래스에 mypcBase 함수를 보여주자
