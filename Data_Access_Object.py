import random

""" BLOOMING GAME

Definition des classes."""
# classe reve.
class Reve:
	def __init__(self):
		self.description = ""
		self.prix = 0
		self.choisir_un_reve()

	def choisir_un_reve(self):
		# Ouverture du fichier.
		with open("reves.txt","r") as fic:
			liste_de_reves = fic.readlines()
		choix_ligne = random.choice(liste_de_reves)
		choix_ligne = choix_ligne.rstrip(choix_ligne[-1]) # enleves le carctere de fin de chaine(\n) dans la chaine choix_ligne		
		nouvelle_liste = choix_ligne.split("|")
		self.description = nouvelle_liste[0]
		self.prix = nouvelle_liste[1]
		return nouvelle_liste

# classe carte_doodads.
class Doodads:
	def __init__(self):
		self.description = ""
		self.prix = 0
		self.Generer_doodads()

	def Generer_doodads(self):
		with open("Doodads.txt","r") as fich_doodads:
			liste_doodads = fich_doodads.readlines()
		choix_doodads = random.choice(liste_doodads) 
		choix_doodads = choix_doodads.rstrip(choix_doodads[-1]) # cette ligne permet de supprimer le dernier element de la chaine contenant la description et le prix.
		nouvelle_liste_doodads = choix_doodads.split("|")
		self.description = nouvelle_liste_doodads[0]
		self.prix = int(nouvelle_liste_doodads[1])
		return nouvelle_liste_doodads



# classe operation
class Operation():
	def __init__(self, nom, prix, description):
		self.nom = nom
		self.prix = prix
		self.description =  description

# classe profession
class Profession:
	def __init__(self):
		self.nom = ""
		self.salaire = 0
		self.coef = 0.2
		self.montant_a_atteindre = 0
		self.Afficher_Profession()

	def Afficher_Profession(self):
		# Ouverture du fichier profession.
		with open("profession.txt","r") as fic:
			liste_de_professions = fic.readlines()
		choix_ligne = random.choice(liste_de_professions)
		choix_ligne = choix_ligne.rstrip(choix_ligne[-1]) # enleves le carctere de fin de chaine(\n) dans la chaine choix_ligne
		nouvelle_liste = choix_ligne.split("|")
		salaire =  int(nouvelle_liste[1])
		self.nom = nouvelle_liste[0]
		self.salaire = salaire
		self.montant_a_atteindre = nouvelle_liste[2]
		return nouvelle_liste

# classe carte
class Cartes():
	def __init__ (self):
		self.nom = ""
		self.description = ""
		self.cout = 0
		self.cashflow = 0

	def Generer_big_opportunite_carte(self): # fonction permettant de prendre une action\investissement_big aleatoirement dans un fichier
		nombre = [1,2]
		if(random.choice(nombre) == 1):
			with open("Action_big.txt","r") as Ab:
				liste_actions_big = Ab.readlines()
			choix_ligne_Ab = random.choice(liste_actions_big)
			choix_ligne_Ab = choix_ligne_Ab.rstrip(choix_ligne_Ab[-1])
			ligne_splitee = choix_ligne_Ab.split("|")
			Cartes.nom = ligne_splitee[0]
			Cartes.description = ligne_splitee[1] 
			Cartes.cout = ligne_splitee[2]
			Cartes.cashflow = ligne_splitee[3]
			return ligne_splitee
		else:
			with open("invest_big.txt","r") as Ib:
				liste_invest_big = Ib.readlines()
			choix_ligne_Ib = random.choice(liste_invest_big)
			choix_ligne_Ib = choix_ligne_Ib.rstrip(choix_ligne_Ib[-1])
			ligne_splitee = choix_ligne_Ib.split("|")
			Cartes.nom = ligne_splitee[0]
			Cartes.description = ligne_splitee[1] 
			Cartes.cout = ligne_splitee[2]
			Cartes.cashflow = ligne_splitee[3]
			return ligne_splitee
	
	def Generer_small_opportunite_carte(self): # fonction permettant de prendre une action\investissement_small aleatoirement dans un fichier
		nombre = [1,2]
		if(random.choice(nombre) == 1):
			with open("Action_small.txt","r") as AS:
				liste_actions_small = AS.readlines()
			choix_ligne_AS = random.choice(liste_actions_small)
			choix_ligne_AS = choix_ligne_AS.rstrip(choix_ligne_AS[-1])
			ligne_splitee = choix_ligne_AS.split("|")
			Cartes.nom = ligne_splitee[0]
			Cartes.description = ligne_splitee[1] 
			Cartes.cout = ligne_splitee[2]
			Cartes.cashflow = ligne_splitee[3]
			return ligne_splitee
		else:
			with open("invest_small.txt","r") as IS:
				liste_invest_small = IS.readlines()
			choix_ligne_IS = random.choice(liste_invest_small)
			choix_ligne_IS = choix_ligne_IS.rstrip(choix_ligne_IS[-1])
			ligne_splitee = choix_ligne_IS.split("|")
			Cartes.nom = ligne_splitee[0]
			Cartes.description = ligne_splitee[1] 
			Cartes.cout = ligne_splitee[2]
			Cartes.cashflow = ligne_splitee[3]
			return ligne_splitee

# classe des cartes investissements/actions small deals qui heritent de la classe carte
class Small_carte(Cartes):
	def __init__ (self):
		Cartes.__init__(self) # appel des attributs et methodes de la classe carte

# classe des cartes actions/investissement big deals qui heritent de la classe carte
class Big_carte(Cartes):
	def __init__ (self):
		Cartes.__init__(self) # appel des attributs de la classe carte et methodes
	
# classe partie
class Partie():
	def __init__(self): # dans toutes  les parties un joueur ne peut avoir que 5 bebes.
		self.nom_partie = ""
		self.nb_bebes = 5

# classe Biens
class Biens():
	def __init__(self):
		self.nom = ""
		self.nombre = 0
		self.cout = 0
		self.cashflow = 0

# classe personne
class Personne():
	def __init__(self):
		self.nom_personne = ""


# classe joueur (HERITE DE PERSONNE)
class Joueur(Personne):
	# Attribut de classe
	def __init__(self):
		Personne.__init__(self) # appel des attributs de la classe Personne()
		self.profession = Profession()
		self.depenses_standards = 0
		self.depenses_bebe = 0
		self.pourcentages_dettes = 0 
		self.dettes = 0
		self.liste_biens = []
		self.cash_hand = 0
		self.revenus_passifs = 0
		self.payday = 0

# classe pion
class Token():
	def __init__(self):
		self.liste_positions_rat_race = [(380,400),(360,360),(350,320),(350,280),(360,240),(380,200),(410,170),(440,140),(480,120),(530,130),(570,150),(600,180),(640,200),(650,240),(660,280),(670,320),(650,360),(640,400),(600,420),(570,450),(530,470),(490,460),(440,460),(410,430)] # liste des positions du token dans la rat race
		self.position_actuelle = 0

	def Deplacement_du_pion(self,position_du_token,taille,resultat_lance):
		if(resultat_lance + position_du_token > taille-1):
			position_du_token = resultat_lance + position_du_token - taille
		else:
			position_du_token = position_du_token + resultat_lance
		self.position_actuelle = position_du_token
		return position_du_token
	
















