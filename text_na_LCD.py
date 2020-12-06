from gpio import *
from time import *

def main():
	text = "Dnes neni pekne, protoze musime programovat" #Základní zadání textu
	znak = "*" * 13
	text = znak + text 		#Přidávání mezer
	vypis = "" 				#Část textu k vypsání
	zacatek = 0				#Slouží k nastavení začátku indexu
	
	pinMode(0, OUT)
	print("Zapnuto.")
	while True:
		
		for pricitani in range(0, len(text)):
			for i in range(0,13):
				if i+pricitani >= len(text): #Kontrola maximálního indexu
					vypis = vypis + text[zacatek]
					zacatek += 1
				else:
					vypis = vypis + text[i+pricitani] 
					zacatek = 0
					
			customWrite(0, vypis)
			vypis = ""
			delay(200)
if __name__ == "__main__":
	main()
