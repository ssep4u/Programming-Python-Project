import random, item, floor

#사교도
cultist_damage = 0  #공격력
cultist_attack = 70  # 공격 성공 확률 1d10
cultist_hp = 50  #피


#주인공
your_damage = 0 #기본공격력 1d3
your_hp = 100 #주인공 피


def 전투():
    print(f'\n================================')
    print(f'현위치: 2층-《A의 방》')
    print(f'----------------------------------')
    print(f'[*] 조사할 곳을 선택해주세요')
    print(f'【1】 공격')
    print(f'【2】 치료하기')
    print(f'【3】 도망치기')
    num = input('선택>> ')
    num=int(num)
    if num==5:
        print(f'\n================================')
        floor.floor2()
    else:
        check_2[num]()