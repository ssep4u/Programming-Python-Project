from infobook import Infobook
from information import Sick_part

def print_part():
    print('1. 강아지 정보 추가')
    print('2. 강아지 정보 확인')
    print('3. 머리')
    print('4. 몸')
    print('5. 재시작/종료')
    part = input('>> 메뉴를 선택하세요 : ')
    return part
def print_disease(disease_part):
    while True:
        if disease_part == '1':
            pass
        elif disease_part == '2':
            pass
        elif disease_part == '3':
            print('1. 눈')
            print('2. 입')
            print('3. 귀')
            region = input('아픈 부위를 선택하세요 : ')
        elif disease_part == '4':
            print('1. 다리')
            print('2. 배')
            region = input('아픈 부위를 선택하세요 : ')
        elif disease_part == '5':
            break
        else:
            break
        return region
def main():
    disease = Sick_part()
    showInfoBook = Infobook()
    while True:
        selected_menu = print_part()
        if selected_menu == '1': #정보 추가
            showInfoBook.add_info()
        elif selected_menu == '2': #정보 확인
            showInfoBook.search_info()
        elif selected_menu == '3': #머리
            part = print_disease('3')
            if part == '1': # 눈
                disease.check_eye()
            elif part == '2': # 입
                disease.check_mouth()
            elif part == '3': #귀
                disease.check_ear()
        elif selected_menu == '4': # 몸통
            part = print_disease('4')
            if part == '1': # 다리
                disease.check_leg()
            elif part == '2': # 배
                disease.check_stomach()
        elif selected_menu == '5':
            answer = input('다시 시작하시겠습니까? (y/n) : ')
            if answer == 'y':
                print('==================')
                print('메뉴를 다시 입력해주세요.')
                print('==================')
                continue
            elif answer == 'n':
                print('프로그램을 종료합니다. 감사합니다^^')
                break
            return answer
        else:
            print('==================')
            print('메뉴를 다시 입력해주세요.')
            print('==================')
main()
