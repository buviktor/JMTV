import festmenyek_class

class Search_name:
	
    def __init__ (self, lista):
            
        if 0 == len(lista):
            self.txt = "Nincs betöltött fájl! Kérlek válassz egy fájlt a Főmenüben."
            print(self.txt)
            self.txt = "Kérlek nyomj ENTER-t  a vissza lépéshez!"
            input(self.txt)
            return 
           
        self.txt = "\nÜdvözöllek a Névkeresőben!"
        print(self.txt)
		
        self.a = 0
        self.answer = 'y'
		
        while self.answer != 'n':
            Search_name.ciklus(self, lista)
            Search_name.question(self, lista)
            
        return
        
    def question(self, lista):
    
        self.txt = "\nSzeretne újból keresni? (y/n)\n>"
        self.answer = input(self.txt).lower()
        
        return
        
		
    def ciklus(self, lista):
        
        self.txt = "\nA keresett festmény: "
        name = input(self.txt)
			
        for i in range (len(lista)):
        
            if name.lower() == lista[i].cim.lower():
                print("\n\t" + 30*"-" + "\n" + lista[i].toString())
                return
            else:
                self.a += 1
                
        if self.a > 0:
            self.txt = "\nNincs ilyen nevű festmény!"
            print(self.txt)
            self.a = 0
            
        return

