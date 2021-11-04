import pickle

class Read:
    def __init__(self):
        pass

    def create(self, dateList):
        with open("bob.db", "wb" ) as f:
            pickle.dump(dateList, f)

    def insert(day):
        with open("bob.db", "rb") as f:
            dateList = pickle.load(f) # 객체들이 있는 리스트
        for i in dateList:
            if i.date == day.date:
                i.breakfast = day.breakfast
                i.lunch = day.lunch
                i.dinner = day.dinner
            else:
                dateList.append(day)
                with open("bob.db","wb") as f:
                    pickle.dump(dateList, f)

    def get_all():
        bob = []
        with open("bob.db", "rb") as f:
            dateList = pickle.load(f)
        for item in dateList:
            bob.append(item)
        return bob

    def create_first(self):
        dateList = []
        dateList.append(Day("2019-11-2", 0, 1, 1))
        dateList.append(Day("2019-11-3", 1, 1, 0))
        dateList.append(Day("2019-11-4", 1, 1, 1))
        dateList.append(Day("2019-11-5", 0, 1, 0))
        self.create(dateList)

class Day:
    def __init__(self, date, breakfast=0, lunch=0, dinner=0):
        self.date = date
        self.breakfast = breakfast
        self.lunch = lunch
        self.dinner = dinner

if __name__ == '__main__':
    r = Read()
    r.create_first()