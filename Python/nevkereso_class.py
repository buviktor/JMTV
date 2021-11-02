import fajlbeolvasas

class Search_name:
	
	def __init__ (self):
		
		if 0 == len(Search_name.proba):
			self.txt = "\tNincs betöltött fájl! Kérlek válassz egy fájlt a Főmenüben."
			print(self.txt)
			self.txt = "\tKérlek nyomj ENTER-t  a vissza lépéshez!"
			input(self.txt)
			return fomenu
		
		self.txt = "\n\tÜdvözöllek a Névkeresőben!\n"
		print(self.txt)
		
		self.ciklus_n = True
		self.i = 0
		self.b = 0
		
		Search_name.ciklus(self)
		
	def question(self):
		print("OK")
		return Search_name.ciklus(self)
		
	def ciklus(self):
	
		self.txt = "\t A keresett festmény: "
		self.name = str(input(self.txt))
		
		while self.ciklus_n == True:
			self.i += 1
			
			for x in range (len(Search_name.proba)):
				if self.name == Search_name.proba[x]:
					self.txt = "\t   <lista ára és stílusa> \n"
					print(self.txt)
					return Search_name.question(self)
				else:
					self.b += 1

			if self.b > 0:
				self.txt = "nincs ilyen a listában!"
				print(self.txt)
				return Search_name.question(self)

Search_name()
input("<<Enter>>")
