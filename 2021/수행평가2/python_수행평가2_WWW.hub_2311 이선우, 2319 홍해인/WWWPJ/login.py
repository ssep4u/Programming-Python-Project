#로그인창 만들기
#기능 : 1. 미림이메일로 고유번호 확인
#      2. 비밀번호 3회 오류시 잠금
#      3. ID : 본인이름 PW : 학교 이메일
    #      4. 전공을 + 이름 환영합니다

class Login:
    def show(self):
        cnt = 0
        while True:
            cnt += 1
            # id = '이선우'
            # pw = 'w2010@e-mirim.hs.kr'
            id = input("ID입력(name) : ")
            pw = input("PW(e-mail)입력 : ")
            check_pw = 'e-mirim.hs.kr' in pw  # pw값에서 'e-mirim'찾기

            if check_pw == True:  # 존재할경우 True / 존재 하지 않을 경우 False
                print(">>>로그인되셨습니다.")
                # show(pw, id)
                print('\033[35m'+"===========LOGIN============"+'\033[0m')
                print("ID : " + id)
                print("PW : " + pw)
                major = pw[:1]  # 과추출
                def check_major(major):
                    if major == 's':
                        return "소프트웨어과"
                    elif major == 'w':
                        return "웹솔루션과"
                    elif major == 'd':
                        return "디자인과"
                print("{0} {1}님 환영합니다.".format(check_major(major), id))
                print('\033[35m'+"============================"+'\033[0m')

                import WWWPJ.menu
                show_file = WWWPJ.menu.Mainmenu()
                show_file.mainmenu()

                break

            else:
                f = cnt
                result = f'로그인 {f}회 실패'
                print(result)
                if cnt >= 3:
                    print("PW를 3회 틀리셨기때문에 시스템을 종료합니다.")
                    break

