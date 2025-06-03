
menuMenjar = [] # LLista on guardare els noms del menjar
preuMenu = [] #Llista per els preus
print("Creador de menus")
for valor in range(8): #Optare per un limit de plats que serien 8 
   #Aqui demanare les dades
   menuMenjar.append(input("Quin menjar voleu afegir (8 Plats Maxim): "))
   preuMenu.append(int(input("Preu del  producte: ")))
   
#Aqui junto 2 elements de les 2 llistes per desprès utilitzar-ho en un print 
seleccio1 = str(menuMenjar[0]) + "......" + str(preuMenu[0])
seleccio2 = str(menuMenjar[1]) + "...... "+ str(preuMenu[1])
seleccio3 = str(menuMenjar[2]) + "......" + str(preuMenu[2])
seleccio4 = str(menuMenjar[3]) + "...... "+ str(preuMenu[3])
seleccio5 = str(menuMenjar[4]) + "......" + str(preuMenu[4])
seleccio6 = str(menuMenjar[5]) + "...... "+ str(preuMenu[5])
seleccio7 = str(menuMenjar[6]) + "......" + str(preuMenu[6])
seleccio8 = str(menuMenjar[7]) + "...... "+ str(preuMenu[7])
#Mostro el menu
print("Menu:\n ------------")
print("Selecciona el que vols num(sense el -):")
print("-1" + " " + seleccio1 + "€" )
print("-2" + " " + seleccio2 + "€")
print("-3" + " " + seleccio3 + "€")
print("-4" + " " + seleccio4 + "€")
print("-5" + " " + seleccio5 + "€")
print("-6" + " " + seleccio6 + "€")
print("-7" + " " + seleccio7 + "€")
print("-8" + " " + seleccio8  + "€")
print("-0 Pagar")

aPagar = 0
#Utilitzo un bucle tipus while 
while True:
   aMenjar = int(input("Resposta: "))
   if aMenjar == 0:
      print("Has de pagar:" + str(aPagar) + "€")
      break
   if aMenjar == 1:
      print("D'acord vols" , str(menuMenjar[0]) + "......" + str(preuMenu[0]) )
      aPagar += preuMenu[0] #Aqui sumo amb el preu corresponent del  menjar
   elif aMenjar == 2:
      print("D'acord vols" +  str(menuMenjar[1]) + "......" + str(preuMenu[1]) )
      aPagar += preuMenu[1]
   elif aMenjar == 3:
      print("D'acord vols" +  str(menuMenjar[2]) + "......" + str(preuMenu[2]) )
      aPagar += preuMenu[2]
   elif aMenjar == 4:
      print("D'acord vols" +  str(menuMenjar[3]) + "......" + str(preuMenu[3]) )   
      aPagar += preuMenu[3]
   elif aMenjar == 5:
      aPagar += preuMenu[4]
      print("D'acord vols" +  str(menuMenjar[4]) + "......" + str(preuMenu[4]) )
   elif aMenjar == 6:
      aPagar += preuMenu[5]
      print("D'acord vols" +  str(menuMenjar[5]) + "......" + str(preuMenu[5]) )
   elif aMenjar == 7:
     aPagar += preuMenu[6]
     print("D'acord vols" +  str(menuMenjar[6]) + "......" + str(preuMenu[6]) )
   elif aMenjar == 8:
      aPagar += preuMenu[7]
      print("D'acord vols" +  str(menuMenjar[7]) + "......" + str(preuMenu[7]) )
   

      





