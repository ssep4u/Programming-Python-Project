from country import *
from recipe import *
from add_country import *
from add_food import *

def show_menu():
    print('🌍 Welcome~ 여행을 떠나볼까요? ✈')
    print('1. 나라 검색 ')
    print('2. 나라 음식 검색')
    print('3. 나라 추가')
    print('4. 음식 메뉴 추가')
    print('5. 종료')

def main():
    show_menu()

    space_list = Country()
    recipe_list = Recipe()
    add_country_list = Add_country()
    add_food_list = Add_food()

    while True:
        choose_num = input('메뉴를 선택해주세요: ')
        if choose_num == '1':
            space_list.show_space()
        elif choose_num == '2':
            recipe_list.show_recipe()
        elif choose_num == '3':
            add_country_list.add_country()
        elif choose_num == '4':
            add_food_list.add_food()
        elif choose_num == '5':
            break

if __name__ == "__main__":
    main()