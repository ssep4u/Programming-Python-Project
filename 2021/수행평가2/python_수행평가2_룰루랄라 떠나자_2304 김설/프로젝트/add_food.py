class Add_food:
    def __init__(self):
         self.food_list = []

    def add_food(self):
        food_name = input('>> 추가할 음식 이름을 입력하세요: ')
        self.food_list.append(food_name.split())
        print('추가된 음식 이름: ')
        print(self.food_list)