import move_limit, rooms1, floor, item, 직원아이템


def 칸1():
    #비상약
    if (floor.count5==0):
        floor.count5+=1
        print(f'\n----------------------------------')
        print(f'『비상약』이 들어있다. 상태이상을 해결할 수 있다.')
        print(f'한번밖에 사용을 못하니 신중하게 사용하자')
        print(f'【item】 비상약을 얻었다!')
        print(f'----------------------------------')
        floor.heal_item.insert(5,'비상약')

        직원아이템.서랍()
    else:
        print(f'----------------------------------')
        print(f'첫번째 칸은 비어있다.')
        print(f'----------------------------------')
        직원아이템.서랍()


def 칸2():

    #머리카락뭉치
    print(f'\n----------------------------------')
    print(f'머리카락 뭉치가 들어있다.')
    print(f'----------------------------------')


    move_limit.lim()
    직원아이템.서랍()


def 칸3():

    #반짝이는 무언가

    print(f'\n----------------------------------')
    print(f'구석에 반짝이는 게 보이는데... 손을 집어넣어볼까?')
    print(f'【1】 넣는다')
    print(f'【2】 넣지 않는다')
    print(f'----------------------------------')
    num = input('선택>> ')
    num=int(num)
    if num == 1:
        print(f'----------------------------------')
        print(f'아야..안쪽에 끼어있는 날붙이였다. 손에서 피가 흐른다. HP -1')
        print(f'----------------------------------')
        직원아이템.서랍()
    else:
        print(f'----------------------------------')
        print(f'궁금하긴 하지만 별로 중요해보이진 않는군.')
        print(f'----------------------------------')


        직원아이템.서랍()

