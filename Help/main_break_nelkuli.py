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

    #while 1: //Erre nincs szükség
        #menu_kiiro.Fomenu() // ezek belekerültek a while ciklusba lentebb
        #prompt = ">"
    
    while answer != 'exit':
        menu_kiiro.Fomenu()
        prompt = ">"
        
        answer = input(prompt)
        if answer == 'a':
            fajlbeolvasas.Beolvasas(rekordok)
            volt_betoltes = True
            
            #break // Természetesen ez nem kell

            continue    # Ez lesz ami kell, hogy jó legyen!
        
            ''' Lényegében annyit csinál, hogy ha vissza kapja az értéket a
            változóból akkor tovább megy, de nem viszi magával. Így
            nem marad a memóriában semmi felesleg.'''
            
        elif answer == 'b':
            if volt_betoltes == True:
                 fajl_kiiras.Kiiras(rekordok)
                 
                #break // Természetesen ez nem kell

                 continue    # Ez lesz ami kell, hogy jó legyen!
                
            else:
                print(hiba_uzenet)
        elif answer == 'c':
            if volt_betoltes == True:
                festmeny_hozzaadas.FestményHozzáadás()
                
                #break // Természetesen ez nem kell

                continue    # Ez lesz ami kell, hogy jó legyen!
            
            else:
                print(hiba_uzenet)
        elif answer == 'd':
            if volt_betoltes == True:
                nevkereso_class.Search_name(rekordok)
                
                #break // Természetesen ez nem kell

                continue    # Ez lesz ami kell, hogy jó legyen!
            
            else:
                print(hiba_uzenet)
        elif answer == 'e':
            if volt_betoltes == True:
                stiluskereso_class.Search_style(rekordok)
                
                #break // Természetesen ez nem kell

                continue    # Ez lesz ami kell, hogy jó legyen!
            
            else:
                print(hiba_uzenet)
        elif answer == 'f':
            if volt_betoltes == True:
                statisztika_class.Statisztika(rekordok)
                
                #break // Természetesen ez nem kell

                continue    # Ez lesz ami kell, hogy jó legyen!
            
            else:
                print(hiba_uzenet)
        elif answer == 'exit':
            quit()
            
        #answer = "" // Felesleges, mert az input() miatt várni fog és úgy is felülírja.
    

main()
