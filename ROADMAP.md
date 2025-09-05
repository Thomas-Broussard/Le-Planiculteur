
# Bibliothèque de plantes

- Créer une bibliothèque de plantes permettant de stocker, consulter et gérer des informations détaillées sur différentes plantes.  
- Les modèles de données incluent les familles de plantes, les types de sol, l’exposition au soleil, ainsi que les points forts et faibles de chaque plante.  
- L’objectif est de permettre l’ajout, la modification et la visualisation des plantes et de leurs caractéristiques principales via l’interface d’administration Django.


# Association de plantes

- Permettre de lier des plantes entre elles avec une relation (compagnonnage ou incompatibilité)
- Gérer ces associations depuis l’interface d’administration Django
- Afficher les associations sur la fiche de chaque plante


# Création d'un modèle d'espace potager 

- Permettre à un utilisateur de créer un modèle d'espace potager pour accueillir une ou plusieurs plantes (modèle : ModeleEspacePotager) avec :
 - Un nom (ex : Jardinière, Carré potager, Parcelle, ...)
 - Une dimensions globale (longueur x largeur)


# Création d'une instance d'espace potager

- Permettre à un utilisateur de créer une instance virtuelle d'un espace potager (modèle : InstanceEspacePotager), dans laquelle il pourra y placer des plantes (modèle : InstancePlante)


# Création d'une carte

- Permettre à l'utilisateur de créer une carte sur laquelle il viendra placer ses espaces potagers (InstancePotager)
- Définir les zones couvertes et les zones extérieures sur la carte

# Créer un outil d'analyse de carte

- Enumérer toutes les plantes disponibles sur la carte
- Etablir une synthèse des aptitudes (points forts et points faibles) du potager


# Créer un outil d'auto-composition de potager

- L'utilisateur prépare sa carte en plaçant ses espaces potagers dessus
- Il appuie sur le bouton "auto composition"
- Il sélectionne les plantes (ModelePlante) qu'il souhaite mettre dans son potager (et leur quantité)
- L'outil détermine automatiquement les plantes à mettre à côté et celles à éviter
- Il propose une carte à l'utilisateur, que ce dernier pourra ensuite éditer à sa convenance


# Ajouter des données météo

- Ajouter la possibilité de saisir des coordonnées GPS réelles pour une carte
- Selon ces coordonnées GPS, récupérer les prévisions météos quotidiennement
- Définir une jauge humidité/sécheresse dépendant des X derniers jours
 