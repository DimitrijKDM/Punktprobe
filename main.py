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


class StuetzvektorErsteGleichung_2_Geraden:
    def __init__(self, stuetzvektor_x, stuetzvektor_y, stuetzvektor_z):
        self.stuetzvektor_z = stuetzvektor_z
        self.stuetzvektor_y = stuetzvektor_y
        self.stuetzvektor_x = stuetzvektor_x


class RichtungsvektorErsteGleichung_2_Geraden:
    def __init__(self, richtungsvektor_x, richtungsvektor_y, richtungsvektor_z):
        self.richtungsvektor_z = richtungsvektor_z
        self.richtungsvektor_y = richtungsvektor_y
        self.richtungsvektor_x = richtungsvektor_x


class StuetzvektorZweiteGleichung_2_Geraden:
    def __init__(self, stuetzvektor_x_2, stuetzvektor_y_2, stuetzvektor_z_2):
        self.stuetzvektor_z_2 = stuetzvektor_z_2
        self.stuetzvektor_y_2 = stuetzvektor_y_2
        self.stuetzvektor_x_2 = stuetzvektor_x_2


class RichtungsvektorZweiteGleichung_2_Geraden:
    def __init__(self, richtungsvektor_x_2, richtungsvektor_y_2, richtungsvektor_z_2):
        self.richtungsvektor_z_2 = richtungsvektor_z_2
        self.richtungsvektor_y_2 = richtungsvektor_y_2
        self.richtungsvektor_x_2 = richtungsvektor_x_2


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
                abfrage_schnittpunkte_oder_abhaengigkeit()
                break
            else:
                print("Only 2 or 1 allowed!")
        except ValueError:
            print("Invalid Value!")


def abfrage_schnittpunkte_oder_abhaengigkeit():
    while True:
        schnittpunkte_oder_abhaengigkeit = input("Schnittpunkte oder Lineare Abhängigkeit berechnen?\n> ")
        if schnittpunkte_oder_abhaengigkeit.lower() == "schnittpunkte":
            pass
        elif schnittpunkte_oder_abhaengigkeit.lower() == "lineare abhängigkeit":
            pass
        else:
            print("Invalid Value! <Schnittpunkte> oder <Lineare Abhängigkeit> eingeben")


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
    stuetzvektor_1_gleichung = StuetzvektorErsteGleichung_2_Geraden(stuetzvektor_x, stuetzvektor_y, stuetzvektor_z)
    richtungsvektor_1_gleichung = RichtungsvektorErsteGleichung(richtungsvektor_x, richtungsvektor_y, richtungsvektor_z)

    return ortsvektor_1_gleichung, stuetzvektor_1_gleichung, richtungsvektor_1_gleichung


def gleichung_aufstellen_punktprobe(ortsvektor_1_gleichung, stuetzvektor_1_gleichung, richtungsvektor_1_gleichung):
    t_x = ortsvektor_1_gleichung.ortsvektor_x - richtungsvektor_1_gleichung.richtungsvektor_x / \
          stuetzvektor_1_gleichung.stuetzvektor_x
    t_y = ortsvektor_1_gleichung.ortsvektor_y - richtungsvektor_1_gleichung.richtungsvektor_y / \
          stuetzvektor_1_gleichung.stuetzvektor_y
    t_z = ortsvektor_1_gleichung.ortsvektor_z - richtungsvektor_1_gleichung.richtungsvektor_z / \
          stuetzvektor_1_gleichung.stuetzvektor_z

    t = T(t_x, t_y, t_z)

    return t


def t_vergleichen(t):
    if t.t_x == t.t_y == t.t_z:
        print("Der Punkt liegt auf der Geraden")
    else:
        print("Der Punkt liegt nicht auf der Geraden")


def abfrage_2_gleichungen():

    stuetzvektor_x = int(input("1. Gleichung: Stützvektor Koordinate x\n> "))
    stuetzvektor_y = int(input("1. Gleichung: Stützvektor Koordinate y\n> "))
    stuetzvektor_z = int(input("1. Gleichung: Stützvektor Koordinate z\n> "))

    richtungsvektor_x = int(input("1. Gleichung: Richtungsvektor Koordinate x\n> "))
    richtungsvektor_y = int(input("1. Gleichung: Richtungsvektor Koordinate y\n> "))
    richtungsvektor_z = int(input("1. Gleichung: Richtungsvektor Koordinate z\n> "))

    stuetzvektor_x_2 = int(input("2. Gleichung: Stützvektor Koordinate x\n> "))
    stuetzvektor_y_2 = int(input("2. Gleichung: Stützvektor Koordinate y\n> "))
    stuetzvektor_z_2 = int(input("2. Gleichung: Stützvektor Koordinate z\n> "))

    richtungsvektor_x_2 = int(input("2. Gleichung: Richtungsvektor Koordinate x\n> "))
    richtungsvektor_y_2 = int(input("2. Gleichung: Richtungsvektor Koordinate y\n> "))
    richtungsvektor_z_2 = int(input("2. Gleichung: Richtungsvektor Koordinate z\n> "))

    stuetzvektor_1 = StuetzvektorErsteGleichung_2_Geraden(stuetzvektor_x, stuetzvektor_y, stuetzvektor_z)
    richtungsvektor_1 = RichtungsvektorErsteGleichung_2_Geraden(richtungsvektor_x, richtungsvektor_y, richtungsvektor_z)
    stuetzvektor_2 = StuetzvektorZweiteGleichung_2_Geraden(stuetzvektor_x_2, stuetzvektor_y_2, stuetzvektor_z_2)
    richtungsvektor_2 = RichtungsvektorZweiteGleichung_2_Geraden(richtungsvektor_x_2, richtungsvektor_y_2,
                                                                 richtungsvektor_z_2)

    return stuetzvektor_1, stuetzvektor_2, richtungsvektor_1, richtungsvektor_2


def gleichung_aufstellen_schnittpunkt():
    pass


def punktprobe():
    ortsvektor_1_gleichung, stuetzvektor_1_gleichung, richtungsvektor_1_gleichung = abfrage_1_gleichung()
    t = gleichung_aufstellen_punktprobe(ortsvektor_1_gleichung, stuetzvektor_1_gleichung, richtungsvektor_1_gleichung)
    t_vergleichen(t)


if __name__ == '__main__':
    abfrage_allgemein()

# todo: Schnittpunkte berechnen, Lineare Abhängigkeit berechnen
