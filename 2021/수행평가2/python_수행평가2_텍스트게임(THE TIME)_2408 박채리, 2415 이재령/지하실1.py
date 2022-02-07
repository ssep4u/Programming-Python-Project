import alley1, floor, item, move_limit, 지하통로2

def 작은열쇠():
    print(f'\n================================')
    print(f'열쇠가 들어가지 않는다. 다른 열쇠를 사용해야 할 것 같다.')
    print(f'----------------------------------')

    alley1.alley_mouth()


def 지하실열쇠():
    check_1 = [0, 지하통로2.alley_aisle]
    if (floor.use_item[2] == '지하실열쇠'):
        print(f'\n================================')
        print(f'열쇠가 들어갔다. 앞으로 나아가자.')
        print(f'【1】 앞으로 간다')
        print(f'【2】 돌아간다')
        print(f'----------------------------------')

        num = input('조사선택>> ')
        num = int(num)
        if num == 2:
            print(f'\n================================')
            move_limit.lim2()
            floor.alley()
        else:
            check_1[num]()
    else:
        print('열쇠가 없다. 문을 열지 못한다.')
        alley1.alley_mouth()
    alley1.alley_mouth()


def 강제():
    print(f'\n================================')
    print(f'굳게 닫혀있다. 강제로는 열리지 않을 것 같다.')
    print(f'----------------------------------')
    alley1.alley_mouth()

