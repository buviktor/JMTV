import festmenyek_class

class Search_name:
	
    def __init__ (self, lista):
        txt = "\nÜdvözöllek a Névkeresőben!\n"
        print(txt)	
        answer = ""
        
        while answer != 'n':
            prompt = "A keresett festmény: "
            name = input(prompt)
            print("\t" + 30*"-")
            van_talalat = False
			
            for i in range (len(lista)):
                if name == lista[i].cim:
                    print(lista[i].toString())
                    van_talalat = True
                    
            if van_talalat == False:
                hibas = "Ilyen festmény nem létezik!"
                print(hibas)
                
            prompt = "Szeretne újból keresni? (y/n)\n>"
            answer = input(prompt)
            
        print("\nA főmenübe való visszatéréshez kérem nyomja meg az entert!")
        input("<< Enter >>")
        
        return
