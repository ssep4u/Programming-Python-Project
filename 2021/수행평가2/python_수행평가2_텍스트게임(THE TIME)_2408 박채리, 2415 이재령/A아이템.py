import move_limit, rooms2, floor, item
from time import sleep
def 침대():
    print(f'\n================================')
    print(f'현위치: 2층-《A의 방》')
    print(f'----------------------------------')
    print(f'가지런히 정리된 이불이 보인다. 그 위로는 먼지가 쌓여있다.')
    rooms2.Aroom()

def 창문():
    print(f'\n================================')
    print(f'현위치: 2층-《A의 방》')
    print(f'----------------------------------')
    print(f'먼지가 껴서 바깥이 보이지 않는다. 별로 만지고 싶지 않다.')
    rooms2.Aroom()

def 벽():
    if (floor.count9)==0:

        print(f'\n================================')
        print(f'현위치: 2층-《A의 방》')
        print(f'----------------------------------')
        print(f'벽에 못이 하나 박혀있다. 망치 같은 공구가 있다면 뺄수 있을것 같다.')
        print(f'----------------------------------')
        print(f'【1】 아이템')
        print(f'【2】 돌아가기')
        num = input(f'선택>> ')
        num=int(num)
        if num==1:
            def 선택():
                print(f'\n================================')
                print(f'【1】 {floor.use_item[1]}\n【2】 {floor.use_item[2]}\n【3】 {floor.use_item[3]}\n【4】 선택취소')
                num1 = input(f'아이템을 선택해주세요>> ')
                print(f'\n----------------------------------')
                num1=int(num1)
                if num1==4:
                    벽()
                elif num1==1:
                    if floor.use_item[1] == '망치':
                        print(f'[*] 아이템 『망치』를 사용합니다.')
                        print(f'『망치』는 망가져 더이상 사용할 수 없을것 같다.')
                        print(f'----------------------------------')
                        floor.use_item.remove('망치')
                        floor.use_item.insert(1, '[사용불가] 망가진 망치')
                        print(f'벽이 정사각형 모양으로 떨어졌다. \n그 안에는 ↑  ←  ↑  →  ←  ↓  라고 적힌 쪽지가 있다. 암호인걸까?')
                        print(f'----------------------------------')
                        print(f'【item】 권총을 얻었다.(3발사용가능)')
                        print(f'【item】 ↑  ←  ↑  →  ←  ↓  라고 적힌 쪽지')

                        floor.hit_item.insert(3, '권총')
                        floor.use_item.insert(2, '쪽지')
                        floor.count9+=1
                        벽()
                    elif floor.use_item[1] =='□':
                        print(f'이곳에 사용할 수 없는 아이템입니다.')
                        선택()

                else:
                    print(f'이곳에 사용할 수 없는 아이템입니다.')
                    선택()
            선택()

        else:
            rooms2.Aroom()
    else:
        print(f'\n================================')
        print(f'현위치: 2층-《A의 방》')
        print(f'----------------------------------')
        print(f'정사각형 모양으로 떨어진 벽이다.')
        print(f'----------------------------------\n')
        rooms2.Aroom()

def 책상():
    print(f'\n================================')
    print(f'현위치: 2층-《A의 방》')
    print(f'----------------------------------')
    print(f'【1】 책상위')
    print(f'【2】 책상아래')
    print(f'【3】 돌아가기')

    num = input('칸선택>> ')
    num = int(num)
    if num == 1:
        print(f'\n================================')
        print(f'현위치: 2층-《A의 방》')
        print(f'----------------------------------')
        print(f'노트가 하나 놓여져 있다.')
        print(f'내용은..')
        sleep(0.8)
        print(f'.')
        sleep(0.8)
        print(f'.')
        sleep(0.8)
        print(f'.')

        print(f'----------------------------------')
        for a in range(1,9+1):
            print(f'실패했다.안돼.실패했다.안돼.실패했다.안돼.')
            sleep(0.4)
        print(f'----------------------------------\n')
        책상()

    elif num == 2:
        if (floor.count6 == 0):
            floor.count6 += 1
            print(f'\n================================')
            print(f'현위치: 2층-《A의 방》')
            print(f'----------------------------------')
            print(f'잔뜩 구겨진 악보 쪼가리들이 나뒹굴고 있다.')
            print(f'----------------------------------\n')
            책상()

    elif num == 3:
        print(f'----------------------------------')
        rooms2.Aroom()