import festmenyek_class
import lista_frissites

uj_rekordok = []

class FestményHozzáadás:
    def __init__(self, lista):
        prompt = "Szeretne festményt feltölteni? (y/n)\n>"
        answer = input(prompt)
        if answer != 'y':
            print("Ön nem adott meg egyetlenegy festményt sem.\n\n"
                  "A főmenübe való visszatéréshez kérem nyomja meg az entert!")
            input("<< Enter >>")
            return
        else:
            #Adatfeltöltés
            answer = ""
            while answer != 'n':
                prompt = "Kérem adja meg a festmény címét: "
                cim = input(prompt)
                prompt = "Kérem adja meg a festmény értékét: "
                ertek = int(input(prompt))
                prompt = "Kérem adja meg a festmény stílusát: "
                stilus = input(prompt)

                példány = festmenyek_class.Festmenyek(cim, ertek, stilus)
                uj_rekordok.append(példány)
                print("\nA feltöltés sikeresen megtörtént!")

                prompt = "Szeretne újabb festményt feltölteni? (y/n)\n>"
                answer = input(prompt)

            #Felvitt adatok kilistázása
            print("Ön az alábbi adatokat töltötte fel:\n\t" + 30*"-")
            for i in range(len(uj_rekordok)):
                print(uj_rekordok[i].toString())

            #Mentés
            prompt = "\n\nKérem adja meg melyik fájlba szeretné menteni a most feltöltött festményeit:\n>"
            fajl = input(prompt)
            if fajl[-4:] != ".txt":
                fajl = fajl + ".txt"
            f = open(fajl, "a", encoding='utf-8')
            for i in range(len(uj_rekordok)):
                f.write(uj_rekordok[i].toFile())
            f.close()

            #Lista frissítése
            lista_frissites.Frissítés(fajl, lista)

            #Kilépés és üzenet
            print("\nA mentés sikeresen megtörtént!"
                  "A program belső adatbázisa frissült!\n\n"
                  "A főmenübe való visszatéréshez kérem nyomja meg az entert!")
            input("<< Enter >>")
            return
