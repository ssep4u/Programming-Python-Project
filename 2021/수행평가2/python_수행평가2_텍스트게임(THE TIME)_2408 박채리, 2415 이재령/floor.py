import rooms1, rooms2, rooms3, alley1,move_limit, item, 사교도
global count, count1, count2, count3, count4, count5, count6, count7, count8,count9, count10, count11, use_item, heal_item, hit_item
use_item=item.use()
heal_item=item.heal()
hit_item = item.hit()
count=0 #도마
count1=0 #칸1
count2=0 #칸2
count3=0 #칸3
count4=0 #홀-어항
count5=0 #서랍칸-칸1
count6=0 #간이침대-망치
count7=0 #의자다리
count8=0 #피아노실-지하실열쇠
count9=0 #A의 방- 벽
count10=0 #빈방-바닥-종이
count11=0 #작은열쇠
scount1 = 0

def select_floor():
    print(f'【1】 1층')
    print(f'【2】 2층')
    print(f'【3】 3층')
    print(f'【4】 지하실')
    num = input('층수선택>> ')

    #move_limit.lim()
    num=int(num)
    if num==1:
        floor1()
    elif num==2:
        floor2()
    elif num==3:
        floor3()
    elif num==4:
        alley()

#-------------------------------------------------------------------------------
room_list1=[0, rooms1.show1,rooms1.show2,rooms1.show3,rooms1.show4]
def floor1():
    print(f'\n================================')
    print(f'현위치: 1층')
    print(f'----------------------------------')
    print(f'【1】 부엌')
    print(f'【2】 홀')
    print(f'【3】 직원휴게실')
    print(f'【4】 식당')
    print(f'【5】 돌아가기')

    num = input('방선택>> ')
    num=int(num)

    if num==5:
        print(f'\n================================')
        move_limit.lim2()
        print(f'\n================================')
        print(f'현위치: 저택')
        print(f'----------------------------------')
        select_floor()
    else:
        room_list1[num]()

#-------------------------------------------------------------------------------
room_list2=[0, rooms2.piano, rooms2.Aroom, rooms2.Broom]
def floor2():
    print(f'\n================================')
    print(f'현위치: 2층')
    print(f'----------------------------------')
    print(f'【1】 피아노실')
    print(f'【2】 A의 방')
    print(f'【3】 B의 방')
    print(f'【4】 돌아가기')
    num = input('방선택>> ')
    num=int(num)

    if num==4:
        print(f'\n================================')
        move_limit.lim2()
        print(f'\n================================')
        print(f'현위치: 저택')
        print(f'----------------------------------')
        select_floor()
    else:
        room_list2[num]()

#-------------------------------------------------------------------------------
room_list3=[0, rooms3.empty, rooms3.book, rooms3.artroom]
def floor3():
    print(f'\n================================')
    print(f'현위치: 3층')
    print(f'----------------------------------')
    print(f'【1】 빈방')
    print(f'【2】 서재')
    print(f'【3】 화실')
    print(f'【4】 돌아가기')

    num = input('방선택>> ')
    num=int(num)
    if num==4:
        move_limit.lim2()
        print(f'\n================================')
        print(f'현위치: 저택')
        print(f'----------------------------------')
        select_floor()
    else:
        room_list3[num]()

#-------------------------------------------------------------------------------
room_list4=[0, alley1.alley_mouth]
def alley():
    print(f'【1】 지하실입구')
    print(f'【2】 돌아가기')
    num = input('방선택>> ')
    num=int(num)
    if num==2:
        print(f'\n================================')
        move_limit.lim2()
        print(f'\n================================')
        print(f'현위치: 저택')
        print(f'----------------------------------')
        select_floor()
    else:
        room_list4[num]()
