import festmenyek_class

class Search_name:
	
    def __init__ (self, lista):
            
        if 0 == len(lista):
            txt = "Nincs betöltött fájl! Kérlek válassz egy fájlt a Főmenüben."
            print(txt)
            txt = "Kérlek nyomj ENTER-t  a vissza lépéshez!"
            input(txt)
            return 
           
        txt = "\nÜdvözöllek a Névkeresőben!"
        print(txt)
		
        self.a = 0
        self.answer = 'y'
		
        while self.answer != 'n':
            Search_name.function(self, lista)
            Search_name.question(self, lista)
            
        print("A főmenübe való visszalépéshez kérem nyomja meg az enter")
        input("<<Enter>>")
        return
        
    def question(self, lista):
    
        txt = "\nSzeretne újból keresni? (y/n)\n>"
        self.answer = input(txt).lower()
        
        return
        
		
    def function(self, lista):
        
        txt = "\nA keresett festmény: "
        name = input(txt)
			
        for i in range (len(lista)):
        
            if name.lower() == lista[i].cim.lower():
                print("\n\t" + 30*"-" + "\n" + lista[i].toString())
                return
            else:
                self.a += 1
                
        if self.a > 0:
            txt = "\nNincs ilyen nevű festmény!"
            print(txt)
            self.a = 0
            
        return

