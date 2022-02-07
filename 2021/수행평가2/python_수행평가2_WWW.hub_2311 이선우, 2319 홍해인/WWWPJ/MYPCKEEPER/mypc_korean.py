class mypc_korean_package:
    def show_mypcfile(self):
        print('\033[94m' + "========KOREAN_MYPC=========")
        print('1.크롬 브라우저를 실행 후 hancom.com 입력')
        print('2.고객지원 클릭')
        print('3.다운로드 클릭')
        print('4.제품구분이 한글인 부분에서 자신의 한글버전에 맞는 보안패치를 다운 후 실행')
        print('5.내PC지키미 점검시작 버튼 클릭'+'\033[0m')

        import WWWPJ.MYPCKEEPER.mypc_base                  #MYPCKEEPER 폴더 속 mypc_base 파일로 임폴트 하자
        show_menu = WWWPJ.MYPCKEEPER.mypc_base.Base()      #mypc_base 파일에 Base 클래스에 들어가자
        show_menu.mypcBase()                               #Base 클래스에 mypcBase 함수를 보여주자

