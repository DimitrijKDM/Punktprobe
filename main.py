class Ortsvektor:
    def __init__(self, ortsvektor_x, ortsvektor_y, ortsvektor_z):
        self.ortsvektor_z = ortsvektor_z
        self.ortsvektor_y = ortsvektor_y
        self.ortsvektor_x = ortsvektor_x


class Stuetzvektor:
    def __init__(self, stuetzvektor_x, stuetzvektor_y, stuetzvektor_z):
        self.stuetzvektor_z = stuetzvektor_z
        self.stuetzvektor_y = stuetzvektor_y
        self.stuetzvektor_x = stuetzvektor_x


class Richtungsvektor:
    def __init__(self, richtungsvektor_x, richtungsvektor_y, richtungsvektor_z):
        self.richtungsvektor_z = richtungsvektor_z
        self.richtungsvektor_y = richtungsvektor_y
        self.richtungsvektor_x = richtungsvektor_x


class T:
    def __init__(self, t_x, t_y, t_z):
        self.t_z = t_z
        self.t_y = t_y
        self.t_x = t_x


def abfrage_1_gleichung():

    ortsvektor_x = int(input("Ortsvektor Koordinate x\n> "))
    ortsvektor_y = int(input("Ortsvektor Koordinate y\n> "))
    ortsvektor_z = int(input("Ortsvektor Koordinate z\n> "))

    stuetzvektor_x = int(input("Stützvektor Koordinate x\n> "))
    stuetzvektor_y = int(input("Stützvektor Koordinate y\n> "))
    stuetzvektor_z = int(input("Stützvektor Koordinate z\n> "))

    richtungsvektor_x = int(input("Richtungsvektor Koordinate x\n> "))
    richtungsvektor_y = int(input("Richtungsvektor Koordinate y\n> "))
    richtungsvektor_z = int(input("Richtungsvektor Koordinate z\n> "))

    ortsvektor = Ortsvektor(ortsvektor_x, ortsvektor_y, ortsvektor_z)
    stuetzvektor = Stuetzvektor(stuetzvektor_x, stuetzvektor_y, stuetzvektor_z)
    richtungsvektor = Richtungsvektor(richtungsvektor_x, richtungsvektor_y, richtungsvektor_z)

    return ortsvektor, stuetzvektor, richtungsvektor


def gleichung_aufstellen_punktprobe(ortsvektor, stuetzvektor, richtungsvektor):
    t_x = ortsvektor.ortsvektor_x - richtungsvektor.richtungsvektor_x / stuetzvektor.stuetzvektor_x
    t_y = ortsvektor.ortsvektor_y - richtungsvektor.richtungsvektor_y / stuetzvektor.stuetzvektor_y
    t_z = ortsvektor.ortsvektor_z - richtungsvektor.richtungsvektor_z / stuetzvektor.stuetzvektor_z

    t = T(t_x, t_y, t_z)

    return t


def t_vergleichen(t):
    if t.t_x == t.t_y == t.t_z:
        print("Der Punkt liegt auf der Geraden")
    else:
        print("Der Punkt liegt nicht auf der Geraden")


def punktprobe():
    ortsvektor, stuetzvektor, richtungsvektor = abfrage_1_gleichung()
    t = gleichung_aufstellen_punktprobe(ortsvektor, stuetzvektor, richtungsvektor)
    t_vergleichen(t)


if __name__ == '__main__':
    punktprobe()

# todo: Schnittpunkte berechnen, Lineare Abhängigkeit berechnen
