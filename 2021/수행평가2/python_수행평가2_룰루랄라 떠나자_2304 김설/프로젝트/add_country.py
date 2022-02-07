class Add_country:
    def __init__(self):
         self.country_list = []

    def add_country(self):
        country_name = input('>> 추가할 나라 이름을 입력하세요: ')
        self.country_list.append(country_name.split())
        print('추가된 나라: ')
        print(self.country_list)

