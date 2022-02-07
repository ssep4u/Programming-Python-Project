class pdf_Science_package:
    def show_pdffile(self):
        print('\033[94m'+"========SCIENCE_PDF=========")
        print("[ 과학 PDF ]", "https://drive.google.com/drive/folders/16qMbGNN1cyAZ4XssjU7zs3ziqe7XspE9?usp=sharing"+'\033[0m')

        import WWWPJ.PDF.pdf_base               #PDF 폴더 속 pdf_base 파일로 임폴트 하자
        show_file = WWWPJ.PDF.pdf_base.Base()   #pdf_base 파일에 Base 클래스에 들어가자
        show_file.pdfBase()                     #Base 클래스에 pdfBase 함수를 보여주자