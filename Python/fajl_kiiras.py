import festmenyek_class

class Kiiras:
    def __init__(self, lista):
   
        print("\tA fájl adatai a következők: ")

        for i in range(len(lista)):
              print(lista[i].toString())

        print("\tA főmenübe való visszalépéshez kérem nyomja meg az entert")
        input("<<Enter>>")
        return

