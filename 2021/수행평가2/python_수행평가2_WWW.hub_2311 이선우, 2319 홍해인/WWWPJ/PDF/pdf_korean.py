class pdf_Korean_package:
    def show_pdffile(self):
        print('\033[94m'+"========KOREAN_PDF=========")
        print("[ 국어 PDF ]", "http://www.hnedu.co.kr/textbook/textbook/ebook/high_korean/index.html"+'\033[0m')

        import WWWPJ.PDF.pdf_base               #PDF 폴더 속 pdf_base 파일로 임폴트 하자
        show_file = WWWPJ.PDF.pdf_base.Base()   #pdf_base 파일에 Base 클래스에 들어가자
        show_file.pdfBase()                     #Base 클래스에 pdfBase 함수를 보여주자