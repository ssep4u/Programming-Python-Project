import alley1, move_limit, item, floor, 지하통로2, 지하실3_5


def alley_finl():
    check_1 = [0, 지하실3_5.alley_finll()]
    print(f'\n================================')
    print('단단히 잠겨있는 문이다. 지하실 열쇠를 사용해서 열 수 있다. 철로 되어있어 힘으론 열지 못할 것 같다.')
    print(f'[*] 무슨 행동을 하지?')
    print('[1] 『작은 열쇠』를 사용하자')
    print('[2] 돌아가기')

    num = input('조사선택>> ')
    num = int(num)
    if num == 2:
        print(f'\n================================')
        move_limit.lim2()
        floor.alley()
    else:
        if(floor.use_item[3] == '작은열쇠'):
            print('문이 열렸다. 들어가자.')
            check_1[1]()
        else:
            print('지하실 열쇠가 없다. 돌아가서 다시 찾아보자.')
            지하통로2.alley_aisle()

    alley1.alley_mouth()

