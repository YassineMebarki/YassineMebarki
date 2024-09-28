#Demander a l'utilisateur d'entrer les valeurs

a=float(input("Saisissez la valeur de A: "))
b=float(input("\nSaisissez la valeur de B: "))
c=float(input("\nSaisissez la valeur de C: "))

#Affichage des valeurs avant le changement

print(" Voici les valeurs avant l'echange")

print("\n A: ",a)
print("\n B: ",b)
print("\n C: ",c)

#Echange et affichage

temp = a
a  = c
c = b
b = temp


##Affichage

print(" Voici les valeurs apres l'echange")

print("\n A: ",a)
print("\n B: ",b)
print("\n C: ",c)
