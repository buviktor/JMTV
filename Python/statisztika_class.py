import festmenyek_class

class Statisztika:
    def __init__(self, lista):
        self.lista = lista
        ertekek = []
        print("Statisztika a feltöltött festményekről:\n")
        for i in range(len(lista)):
            ertekek.append(lista[i].ertek)
        print("\nA legdrágább festmény(ek):")
        for i in range(len(lista)):
            if max(ertekek) == lista[i].ertek:
                print("\t" + lista[i].toString)
        print("\nA legolcsóbb festmény(ek):")
        for i in range(len(lista)):
            if min(ertekek) == lista[i].ertek:
                print("\t" + lista[i].toString)
        print("\nA festmények átlagértéke:", str(sum(ertekek)/len-(ertekek))
        return






