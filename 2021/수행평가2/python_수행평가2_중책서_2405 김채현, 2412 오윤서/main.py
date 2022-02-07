from book import Book

def print_menu():
    print("\n-------------------")
    print('1. 매장 검색')
    print('2. 책검색')
    print('3. 책등록')
    print('4. (서점 상관없이) 모든 책 보기')
    print('5. 종료하기')
    num = input('메뉴를 선택하세요 : ')
    print("-------------------\n")
    return num

def main():
    book = Book()
    while True:
        num = print_menu()
        if num == '1':
            # 지역에 있는 매장 보여주기
            book.search_store()
        elif num == '2':
            # 책 검색 후 그 책 보여주기
            book.search_book()
        elif num == '3':
            # 책 등록
            book.add_book()
        elif num == '4':
            # 서점 상관없이 책 목록 보여주기
            book.show_book()
        elif num == '5':
            break
        else:
            print('해당 메뉴가 없습니다.')

if __name__ == '__main__':
    main()