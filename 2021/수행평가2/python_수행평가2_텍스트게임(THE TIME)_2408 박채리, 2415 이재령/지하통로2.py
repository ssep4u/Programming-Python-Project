import alley1, move_limit, 지하실3


def alley_aisle():
    print(f'\n================================')
    print(f'현위치: 지하실 통로입구')
    print(f'----------------------------------')
    move_limit.lim2()
    print(f'입구로 보이는 문에는 쇠로 만들어진 래버가 달려있다. 잘 돌리면 열릴 것 같은데... 어떻게 돌려야하지?')
    print('[1] ↑')
    print('[2] ↓')
    print('[3] ←')
    print('[4] →')
    print(f'----------------------------------') #답 ↑  ←  ↑  →  ←  ↓

    print('입력 예시(숫자만 입력) : 1(↑)')
    num =input('순서대로 입력하시오(하나씩)>> ')
    num = int(num)
    if num == 1:
        num = input('순서대로 입력하시오(하나씩)>> ')
        num = int(num)
        if num == 3:
            num = input('순서대로 입력하시오(하나씩)>> ')
            num = int(num)
            if num == 1:
                num = input('순서대로 입력하시오(하나씩)>> ')
                num = int(num)
                if num == 4:
                    num = input('순서대로 입력하시오(하나씩)>> ')
                    num = int(num)
                    if num == 3:
                        num = input('순서대로 입력하시오(하나씩)>> ')
                        num = int(num)
                        if num == 2:
                            print('문이 열렸다. 퀴퀴한 곰팡이 냄새가 나는 통로다. 이젠 검은색이 된 피가 박과 벽에 잔뜩 눌러 붙어있다. 이대로 쭉 걸어가자.')
                            지하실3.alley_finl()
                        else:
                            print('틀렸다.')
                    else:
                        print('틀렸다.')
                else:
                    print('틀렸다.')
            else:
                print('틀렸다.')
        else:
            print('틀렸다.')
    else:
        print('틀렸다.')
    # if a == 1:
    #     check_1[a]()

    alley_aisle()

