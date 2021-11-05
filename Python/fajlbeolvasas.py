import festmenyek_class
import os

fajlok = []

class Beolvasas:

    def __init__(self, lista):
        fajl = input("Kérem a fájl nevét: ")
        
        while 1:
        
            if fajl[-4:] != ".txt":
                    fajl = fajl + ".txt"
            
            files = os.listdir(path='.')
            for e in files:
                parts = e.split('.')
                fname = parts[0]
                ext = parts[-1]
                if ext == 'txt':
                    fajlok.append(fname + '.' + ext)
                    
            for delete in range (len(fajlok)):
                if fajlok[delete] == 'Readme.txt':
                    del fajlok[delete]
            for d in range (len(fajlok)):
                if fajl == fajlok[d]:
                    fajlok.clear()
                    
                    self.inputFile(fajl, lista)
                    print("\tA fájl beolvasása ... kész!")
                    input("<< Enter >>")
                    return
            
            print("\nNincs ilyen nevű festmény!\nKérlek válasz az alábbi fájlok közül:\n")
            for i in range (len(fajlok)):
                print("\t" + fajlok[i])
            fajlok.clear()
            fajl = input("\nKérem a fájl nevét: ")
    

    def inputFile(self, fajl, lista):
        f = open(fajl, "r", encoding='utf-8')
        lista[:] = []
        for sor in f:
            sor=sor[:-1].split(";")
            peldany = festmenyek_class.Festmenyek(sor[0],sor[1],sor[2])
            lista.append(peldany)
        f.close()
        return


