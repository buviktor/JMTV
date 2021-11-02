import festmenyek_class

class Beolvasas:

    def __init__(self, lista):
        self.lista = lista
        self.fajl = input("Kérem a fájl nevét: ")
        if self.fajl[-4:] != ".txt":
                self.fajl = self.fajl + ".txt"
        self.inputFile()
        print("\tA fájl beolvasása ... kész!")
        input("<< Enter >>")
        return
        
    

    def inputFile(self):
        f = open(self.fajl, "r", encoding='utf-8')
        self.lista[:] = []
        for sor in f:
            sor=sor[:-1].split(";")
            peldany = festmenyek_class.Festmenyek(sor[0],sor[1],sor[2])
            self.lista.append(peldany)
        f.close()
        return


