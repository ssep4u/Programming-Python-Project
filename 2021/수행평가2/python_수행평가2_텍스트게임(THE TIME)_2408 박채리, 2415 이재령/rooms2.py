import floor, move_limit, 피아노아이템, A아이템, B아이템
def piano(): #피아노실

    check_1=[0,피아노아이템.그랜드, 피아노아이템.바닥, 피아노아이템.진열장]
    print(f'\n================================')
    print(f'현위치: 2층-《피아노실》')
    print(f'----------------------------------')
    print(f'[*] 조사할 곳을 선택해주세요')
    print(f'【1】 그랜드피아노')
    print(f'【2】 바닥')
    print(f'【3】 진열장')
    print(f'【4】 돌아가기')

    num = input('조사선택>> ')
    num=int(num)
    if num==4:
        print(f'\n================================')
        move_limit.lim2()
        floor.floor2()
    else:
        check_1[num]()

def Aroom(): #A의 방
    check_2=[0,A아이템.침대, A아이템.창문, A아이템.벽, A아이템.책상]
    print(f'\n================================')
    print(f'현위치: 2층-《A의 방》')
    print(f'----------------------------------')
    print(f'[*] 조사할 곳을 선택해주세요')
    print(f'【1】 침대')
    print(f'【2】 창문')
    print(f'【3】 벽')
    print(f'【4】 책상')
    print(f'【5】 돌아가기')

    num = input('조사선택>> ')
    num=int(num)
    if num==5:
        print(f'\n================================')
        move_limit.lim2()
        floor.floor2()
    else:
        check_2[num]()

def Broom(): #B의 방
    check_3 = [0, B아이템.캔버스, B아이템.물감통, B아이템.커다란창문, B아이템.하얀상자]
    print(f'\n================================')
    print(f'현위치: 2층-《명패가 지워진 방》')
    print(f'----------------------------------')
    print(f'[*] 조사할 곳을 선택해주세요')
    print(f'【1】 캔버스')
    print(f'【2】 물감통')
    print(f'【3】 커다란창문')
    print(f'【4】 하얀상자')
    print(f'【5】 돌아가기')

    num = input('조사선택>> ')
    num = int(num)
    if num == 5:
        print(f'\n================================')
        move_limit.lim2()
        floor.floor2()
    else:
        check_3[num]()
