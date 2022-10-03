class Player:
    def __init__(self):
        self.name = ""
        self.height = 20
        self.surname = ""
        self.weight = 10
        self.iq = 60
        self.haircolor = ""


Petar_martich = Player()
Petar_martich.name = "Petar martich"
Petar_martich.surname = "Igorevich"
Petar_martich.height = 187
Petar_martich.weight = 84
Petar_martich.iq = 200
Petar_martich.haircolor = "Green"

Pasosh = Player()
Pasosh.name = "Группа пасош"
Pasosh.surname = "Group"
Pasosh.height = 323
Pasosh.weight = 200
Pasosh.iq = 100
Pasosh.haircolor = "Much hair colors"

print(Petar_martich.name, Petar_martich.surname, Petar_martich.height, Petar_martich.weight, Petar_martich.iq,
      Pasosh.haircolor,"\n", sep= " / ")
print(Pasosh.name, Pasosh.surname,Pasosh.height,Pasosh.weight, Pasosh.iq, Pasosh.haircolor,"\n", sep= " / ")
