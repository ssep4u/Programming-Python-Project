import move_limit, rooms3, floor, item, 책장아이템

def 책장():
    check_4 = [0, 책장아이템.신화서, 책장아이템.A의일기, 책장아이템.차원과시간]
    print(f'\n================================')
    print(f'현위치: 3층-《서재》')
    print(f'----------------------------------')
    print(f'낡은 책들이 꽂혀있다.')
    print(f'【1】 신화서')
    print(f'【2】 A의 일기')
    print(f'【3】 차원과 시간에 대하여')
    print(f'【4】 돌아가기')

    num = input('조사선택>> ')
    num = int(num)
    if num == 4:
        print(f'\n================================')
        rooms3.book()
    else:
        check_4[num]()


def 책상서랍():
    print(f'\n================================')
    print(f'현위치: 3층-《서재》')
    print(f'----------------------------------')
    print(f'수많은 편지봉투와 편지가 들어있다.')
    print('편지들을 읽어보면, 대부분이 의사들에게 제발 환자를 받아달라는 식의 도움을 요청하는 내용이다. ')
    rooms3.book()


def 카펫():
    if (floor.count11==0):
        floor.count11+=1
        print(f'\n================================')
        print(f'현위치: 3층-《서재》')
        print(f'----------------------------------')
        print(f'작은 열쇠를 발견했다. 쓸 곳이 있을까?')
        print(f'【item】 작은 열쇠를 얻었다!')
        print(f'----------------------------------')
        floor.use_item.insert(3, '작은열쇠')
    else:
        print(f'\n================================')
        print(f'현위치: 3층-《서재》')
        print(f'----------------------------------')
        print('빈말로도 부드럽다고 할 수 없는 카펫이다.')
    rooms3.book()


def 액자():
    print(f'\n================================')
    print(f'현위치: 3층-《서재》')
    print(f'----------------------------------')
    print(f'밝게 웃고있는 연인의 사진이 걸려있다. 액자가 많이 낡았지만 사진에는 그 당시의 행복이 남아있는 것 같다.')
    rooms3.book()