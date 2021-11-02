import festmenyek_class

class Kiiras:
    def __init__(self, lista):
   
        print("A fájl adatai a következők: ")

        for i in range(len(lista)):
              print(lista[i].toString())

        print("A főmenübe való visszalépéshez kérem nyomja meg az entert")
        input("<<Enter>>")
        return

