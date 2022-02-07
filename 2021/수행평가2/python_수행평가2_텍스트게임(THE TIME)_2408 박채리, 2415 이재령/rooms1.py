import 도마, floor, 홀아이템,직원아이템,식당아이템,move_limit
def show1(): #부엌

    check_list1=[0,도마.도마,도마.냉장고]
    print(f'\n================================')
    print(f'현위치: 1층-《부엌》')
    print(f'----------------------------------')
    print(f'[*] 조사할 곳을 선택해주세요')
    print(f'【1】 도마')
    print(f'【2】 냉장고')
    print(f'【3】 돌아가기')

    num = input('조사선택>> ')
    num=int(num)
    if num==3:
        print(f'\n================================')
        move_limit.lim2()
        floor.floor1()
    else:
        check_list1[num]()

def show2(): #홀
    check_list2 = [0, 홀아이템.샹들리에, 홀아이템.꽃병, 홀아이템.어항]
    print(f'\n================================')
    print(f'현위치: 1층-《홀》')
    print(f'----------------------------------')
    print(f'[*] 조사할 곳을 선택해주세요')
    print(f'【1】 샹들리에')
    print(f'【2】 꽃병')
    print(f'【3】 어항')
    print(f'【4】 돌아가기')

    num = input('조사선택>> ')
    num=int(num)
    if num==4:
        print(f'\n================================')
        move_limit.lim2()
        floor.floor1()
    else:
        check_list2[num]()

def show3(): #직원휴게실
    check_list3 = [0, 직원아이템.서랍, 직원아이템.간이침대, 직원아이템.옷장]
    print(f'\n================================')
    print(f'현위치: 1층-《직원휴게실》')
    print(f'----------------------------------')
    print(f'[*] 조사할 곳을 선택해주세요')
    print(f'【1】 서랍')
    print(f'【2】 간이침대')
    print(f'【3】 옷장')
    print(f'【4】 돌아가기')


    num = input('조사선택>> ')
    num=int(num)
    if num==4:
        floor.floor1()
    else:
        check_list3[num]()

def show4(): #식당
    check_list4 = [0, 식당아이템.식탁, 식당아이템.트레이, 식당아이템.의자]
    print(f'\n================================')
    print(f'현위치: 1층-《식당》')
    print(f'----------------------------------')
    print(f'[*] 조사할 곳을 선택해주세요')
    print(f'【1】 식탁')
    print(f'【2】 트레이')
    print(f'【3】 의자')
    print(f'【4】 돌아가기')

    num = input('조사선택>> ')
    num = int(num)
    if num == 4:
        print(f'\n================================')
        move_limit.lim2()
        floor.floor1()
    else:
        check_list4[num]()