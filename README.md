oph
===

openerp for ophthalmologist.
for odoo 7.0 version

Feature
----------

Gestion administrative patient
*****************************
	
	- signale la création d'un homonyme
	
Relation avec la CAFAT
*********************

	- envoie de mail pour les demandes de rajout de code, de prise en charge en LM avec les actes à prevoir.
	- realisation des états à adresser à la CAFAT

Relation avec la clinique
***********************

	-  possibilité pour le personnel de se connecter sur un portail avec l'acces uniquement aux blocs
	-  possibilité de se connecter aux dossiers patients depuis la clinique.
	-  editions des documents pour les anesthésistes, pour la clinique, pour les consignes post-opératoire.
	-  envoie de mail pour la commande des implants.
	- rajout de champs, de documents au fil de l'eau en fonction des demandes de la clinique.
	
Compte rendu opératoire
************************
	- indications 
	- procédures
	- dilatation suivant la procédure.
	-  case à cocher , items à selectionner pour la réalisation des comptes rendus opératoires
	
Facturations
************

	-	 liste de prix pour les carte B avec ticket moderateur.
	-  liste des produits en NGAP et pas en CCAM
	-  rajout possible de produit. 
	-  KC possibilité de modifier la valeur du KC.

# Request

## Images
###  importations des images
aujourd'hui à partir du matériel d'acquisition d'image j'exporte les images en pdf, jpg, png. Puis je les importe en piece dans la fiche patient. 
### viewer d'image sur odoo
il faut pouvoir manipuler les images pour pouvoir faire des comparaisons.

## Gestion des emails envoyés par les patients
Aujourd'hui je les exporte en PDF et je les importe en PJ dans le dossier patient.
Est ce qu'on peut faire mieux avec ODOO? 

## Compte rendu
Actuellement les rapports sont des fichiers libres offices. Je fais quasiment systématiquement des modifications dans le fichier et regulierment j'oublie de recuperer les modifications dans le doisser patient odoo.

