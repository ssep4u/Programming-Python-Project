from info import Info
class Infobook:
    def __init__(self):
        self.info_list = []

    def add_info(self):
        # 정보추가
        info_name = input ('>> 강아지 이름을 입력하세요 : ')
        for info in self.info_list:
            if info_name == info.name:
                print('이미 존재하는 이름입니다')
                return

        new_info = Info(info_name)
        new_info.set_info()

        self.info_list.append(new_info)

    def search_info(self):
        # 검색
        info_name = input('>> 강아지 이름을 입력하세요 : ')
        searched_info = []

        for info in self.info_list:
            if info_name in info.name:
                print(info)
                searched_info.append(info)

        if len(searched_info) == 0:
            choice = input('강아지 이름을 찾을 수 없습니다. 추가하시겠습니까? (y/n) : ')
            if choice == '1':
                self.add_info()
            else:
                return
