import cv2  # 이미지 불러오기
import glob # 리스트 불러오기
from content import *

class Country:
    def picture(self):
        cv2.waitKey()
        cv2.destroyAllWindows()
    def choose_country(self):
        country = input('나라를 입력하세요 (ex: 미국): ')
        return country
    def usa(self):
        Content().usa()
        img_files = glob.glob('.\\usa\\*.png')
        for pics in img_files:
            img = cv2.imread(pics)
            cv2.imshow('image', img)
            self.picture()
    def korea(self):
        Content().korea()
        img_files = glob.glob('.\\korea\\*.png')
        for pics in img_files:
            img = cv2.imread(pics)
            cv2.imshow('image', img)
            self.picture()
    def japan(self):
        Content().japan()
        img_files = glob.glob('.\\japan\\*.png')
        for pics in img_files:
            img = cv2.imread(pics)
            cv2.imshow('image', img)
            self.picture()
    def china(self):
        Content().china()
        img_files = glob.glob('.\\china\\*.png')
        for pics in img_files:
            img = cv2.imread(pics)
            cv2.imshow('image', img)
            self.picture()
    def france(self):
        Content().france()
        img_files = glob.glob('.\\france\\*.png')
        for pics in img_files:
            img = cv2.imread(pics)
            cv2.imshow('image', img)
            self.picture()
    def russia(self):
        Content().russia()
        img_files = glob.glob('.\\russia\\*.png')
        for pics in img_files:
            img = cv2.imread(pics)
            cv2.imshow('image', img)
            self.picture()
    def uk(self):
        Content().uk()
        img_files = glob.glob('.\\uk\\*.png')
        for pics in img_files:
            img = cv2.imread(pics)
            cv2.imshow('image', img)
            self.picture()
    def singapore(self):
        Content().singapore()
        img_files = glob.glob('.\\singapore\\*.png')
        for pics in img_files:
            img = cv2.imread(pics)
            cv2.imshow('image', img)
            self.picture()
    def turkey(self):
        Content().turkey()
        img_files = glob.glob('.\\turkey\\*.png')
        for pics in img_files:
            img = cv2.imread(pics)
            cv2.imshow('image', img)
            self.picture()
    def brazil(self):
        Content().brazil()
        img_files = glob.glob('.\\brazil\\*.png')
        for pics in img_files:
            img = cv2.imread(pics)
            cv2.imshow('image', img)
            self.picture()
    def spain(self):
        Content().spain()
        img_files = glob.glob('.\\spain\\*.png')
        for pics in img_files:
            img = cv2.imread(pics)
            cv2.imshow('image', img)
            self.picture()
    def guam(self):
        Content().guam()
        img_files = glob.glob('.\\guam\\*.png')
        for pics in img_files:
            img = cv2.imread(pics)
            cv2.imshow('image', img)
            self.picture()
    def taiwan(self):
        Content().taiwan()
        img_files = glob.glob('.\\taiwan\\*.png')
        for pics in img_files:
            img = cv2.imread(pics)
            cv2.imshow('image', img)
            self.picture()
    def italy(self):
        Content().italy()
        img_files = glob.glob('.\\italy\\*.png')
        for pics in img_files:
            img = cv2.imread(pics)
            cv2.imshow('image', img)
            self.picture()
    def canada(self):
        Content().canada()
        img_files = glob.glob('.\\canada\\*.png')
        for pics in img_files:
            img = cv2.imread(pics)
            cv2.imshow('image', img)
            self.picture()

    def show_space(self):
        result = self.choose_country()
        if result == '미국':
            self.usa()
        elif result == '한국':
            self.korea()
        elif result == '일본':
            self.japan()
        elif result == '중국':
            self.china()
        elif result == '프랑스':
            self.france()
        elif result == '러시아':
            self.russia()
        elif result == '영국':
            self.uk()
        elif result == '싱가폴':
            self.singapore()
        elif result == '터키':
            self.turkey()
        elif result == '브라질':
            self.brazil()
        elif result == '스페인':
            self.spain()
        elif result == '괌':
            self.guam()
        elif result == '대만':
            self.taiwan()
        elif result == '이탈리아':
            self.italy()
        elif result == '캐나다':
            self.canada()
        else:
            print('해당 나라가 없습니다. 추가해 주세요.')