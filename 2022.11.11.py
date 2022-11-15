#  Урок Объяснения классов от АБ 

# class Human:
#      def __init__(self):
#           self.height = 150
#           self.mass = 100
#      def eat(self, mass_food):
#           self.mass += mass_food / 3

# h = Human()
# h.height = 190
# h.mass = 190
# h.eat(190) # == Human.eat(h, 190)

# class Littlebell:
#      def __init__(self):
#           #self.sound_1 = "ding"
#           pass
#      def sound(self):
#           print("ding")



# bell = Littlebell()
# print(bell.sound)
# bell.sound()
# bell.sound()
# bell.sound()

# class Button:
#      def __init__(self):
#           self.click_1 = 0
#           self.count = 0
#      def click(self):
#           self.click_1 += 1
#           self.count += 1
#      def reset(self):
#           self.count = 0
#      def click_count(self):
#           self.count
#           return self.count
          
         
#      # def clic_count(self):
#      #      print()


# button = Button()
# button.click()
# button.click()
# print(button.click_count())
# button.click()
# print(button.click_count())          
          

# class Balance:

#      def __init__(self):
#           self.left = 0
#           self.right = 0
#      def add_left(self, left):
#           self.left += left
#      def add_right(self, right):
#           self.right += right
#      def result(self):
#           if self.left == self.right:
#                print("=")
#           elif self.left > self.right:
#                print("L")
#           else:
#                print("R")

# balance = Balance()
# balance.add_left(9)
# print(balance.result())

class OddEvenSeperator:
     def __init__(self):
          self.odd1 = []
          self.even1 = []
     def add_number(self, number):
          if number % 2 == 0:
               self.odd1.append(number)
          else:
               self.even1.append(number)
     def even(self):
          return self.even1
     def odd(self):
          return self.odd1 
          
               


separator = OddEvenSeperator()
separator.add_number(9)
separator.add_number(2)
print(' '.join(map(str, separator.even())))
print(' '.join(map(str, separator.odd())))


# class BoundindRectangle:
#      def __init__(self):
#           self.x = []
#           self.y = []
#      def add_point(self, x, y):
#           self.x.append(x)
#           self.y.append(y)
     
#      def bottom_y(self):
#           return min(self.y)

#      def top_y(self):
#           return max(self.y)

#      def right_x(self):
#           return max(self.x)

#      def left_x(self):
#           return min(self.x)

#      def height(self):
#           return max(self.y) - min(self.y)

#      def width(self):
#           return max(self.x) - min(self.x)


# rect = BoundindRectangle()
# rect.add_point(-1, -2)
# rect.add_point(3, 4)
# print(rect.left_x(), rect.right_x())
# print(rect.bottom_y(), rect.top_y())
# print(rect.width(), rect.height())

class Situation:
     def __init__(self):
          self.description = ""
          self.ways = dict()
          self.name = ""

situations = dict()

start = Situation()
start.description = "Теплый оченний день, вы решили пройтись по Теплому стану в надежде отыскать хорошее настроение"
start.ways["Диалог"] = "Вы пошли в дикси"
start.ways["Смерть"] = "Вы пошли в пятерочку"
start.name = "Старт"
situations[start.name] = start

Dialog = Situation()
Dialog.description = "Вы подошли и заказали шаурму"
Dialog.ways["Занятие"] = "Вы увидели Антона Борисовича и  покупаете шаурму Антону Борисовичу"
Dialog.ways["Смерть"] = "ВЫ не увидели Антона Борисовича"
Dialog.name = "Диалог"
situations[Dialog.name] = Dialog

death = Situation()
death.description = "Вам поставили 2 на гейм-дизайн"
death.name = "Смерть"
situations[death.name] = death

lessons = Situation()
lessons.description = "Вы пришли на урок к Антону Борисовичу"
lessons.ways["смерть"] = "Антон Борисович поставил 2 за текстовый квест"
lessons.ways["ПЕРЕМЕНА"] = "КОГДА УРОК КОНЧИТСЯ УЖЕ"
lessons.ways["смерть"] = "Антон Борисович поставил 2 за переменную массива на русском"
lessons.name = "Занятие"
situations[lessons.name] = lessons

lesson_break = Situation()
lesson_break.description = "10 минут без Антона Борисовича ощущаются"
lesson_break.ways["Посидеть"] = "Сижу на лавочке кушаю пиццу"
lesson_break.ways["Встреча"] = "Идёшь в столовую, навстречу Михаил Игоревич"
lesson_break.name = "ПЕРЕМЕНА"
situations[lesson_break.name] = lesson_break

seat = Situation()
seat.description = "сидите кушаете пиццу и жизнь налаживается..."
seat.ways["смерть"] = "К вам подошли кадеты"
seat.name = "Посидеть"
situations[seat.name] = seat

meeting = Situation()
meeting.description = "Вы встретили Михаила Игоревича ещё раз... кажется, он не довоелен"
meeting.ways["после школы"] = "Вы поздаровались с Михаилом Игоревичем...кажется, он не услышал"
meeting.ways["игнор"] = "Вы не обратили внимение на Михаила Игоревича"
meeting.name = "Встреча"
situations[meeting.name] = meeting

death_two = Situation()
death_two.description = "Михаил игоревич кинул вас в .gitignore"
death_two.name = "игнор"
situations[death_two.name] = death_two

after = Situation()
after.description = "Уроки закончились, вы идёте домой"
after.ways["остановка"] = "Вы стоите с Альбертом на остановке"
after.ways["автобус"] = "Вы решаете сесть на 982 автобус"
after.name = "после школы"
situations[after.name] = after

bus = Situation()
bus.description = "В автобусе к Альберту подошли контролёры"
bus.ways["конец"] = "Альберт не заплатил за проезд...его департировали"
bus.ways["конец?"] = "Альберт выпрыгнул из автобуса и побежал до татарстана"
bus.name = "автобус"
situations[bus.name] = bus

bus_stop = Situation()
bus_stop.description = "альберт слушает MIYAGI, приежает автобус, день подходит к концу и с лёгкой скорбью в душе, под солнечный закат тёплого мая вы едете домой, смеясь с чурок в автобусе. Едете туда, где боль остаётся позади, где люди, что не смогли привнести в вашу жизнь добро остаются там, где всё началось. Двери закрываются и алоьберт уезжает дальше. Смотря ему вслед, вы понимаете, что ещё никогда не были так счастливы."
bus_stop.name = "остановка"
situations[bus_stop.name] = bus_stop

end = Situation()
end.description = "Альберт уехал домой"
end.name = "конец?"
situations[end.name] = end

bad_end = Situation()
bad_end.description = "Альберт уехал домой"
bad_end.name = "конец"
situations[bad_end.name] = bad_end

death_three = Situation()
death_three.description = "Антон Бориович убил вас и кинул в .gitignore"
death_three.name = "смерть"
situations[death_three.name] = death_three


current_situation = situations["Старт"]


#print(current_situation.ways)
while True:
     print(current_situation.description, "\n")
     for k, v in current_situation.ways.items():
          print(k, v)
     choice = input()
     current_situation = situations[choice]
     if len(current_situation.ways) == 0:
          break

print(current_situation.description)
