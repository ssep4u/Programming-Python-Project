class env_Db_package:
    def show_envfile(self):
        print('\033[94m'+"========DB_ENVIROMENT=========")
        print("1. SQL Developer 환경설정하기")
        print("1-1. 인코딩 UTF-8로 변경하기(환경설정-->환경-->인코딩)")
        print("1-2. 주석(환경설정-> 코드편집기-> PL/SQL구문색상-> 기본주석-> 글꼴,색상,배경색)")
        print("1-3. 행번호(환경설정-> 코드편집기-> PL/SQL구문색상-> 행 여백-> 행 번호 표시)")
        print("1-4. 나머지는 환경설정에 들어가 설정하기")
        print("2. 계정 새로 만들기")
        print("2-1. 왼속상단에 초록색 +버튼을 누르기")
        print("2-2. 사용자이름, 비밀번호를 적기(비밀번호 잊어버리지 않도록 주의)")
        print("2-3. 접속유형이 호스트이름 : localhost, 포트 : 1521, sid기본값 xe로 되어있는지 확인하기")
        print("2-4. 테스트 성공이라고 뜨면 저장하기(저장-> 왼쪽에 접속이름, 접속 세부정보)"+'\033[0m')

        import WWWPJ.ENVIROMENT.env_base                #LECTURE 폴더 속 lec_base 파일로 임폴트 하자
        show_menu = WWWPJ.ENVIROMENT.env_base.Base()    #lec_base 파일에 Base 클래스에 들어가자
        show_menu.envBase()                             #Base 클래스에 lecBase 함수를 보여주자