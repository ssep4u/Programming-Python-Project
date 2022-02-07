class mypc_vaccine_package:
    def show_mypcfile(self):
        print('\033[94m' + "========VACCINE_MYPC=========")
        print('1. V3가 설치된 경우 2번 생략')
        print('2. 설치순서를 꼭 지킬 것')
        print('3. PC지키미 항목을 100점(10개 항목 안전)으로 맞출 것')
        print('4. PC지키미 점검은 반드시 학교 혹은 기숙사에서 실시해야함')
        print('5. 100점 미충족 시 해당 학생 IP가 차단됨');
        print('6. 프로그램 실행이 안 되거나, [안전] 항목으로 변경되지 않을 경우에는 실습 조교님 혹은 마이스터기획부 박지우 선생님에게 찾아갈 것')
        print('7.백신관련 오류가 났을때는 V3를 실행하여 최신버전으로 업데이트를 하고 간편검사를 실시한다. 이후 PC지키미 점검버튼을 누른다.'+'\033[0m')

        import WWWPJ.MYPCKEEPER.mypc_base                  #MYPCKEEPER 폴더 속 mypc_base 파일로 임폴트 하자
        show_menu = WWWPJ.MYPCKEEPER.mypc_base.Base()      #mypc_base 파일에 Base 클래스에 들어가자
        show_menu.mypcBase()                               #Base 클래스에 mypcBase 함수를 보여주자
