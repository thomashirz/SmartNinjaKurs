class Player():
    def __init__(self, first_name, last_name, height_cm, weight_kg):
        self.first_name = first_name
        self.last_name = last_name
        self.height_cm = height_cm
        self.weight_kg = weight_kg


class BasketballPlayer(Player):
    def __init__(self, first_name, last_name, height_cm, weight_kg, points, rebounds, assists):
        super().__init__(first_name=first_name, last_name=last_name, height_cm=height_cm, weight_kg=weight_kg)
        self.points = points
        self.rebounds = rebounds
        self.assists = assists

    def set_points(self, points):
        self.points = points


class FootballPlayer(Player):
    def __init__(self, first_name, last_name, height_cm, weight_kg, goals, yellow_cards, red_cards):
        super().__init__(first_name=first_name, last_name=last_name, height_cm=height_cm, weight_kg=weight_kg)
        self.goals = goals
        self.yellow_cards = yellow_cards
        self.red_cards = red_cards



if __name__ == "__main__":
    j = BasketballPlayer("Michael", "Jordan", 205, 10, 98, 35, 99)
    d = BasketballPlayer("Dirk", "Nowitzki", 235, 0, 102, 27, 70)
    messi = FootballPlayer("Lionel", "Messi", 220, 170, 60, 220, 27, 4)

    d.set_points(900)
    player = [j, d]

    for item in player:
        print(item.first_name)
        print(item.points)


user_input():
first_name = input("First name: ")
last_name = input("Last name: ")
