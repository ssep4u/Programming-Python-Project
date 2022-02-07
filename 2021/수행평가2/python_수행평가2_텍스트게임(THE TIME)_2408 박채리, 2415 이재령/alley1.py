import floor, move_limit, 지하실1

alley_count = 0 #지하실 퍼즐 깼는지 안 깼는지

def alley_mouth(): #지하실입구
    check_1 = [0, 지하실1.작은열쇠, 지하실1.지하실열쇠, 지하실1.강제]
    print(f'\n================================')
    print(f'현위치: 지하실입구')
    print(f'----------------------------------')
    print(f'[*] 지하실 앞을 철문이 막고 있다. 힘으론 열지 못한다. 열쇠구멍이있다. 열쇠가 필요할 것 같다.')
    print(f'----------------------------------')
    print(f'[*] 무슨 행동을 하지?')
    print(f'【1】 『작은열쇠』를 사용하자')
    print(f'【2】 『지하실열쇠』를 사용하자')
    print(f'【3】 강제로 열어보자')
    print(f'【4】 돌아가기')

    num = input('조사선택>> ')
    num = int(num)
    if num == 4:
        print(f'\n================================')
        move_limit.lim2()
        floor.select_floor()
    else:
        check_1[num]()