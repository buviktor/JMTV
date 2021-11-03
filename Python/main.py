import udvozles_kiiro
import menu_kiiro
import fajlbeolvasas
import festmeny_hozzaadas
import festmenyek_class
import fajl_kiiras
import nevkereso_class
import statisztika_class

rekordok = []

def main():
    udvozles_kiiro.Udvozles()
    
    answer = ""
    volt_betoltes = False
    hiba_uzenet = 30*"-" + "\n**Nincs feltöltött fájl még!**\n" + 30*"-"

    while 1:
        menu_kiiro.Fomenu()
        prompt = ">"
        while answer != 'exit':
            answer = input(prompt)
            if answer == 'a':
                fajlbeolvasas.Beolvasas(rekordok)
                volt_betoltes = True
                break
            elif answer == 'b':
                if volt_betoltes == True:
                    fajl_kiiras.Kiiras(rekordok)
                    break
                else:
                    print(hiba_uzenet)
            elif answer == 'c':
                if volt_betoltes == True:
                    festmeny_hozzaadas.FestményHozzáadás()
                    break
                else:
                    print(hiba_uzenet)
            elif answer == 'd':
                if volt_betoltes == True:
                    nevkereso_class.Search_name(rekordok)
                    break
                else:
                    print(hiba_uzenet)
            #elif answer == 'e':
                #if volt_betoltes == True:
                #else:
                    #print(hiba_uzenet)
            elif answer == 'f':
                if volt_betoltes == True:
                    statisztika_class.Statisztika(rekordok)
                    break
                else:
                    print(hiba_uzenet)
            elif answer == 'exit':
                quit()
            answer = ""
    



main()
