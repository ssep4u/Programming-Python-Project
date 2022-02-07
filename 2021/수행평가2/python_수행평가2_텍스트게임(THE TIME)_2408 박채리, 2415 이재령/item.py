import random
tanum=0
def use(): #문제해결용 아이템
    item_get=[0,'□', '□', '□']       #일단13개
    return(item_get)

def hit(): #공격무기
    warn_get=[0,'□','□','□']
    return(warn_get)

def heal(): #힐링용아이템
    heal_get=[0,'□','□','□','□','□']
    return (heal_get)

def 권총():
    global tanum
    #2d6+3
    if tanum<=3:
        a= random.randint(1, 6 + 1)
        b= random.randint(1, 6 + 1)
        권총deal=a+b+3
        print(f'총알이 {3-tanum} 남았습니다.')
        tanum +=1
        return 권총deal
    elif tanum>3:
        return f'총알이 없습니다.'




