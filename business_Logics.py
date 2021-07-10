from PyQt5 import QtWidgets # importation du package QWidget pour afficher les interfaces
from PyQt5.QtWidgets import * # importation des elements necessaires pour l'aaffichage des interfaces
from user_interface import Ui_MainWindow # importation de la classe contenant toutes les interfaces graphiques.
from Data_Access_Object import * # importation du fichier algorithmes contenant les classes et les methodes qui seront executees derriere les boutons.
import random # importation du module permettant de faire les choix aleatoires
import sys # importation...


class Les_actions(QMainWindow): # je definie la classe qui contiendra toutes les methodes derrieres les boutons et les interactions
	def __init__(self):
		super(Les_actions,self).__init__() # appel des attirbuts et methodes des classes parents de (Les_actions)
		self.userInterface = Ui_MainWindow() # j'instancie la classe contenant toutes les interfaces pour pouvoir manipuler ces interfaces dans ce fichier .py
		self.userInterface.setupUi(self) # j'appele sa methode permettant d'afficher les elements dans l'ordre standard.
		self.userInterface.bouton_creer_partie.clicked.connect(lambda: self.userInterface.stackedWidget.setCurrentIndex(3)) # je definie une fonction lambda qui permettra de changer l'index de la page courante(page_accceuil) pour mettre celle de la page me permettant de creer une partie(enreg_partie index = ).
		self.userInterface.appuyer_et_creer.clicked.connect(lambda: self.Recuperer_valeur_QTextEdit())# je definie une fonction lambda qui permettra de changer l'index de la page courante(enreg_partie) pour mettre celle de la page me permettant de lancer la partie(interface de validation)
		self.userInterface.boutton_lancer_la_partie.clicked.connect(lambda: self.userInterface.stackedWidget.setCurrentIndex(5))# je definie une fonction lambda qui permettra de changer l'index de la page courante(interface de validation) pour mettre celle de l'espace de jeu(index=5)
		self.reve = Reve() # j'instancie ma classe reve
		self.partie_en_cours = Partie() # J'instancie la classe Partie
		self.un_doodads = Doodads() # j'instancie ma classe doodads.
		self.joueur_courant = Joueur() # j'instancie ma classe joueur
		self.Definir_le_reve()  # j'apelle la fonction qui va ecrire le reve sur l'interface de la carte de choix du reve
		self.Definir_la_profession() # j'appelle la fonction qui va enregistrer la profession et ecrire sur l'interface de l'etat financier et sur l'interface de la carte de choix de reve
		self.Definir_un_joueur() # J'appelle egalement la fonction qui permettra de definir les proprietes du joueur courant
		self.smalldeal = Small_carte() # j'instancie la classe permettant d'executer les small deals(investissements ou actions)
		self.bigdeal = Big_carte() # j'instancie la classe permettant d'executer les bigs deals(investissements ou actions)
		self.pion = Token()# j'instancie la classe du pion
		self.montant_emprunt = 0 # j'initialise la variable qui va contenir le montant de l'emprunt a 0
		self.mois = 0 #variable qui stocke le nombre de mois au quel nous sommes.
		self.ancienne_position = 0 # variable qui va contenir l'ancienne position du token.
		self.numero_bien = 0 # variable qui stocke en fait le nombre de ligne de l'espace bien dans l'interface de bien pour me dire ou placer le nouveau bien du joueur
		self.userInterface.choisir_smalldeal.clicked.connect(lambda: self.userInterface.stack_des_cartes_de_jeu.setCurrentIndex(13)) # je change l'index de la page pour afficher celle de l'interface smalldeal
		self.userInterface.passer_sur_marche.clicked.connect(lambda: self.userInterface.stack_des_cartes_de_jeu.setCurrentIndex(3)) # je change l'index de la page pour afficher celle de l'interface du lance du de sil decide de ne pas vendre.
		self.userInterface.choisir_bigdeal.clicked.connect(lambda: self.userInterface.stack_des_cartes_de_jeu.setCurrentIndex(12)) # je change l'index de la page pour afficher celle de l'interface bigdeal
		self.userInterface.payer_le_chomage.clicked.connect(lambda: self.Gerer_chomage()) # j'execute la fonction permettant de mettre le cash hand du joueur chaque fois qu'on appuie sur le payer le chomage.
		self.userInterface.ok_chomage_transit.clicked.connect(lambda: self.userInterface.stack_des_cartes_de_jeu.setCurrentIndex(3)) # je change maintenant l'index de la page pour afficher celle permettant de relancer le de
		self.userInterface.Valid_emprunt_chomage_cash_inf.clicked.connect(lambda: self.Emprunt_obligatoire_doodad()) # j'appelle la fonction qui permettra de faire un pret obligatoire au joueur pour lui permettre de faire le chomage
		self.userInterface.ok_chom_confirm_emprunt.clicked.connect(lambda: self.userInterface.stack_des_cartes_de_jeu.setCurrentIndex(3)) # je change maintenant l'index de la page pour afficher celle permettant de relancer le de comme il bien payer son downsized
		self.userInterface.etatfinancier.clicked.connect(lambda: self.userInterface.stackedWidget.setCurrentIndex(1)) # je definie une fonction lambda qui permettra de changer l'index de la page courante(espace de jeu) pour mettre celle de l'etat financier(index=1)
		self.userInterface.emprunter.clicked.connect(lambda: self.userInterface.stack_des_cartes_de_jeu.setCurrentIndex(1)) # je definie une fonction lambda qui permettra de changer l'index de la page courante(espace choix reve) pour mettre celle de l'emprunt dans la stac des cartes de jeu(index=1)
		self.userInterface.rembourser.clicked.connect(lambda: self.userInterface.stack_des_cartes_de_jeu.setCurrentIndex(2)) # je definie une fonction lambda qui permettra de changer l'index de la page courante(espace choix reve) pour mettre celle de remboursement dans la stac des cartes de jeu(index=2)
		self.userInterface.boutton_retour.clicked.connect(lambda: self.userInterface.stackedWidget.setCurrentIndex(5))# je definie une fonction lambda qui permettra de changer l'index de la page courante(etat financier) pour mettre celle de l'espace de jeu(index=5)
		self.userInterface.quitterlejeu.clicked.connect(lambda: self.userInterface.stackedWidget.setCurrentIndex(0))# je definie une fonction lambda qui permettra de changer l'index de la page courante(espace de jeu) pour mettre l'interface de quitter la partie(index=0)
		self.userInterface.choisirlereve.clicked.connect(lambda: self.userInterface.stack_des_cartes_de_jeu.setCurrentIndex(3))# je definie une fonction lambda qui permettra de changer l'index de la page courante(espace choix du reve) pour mettre l'interface de lancer du de(index=3)
		self.userInterface.ok_opp_invest_cash_inf.clicked.connect(lambda: self.userInterface.stack_des_cartes_de_jeu.setCurrentIndex(3))# je definie une fonction lambda qui permettra de changer l'index de la page courante(espace de l'interface lui disant qu'il n'a pas d'argent pour investir) pour mettre l'interface de lancer du de(index=3)
		self.userInterface.zapper_arriere.clicked.connect(lambda : self.Definir_le_reve()) # j'excute la fonction qui permet de definir un reve a chaque fois qu'on appuie sur le bouton zapper
		self.userInterface.zapper_avant.clicked.connect(lambda: self.Definir_le_reve()) # j'excute la fonction qui permet de definir un reve a chaque fois qu'on appuie sur le bouton zapper
		self.userInterface.lancer_le_de.clicked.connect(lambda: self.Lancer_le_de()) # j'excute la fonction qui permet de choisir un espace daleatoirement a chaque fois qu'on appuie sur le bouton lancer le de
		self.userInterface.decaisser.clicked.connect(lambda: self.Gerer_le_paychek()) # j'excute la fonction qui permet de mettre le cash hand du joueur a jour a chaque fois qu'on appuie sur le bouton decaisser
		self.userInterface.valider_emprunt.clicked.connect(lambda: self.Executer_emprunt()) # j'excute la fonction qui permet de mettre le cash hand du joueur a jour et le reste de ses attributs (pourcentages de dettes, dettes et depenmses totales sur l'interface de l'etat financier)a chaque fois qu'on appuie sur le bouton emprunt 
		self.userInterface.payer_le_doodads.clicked.connect(lambda: self.Gerer_doodads()) # j'excute la fonction qui permet de mettre le cash hand du joueur a jour(decrementer du prix du doodad) a chaque fois qu'on appuie sur le bouton payer  
		self.userInterface.ok_paycheck_transit.clicked.connect(lambda: self.userInterface.stack_des_cartes_de_jeu.setCurrentIndex(3)) # je definie la fonction qui permettra de revenir sur l'interface lancer le de une fois qu'il a decaisse son salaire
		self.userInterface.ok_doodad_transit.clicked.connect(lambda: self.userInterface.stack_des_cartes_de_jeu.setCurrentIndex(3)) # je definie la fonction qui permettra de revenir sur l'interface lancer le de une fois qu'il a clique sur ok
		self.userInterface.passer_sur_paycheck.clicked.connect(lambda: self.userInterface.stack_des_cartes_de_jeu.setCurrentIndex(3)) # je definie la fonction qui permettra de revenir sur l'interface lancer le de s'il refuse de decaisser son salaire.
		self.userInterface.ok_emprunt_transit.clicked.connect(lambda: self.userInterface.stack_des_cartes_de_jeu.setCurrentIndex(3)) # je definie la fonction qui permettra de revenir sur l'interface lancer le de une fois qu'il clique sur ok.
		self.userInterface.ok_remboursement_transit.clicked.connect(lambda: self.userInterface.stack_des_cartes_de_jeu.setCurrentIndex(3)) # je definie la fonction qui permettra de revenir sur l'interface lancer le de une fois qu'il clique sur ok.
		self.userInterface.valider_le_remboursement.clicked.connect(lambda: self.Rembourser()) # j'appele la fonction qui permet de mettre les informations du joueur a jour quand il valide le remboursement
		self.userInterface.passerlesmalldeal.clicked.connect(lambda: self.userInterface.stack_des_cartes_de_jeu.setCurrentIndex(3)) # cliquer pour passer sur le small_deal
		self.userInterface.passerlebigdeal.clicked.connect(lambda: self.userInterface.stack_des_cartes_de_jeu.setCurrentIndex(3)) # cliquer pour passer sur le big_deal
		self.userInterface.valid_emprunt_doodad_caash_inf.clicked.connect(lambda: self.Emprunt_obligatoire_doodad()) # fonction permettant de faire un pret obligatoi re au joueur pour lui permettre de faire le doodad
		self.userInterface.valider_le_bebe.clicked.connect(lambda: self.Avoir_un_nouveau_bebe()) # j'excute la fonction qui permet de mettre le cheque de paie du joueur a jour  et egalement d'ajouter 25000 sur ses depenses totales a chaque fois qu'on appuie sur le bouton valider
		self.userInterface.ok_bebe_transit.clicked.connect(lambda: self.userInterface.stack_des_cartes_de_jeu.setCurrentIndex(3)) # je definie la fonction qui permettra de revenir sur l'interface lancer le de une fois qu'il clique sur ok.
		self.userInterface.ok_opp_validation.clicked.connect(lambda: self.userInterface.stack_des_cartes_de_jeu.setCurrentIndex(3)) # je definie la fonction qui permettra de revenir sur l'interface lancer le de une fois qu'il clique sur ok.
		self.userInterface.acheterlebigdeal.clicked.connect(lambda: self.Payer_big_deal())# j'appele la fonction permettant d'executer les actions lorsque le joueur decide de payer le big deal(cliquer sur payer)
		self.userInterface.acheterlesmalldeal.clicked.connect(lambda: self.Payer_small_deal())# j'appele la fonction permettant d'executer les actions lorsque le joueur decide de payer le small deal(cliquer sur payer)
		self.userInterface.ok_remboursement_cah_inf.clicked.connect(lambda: self.userInterface.stack_des_cartes_de_jeu.setCurrentIndex(3)) # je definie la fonction qui permettra de revenir sur l'interface lancer le de une fois qu'il clique sur ok.
		self.userInterface.ok_remboursement_mont_sup.clicked.connect(lambda: self.userInterface.stack_des_cartes_de_jeu.setCurrentIndex(3)) # je definie la fonction qui permettra de revenir sur l'interface lancer le de une fois qu'il clique sur ok.
		self.userInterface.ok_auc_dette.clicked.connect(lambda: self.userInterface.stack_des_cartes_de_jeu.setCurrentIndex(3)) # je definie la fonction qui permettra de revenir sur l'interface lancer le de une fois qu'il clique sur ok.
		self.userInterface.faire_la_charite.clicked.connect(lambda: self.Gerer_la_charite()) # je definie la fonction qui permettra d'appeler la fonction qui gere la charite
		self.userInterface.passer_sur_charite.clicked.connect(lambda: self.userInterface.stack_des_cartes_de_jeu.setCurrentIndex(3)) # je definie la fonction qui permettra de revenir sur l'interface lancer le de s'il refuse de faire la charite
		self.userInterface.ok_charite_transit.clicked.connect(lambda: self.userInterface.stack_des_cartes_de_jeu.setCurrentIndex(3)) # je definie la fonction qui permettra de revenir sur l'interface lancer le de une fois qu'il clique sur ok.
		self.userInterface.ok_bebe_nbbb_atteint.clicked.connect(lambda: self.userInterface.stack_des_cartes_de_jeu.setCurrentIndex(3)) # je definie la fonction qui permettra de revenir sur l'interface lancer le de une fois qu'il clique sur ok.

	def Definir_le_reve(self): # fonction qui permet d'affuicher le reve et son prisx sur l'interface de la carte choix de reve
		self.reve_choisi = self.reve.choisir_un_reve() # j'appele la fonction me retournant un reve aleatoire dans une liste
		self.userInterface.reve.setText(self.reve_choisi[0]) # je recupere le premier element de la liste qui est le reve en lui meme et j'affiche sur l'interface de la carte choix reve
		self.prix_fcfa = self.reve_choisi[1]+" FCFA" # je concatene avec la chaine fcfa avec le deuxieme element de la liste qui m'a ete retournee(contenant le prix du reve) pour afficher le prix suivi de la chaine fcfa
		self.userInterface.le_prix.setText(self.prix_fcfa) # j'affiche le prix concatene avec "FCFA" sur l'interface de la carte de jeu

	def Definir_la_profession(self): # fonction qui permet de charger la profession du joueur sur l'interface de l'etat financier			
		self.profession_choisie = self.joueur_courant.profession.Afficher_Profession() # j'accede a la profession du joueur courant
		self.entrees_totales_joueur = int(self.profession_choisie[1]) + self.joueur_courant.revenus_passifs # je fais la somme des entrees totales du joeur(salaire de la profession choisie + ses revenus passifs.
		self.userInterface.proffession.setText(self.profession_choisie[0]) # j'affiche la proffesion sur l'interface
		self.salaire_fcfa = self.profession_choisie[1]+" FCFA" # je concatene avec la chaine fcfa pour afficher le salaire suivi de la chaine fcfa
		self.montant_gain_fcfa = self.profession_choisie[2]+" FCFA" # je concatene avec la chaine fcfa pour afficher le montant_gain suivi de la chaine fcfa
		self.userInterface.salaire_sur_carte.setText(self.salaire_fcfa) # j'affiche le salaire de la proffession sur l'interface des cartes
		self.userInterface.montant_gain.setText(self.montant_gain_fcfa) # j'affiche le montant_gain de la proffession sur l'interface des cartes
		self.userInterface.metier.setText(self.profession_choisie[0]) # j'affiche le metier de la proffession sur l'interface de l'etat financier
		self.userInterface.salaire_etat_financier.setText(self.salaire_fcfa) # j'affiche le salaire de la proffession sur l'interface de l'etat financier
		self.entrees_totales_joueur = str(self.entrees_totales_joueur) + " FCFA" # je concatene la somme des entrees du joueur avec fcfa pour afficher cela sur l'interface de l'etat financier
		self.userInterface.entrees_totales.setText(self.entrees_totales_joueur) # ensuite j'affiche
		self.userInterface.choisir_smalldeal.clicked.connect(lambda: self.userInterface.stack_des_cartes_de_jeu.setCurrentIndex(3))

	def Definir_un_joueur(self): # la fonction qui permet de mettre l'interface etat financier a jour avec les infos du joueur courant
		self.joueur_courant.cash_hand = self.joueur_courant.profession.salaire * 0.3 # l'argent de poche du joueur est egal au 30 pourcents de son salaire
		self.cash_hand_affich = int(self.joueur_courant.cash_hand) # je convertis le cahhand en entier pour pouvoir le convertir en chaine et concatener avec FCFA
		self.cash_hand_affich = str(self.cash_hand_affich) + " FCFA" # je concatene le cashhand avec la chaine " FCFA"
		self.userInterface.cash_hand.setText(self.cash_hand_affich) # j'affiche ce cashhand sur l'interface de l'etat financier
		self.joueur_courant.depenses_standards = self.joueur_courant.profession.salaire * 0.2 # les depenses standards du joueur est egal au 20 pourcents de son salaire
		self.depenses_standards_affich = int(self.joueur_courant.depenses_standards) # je convertis le depenses totales en entier pour pouvoir le convertir en chaine et concatener avec FCFA
		self.depenses_standards_affich = str(self.depenses_standards_affich) + " FCFA" # je concatene le depenses standards avec la chaine " FCFA"
		self.userInterface.label_loyer.setText(str(int(self.joueur_courant.depenses_standards*0.4))+ " FCFA") # je suppose que le loyer du joueur correspond au 40% de ses depenses standards. 
		self.userInterface.label_ration.setText(str(int(self.joueur_courant.depenses_standards*0.6))+ " FCFA") # je suppose que la ration du joueur correspond au 60% de ses depenses standards.
		self.userInterface.standard_mensuel.setText(self.depenses_standards_affich) # j'affiche ce depenses standards sur l'interface
		self.depenses_totales_joueur = self.joueur_courant.depenses_standards + self.joueur_courant.depenses_bebe + self.joueur_courant.pourcentages_dettes # je fais la somme des depenses totales du joueur.
		self.depenses_totales_joueur = int(self.depenses_totales_joueur) # je convertis d'abord en entier pour ne pas avoir les virgules
		self.depenses_totales_joueur_fcfa = str(self.depenses_totales_joueur) + " FCFA"  # je convertis la variable contenant la somme des depenses totales du joueur en chaine pour pouvoir la concatener avec "FCFA" et l'ecrire sur l'interface de l'etat financier
		self.userInterface.depenses_totales.setText(self.depenses_totales_joueur_fcfa) # ensuite j'affiche
		self.entrees_totales_joueur = int(self.profession_choisie[1]) + self.joueur_courant.revenus_passifs
		self.a_decaisser_a_la_fin_du_mois = self.entrees_totales_joueur - self.depenses_totales_joueur # je recupere le payday du joueur en faisant la difference entre son salaire et ses depenses totales
		self.joueur_courant.payday = self.a_decaisser_a_la_fin_du_mois # j'attribue le checque de paie du joueur a son attribue payday
		self.a_decaisser_a_la_fin_du_mois_fcfa = str(self.a_decaisser_a_la_fin_du_mois) + " FCFA" # je convertis ce la en chaine puis je concatene avec la chaine "FCFA"
		self.userInterface.payday.setText(self.a_decaisser_a_la_fin_du_mois_fcfa) # j'affiche maintenant ca sur l'interface de l'etat financier

	def Gerer_le_paychek(self):
		self.mois = self.mois + 1
		self.joueur_courant.cash_hand = self.joueur_courant.cash_hand + self.joueur_courant.payday # j'ajoute au cash_hand du joueur son cheque de paie
		self.nouveau_cashhand = str(int(self.joueur_courant.cash_hand)) + " FCFA" # je convertis le cahhand du joueur en chaine pour concatener avec la chaine"FCFA" 
		self.userInterface.cash_hand.setText(self.nouveau_cashhand) # je modifie le cahhand du joueur sur l'interface de l'etat financier
		self.userInterface.stack_des_cartes_de_jeu.setCurrentIndex(10) # ensuite je change l'index pour afficher l'interface de transition avant de revenir lancer le de.
		self.userInterface.label_affiche_mois_courant.setText("Deja au "+str(self.mois)+ "eme mois.")

	def Gerer_la_charite(self):
		self.joueur_courant.cash_hand = self.joueur_courant.cash_hand - self.joueur_courant.cash_hand/10 # je decremente le cash_hand du joueur de 10% de son cash hand
		self.nouveau_cashhand = str(int(self.joueur_courant.cash_hand)) + " FCFA" # je convertis le cahhand du joueur en chaine pour concatener avec la chaine"FCFA" 
		self.userInterface.cash_hand.setText(self.nouveau_cashhand) # je modifie le cahhand du joueur sur l'interface de l'etat financier
		self.userInterface.stack_des_cartes_de_jeu.setCurrentIndex(8) # ensuite je change l'index pour afficher l'interface de transition avant de revenir lancer le de.	
	
	def Traitement_description_des_cartes(self,chaine): #fonction permettant de mettre les sauts de ligne sur une chaine de caractere
		self.new = ""
		for element in chaine:
			if element == '#':
				self.new = self.new + '\n'
			else:
				self.new = self.new + element
		return self.new

	def Verifier_si_chaine_a_seulement_les_chiffres(self,chaine): #fonction permettant de verifier si la chaine en parametre n'a que les chiffres ou pas
		liste = "0123456789"
		for element in chaine:
			if element in liste:
				print("",end="")
			else: 
				return False
		return True

	def Recuperer_valeur_QTextEdit(self): # fonction permettant de recuperer le nom du joueur et de la partie entres par l'utilisateur
		self.chaine = ""
		self.personne_1 = Personne() # j'instancie la classe personne.
		self.personne_1.nom_personne = self.userInterface.mdp_partie.toPlainText() # je met le nom de la personne dans l'attribut nom de la personne
		self.joueur_courant.nom_personne = self.personne_1.nom_personne # je met le nom du joueur dans l'attribut nom du joueur(qui est en fait le nom de la personne(heritage))
		self.partie_1 = Partie() # j'instancie la classe partie
		self.partie_1.nom_partie = self.userInterface.nom_partie.toPlainText() # je met le nom de la partie dans l'attribut nom de la parte de la partie
		self.chaine = "M. " + self.personne_1.nom_personne + " est entrain de jouer la partie [" + self.partie_1.nom_partie + "]" # je modifie la chaine (comportant le nom de la partie et celle du joueur) que j'affiche sur linterface de jeu
		self.userInterface.info_partie_en_cours.setText(self.chaine) # j'affiche cette chaine finalement
		self.chaine = self.personne_1.nom_personne + "'S TURN" # je modifie la chaine (comportant le nom du joueur) que j'affiche sur linterface de lance du de
		self.userInterface.titre_lancer_le_de.setText(self.chaine) #j'affiche egalement le nom du joueur sur l'interface de lance du de
		self.userInterface.stackedWidget.setCurrentIndex(4) # ensuite je change l'index pour afficher celui de l'espace de jeu

	def Affich_doodad(self): # fonction qui permet d'afficher le doodad
		self.doodad_choisi = self.un_doodads.Generer_doodads() # j'affecte la liste retournee a la variable doodad_choisi
		self.userInterface.description_doodads.setText(self.Traitement_description_des_cartes(self.doodad_choisi[0])) # je modifie le texte(description) de l'interface du doodads en appelant la fonction me permettant de mettre les sauts de ligne pour que ca afiche de facon totale sur le label description du doodad
		self.prix_doodad_fcfa = self.doodad_choisi[1] + " FCFA"# je concatene d'abord la chaine prix avec la chaine "FCFA" 
		self.userInterface.prix_doodads.setText(self.prix_doodad_fcfa) # ensuite je modifie le texte(prix) de l'interface du doodads

	def Affich_small_deal(self): # fonction qui permet d'afficher le smalldeal
		self.smalldeal_choisi = self.smalldeal.Generer_small_opportunite_carte() # j'affecte la liste retournee a la variable smalldeal_choisie
		self.userInterface.nom_smalldeal.setText(str(self.smalldeal_choisi[0])) # je modifie le texte(description) de l'interface du doodads en appelant la fonction me permettant de mettre les sauts de ligne pour que ca afiche de facon totale sur le label description du doodad
		self.userInterface.description_smalldeal.setText(self.Traitement_description_des_cartes(str(self.smalldeal_choisi[1])))
		self.userInterface.cout_smalldeal.setText(str(self.smalldeal_choisi[2]) + " FCFA") # ensuite je modifie le texte(prix) de l'interface du doodads
		self.userInterface.casflow_smalldeal.setText(str(self.smalldeal_choisi[3]) + " FCFA")

	def Affich_big_deal(self): # fonction qui permet d'afficher le bigdeal
		self.bigdeal_choisi = self.bigdeal.Generer_big_opportunite_carte() # j'affecte la liste retournee a la variable smalldeal_choisie
		self.userInterface.nom_bigdeal.setText(str(self.bigdeal_choisi[0])) # je modifie le texte(description) de l'interface du doodads en appelant la fonction me permettant de mettre les sauts de ligne pour que ca afiche de facon totale sur le label description du doodad
		self.userInterface.description_bigdeal.setText(self.Traitement_description_des_cartes(str(self.bigdeal_choisi[1])))
		self.userInterface.cout_bigdeal.setText(str(self.bigdeal_choisi[2] + " FCFA")) # ensuite je modifie le texte(prix) de l'interface du doodads
		self.userInterface.cashflow_bigdeal.setText(str(self.bigdeal_choisi[3] + " FCFA"))

	def Payer_small_deal(self):
		if(self.joueur_courant.cash_hand < int(self.smalldeal_choisi[2])):
			self.userInterface.stack_des_cartes_de_jeu.setCurrentIndex(28)
		else:
			self.joueur_courant.revenus_passifs = self.joueur_courant.revenus_passifs + int((self.smalldeal_choisi[3]))
			self.entrees_totales_joueur = int(self.profession_choisie[1]) + self.joueur_courant.revenus_passifs
			self.joueur_courant.payday = self.entrees_totales_joueur - self.depenses_totales_joueur
			self.userInterface.revenus_passifs.setText(str(self.joueur_courant.revenus_passifs) + " FCFA")
			self.userInterface.entrees_totales.setText(str(self.entrees_totales_joueur)+" FCFA")
			self.userInterface.payday.setText(str(int(self.joueur_courant.payday))+ " FCFA")
			self.joueur_courant.cash_hand = self.joueur_courant.cash_hand - int(self.smalldeal_choisi[2])
			self.userInterface.cash_hand.setText(str(int(self.joueur_courant.cash_hand))+" FCFA")
			if(self.numero_bien == 0):
				self.userInterface.nombien1.setText(str(self.smalldeal_choisi[0]))
				self.userInterface.cout_bien1.setText(str(self.smalldeal_choisi[2]) + " FCFA")
				self.userInterface.cashflowbien1.setText(str(self.smalldeal_choisi[3]) + " FCFA")
				self.userInterface.nombre_bien1.setText("1")
				self.numero_bien = self.numero_bien + 1
			elif(self.numero_bien == 1):
				self.userInterface.nom_bien_2.setText(str(self.smalldeal_choisi[0]))
				self.userInterface.cout_bien_2.setText(str(self.smalldeal_choisi[2]) + " FCFA")
				self.userInterface.cashflow_bien_2.setText(str(self.smalldeal_choisi[3]) + " FCFA")
				self.userInterface.nombre_bien_2.setText("1")
				self.numero_bien =self.numero_bien+1
			elif(self.numero_bien == 2):
				self.userInterface.nom_bien_3.setText(str(self.smalldeal_choisi[0]))
				self.userInterface.cout_bien_3.setText(str(self.smalldeal_choisi[2]) + " FCFA")
				self.userInterface.cashflow_bien_3.setText(str(self.smalldeal_choisi[3]) + " FCFA")
				self.userInterface.nombre_bien3.setText("1")
				self.numero_bien = self.numero_bien+1
			elif(self.numero_bien == 3):
				self.userInterface.nom_bien_4.setText(str(self.smalldeal_choisi[0]))
				self.userInterface.cout_bien_4.setText(str(self.smalldeal_choisi[2]) + " FCFA")
				self.userInterface.cashflow_bien_4.setText(str(self.smalldeal_choisi[3]) + " FCFA")
				self.userInterface.nombre_bien_4.setText("1")
				self.numero_bien = self.numero_bien +1
			elif(self.numero_bien == 4):
				self.userInterface.nom_bien_5.setText(str(self.smalldeal_choisi[0]))
				self.userInterface.cout_bien_5.setText(str(self.smalldeal_choisi[2]) + " FCFA")
				self.userInterface.cashflow_bien_5.setText(str(self.smalldeal_choisi[3]) + " FCFA")
				self.userInterface.nombre_bien_5.setText("1")
				self.numero_bien = self.numero_bien + 1 
			self.userInterface.stack_des_cartes_de_jeu.setCurrentIndex(27)

	def Payer_big_deal(self):
		if(self.joueur_courant.cash_hand < int(self.bigdeal_choisi[2])):
			self.userInterface.stack_des_cartes_de_jeu.setCurrentIndex(28)
		else:
			self.joueur_courant.revenus_passifs = self.joueur_courant.revenus_passifs + int((self.bigdeal_choisi[3]))
			self.entrees_totales_joueur = int(self.profession_choisie[1]) + self.joueur_courant.revenus_passifs
			self.joueur_courant.payday = self.entrees_totales_joueur - self.depenses_totales_joueur
			self.userInterface.revenus_passifs.setText(str(self.joueur_courant.revenus_passifs) + " FCFA")
			self.userInterface.entrees_totales.setText(str(self.entrees_totales_joueur)+" FCFA")
			self.userInterface.payday.setText(str(int(self.joueur_courant.payday))+ " FCFA")
			self.joueur_courant.cash_hand = self.joueur_courant.cash_hand - int(self.bigdeal_choisi[2])
			self.userInterface.cash_hand.setText(str(int(self.joueur_courant.cash_hand))+" FCFA")
			if(self.numero_bien == 0):
				self.userInterface.nombien1.setText(str(self.bigdeal_choisi[0]))
				self.userInterface.cout_bien1.setText(str(self.bigdeal_choisi[2]) + " FCFA")
				self.userInterface.cashflowbien1.setText(str(self.bigdeal_choisi[3]) + " FCFA")
				self.userInterface.nombre_bien1.setText("1")
				self.numero_bien = self.numero_bien +1
			elif(self.numero_bien == 1):
				self.userInterface.nom_bien_2.setText(str(self.bigdeal_choisi[0]))
				self.userInterface.cout_bien_2.setText(str(self.bigdeal_choisi[2]) + " FCFA")
				self.userInterface.cashflow_bien_2.setText(str(self.bigdeal_choisi[3]) + " FCFA")
				self.userInterface.nombre_bien_2.setText("1")
				self.numero_bien =self.numero_bien + 1 
			elif(self.numero_bien == 2):
				self.userInterface.nom_bien_3.setText(str(self.bigdeal_choisi[0]))
				self.userInterface.cout_bien_3.setText(str(self.bigdeal_choisi[2]) + " FCFA")
				self.userInterface.cashflow_bien_3.setText(str(self.bigdeal_choisi[3]) + " FCFA")
				self.userInterface.nombre_bien3.setText("1")
				self.numero_bien =self.numero_bien + 1
			elif(self.numero_bien == 3):
				self.userInterface.nom_bien_4.setText(str(self.bigdeal_choisi[0]))
				self.userInterface.cout_bien_4.setText(str(self.bigdeal_choisi[2]) + " FCFA")
				self.userInterface.cashflow_bien_4.setText(str(self.bigdeal_choisi[3]) + " FCFA")
				self.userInterface.nombre_bien_4.setText("1")
				self.numero_bien =self.numero_bien+1
			elif(self.numero_bien == 4):
				self.userInterface.nom_bien_5.setText(str(self.bigdeal_choisi[0]))
				self.userInterface.cout_bien_5.setText(str(self.bigdeal_choisi[2]) + " FCFA")
				self.userInterface.cashflow_bien_5.setText(str(self.bigdeal_choisi[3]) + " FCFA")
				self.userInterface.nombre_bien_5.setText("1")
				self.numero_bien =self.numero_bien+1
			self.userInterface.stack_des_cartes_de_jeu.setCurrentIndex(27)

	def Gerer_doodads(self):
		if(self.joueur_courant.cash_hand < int(self.doodad_choisi[1])):
			self.dette_emprunt = int(int(self.doodad_choisi[1]) - self.joueur_courant.cash_hand)
			self.userInterface.label_emprunt_doodad.setText(str(self.dette_emprunt) + " FCFA")
			self.userInterface.stack_des_cartes_de_jeu.setCurrentIndex(26)
		else:
			self.joueur_courant.cash_hand = self.joueur_courant.cash_hand - int(self.doodad_choisi[1]) # j'enleve au cash_hand du joueur le prix du doodad
			self.nouveau_cashhand = str(int(self.joueur_courant.cash_hand)) + " FCFA" # je convertis le cahhand du joueur en chaine pour concatener avec la chaine"FCFA" 
			self.userInterface.cash_hand.setText(self.nouveau_cashhand) # je modifie le cahhand du joueur sur l'interface de l'etat financier
			self.userInterface.stack_des_cartes_de_jeu.setCurrentIndex(19) # ensuite je change l'index pour afficher l'interface de transition (doodad) avant de revenir lancer le de.				

	def Emprunter(self, nouvelle_dette):		
		nouvelle_dette = int(nouvelle_dette)	
		self.userInterface.label_error_emprunt.setText("") #Je remet le label de l'erreur a une chaine vide
		self.joueur_courant.dettes = self.joueur_courant.dettes + nouvelle_dette # j'ajoute la dette que le joueur entre a ses dettes.
		self.joueur_courant.cash_hand = self.joueur_courant.cash_hand + nouvelle_dette # j'ajoute au cash_hand du joueur la somme qu'il a entre(celle au'il veut nouvelement emprunter)
		self.nouveau_cashhand = str(int(self.joueur_courant.cash_hand)) + " FCFA" # je convertis le cashhand du joueur en chaine pour concatener avec la chaine"FCFA" 
		self.userInterface.cash_hand.setText(self.nouveau_cashhand) # je modifie le cashhand du joueur sur l'interface de l'etat financier
		self.joueur_courant.pourcentages_dettes = self.joueur_courant.pourcentages_dettes +  int((nouvelle_dette)/10) # j'ajoute au pourcentage de dettes du joueur, le pourcentage de la dette qu'il vient de faire.
		self.depenses_totales_joueur = self.joueur_courant.depenses_standards + self.joueur_courant.depenses_bebe + self.joueur_courant.pourcentages_dettes # je fais la somme des depenses totales du joueur pour mettre ses informations a jour.
		self.userInterface.pourcentage_dettes.setText(str(int(self.joueur_courant.pourcentages_dettes)) + " FCFA") # je modifie le label qui affiche le pourcentage de dettes du joueur afin qu'il affiche le nouveau pourcentage de dette(pourcentage modifie)
		self.userInterface.depenses_totales.setText(str(int(self.depenses_totales_joueur)) + " FCFA")# je modifie le label qui affiche les depenses totales du joueur afin qu'il affiche le depenses totales (depenses totales modifiee)
		self.userInterface.montant_prets.setText(str(self.joueur_courant.dettes) + " FCFA") # j'affiche sur l'interface de l'etat financier, le montant de la dette qu'il vient de faire ajoutee a la dette qu'il devait deja.
		self.entrees_totales_joueur = int(self.profession_choisie[1]) + self.joueur_courant.revenus_passifs # je reanrrange les entrees totales du joueur
		self.joueur_courant.payday = self.entrees_totales_joueur - self.depenses_totales_joueur # pareil pour le payday
		self.nouveau_payday = str(int(self.joueur_courant.payday)) + " FCFA" # je convertis le cheque de paie du joueur en chaine et je concatene avec "FCFA" 
		self.userInterface.payday.setText(self.nouveau_payday) # jaffiche le nouveau payday sur l'interface de l'etat financier
		self.userInterface.stack_des_cartes_de_jeu.setCurrentIndex(17) # ensuite je change l'index pour afficher l'interface de transition avant de revenir lancer le de.		
		self.userInterface.somme_emprunt.clear() # je nettoie l'espace de saisie			

	def Executer_emprunt(self): # fonction qui execute l'emprunt
		self.nouvelle_dette = (self.userInterface.somme_emprunt.toPlainText()) # je stocke la nouvelle dette dans cette variable
		if(self.Verifier_si_chaine_a_seulement_les_chiffres(self.nouvelle_dette) == False): # je verifie si la chaine n'a que les chiffres
			self.userInterface.somme_emprunt.clear() # j'efface l'ancienne saisie du joueur pour lui permettre d'entrer une nouvelle valeur correcte
			self.userInterface.label_error_emprunt.setText(" Entrez une somme correcte..") # et j'affiche un message d'erreur
		elif(self.nouvelle_dette == ""): # s'il entre une chaine vide
			self.userInterface.label_error_emprunt.setText(" Veuillez remplir le champ...") # je lui retourne un message d'erreur	
		else: # si le joueur entre une valeur correcte
			self.Emprunter(self.nouvelle_dette) # j'appelle la fonction permettant d'executer l'emprunt avec la somme en parametre.
			
	def Rembourser(self):
		self.chaine = ""
		self.nouveau_remboursement = self.userInterface.somme_de_remboursement.toPlainText() # je stocke la nouveau remboursement dans cette variable
		if(self.Verifier_si_chaine_a_seulement_les_chiffres(self.nouveau_remboursement) == False): # je verifie si la chaine n'a que les chiffres
			self.userInterface.somme_de_remboursement.clear() # je nettoie l'espace de saisie pourque le joueur entre une nouvelle somme.
			self.userInterface.label_error_remb.setText(" Entrez une somme correcte..") # j'affiche un sms d'erreur
		elif(self.nouveau_remboursement == ""): # s'il entre une chaine vide
			self.userInterface.label_error_remb.setText(" Veuillez remplir le champ...") # j'affiche un sms d'erreur
		else: # si le joueur entre une valeur correcte
			self.userInterface.label_error_remb.setText("") #Je remet le label de l'erreur a une chaine vide
			self.nouveau_remboursement = int(self.userInterface.somme_de_remboursement.toPlainText()) # je convertis la valeur entree en entier pour pouvoir la manipuler
			self.userInterface.somme_de_remboursement.clear() # je nettoie l'espace de saisie
			if(self.joueur_courant.cash_hand < self.joueur_courant.dettes and self.joueur_courant.dettes > 0): # si le joueur a une dette mais son cash est plus petit que cette dette
				self.userInterface.stack_des_cartes_de_jeu.setCurrentIndex(22) # ensuite je change l'index pour afficher l'interface lui disant cela.		
			elif(self.nouveau_remboursement > self.joueur_courant.cash_hand and self.nouveau_remboursement > self.joueur_courant.dettes and self.joueur_courant.dettes > 0): # si le joueur a une dette, que la somme qu'il entre est plus grande que la somme qu'il doit et si la somme a rembourser que le joueur entre depasse la somme que le joueur entre
				self.userInterface.stack_des_cartes_de_jeu.setCurrentIndex(21) # ensuite je change l'index pour afficher l'interface lui disant cela.		
			elif(self.joueur_courant.dettes == 0): # s'il n'a pas de dettes
				self.userInterface.stack_des_cartes_de_jeu.setCurrentIndex(20) # ensuite je change l'index pour afficher l'interface lui disant cela.
			elif(self.joueur_courant.cash_hand > int(self.nouveau_remboursement) and self.joueur_courant.dettes > 0): # s'il a une dette superieure a 0 et si son cash peut payer cette dette
				if(self.nouveau_remboursement > self.joueur_courant.dettes): # s'il entre une somme superieure a celle qu'il doit
					self.userInterface.stack_des_cartes_de_jeu.setCurrentIndex(21) # ensuite je change l'index pour afficher l'interface lui disant cela.
				else:
					self.joueur_courant.cash_hand = self.joueur_courant.cash_hand - self.nouveau_remboursement # j'enleve au cash_hand du joueur la somme qu'il a entre(celle qu'il veut rembourser)
					self.nouveau_cashhand = str(int(self.joueur_courant.cash_hand)) + " FCFA" # je convertis le cashhand du joueur en chaine pour concatener avec la chaine"FCFA" 
					self.userInterface.cash_hand.setText(self.nouveau_cashhand) # je modifie le cashhand du joueur sur l'interface de l'etat financier
					self.joueur_courant.pourcentages_dettes = self.joueur_courant.pourcentages_dettes -  int(self.nouveau_remboursement)/10 # j'enleve au pourcentage de dettes du joueur, le pourcentage de la dette qu'il vient de rembourser.
					self.userInterface.pourcentage_dettes.setText(str(int(self.joueur_courant.pourcentages_dettes)) + " FCFA") # je modifie le label qui affiche le pourcentage de dettes du joueur afin qu'il affiche le nouveau pourcentage de dette(pourcentage modifie)		
					self.depenses_totales_joueur = self.joueur_courant.depenses_standards + self.joueur_courant.depenses_bebe + self.joueur_courant.pourcentages_dettes # je fais la somme des depenses totales du joueur pour mettre ses informations a jour.
					self.userInterface.depenses_totales.setText(str(int(self.depenses_totales_joueur)) + " FCFA")# je modifie le label qui affiche les depenses totales du joueur afin qu'il affiche le depenses totales (depenses totales modifiee)
					self.joueur_courant.dettes = self.joueur_courant.dettes - self.nouveau_remboursement # j'enleve aux dettes du joueur la somme qu'il a deja rembourse
					self.userInterface.montant_prets.setText(str(self.joueur_courant.dettes) + " FCFA") # j'affiche sur l'interface de l'etat financier, le nouveau montant de dettes qu'il a.
					self.entrees_totales_joueur = int(self.profession_choisie[1]) + self.joueur_courant.revenus_passifs
					self.joueur_courant.payday = self.entrees_totales_joueur - self.depenses_totales_joueur
					self.nouveau_payday = str(int(self.joueur_courant.payday)) + " FCFA" # je convertis le cheque de paie du joueur en chaine et je concatene avec "FCFA" 
					self.userInterface.payday.setText(self.nouveau_payday) # j'affiche le nouveau montant de son payday sur l'interface de l'etat financier
					self.userInterface.stack_des_cartes_de_jeu.setCurrentIndex(18) # ensuite je change l'index pour afficher l'interface de transition avant de revenir lancer le de.		
	
	def Emprunt_obligatoire_doodad(self):	# fonction qui est apelee lorsque le joueur n'a pas asez d'argent pour faire le doodad et qui permet de le faire emprunter obligatoiremnt
		self.Emprunter(self.dette_emprunt)
		self.joueur_courant.cash_hand = self.joueur_courant.cash_hand - int(self.doodad_choisi[1]) # j'enleve au cash_hand du joueur le prix du doodad
		self.nouveau_cashhand = str(int(self.joueur_courant.cash_hand)) + " FCFA" # je convertis le cahhand du joueur en chaine pour concatener avec la chaine"FCFA" 
		self.userInterface.cash_hand.setText(self.nouveau_cashhand) # je modifie le cahhand du joueur sur l'interface de l'etat financier
		self.userInterface.stack_des_cartes_de_jeu.setCurrentIndex(19) # ensuite je change l'index pour afficher l'interface de transition (doodad) avant de revenir lancer le de.				

	def Emprunt_obligatoire_chomage(self):	# fonction qui est apelee lorsque le joueur n'a pas asez d'argent pour faire le chomage et qui permet de le faire emprunter obligatoiremnt
		self.Emprunter(self.dette_emprunt) # j'appelle la fonction permettant d'emprunter avec le prix qui a ete calcule dans gerer chomage
		self.depenses_totales_joueur = self.joueur_courant.depenses_standards + self.joueur_courant.depenses_bebe + self.joueur_courant.pourcentages_dettes # je fais la somme des depenses totales du joueur pour mettre ses informations a jour.
		self.joueur_courant.cash_hand = self.joueur_courant.cash_hand - self.depenses_totales_joueur # j'enleve au cash hand du joueur ses depenses totales
		self.nouveau_cashhand = str(int(self.joueur_courant.cash_hand)) + " FCFA" # je convertis le cahhand du joueur en chaine pour concatener avec la chaine"FCFA" 
		self.userInterface.cash_hand.setText(self.nouveau_cashhand) # je modifie le cahhand du joueur sur l'interface de l'etat financier
		self.userInterface.stack_des_cartes_de_jeu.setCurrentIndex(25)

	def Gerer_chomage(self):
		if(self.joueur_courant.cash_hand < self.depenses_totales_joueur): # boucle permettant de lui dire ce qu'i doit emprunter s'il n'a pas assew d'argent pour fare le chomage (quand son cash ne suffit pas)
			self.dette_emprunt = int(self.depenses_totales_joueur - self.joueur_courant.cash_hand) + int(self.depenses_totales_joueur - self.joueur_courant.cash_hand)/5 
			self.userInterface.label_prix_emprunt.setText(str(self.dette_emprunt) + " FCFA")
			self.userInterface.stack_des_cartes_de_jeu.setCurrentIndex(24)
		else:			
			self.depenses_totales_joueur = self.joueur_courant.depenses_standards + self.joueur_courant.depenses_bebe + self.joueur_courant.pourcentages_dettes # je fais la somme des depenses totales du joueur pour mettre ses informations a jour.
			self.joueur_courant.cash_hand = self.joueur_courant.cash_hand - self.depenses_totales_joueur # j'enleve au cash hand du joueur ses depenses totales
			self.nouveau_cashhand = str(int(self.joueur_courant.cash_hand)) + " FCFA" # je convertis le cahhand du joueur en chaine pour concatener avec la chaine"FCFA" 
			self.userInterface.cash_hand.setText(self.nouveau_cashhand) # je modifie le cahhand du joueur sur l'interface de l'etat financier
			self.userInterface.stack_des_cartes_de_jeu.setCurrentIndex(23) # ensuite je change l'index pour afficher l'interface de transition avant de revenir lancer le de.	

	def Avoir_un_nouveau_bebe(self):
		if(self.joueur_courant.depenses_bebe >= 125000): # je verifie si le joueur a deja cinq enfants
			self.userInterface.stack_des_cartes_de_jeu.setCurrentIndex(6) # je change l'index pour afficher plutot celle de l'interface de nombre_bebe_max_atteint
		else: # s'il n'a pas encore  beaucoup de bebes.
			self.joueur_courant.depenses_bebe = self.joueur_courant.depenses_bebe + 25000 # j'incremente les depenses pour bebe de 25000.
			self.depenses_totales_joueur = self.joueur_courant.depenses_standards + self.joueur_courant.depenses_bebe + self.joueur_courant.pourcentages_dettes # je fais la somme des depenses totales du joueur(pour modifier sa valeur car les depenses pour le bebe ont augmentees).
			self.nouveau_dep_totales = str(int(self.depenses_totales_joueur)) + " FCFA" # je convertis les nouvelles depenses du joueur en chaine pour pouvoir concatener avec la chaine " FCFA" 
			self.userInterface.depenses_totales.setText(self.nouveau_dep_totales) #je modifie les nouvelles depenses totales(la somme de toutes les depenses) sur l'interface de l'etat financier en affichant juste la chaine convertis ici en haut.
			self.entrees_totales_joueur = int(self.profession_choisie[1]) + self.joueur_courant.revenus_passifs
			self.joueur_courant.payday = self.entrees_totales_joueur - self.depenses_totales_joueur
			self.nouveau_payday = str(int(self.joueur_courant.payday)) + " FCFA" # je convertis le cheque de paie du joueur en chaine et je concatene avec "FCFA" 
			self.userInterface.payday.setText(self.nouveau_payday) # j'affiche ce nouveau payday sur l'interface de l'etat financier
			self.nouveau_depenses_pour_bebes = str(self.joueur_courant.depenses_bebe) + " FCFA" # je convertis les depenses pour bebes en chaine pour pouvoir concatener avec la chaine " FCFA"
			self.userInterface.depenses_bebes.setText(self.nouveau_depenses_pour_bebes) # je modifie le prix des depenses pour bebe sur l'interface de l'etat financier
			self.userInterface.stack_des_cartes_de_jeu.setCurrentIndex(5) # ensuite je change l'index pour afficher l'interface de transition avant de revenir lancer le de.

	def Lancer_le_de(self):
		self.liste_de = [1,2,3,4,5,6]
		self.valeur_de = random.choice(self.liste_de)
		self.userInterface.label_valeur_de_lance.setText(str(self.valeur_de))
		self.new_position = self.pion.Deplacement_du_pion(self.pion.position_actuelle,24,self.valeur_de)
		if(((self.ancienne_position < 5 and self.new_position > 5) or (self.ancienne_position < 21 and self.new_position < 3 and self.ancienne_position>13) or (self.ancienne_position < 13 and self.new_position > 13) or (self.ancienne_position < 21 and self.new_position > 21)) and (self.new_position != 5 and self.new_position != 13 and self.new_position != 1)):  # cette boucle en fait permet d'executer paycheck s'il traverse cet espace en lancant le de
			self.mois = self.mois + 1
			self.joueur_courant.cash_hand = self.joueur_courant.cash_hand + self.joueur_courant.payday # j'ajoute au cash_hand du joueur son cheque de paie
			self.nouveau_cashhand = str(int(self.joueur_courant.cash_hand)) + " FCFA" # je convertis le cahhand du joueur en chaine pour concatener avec la chaine"FCFA" 
			self.userInterface.cash_hand.setText(self.nouveau_cashhand) # 
			self.userInterface.label_affiche_mois_courant.setText("Deja au "+str(self.mois)+ "eme mois.")
		a = self.pion.liste_positions_rat_race[self.new_position][0]
		b = self.pion.liste_positions_rat_race[self.new_position][1]
		self.userInterface.token.move(a,b)
		self.dict_correspondance = {0:11,1:14,2:11,3:7,4:11,5:9,6:11,7:16,8:11,9:14,10:11,11:15,12:11,13:9,14:11,15:16,16:11,17:14,18:11,19:4,20:11,21:9,22:11,23:16} # dictionnaire de correspondance entre l'espace et la carte.
		self.userInterface.stack_des_cartes_de_jeu.setCurrentIndex(self.dict_correspondance[self.new_position])			
		if(self.dict_correspondance[self.new_position] == 14): #s'il choisi de tomber sur l'espace doodad, j'affiche d'abord les infos du doodad choisi aleatoirement
			self.Affich_doodad() # j'appele la fonction permettant de le faire.
		if(self.dict_correspondance[self.new_position] == 11): #s'il choisi de tomber sur l'espace opportunite, j'affiche d'abord les infos du small/deal choisi aleatoirement
			self.Affich_small_deal() # j'affiche les infos du small_deal sur l'interface
			self.Affich_big_deal() # j'affiche les infos du big_deal sur l'interface
		self.ancienne_position = self.new_position

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ui = Les_actions()
    ui.show()
    sys.exit(app.exec_())
