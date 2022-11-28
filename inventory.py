class Situation:
    def __init__(self, name, description, ways={}, items=[]):
        self.name = name
        self.description = description
        self.ways = ways
        self.items = items

    def get_item(self, item):
        if item not in self.items:
            print("Сквозь ваши руки пустота.")
            return
        self.items.remove(item)
        return item



class Game:
    def __init__(self):
        lst = [Situation("Старт", "Вы просыпаетесь на поляне полной цветов",
                         {"Подняться": "Вы поднимаетесь на ноги, осматриваясь..", "Смерть": "Вы засыпаете.."}),
               Situation("Подняться", "Вы вошли в темный лес",
                         {"Старт": "Вы возвращаетесь", "Смерть": "Вам оторвало ногу",
                          "Победа": "Вы находите тайник..."}, ["Нож", "Душа", "Кожаные перчатки"]),
               Situation("Смерть", "Вы сдались под натиском необъятного"),
               Situation("Победа", "Вы проснулись но..кажется..все повторяется..")
               ]

        self.situations = dict()
        for situation in lst:
            self.situations[situation.name] = situation

        self.inventory = []

    def start(self):
        current_situation = self.situations["Старт"]
        while True:
            print(current_situation.description)
            for i, (k, v) in enumerate(current_situation.ways.items()):
                print(i + 1, v)
            if current_situation.items:
                print(f"{i+2} Вы поднимаете что-то")
            print(f"{i+3} Порыться в карманах")
            choice_number = int(input())
            if choice_number != i + 2 and choice_number != i + 3:
                choice = list(current_situation.ways.keys())[choice_number - 1]
                current_situation = self.situations[choice]
            elif choice_number == i + 3:
                print(f"В правом кармане: {', '.join(self.inventory)}")
            else:
                print("Достать: " + " ".join(current_situation.items))
                choice_item = input()
                self.inventory.append(current_situation.get_item(choice_item))

            if len(current_situation.ways) == 0:
                break
        print(current_situation.description)


Game().start()