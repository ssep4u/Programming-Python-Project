from contentsbook import contentsBook

class Book:
    def __init__(self):
        self.book_list = []
        self.store_list = []
        self.location_list = []

    def add_book(self):  # 책 새로 추가
        # 책 추가
        new_book = contentsBook()
        new_book.set_book()
        self.book_list.append(new_book)

    # 책 검색
    def search_book(self):
        searched_book = []

        print("-------------------")
        name = input('책 검색하세요 : ')
        print("-------------------")
        for book in self.book_list:
            if name == book.title:
                print(book)
                print("-------------------")
                searched_book.append(book)

        if len(searched_book) == 0:
            print("책을 찾을 수 없습니다.")

# 모든 책 보여주기
    def show_book(self):
        for index, book in enumerate(self.book_list):
            print('-------------------')
            print(f'{index + 1}')
            print(book)
            print('-------------------')

    # 매장 검색
    def search_store(self):
        searched_store = []

        print("-------------------")
        print('1. 관악')
        print('2. 영등포')
        print('3. 강남')
        bookstore = input('매장을 검색하세요 : ')
        print("-------------------")
        for store in self.book_list:
            if bookstore == store.bookstore:
                print(store)
                print("-------------------")
                searched_store.append(store)

        if len(searched_store) == 0:
            print("서점에 등록된 책이 없습니다.")