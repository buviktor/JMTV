class Festmenyek:
    def __init__(self, cim, ertek, stilus):
        self.cim = cim
        self.ertek = int(ertek)
        self.stilus = stilus

    def toString(self):
        txt ="\tFestmény címe: "+self.cim +"\n\tÉrtéke: "+ str(self.ertek)+ " Ft" + "\n\tStílusa: "+self.stilus+"\n\t"
        txt = txt + 30*"-"
        return txt

    def toFile(self):
        txt = self.cim + ";" + self.ertek + ";" + self.stilus + "\n"
        return txt









