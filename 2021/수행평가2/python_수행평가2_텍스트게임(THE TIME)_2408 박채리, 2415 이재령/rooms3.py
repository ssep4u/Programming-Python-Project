import floor, move_limit, 빈방, 서재, 화실, 사교도

def empty(): #빈방
    check_1 = [0, 빈방.의자, 빈방.밧줄, 빈방.주변, 빈방.바닥]
    print(f'\n================================')
    print(f'현위치: 3층-《빈방》')
    print(f'----------------------------------')
    print(f'[*] 조사할 곳을 선택해주세요')
    print(f'【1】 의자')
    print(f'【2】 밧줄')
    print(f'【3】 주변')
    print(f'【4】 바닥')
    print(f'【5】 돌아가기')

    num = input('조사선택>> ')
    num = int(num)
    if num == 5:
        print(f'\n================================')
        if floor.scount1 == 0:
            사교도.script()
        move_limit.lim2()
        floor.floor3()
    else:
        check_1[num]()

def book(): #서재
    check_4 = [0, 서재.책장, 서재.책상서랍, 서재.카펫, 서재.액자]
    print(f'\n================================')
    print(f'현위치: 3층-《서재》')
    print(f'----------------------------------')
    print(f'[*] 조사할 곳을 선택해주세요')
    print(f'【1】 책장')
    print(f'【2】 책상서랍')
    print(f'【3】 카펫')
    print(f'【4】 액자')
    print('【5】 돌아가기')

    num = input('조사선택>> ')
    num = int(num)
    if num ==5:
        print(f'\n================================')
        floor.floor3()
    else:
        check_4[num]()

def artroom(): #화실
    check_1 = [0, 화실.그림1, 화실.그림2, 화실.그림3, 화실.조각상]
    print(f'\n================================')
    print(f'현위치: 3층-《화실》')
    print(f'----------------------------------')
    print(f'[*] 조사할 곳을 선택해주세요')
    print(f'【1】 그림1')
    print(f'【2】 그림2')
    print(f'【3】 그림3')
    print(f'【4】 조각상')
    print('[5] 돌아가기')

    num = input('조사선택>> ')
    num = int(num)
    if num == 5:
        print(f'\n================================')
        move_limit.lim2()
        floor.floor3()
    else:
        check_1[num]()
