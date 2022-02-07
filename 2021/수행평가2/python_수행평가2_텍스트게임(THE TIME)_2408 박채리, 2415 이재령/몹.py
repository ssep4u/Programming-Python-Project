import random, item, floor
global cultist_damage
cultist_hp = 50  # 체력
cultist_damage = 0 # 공격력
cultist_attack = 70  # 공격 성공 확률 /1d3
# --
tyndalos_hp = 80  # 체력
tyndalos_damage = 0 # 공격력
tyndalos_attack = 70  # 공격 성공 확률 /1d3
#--
ghoule_hp = 70  # 체력
ghoule_damage = 0 # 공격력
ghoule_attack = 40  # 공격 성공 확률 /1d3
#--
주인공_damage = item.권총()
주인공hp = 100




def 주인공1():
    global 주인공_damage
    global cultist_hp

    if cultist_hp<=0:
        print(f'사교도는 쓰러졌습니다.')
        print(f'\n----------------------------------')
    else:
        print(f'주인공의 공격. 사교도가 {주인공_damage} 만큼의 피해를 입었다.')
        item.권총()
        cultist_hp = cultist_hp - (주인공_damage)
        print(f'사교도의 체력| {cultist_hp}')
        print(f'\n----------------------------------')

def 주인공2():
    global 주인공_damage
    global ghoule_hp

    if ghoule_hp<=0:
        print(f'구울은 쓰러졌습니다.')
        print(f'\n----------------------------------')
    else:
        print(f'주인공의 공격. 구울이 {주인공_damage} 만큼의 피해를 입었다.')
        item.권총()
        ghoule_hp = ghoule_hp - (주인공_damage)
        print(f'구울의 체력| {ghoule_hp}')
        print(f'\n----------------------------------')

def 주인공3():
    global 주인공_damage
    global tyndalos_hp

    if tyndalos_hp<=0:
        print(f'틴달로스의 사냥개는 쓰러졌습니다.')
        print(f'\n----------------------------------')
    else:
        print(f'주인공의 공격. 틴달로스의 사냥개가 {주인공_damage} 만큼의 피해를 입었다.')
        item.권총()
        tyndalos_hp = tyndalos_hp - (주인공_damage)
        print(f'틴달로스의 사냥개의 체력| {tyndalos_hp}')
        print(f'\n----------------------------------')


def c_attack():
    global 주인공hp
    global cultist_damage

    if random.randint(1, 100) < cultist_attack:
        cultist_damage = random.randint(1, 10)

        print(f'사교도의 공격. 내가 {cultist_damage} 만큼의 피해를 입었다.')
        주인공hp=주인공hp-(cultist_damage)
        print(f'주인공의 체력| {주인공hp}')
        print(f'\n----------------------------------')
    else:
        print('사교도의 공격 실패.')
        print(f'주인공의 체력| {주인공hp}')
        print(f'\n----------------------------------')


def t_attack():
    global 주인공hp
    global tyndalos_damage

    if random.randint(1, 100) < tyndalos_attack:
        tyndalos_damage = random.randint(1, 6) + random.randint(1, 6) + random.randint(1, 3)

        print(f'틴달로스의 사냥개의 공격. 내가 {tyndalos_damage} 만큼의 피해를 입었다.')
        주인공hp=주인공hp-(tyndalos_damage)
        print(f'주인공의 체력| {주인공hp}')
        print(f'\n----------------------------------')
    else:
        print('틴달로스의 사냥개의 공격 실패.')
        print(f'주인공의 체력| {주인공hp}')
        print(f'\n----------------------------------')


def g_attack():
    global 주인공hp
    global ghoule_damage

    if random.randint(1, 100) < ghoule_attack:
        ghoule_damage = random.randint(1, 6) + random.randint(1, 4)

        print(f'구울의 공격. 내가 {ghoule_damage} 만큼의 피해를 입었다.')
        주인공hp=주인공hp-(ghoule_damage)
        print(f'주인공의 체력| {주인공hp}')
        print(f'\n----------------------------------')
    else:
        print('구울의 공격 실패.')
        print(f'주인공의 체력| {주인공hp}')
        print(f'\n----------------------------------')
