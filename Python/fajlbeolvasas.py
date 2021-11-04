import festmenyek_class

class Beolvasas:

    def __init__(self, lista):
        fajl = input("Kérem a fájl nevét: ")
        if fajl[-4:] != ".txt":
                fajl = fajl + ".txt"
        self.inputFile(fajl, lista)
        print("\tA fájl beolvasása ... kész!")
        input("<< Enter >>")
        return
        
    

    def inputFile(self, fajl, lista):
        f = open(fajl, "r", encoding='utf-8')
        lista[:] = []
        for sor in f:
            sor=sor[:-1].split(";")
            peldany = festmenyek_class.Festmenyek(sor[0],sor[1],sor[2])
            lista.append(peldany)
        f.close()
        return


