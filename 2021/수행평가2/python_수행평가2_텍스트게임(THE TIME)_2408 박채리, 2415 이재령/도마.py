import move_limit, rooms1, floor, item, 냉장고내부
def 도마():

    if (floor.count==0):
        floor.count+=1
        print(f'\n================================')
        print(f'현위치: 1층-《부엌》')
        print(f'----------------------------------')
        print(f'『식칼』을 발견했다. 혹시 모르니 챙겨두자')
        print(f'【item】 식칼을 얻었다!')
        print(f'----------------------------------')
        floor.hit_item.insert(1,'식칼')

        rooms1.show1()
    else:
        print(f'\n================================')
        print(f'현위치: 1층-《부엌》')
        print(f'----------------------------------')
        print(f'오래되어 보이는 도마이다.')
        print(f'----------------------------------')
        rooms1.show1()


def 냉장고():
    refre_list=[0,냉장고내부.칸1,냉장고내부.칸2, 냉장고내부.칸3]
    print(f'\n================================')
    print(f'현위치: 1층-《부엌》')
    print(f'----------------------------------')
    print(f'냉장고를 열었다!')
    print(f'【1】 첫번째칸')
    print(f'【2】 두번째칸')
    print(f'【3】 세번째칸')
    print(f'【4】 돌아가기')
    num = input('칸선택>> ')
    num=int(num)
    print(f'----------------------------------')
    if num==4:
        rooms1.show1()
    else:
        refre_list[num]()