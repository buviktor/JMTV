import festmenyek_class

class Search_style:
	
    def __init__ (self, lista):
            
        if 0 == len(lista):
            txt = "Nincs betöltött fájl! Kérlek válassz egy fájlt a Főmenüben."
            print(txt)
            txt = "Kérlek nyomj ENTER-t  a vissza lépéshez!"
            input(txt)
            return 
           
        txt = "\nÜdvözöllek a Stíluskeresőben!"
        print(txt)
		
        self.a = 0
        self.answer = 'y'
		
        while self.answer != 'n':
            Search_style.function(self, lista)
            Search_style.question(self, lista)
            
        return
        
    def question(self, lista):
    
        txt = "\nSzeretne újból keresni? (y/n)\n>"
        self.answer = input(txt).lower()
        
        return
        
		
    def function(self, lista):
        
        txt = "\nA keresett stílus: "
        name = input(txt)
			
        for i in range (len(lista)):
        
            if name.lower() == lista[i].stilus.lower():
                print("\n\t" + 30*"-" + "\n" + lista[i].toString())
                self.a += 1
                
        if self.a == 0:
            txt = "\nNincs ilyen stílusu festmény!"
            print(txt)
            self.a = 0
           
        self.a = 0
        return

