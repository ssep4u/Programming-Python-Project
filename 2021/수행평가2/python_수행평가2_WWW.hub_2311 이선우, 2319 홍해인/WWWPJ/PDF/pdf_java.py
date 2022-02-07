class pdf_Java_package:
    def show_pdffile(self):
        print('\033[94m'+"========JAVA_PDF=========")
        print("[ 자바 PDF ]", "https://drive.google.com/drive/folders/1T1Mei0ElAXIQ9QeHU3w18JR49yeqM5Hi?usp=sharing"+'\033[0m')

        import WWWPJ.PDF.pdf_base               #PDF 폴더 속 pdf_base 파일로 임폴트 하자
        show_file = WWWPJ.PDF.pdf_base.Base()   #pdf_base 파일에 Base 클래스에 들어가자
        show_file.pdfBase()                     #Base 클래스에 pdfBase 함수를 보여주자