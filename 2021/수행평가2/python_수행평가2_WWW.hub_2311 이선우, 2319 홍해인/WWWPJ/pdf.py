class Pdf_Package:
    def detailmenu(self):
        print('￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣')
        print('| 　PDFMENU!　　       　　　　　　　　　　　　　   　　  [－][口][×]   |')
        print('| ￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣  |')
        print('| 　＿＿＿　　＿＿＿＿　　＿＿＿＿　　 ＿＿＿＿＿＿    ＿＿　   ＿＿＿＿    |')
        print('| ｜1.국어 | ｜2.수학 ｜ |3.영어 |  |4.과학 |  |5.자바 |  |6.C언어 |  |')
        print('| 　￣￣￣　　￣￣￣￣　　￣￣￣￣　　  ￣￣￣￣￣　   ￣￣     ￣￣￣￣    |')
        print('￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣')

        menu = input('메뉴를 선택하세요: ')                            #사용자가 메뉴 선택하게 하자
        menu = int(menu)                                            #인덱스를 위해 문자를 순자로 바꿔주자

        if (menu == 1):
            print("1번 [국어] 로 이동합니다.")
            import WWWPJ.PDF.pdf_korean                             #PDF 폴더 속 pdf_korean 파일로 임폴트 하자
            show_file = WWWPJ.PDF.pdf_korean.pdf_Korean_package()   #pdf_korean 파일에 pdf_Korean_package 클래스에 들어가자
            show_file.show_pdffile()                                #pdf_Korean_package 클래스에 show_pdffile 함수를 보여주자

        elif (menu == 2):
            print("2번 [수학] 로 이동합니다.")
            import WWWPJ.PDF.pdf_math                               #PDF 폴더 속 pdf_math 파일로 임폴트 하자
            show_file = WWWPJ.PDF.pdf_math.pdf_Math_package()       #pdf_math 파일에 pdf_Math_package 클래스에 들어가자
            show_file.show_pdffile()                                #pdf_Math_package 클래스에 show_pdffile 함수를 보여주자

        elif (menu == 3):
            print("3번 [영어] 로 이동합니다.")
            import WWWPJ.PDF.pdf_english                            #PDF 폴더 속 pdf_english 파일로 임폴트 하자
            show_file = WWWPJ.PDF.pdf_english.pdf_English_package() #pdf_english 파일에 pdf_English_package 클래스에 들어가자
            show_file.show_pdffile()                                #pdf_English_package 클래스에 show_pdffile 함수를 보여주자

        elif (menu == 4):
            print("4번 [과학] 로 이동합니다.")
            import WWWPJ.PDF.pdf_science                            #PDF 폴더 속 pdf_science 파일로 임폴트 하자
            show_file = WWWPJ.PDF.pdf_science.pdf_Science_package() #pdf_science 파일에 pdf_Science_package 클래스에 들어가자
            show_file.show_pdffile()                                #pdf_Science_package 클래스에 show_pdffile 함수를 보여주자

        elif (menu == 5):
            print("5번 [자바] 로 이동합니다.")
            import WWWPJ.PDF.pdf_java                               #PDF 폴더 속 pdf_java 파일로 임폴트 하자
            show_file = WWWPJ.PDF.pdf_java.pdf_Java_package()       #pdf_java 파일에 pdf_Java_package 클래스에 들어가자
            show_file.show_pdffile()                                #pdf_Java_package 클래스에 show_pdffile 함수를 보여주자

        elif (menu == 6):
            print("6번 [C언어] 로 이동합니다.")
            import WWWPJ.PDF.pdf_c                                  #PDF 폴더 속 pdf_c 파일로 임폴트 하자
            show_file = WWWPJ.PDF.pdf_c.pdf_C_package()             #pdf_c 파일에 pdf_C_package 클래스에 들어가자
            show_file.show_pdffile()                                #pdf_C_package 클래스에 show_pdffile 함수를 보여주자

        else:
            print(" ╭┈┈┈┈╯   ╰┈┈┈╮")
            print("  ╰┳┳╯  ╰┳┳╯")
            print("   💧 　　 💧")
            print("  💧　 　　 💧")
            print(" 💧   ╰┈┈╯   💧  ")
            print(" 💧  ╭━━━━━╮　 💧")
            print("   💧  ┈┈┈┈   1-6을 선택해 주세요ㅠㅠ  ")  # 1번부터 6번까지 고르지 않았을 경우엔 에러메세지를 보내주자
            import WWWPJ.pdf                              # pdf 파일로 임폴트 하자
            show_file = WWWPJ.pdf.Pdf_Package()           # pdf 파일에 Pdf_Package 클래스에 들어가자
            show_file.detailmenu()                        # Pdf_Package 클래스에 detailmenu 함수를 보여주자