import festmenyek_class

class Search_name:
	
    def __init__ (self, lista):
            
        if 0 == len(lista):
            self.txt = "\tNincs betöltött fájl! Kérlek válassz egy fájlt a Főmenüben."
            print(self.txt)
            self.txt = "\tKérlek nyomj ENTER-t  a vissza lépéshez!"
            input(self.txt)
            return 
           
        self.txt = "\n\tÜdvözöllek a Névkeresőben!\n"
        print(self.txt)
		
        self.b = 0
		
        Search_name.ciklus(self, lista)
        Search_name.question(self, lista)
        return
        
    def question(self, lista):
        self.txt = "Szeretne újból keresni? (y/n)\n>"
        self.answer = input(self.txt)
        
        if self.answer == 'y':
            Search_name.ciklus(self, lista)
        else:
            return
        
		
    def ciklus(self, lista):
        
        self.txt = "\t A keresett festmény: "
        self.name = str(input(self.txt))
			
        for i in range (len(lista)):
            if self.name == lista[i].cim:
                print(lista[i].toString())
                Search_name.question(self, lista)
            else:
                self.hibas = "Ilyen festmény nem létezik!"
                print(self.hibas)
                # self.b = 0
                # Search_name.question(self, lista)
                return

