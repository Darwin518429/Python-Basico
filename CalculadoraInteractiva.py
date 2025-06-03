
#Variables per utilitzar les condicionals
suma = "+"
resta = "-"
multi = "x" 
dividir = "/"
residuo = "%"
# He utilitzat while per fer un bucle.
while True:
    num1 = int(input("NUMERO 1: ")) #Demana primer valor 
    num2 = int(input("NUMERO 2: ")) #Demana segon valor
    signeOperacio = input("Que signe de operació faras servir?: ") #demana el signe
    #condicionals
    #Quan compleix aquestes algunes de les condicions (break) fara que sorti del bucle.
    if signeOperacio == suma :
        print(num1 + num2)
        break 
    elif signeOperacio == resta:
        print(num1 - num2)
        break
    elif signeOperacio == multi:
        print(num1 * num2)
        break
    elif signeOperacio == dividir:
        print(num1 / num2)
        break
    elif signeOperacio == residuo:
        print(num1 % num2)
        break
    else:
        print("Mal repita")
        
    