class mypc_download_package:
    def show_mypcfile(self):
        print('\033[94m' + "========DOWNLOAD_MYPC=========")
        print('1. PC용 백신프로그램 설치 파일을 다운받고, 설치->혹은 http://10.97.100.100/sen/agent/ahnlab/Ahnlab_V3_ES_9.0.exe 접속')
        print('2. 안랩 내PC지키미 에이전트 설치파일을 다운받고 설치(4번부터 설치방법 제시)->혹은 http://10.97.100.100/sen/agent/ahnlab/MYPC_97vSetup.exe 접속')
        print('2-1. 안랩 내 PC지키미 에이전트 설치파일 + PC용 백신프로그램 설치파일')
        print('3. MYPC_97vSetup.exe를 우클릭 후 관리자 권한으로 실행 그리고 잠시 대기')
        print('3-1. 다음과 같은 메시지가 발생시 c:\Temp\AgentBase.exe를 “관리자 권한”으로 실행')
        print('4. 윈도우 왼쪽 아래에 파란색 APC Agent 아이콘이 표시되면 설치 완료')
        print('5. 바탕화면에 내PC지키미 아이콘이 생성이 안 될 경우 5~10분 기다리거나 재부팅을 시도 후 대기. 혹은 "C:\Program Files (x86)\AhnLab\APC2\MyPC Agent\MYPCUI.EXE" 실행' + '\033[0m')

        import WWWPJ.MYPCKEEPER.mypc_base                  #MYPCKEEPER 폴더 속 mypc_base 파일로 임폴트 하자
        show_menu = WWWPJ.MYPCKEEPER.mypc_base.Base()      #mypc_base 파일에 Base 클래스에 들어가자
        show_menu.mypcBase()                               #Base 클래스에 mypcBase 함수를 보여주자

