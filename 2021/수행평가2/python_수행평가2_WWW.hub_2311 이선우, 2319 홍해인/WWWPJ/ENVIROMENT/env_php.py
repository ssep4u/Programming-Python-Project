class env_Php_package:
    def show_envfile(self):
        print('\033[94m'+"========PHP_ENVIROMENT=========")
        print("1. PHP개발환경 구축하기(Git설치-> XAMPP설치(or APMsetup, AutoSet)")
        print("     1-1. 개발에디터설치 하기(Editplus, Visual Studio, Eclipse, Vim)")
        print("     1-2. iPuTTY다운로드 하기(자신의 포트번호와 비밀번호 설정)")
        print("     1-3. AWS Educate 신청&사용하기")
        print("2. iPuTTY환경설정하기(웹서버 설정)")
        print("     serverAdmin #자신의 이메일 주소")
        print("     DocumentRoot /home/계정/ www")
        print("     <Directory /home/계정 /www>")
        print("     Options FllowSymLinks MultiViews")
        print("     AllowOverride All")
        print("         allow from all")
        print("         require all granted")
        print("         serverAdmin #자신의 이메일 주소")
        print("     DocumentRoot /home/계정/ www")
        print("     <Directory /home/계정 /www>")
        print("     Options FllowSymLinks MultiViews")
        print("         serverAdmin #자신의 이메일 주소")
        print("         AllowOverride All")
        print("         allow from all")
        print("         require all granted")
        print("         <LimitExcpt GET POST>")
        print("     Order allow, deny")
        print("     Deny from all")
        print("     </LimitExcept>")
        print("     </Directory>")
        print("3. ⇒iPuTTY에서 HelloWorld출력(PHP시작)")
        print("     <?php")
        print("     echo Hello World!;")
        print("     phpinfo();")
        print("         ?>"+'\033[0m')

        import WWWPJ.ENVIROMENT.env_base                #LECTURE 폴더 속 lec_base 파일로 임폴트 하자
        show_menu = WWWPJ.ENVIROMENT.env_base.Base()    #lec_base 파일에 Base 클래스에 들어가자
        show_menu.envBase()                             #Base 클래스에 lecBase 함수를 보여주자