# Fonction pour calculer la somme des nombres
def somme_nombres():
    total = 0
    compteur = 0

    while True:
        # Demander à l'utilisateur d'entrer un nombre
        entree = input("Entrez un nombre  (ou 'stop' pour terminer) : ")

        # Vérifier si l'utilisateur veut arrêter
        if entree.lower() == 'stop':
            break
        
        try:
            # Convertir l'entrée en nombre
            nombre = float(entree)
            total += nombre
            compteur += 1
        except ValueError:
            print("Ce n'est pas un nombre valide. Essayez encore.")

    # Afficher la somme et le nombre de valeurs entrées
    print(f"La somme des {compteur} nombres est : {total}")

# Appeler la fonction
somme_nombres()
