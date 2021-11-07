import udvozles_kiiro
import menu_kiiro
import fajlbeolvasas
import festmeny_hozzaadas
import festmenyek_class
import fajl_kiiras
import nevkereso_class
import statisztika_class
import stiluskereso_class

rekordok = []

def main():
    udvozles_kiiro.Udvozles()
    
    answer = ""
    volt_betoltes = False
    hiba_uzenet = 30*"-" + "\n**Nincs feltöltött fájl még!**\n" + 30*"-"
    
    while answer != 'exit':
        menu_kiiro.Fomenu()
        prompt = ">"
        
        answer = input(prompt)
        if answer == 'a':
            fajlbeolvasas.Beolvasas(rekordok)
            volt_betoltes = True
            continue
            
        elif answer == 'b':
            if volt_betoltes == True:
                 fajl_kiiras.Kiiras(rekordok)
                 continue
            else:
                print(hiba_uzenet)
                
        elif answer == 'c':
            if volt_betoltes == True:
                festmeny_hozzaadas.FestményHozzáadás(rekordok)
                continue
            else:
                print(hiba_uzenet)
                
        elif answer == 'd':
            if volt_betoltes == True:
                nevkereso_class.Search_name(rekordok)
                continue
            else:
                print(hiba_uzenet)
                
        elif answer == 'e':
            if volt_betoltes == True:
                stiluskereso_class.Search_style(rekordok)
                continue
            else:
                print(hiba_uzenet)
                
        elif answer == 'f':
            if volt_betoltes == True:
                statisztika_class.Statisztika(rekordok)
                continue
            else:
                print(hiba_uzenet)
                
        elif answer == 'exit':
            quit()
    

main()
