import move_limit, rooms2, floor, item
def 캔버스():
    print(f'\n================================')
    print(f'현위치: 2층-《명패가 지워진 방》')
    print(f'----------------------------------')
    print(f'나이프로 찢긴 캔버스다. 벌레가 갉아먹은 흔적까지 보인다.')
    print(f'----------------------------------\n')
    rooms2.Broom()

def 물감통():
    print(f'\n================================')
    print(f'현위치: 2층-《명패가 지워진 방》')
    print(f'----------------------------------')
    print(f'딱딱하게 굳은 물감들이다. 오래돼 터지기라도 한 건지 바닥에는 여러 색의 물감들이 묻어있다.')
    print(f'----------------------------------\n')
    rooms2.Broom()

def 커다란창문():
    print(f'\n================================')
    print(f'현위치: 2층-《명패가 지워진 방》')
    print(f'----------------------------------')
    print(f'검은색의 물감들이 말라붙어있다. 썩은 내가 나는 덩어리들이 간간히 보인다. 정말 물감이 맞을까?')
    move_limit.lim3()
    print('버석거리는 겉면을 살짝 건드리자 금방 벗겨진다.')
    move_limit.lim3()
    print('드러난 깨끗한 창문에는 내 모습이 비친다.')
    move_limit.lim3()
    print('원래 이렇게 혈색이 안 좋았나? 그러고보니 칼에 찔렸던 부분도 아프지 않다.')
    move_limit.lim3()
    print('파리가 근처에서 날아다니다 감지 못한 눈 위에 앉았다. 털어내려 손을 들었다.')
    move_limit.lim3()
    print('구더기가 잔뜩 붙어있다. 더러워, 더러워. 더러워. 더러워. 더러워. 더러워. 더러워. 더러워. 더러워. 더러워. 더러워.')
    move_limit.lim3()
    print('본능적으로 입을 벌렸다가, 빠르게 손을 털어냈다. 구더기가 살갗을 파고 들어가려 했다. 기분 나빠.')
    move_limit.lim3()
    print(f'----------------------------------\n')
    rooms2.Broom()

def 하얀상자():
    print(f'\n================================')
    print(f'현위치: 2층-《명패가 지워진 방》')
    print(f'----------------------------------')
    print(f'화장대 위에 놓여져있는 상자다. 그 안에는 하얀색의 면사포 하나가 고이 개어져 들어가있다.')
    print(f'A라는 사람과 동거하던 사람이 아닐까...?')
    print(f'----------------------------------\n')
    rooms2.Broom()