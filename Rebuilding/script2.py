a= int(input("entrer A"))
while (a>0):
    a=int(input("entrer A valeur positif"))
b=int(input("Entrer la valeur de b"))
while(b<0):
    b=int(input("Entrer la valeur de b positif"))
if (a>b):
    c=a
    a=b
    b=c
print(a, b)
if(a==0):
    print("PGCD"(",a," ",b,")
    
