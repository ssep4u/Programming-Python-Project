import random
import 몹

cul = random.randint(1, 6)
tyn = random.randint(1, 6)
gho = random.randint(1, 6)
쥔공 = random.randint(1, 6)
공격지문 = random.randint(1, 3)

def cul_fight():
    if cul > 쥔공:
        if 공격지문 == 1:
            print('사교도가 팔을 휘둘렀다.')
            몹.c_attack()
        elif 공격지문 == 2:
            print('사교도가 소리를 지르며 달려들었다.')
            몹.c_attack()
        else:
            print('사교도가 주먹을 휘둘렀다.')
            몹.c_attack()
    else:
        print('내가 선수를 쳤다.')
        몹.주인공1()

def gho_fight():
    if gho > 쥔공:
        if 공격지문 == 1:
            print('구울이 쥐어뜯을 듯이 팔을 휘둘렀다.')
            몹.g_attack()
        elif 공격지문 == 2:
            print('구울이 입을 벌리며 달려들었다.')
            몹.g_attack()
        else:
            print('날카로운 손톱을 휘둘렀다.')
            몹.g_attack()
    else:
        print('내가 선수를 쳤다.')
        몹.주인공2()

def tyn_fight():
    if tyn > 쥔공:
        if 공격지문 == 1:
            print('입을 쩌억 벌리고는 날카로운 혀를 휘둘렀다.')
            몹.t_attack()
        elif 공격지문 == 2:
            print('침을 뚝뚝 흘리며 내게 달려들었다.')
            몹.t_attack()
        else:
            print('발톱을 세워 찢어발기려 한다.')
            몹.t_attack()
    else:
        print('내가 선수를 쳤다.')
        몹.주인공()

tyn_fight()