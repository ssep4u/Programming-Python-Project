import floor,move_limit, item, rooms1
def 샹들리에():
    print(f'\n================================')
    print(f'현위치: 1층-《홀》')
    print(f'----------------------------------')
    print(f'바닥에 떨어져 날카로운 파편이 주변에 잔뜩 튀어있다. 샹들리에 아래로 사람의 손 같은 게 보인다.')
    print(f'----------------------------------')
    rooms1.show2()

def 꽃병():
    print(f'\n================================')
    print(f'현위치: 1층-《홀》')
    print(f'----------------------------------')
    print(f'엉망진창이 된 곳에서 유일하게 멀쩡한 물체. 싱그러운 장미꽃 하나가 꽂혀있다.')
    print(f'----------------------------------')
    rooms1.show2()

def 어항():
    if (floor.count4==0):
        floor.count4+=1
        print(f'\n================================')
        print(f'현위치: 1층-《홀》')
        print(f'----------------------------------')
        print(f'깨끗한 물이 들어있다. 금붕어 한 마리가 다른 금붕어를 잡아 먹고 살았는지, 바닥에는 사체로 보이는 것들이 나뒹굴고 있다.')
        move_limit.lim3()
        print('나도 모르게 침을 삼켰다. 배가 고픈가? 배가 고프다. 알 수 없는 허기가 뇌를 쿡쿡 찔렀다.')
        move_limit.lim3()
        print('금붕어의 눈을 빤히 쳐다봤다. 그래, 이 물고기도 살기 위해 동족을 뜯어먹었다. 나라고 안 될 게 있나?')
        move_limit.lim3()
        print('문득 아까 만났던 남자가 떠올랐다. 남자를 찾아서...')
        move_limit.lim3()
        print('찾아서......')
        move_limit.lim3()
        move_limit.lim3()
        print('찾아서 뭘 하려고?')
        move_limit.lim3()
        print('정신이 들었다. 머리가 제대로 돌아가지 않는다.')
        move_limit.lim3()
        print(f'----')
        print(f'죽일까...?')
        print(f'【1】 죽인다')
        print(f'【2】 물을 버린다')
        print(f'----------------------------------')
        print(f'『죽이는건 신중해야한다. 죽일땐 직접타자를 치자.』')
        num=input('선택>> ')
        if num=='죽인다':
            print(f'\n금붕어를 꺼내 바닥에 던졌다. 발로 즈려 밟으니 팔딱거리던 움직임이 멎는다. 이제 이 저택에 살아있는 생명은 당신밖에 없다.')
            print(f'【item】 『금붕어사체』를 얻었다.')
        elif num=='죽인다.':
            print(f'\n금붕어를 꺼내 바닥에 던졌다. 발로 즈려 밟으니 팔딱거리던 움직임이 멎는다. 이제 이 저택에 살아있는 생명은 당신밖에 없다.')
            print(f'【item】 『금붕어사체』를 얻었다.')
        elif num=='죽인다 ':
            print(f'\n금붕어를 꺼내 바닥에 던졌다. 발로 즈려 밟으니 팔딱거리던 움직임이 멎는다. 이제 이 저택에 살아있는 생명은 당신밖에 없다.')
            print(f'【item】 『금붕어사체』를 얻었다.')
        else:
            print(f'\n어항을 들어 바닥에 물을 쏟았다. 금붕어가 살려달라는 듯 팔딱거린다. 더 볼 것은 없어 보인다.')
            print(f'【item】 금붕어사체를 얻었다.')
        print(f'----------------------------------')
        floor.heal_item.insert(4,'금붕어사체')

        rooms1.show2()
    else:
        print(f'\n================================')
        print(f'현위치: 1층-《홀》')
        print(f'----------------------------------')
        print(f'빈 어항이다.')
        print(f'----------------------------------')
        rooms1.show2()