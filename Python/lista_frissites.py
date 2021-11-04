import festmenyek_class

class Frissítés:

    def __init__(self, fajl, lista):
        f = open(fajl, "r", encoding='utf-8')
        lista[:] = []
        for sor in f:
            sor = sor[:-1].split(";")
            peldany = festmenyek_class.Festmenyek(sor[0], sor[1], sor[2])
            lista.append(peldany)
        f.close()
        return
















