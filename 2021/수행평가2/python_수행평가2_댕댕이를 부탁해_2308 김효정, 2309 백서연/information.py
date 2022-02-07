class Sick_part:
    def check_stomach(self):
        #몸
        #배
        print('1. 반복적으로 토한다.')
        print('2. 식후에 토한다.')
        print('3. 식사 직후에 심하게 자주 토한다.')
        print('4. 토하려는 기색이 있고, 입을 핥거나 침을 흘린다.')
        print('5. 심한 설사를 반복한다.')
        print('6. 설사나 무른 변이 만성적으로 계속된다.')
        print('7. 단시간에 급격하게 배가 붓는다.')
        print('8. 하복부가 붓는다.')
        print('9. 배가 부어오르고, 1~2회 설사를 했다. 건강하고 식욕도 있다.')
        print('10. 배가 부어오르고, 탈모를 동반한다.')
        print('11. 배 일부가 붓는다.')
        print('12. 이상한 고열(41도 이상)')
        print('13. 열 외에도 심각한 증상을 동반한다.')
        print('14. 미열이 있다.')
        symptom = input('>> 증상을 선택하세요 : ')
        if symptom == '1':
            print('질병 : 자궁 축농증, 파보바이러스, 장폐색, 급성 위염, 만성 위염, 췌염, \n'
                  '출혈성 위장염, 급성 간염, 급성 신부전, 요독증, 중독')
        elif symptom == '2':
            print('질병 : 파보바이러스, 장폐색, 급성 위염, 만성 위염, 췌염, \n'
                  '출혈성 위장염, 급성 간염, 급성 신부전, 요독증, 중독')
        elif symptom == '3':
            print('질병 : 거대 식도증, 식도 내 이물')
        elif symptom == '4':
            print('질병 : 급성 간염')
        elif symptom == '5':
            print('질병 : 파보바이러스, 코로나바이러스, 홍역, 출혈성 위장염, \n'
                  '췌염, 대장염, 소화관 내 기생충, 중독')
        elif symptom == '6':
            print('질병 : 대장염, 췌염, 췌외분비부전, 소화기 종양, \n'
                  '소화관 내 기생충, 장폐색')
        elif symptom == '7':
            print('질병 : 위확장, 위염전')
        elif symptom == '8':
            print('질병 :자궁 축농증, 요로결석증')
        elif symptom == '9':
            print('질병 : 폐동맥 협착증, 심실 중격 결손증, 심근증, \n'
                  '심장사상충증, 만성 간염, 소화관 내 기생충')
        elif symptom == '10':
            print('질병 : 부신피질 기능향진증')
        elif symptom == '11':
            print('질병 : 소화기 종양')
        elif symptom == '12':
            print('질병이 없어요 즉시 몸을 식히고 긴급히 병원으로 가세요!')
        elif symptom == '13':
            print('질병 : 열사병, 감염증, 호흡기 질환, 소화기 질환, 자궁축농증\n'
                  '중독, 종양, 내이염, 중이염, 관절염, 자기면역에 의한 피부병')
        elif symptom == '14':
            print('질병 : 열사병, 감염증, 호흡기 질환, 소화기 질환, 자궁축농증\n'
                  '중독, 종양, 내이염, 중이염, 관절염, 자기면역에 의한 피부병')

    def check_leg(self):
        # 다리
        print('1. 다리를 든 채 땅에 대지 않고 다리가 부어 있거나 피를 흘린다.')
        print('2. 뒷다리가 마비되었다.')
        print('3. 똑바로 걷지 못하고 같은 곳을 빙글빙글 돈다.')
        print('4. 허리를 흔들면서 걷고 후들거린다.')
        print('5. 다리를 질질 끌고 감싼다.')
        symptom = input('>> 증상을 선택하세요 : ')
        if symptom == '1':
            print('질병 : 골절, 관절염, 탈구, 전십자인대단열')
        elif symptom == '2':
            print('질병 : 추간판 헤르니아')
        elif symptom == '3':
            print('질병 : 전정장애, 내이염, 중이염')
        elif symptom == '4':
            print('질병 ; 고관절 형성부전, 추간판 헤르니아')
        elif symptom == '5':
            print('질병 : 탈구, 슬개골 탈구, 관절염, 뼈의 종양, 상처')
    def check_eye(self):
        #머리
        print('1. 눈의 이상외에 경련발작, 안구가 떨린고 동공이 열리고 좌우대칭이 맞지 않는다.')
        print('2. 눈을 심하게 아파하고 눈이 보이지 않는다.')
        print('3. 눈이 앞으로 튀어나와 있다.')
        print('4. 렌즈가 하얗고 뿌옇다.')
        print('5. 끈적이는 눈곱이 많이 나오고 눈이 빨개지고 눈물이 많이 나오고 눈을 가려워하고 통증이 있다.')
        symptom = input('>> 증상을 선택하세요 : ')
        if symptom == '1':
            print('질병 : 녹내장, 전정장애, 뇌나 신경장애')
        elif symptom == '2':
            print('질병 : 백내장, 포도막염, 녹내장, 눈의 상처와 이물질, 각막염, 망막박리')
        elif symptom == '3':
            print('질병 : 녹내장, 안구 탈출')
        elif symptom == '4':
            print('질병 : 백내장, 당뇨병')
        elif symptom == '5':
            print('질병 : 결막염, 포도막염, 체리아이, 안검내반과 외반, 속눈썹 이상, 알레르기 \n'
                  '각막염, 유루증, 홍역')
    def check_ear(self):
        #귀
        print('1. 귀가 들리지 않는다')
        print('2. 귓속에서 피가 난다.')
        print('3. 귀를 가려워 한다, 아파한다, 머리를 흔든다.')
        symptom = input('>> 증상을 선택하세요 : ')
        if symptom == '1':
            print('질병 : 내이염, 중이염, 전정장애, 종양')
        elif symptom == '2':
            print('질병 : 종양')
        elif symptom == '3':
            print('질병 : 외이염, 중이염, 개선충증, 마라세티아 감염증, 이혈종')
    def check_nose(self):
        #코
        print('3. 코피가 난다.(많이 나오고 멈추지 않는다)')
        print('질병 : 폐수종, 혈소판 감소증, 비염, 부비감염, 종양, 상처')
        #입
    def check_mouth(self):
        print('1. 코를 고는데 호흡곤란을 동반한다.')
        print('2. 호흡이 이상하게 빠르고 콧구멍이 실룩거린다.')
        print('3. 입을 벌리고 뻐끔거린다.')
        print('4. 주저앉는다. 턱을 들고 숨쉰다, 눕지 못한다.')
        print('5. 거위 울음처러 뻐억뻐억 소리가 들린다.')
        print('6. 쌕쌕 소리가 난다')
        print('7. 검붉은 피를 토한다.')
        print('8. 기침과 함께 지한 붉은 피를 토한다, 피에 작은 거품이 섞여 있다.')
        print('9. 입안이나 코에서 출혈이 난다.')
        symptom = input('>> 증상을 선택하세요 : ')
        if symptom == '1':
            print('질병 : 연구개 과장증, 종양')
        elif symptom == '2':
            print('질병 : 열사병, 기흉, 기관지염, 종양, 폐렴, 폐수종')
        elif symptom == '3':
            print('질병 : 식도 내 이물, 폐수종, 기관지염')
        elif symptom == '4':
            print('질병 : 횡경막 헤르니아, 폐수종, 기흉, 심근증')
        elif symptom == '5':
            print('질병 : 기관허탈, 연구개 과장증')
        elif symptom == '6':
            print('질병 : 기관지염, 폐렴')
        elif symptom == '7':
            print('질병 : 급성 위염, 만성 위염, 혈소판 감소증, 종양')
        elif symptom == '8':
            print('질병 : 폐렴, 기관지염, 폐수종, 인두염, 심장사상충증, 혈소판 감소증')
        elif symptom == '9':
            print('질병 : 비염, 종양, 부비강염, 치주 질환')
    def whole_body(self):
        #전신
        print('1. 피부가 노랗다.')
        print('2. 다치지 않았는데 보라색이 멍이 들었다.')
        print('3. 피부에서 이상한 냄새가 난다.')
        print('4. 멍울이 있다.')
        print('5. 붉은기, 습진, 비듬이 있고 가려워한다.')
        print('6. 전신에 경련을 일으킨다.')
        print('7. 부분적으로 경련을 일으킨다')
        print('8. 의식을 잃는다.(몇 분이상 지속되고 의식을 되찾았지만 기운이 없다. ')
        symptom = input('>> 증상을 선택하세요 : ')
        if symptom == '1':
            print('질병 : 급성 간염, 중독, 빈혈')
        elif symptom == '2':
            print('질병 : 혈소판 감소증')
        elif symptom == '3':
            print('질병 : 피부 감염증, 피부 괴사나 화농')
        elif symptom == '4':
            print('질병 : 피부 종양, 유선 종양')
        elif symptom == '5':
            print('질병 : 알레르기성 피부병, 내분비 질병, 피부 감염증')
        elif symptom == '6':
            print('질병 : 저칼슘혈증, 간질, 중독, 종양, 신부전, 광견병, 홍역')
        elif symptom == '7':
            print('질병 : 간질, 홍역의 후유증')
        elif symptom == '8':
            print('질병 : 동맥관 개존증, 심실 중격 결손증, 폐동맥 협착증, \n'
                  '심장사상충증, 승모판 폐쇄부전, 심근증, 부정맥')



