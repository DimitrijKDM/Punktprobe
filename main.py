class OrtsvektorErsteGleichung:
    def __init__(self, ortsvektor_x, ortsvektor_y, ortsvektor_z):
        self.ortsvektor_z = ortsvektor_z
        self.ortsvektor_y = ortsvektor_y
        self.ortsvektor_x = ortsvektor_x


class StuetzvektorErsteGleichung:
    def __init__(self, stuetzvektor_x, stuetzvektor_y, stuetzvektor_z):
        self.stuetzvektor_z = stuetzvektor_z
        self.stuetzvektor_y = stuetzvektor_y
        self.stuetzvektor_x = stuetzvektor_x


class RichtungsvektorErsteGleichung:
    def __init__(self, richtungsvektor_x, richtungsvektor_y, richtungsvektor_z):
        self.richtungsvektor_z = richtungsvektor_z
        self.richtungsvektor_y = richtungsvektor_y
        self.richtungsvektor_x = richtungsvektor_x


class OrtsvektorZweiteGleichung:
    def __init__(self, ortsvektor_x, ortsvektor_y, ortsvektor_z):
        self.ortsvektor_z = ortsvektor_z
        self.ortsvektor_y = ortsvektor_y
        self.ortsvektor_x = ortsvektor_x


class StuetzvektorZweiteGleichung:
    def __init__(self, stuetzvektor_x, stuetzvektor_y, stuetzvektor_z):
        self.stuetzvektor_z = stuetzvektor_z
        self.stuetzvektor_y = stuetzvektor_y
        self.stuetzvektor_x = stuetzvektor_x


class RichtungsvektorZweiteGleichung:
    def __init__(self, richtungsvektor_x, richtungsvektor_y, richtungsvektor_z):
        self.richtungsvektor_z = richtungsvektor_z
        self.richtungsvektor_y = richtungsvektor_y
        self.richtungsvektor_x = richtungsvektor_x


class T:
    def __init__(self, t_x, t_y, t_z):
        self.t_z = t_z
        self.t_y = t_y
        self.t_x = t_x


def abfrage_allgemein():
    while True:
        try:
            zwei_oder_eine_gleichung = int(input("2 oder 1 Gleichung?\n> "))
            if zwei_oder_eine_gleichung == 1:
                punktprobe()
                break
            elif zwei_oder_eine_gleichung == 2:
                pass
                break
            else:
                print("Only 2 or 1 allowed!")
        except ValueError:
            print("Invalid Value!")


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

    ortsvektor_1_gleichung = OrtsvektorErsteGleichung(ortsvektor_x, ortsvektor_y, ortsvektor_z)
    stuetzvektor_1_gleichung = StuetzvektorErsteGleichung(stuetzvektor_x, stuetzvektor_y, stuetzvektor_z)
    richtungsvektor_1_gleichung = RichtungsvektorErsteGleichung(richtungsvektor_x, richtungsvektor_y, richtungsvektor_z)

    return ortsvektor_1_gleichung, stuetzvektor_1_gleichung, richtungsvektor_1_gleichung


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


def abfrage_2_gleichung():

    ortsvektor_x = int(input("Ortsvektor Koordinate x\n> "))
    ortsvektor_y = int(input("Ortsvektor Koordinate y\n> "))
    ortsvektor_z = int(input("Ortsvektor Koordinate z\n> "))

    stuetzvektor_x = int(input("Stützvektor Koordinate x\n> "))
    stuetzvektor_y = int(input("Stützvektor Koordinate y\n> "))
    stuetzvektor_z = int(input("Stützvektor Koordinate z\n> "))

    richtungsvektor_x = int(input("Richtungsvektor Koordinate x\n> "))
    richtungsvektor_y = int(input("Richtungsvektor Koordinate y\n> "))
    richtungsvektor_z = int(input("Richtungsvektor Koordinate z\n> "))

    ortsvektor_2_gleichung = OrtsvektorZweiteGleichung(ortsvektor_x, ortsvektor_y, ortsvektor_z)
    stuetzvektor_2_gleichung = StuetzvektorZweiteGleichung(stuetzvektor_x, stuetzvektor_y, stuetzvektor_z)
    richtungsvektor_2_gleichung = RichtungsvektorZweiteGleichung(richtungsvektor_x, richtungsvektor_y, richtungsvektor_z)

    return ortsvektor_2_gleichung, stuetzvektor_2_gleichung, richtungsvektor_2_gleichung


def punktprobe():
    ortsvektor, stuetzvektor, richtungsvektor = abfrage_1_gleichung()
    t = gleichung_aufstellen_punktprobe(ortsvektor, stuetzvektor, richtungsvektor)
    t_vergleichen(t)


if __name__ == '__main__':
    abfrage_allgemein()

# todo: Schnittpunkte berechnen, Lineare Abhängigkeit berechnen
