import festmenyek_class

class Statisztika:
    def __init__(self, lista):
        self.lista = lista
        ertekek = []

        print("Statisztika a feltöltött festményekről:\n")
        for i in range(len(lista)):
            ertekek.append(lista[i].ertek)

        print("\nA legdrágább festmény(ek):")
        for i in range(len(self.lista)):
            if max(ertekek) == self.lista[i].ertek:
                print(self.lista[i].toString())

        print("\nA legolcsóbb festmény(ek):")
        for i in range(len(self.lista)):
            if min(ertekek) == self.lista[i].ertek:
                print(self.lista[i].toString())

        print("\nA festmények átlagértéke:", str(sum(ertekek)/len(ertekek)), "Ft"
        print("A főmenübe való visszalépéshez kérem nyomja meg az enter")
        input("<<Enter>>")
        return






