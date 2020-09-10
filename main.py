import random  #importation de la librairie python random


#variables
choix1, choix2, choix3 = "pierre", "feuille", "ciseaux"

#accueil
print("Bienvenue, veuillez séléctionner un des choix suivant")
print("1- " + choix1)
print("2- " + choix2)
print("3- " + choix3)


#Utilisateur
entree_utilisateur = int(input("Choix: "))
#print(type(entree_utilisateur))
if entree_utilisateur == 1:
	print("Vous avez choisi pierre")
elif entree_utilisateur == 2:
	print("Vous avez choisi feuille")
elif entree_utilisateur == 3:
	print("Vous avez choisi ciseaux")
else:
	print("Votre choix ne fait pas partie des propositions")


#bot
entree_bot = random.randint(1,3)
if entree_bot == 1:
	print("Le bot a choisi la pierre")
elif entree_bot == 2:
	print("Le bot a choisi la feuille")
elif entree_bot == 3:
	print("Le bot a choisi le ciseaux")
else:
	print("erreur")

if ((entree_bot == 1) and (entree_utilisateur == 1)) or ((entree_bot == 2) and (entree_utilisateur == 2)) or ((entree_bot == 3) and (entree_utilisateur == 3)):
	print("manche nul")
elif ((entree_bot == 1) and (entree_utilisateur == 2)) or ((entree_bot == 2) and (entree_utilisateur == 3)) or ((entree_bot == 3) and (entree_utilisateur == 1)):
	print("Vous avez gagne!")
elif ((entree_bot == 1) and (entree_utilisateur == 3)) or ((entree_bot == 2) and (entree_utilisateur == 1)) or ((entree_bot == 3) and (entree_utilisateur == 2)):
	print("Vous avez perdu!")
else:
	print("erreur")