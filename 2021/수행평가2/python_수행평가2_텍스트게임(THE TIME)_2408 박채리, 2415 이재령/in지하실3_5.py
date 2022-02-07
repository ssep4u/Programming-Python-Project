import move_limit, floor, item, 지하실3_5, 재단


def box(): #관

    print(f'----------------------------------')
    print(f"이 처참한 공간 안에 있음에도 불구하고, 관 주변만큼은 깨끗하기 그지없다. 관의 겉면에는 '사랑하는 나의 다가.'라고 적혀있다.")
    print(f'관을 열 수 있을 것 같다.')
    print(f'----------------------------------')
    print(f'[*] 무슨 행동을 하지?')
    print(f'【1】 관을 열어보자')
    print(f'【2】 돌아가기')

    num = input('조사선택>> ')
    num = int(num)
    if num == 2:
        print(f'\n================================')
        move_limit.lim2()
        지하실3_5.alley_finll()
    elif num == 1:
        print('안에는 죽은지 얼마 안 된 것 같은 시체 하나가 들어있다. 구더기 하나도 보이지 않는다. 보호자가 관리를 열심히 한 티가 난다.')

    지하실3_5.alley_finll()


def foundation(): #재단



    print(f'----------------------------------')
    print(f'피로 온갖 문자들이 그려진 재단. 이상한 물건과 동상들이 늘어서있다. 여기서 주문을 쓰면 될 것 같다.')
    print(f'----------------------------------')
    print(f'[*] 무슨 행동을 하지?')
    print(f'【1】 주문을 쓰자')
    print(f'【2】 돌아가기')

    num = input('행동선택>> ')
    num = int(num)
    if num == 2:
        print(f'\n================================')
        move_limit.lim2()
        지하실3_5.alley_finll()
    else:
        check_1 = [0, 재단.fish, 재단.piece, 재단.daga]
        print('주문을 사용하려면 제물이 필요하다.')
        print(f'\n================================')
        print(f'[*] 어떤 제물을 쓰지?')
        print(f'【1】 금붕어')
        print(f'【2】 시체조각')
        print(f'【3】 관에 들어있는 시체')

        num = input('조사선택>> ')
        num = int(num)
        check_1[num]()

    지하실3_5.alley_finll()