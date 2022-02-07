class pdf_Math_package:
    def show_pdffile(self):
        print('\033[94m'+"========MATH_PDF=========")
        print("[ 수학 PDF ]", "https://drive.google.com/drive/folders/1lhGrJLUrsLsz2ILDTq8YlHQ_HgRo4Xtu?usp=sharing"+'\033[0m')

        import WWWPJ.PDF.pdf_base               #PDF 폴더 속 pdf_base 파일로 임폴트 하자
        show_file = WWWPJ.PDF.pdf_base.Base()   #pdf_base 파일에 Base 클래스에 들어가자
        show_file.pdfBase()                     #Base 클래스에 pdfBase 함수를 보여주자