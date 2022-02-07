class Survey:
    def show(a,b=[]):
        print('\n')
        print('┌───────────────────┐')
        print(' 정보가 마음에 드셨나요? ')
        print('\033[93m'+' 1.만족 2.보통 3.불만족'+'\033[0m')
        print('└───────────────────┘')
        print('　 　ᕱ ᕱ  ||')
        print('　  ( ･ω･ ||')
        print('　  /　つΦ')

        survery_menu = int(input('받으신 서비스의 얼마나 만족하셨나요? : '))
        # print(survery_menu)
        if (survery_menu == 1):  # 만약 1. 만족을 선택하였다면
            print("답변감사드립니다.")  # 답변 감사드립니다 출력
            b.append(survery_menu)  # 설문 값에 1넣기
        elif (survery_menu == 2):  # 만약 2.보통을 선택하였다면
            print("답변감사드립니다.")  # 답변 감사드립니다 출력
            b.append(survery_menu)  # 설문 값에 2넣기
        elif (survery_menu == 3):  # 만약 3.불만족을 선택하였다면
            print("답변감사드립니다.")  # 답변 감사드립니다 출력
            b.append(survery_menu)  # 설문 값에 3넣기
        else:
            s = survery_menu  # 만약 1, 2, 3을 제외한 다른 수를 넣었다면
            result = f'{s}...{s}...{s}라...왜{s}를..누른거지..?'  # 그 수를 이용해 왜 그 수를 눌렀냐고 물어보기(개그요소)
            print(result)

        b.append(1) #임의로 만든 설문
        b.append(1)
        b.append(2)

        survery_add = sum(b)               #survery_add에 설문응답 숫자들을 더해 넣자
        survery_avg = survery_add/len(b)   #survery_avg에 survery_add의 숫자를 설문응답 길이만큼 나눠 평균 구하자
        res = survery_avg                  #res에 평균값 넣어주자

        # print(result)


        print('\033[93m')                   #색추가
        if 1 <= res < 1.5:                 #만약 점수가 1에서 1.5점 이라면
            print("평균 답변 : ★★★★★")     #별 5점
        elif 1.5 <= res < 2.0:              #만약 점수가 1.6에서 2.0점 이라면
            print("평균 답변 : ★★★★☆")     #별 4점
        elif 2.0 <= res < 2.5:              #만약 점수가 2.1에서 2.5점 이라면
            print("평균 답변 : ★★★☆☆")     #별 3점
        elif 2.5 <= res < 3.0:              #만약 점수가 2.6에서 2.9점 이라면
            print("평균 답변 : ★★☆☆☆")     #별 2점
        elif res == 3:                      #만약 점수가 3점이라면
            print("평균 답변 : ★☆☆☆☆")     #별 1점
        print('\033[0m')