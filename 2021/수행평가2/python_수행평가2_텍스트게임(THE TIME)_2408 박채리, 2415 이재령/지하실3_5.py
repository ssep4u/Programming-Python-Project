import move_limit, 지하실3, in지하실3_5

def alley_finll():
    check_1 = [0, in지하실3_5.box, in지하실3_5.foundation]
    print(f'\n================================')
    print(f'현위치: 지하실')
    print(f'----------------------------------')
    print('말로 표현하기 힘들 정도로 구역질이 나는 광경이다. 온갖 관과 시체라 부르기도 힘든 단백질 조각들이 여기저기 흐트러져있다.')

    print(f'[*] 조사할 곳을 선택해주세요')
    print(f'【1】 관')
    print(f'【2】 재단')
    print(f'【3】 돌아가기')

    num = input('조사선택>> ')
    num = int(num)
    if num == 3:
        print(f'\n================================')
        move_limit.lim2()
        print(f'돌아갈수없다.')
    else:
        check_1[num]()

    지하실3.alley_finl()