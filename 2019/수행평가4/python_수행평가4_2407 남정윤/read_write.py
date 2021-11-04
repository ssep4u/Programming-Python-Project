import pickle
class read:
    def __init__(self):
        pass
    def create1(foodList):
        with open("food.db","wb") as f:
            pickle.dump(foodList, f)

    def create(food):
        with open ("food.db","rb") as f:
            foodList = pickle.load(f)
        foodList.append(food)
        with open ("food.db","wb") as f:
            pickle.dump(foodList, f)
        print(food)
        
    def get_all():
        recipe = []
        with open("food.db","rb") as f:
            foodList = pickle.load(f)
        for item in foodList:
            recipe.append(item)
        return recipe

