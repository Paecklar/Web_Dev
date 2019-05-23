import json



class Person():
    def __init__(self, first_name, last_name, height_cm, weight_kg):
        self.first_name = first_name
        self.last_name = last_name
        self.height_cm = height_cm
        self.weight_kg = weight_kg


class BasketballPlayer(Person):
    def __init__(self, first_name, last_name, height_cm, weight_kg, points):
        super().__init__(first_name, last_name, height_cm, weight_kg)
        self.points = points

    def set_points(self, points):
        if points > 0:
            self.points = points


class FootballPlayer(Person):
    def __init__(self, first_name, last_name, height_cm, weight_kg, goals):
        super().__init__(first_name, last_name, height_cm, weight_kg)
        self.goals = goals

def new_basketballplayer():
    first_name = input("First name: ")
    last_name = input("last name: ")
    height_cm = int(input("Height: "))
    weight_kg = int(input("Weight: "))
    points = int(input("Points: "))

    return BasketballPlayer(first_name, last_name, height_cm, weight_kg, points)


if __name__ == "__main__":
    player1 = new_basketballplayer()

    with open("basketballplayer.json", "w") as json_file:
        json_file.write(json.dumps(player1.__dict__))




