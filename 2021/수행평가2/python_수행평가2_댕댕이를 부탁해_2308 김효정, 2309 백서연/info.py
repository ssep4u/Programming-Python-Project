class Info:
    def __init__(self, name):
        #이름
        self.name = name
        #종류
        self.species = ''
        #나이
        self.age = 1
        #성별
        self.gender = ''
        #몸무게
        self.weight = 1
        #특이질환 (생략가능)
        self.disease = ''


    def set_species(self):
        species = input('>> 견종을 입력해주세요 : ')
        self.species ='필수 항목입니다.' if species == '' else species

    def set_age(self):
        age = input('>> 나이를 입력해주세요 : ')
        self.age = '필수 항목입니다.' if age == '' else age

    def set_gender(self):
        gender = input('>> 성별을 입력해주세요 : ')
        self.gender = '필수 항목입니다.' if gender == '' else gender

    def set_weight(self):
        weight = input('>> 몸무게를 입력해주세요 : ')
        self.weight = '필수 항목입니다.' if weight == '' else weight

    def set_disease(self):
        disease = input('>> 특이질환을 입력해주세요(생략가능) : ')
        self.disease = '' if disease == '' else disease
        return disease

    def set_info(self):
        self.set_species()
        self.set_age()
        self.set_gender()
        self.set_weight()
        self.set_disease()

    def __str__(self):
        return f'이름: {self.name}\n종: {self.species}\n나이: {self.age}살\n성별: {self.gender}\n' \
        f'몸무게: {self.weight}kg\n특이질환: {self.disease}'



