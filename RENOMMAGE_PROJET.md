# Renommage du Projet Django

## Changement effectué

Le projet Django a été renommé de **"planiculture"** vers **"le_planiculteur"**.

## Fichiers modifiés

### Fichiers de configuration Django
- `le_planiculteur/settings.py` - Références ROOT_URLCONF et WSGI_APPLICATION
- `le_planiculteur/urls.py` - Commentaire d'en-tête
- `le_planiculteur/wsgi.py` - Référence au module settings et commentaire
- `le_planiculteur/asgi.py` - Référence au module settings et commentaire

### Scripts utilitaires
- `manage.py` - Référence au module settings
- `reset_db.py` - Référence au module settings
- `restore_latest_backup.py` - Référence au module settings

### Modèles
- `plantes/models/plante.py` - Import depuis le module common.choices

## Structure du projet

```
le_planiculteur/          # Dossier principal du projet Django
├── __init__.py
├── asgi.py
├── common/
├── settings.py
├── urls.py
├── wsgi.py
└── __pycache__/

plantes/                   # Application des plantes
plantes_configuration/     # Application de configuration
backups/                   # Sauvegardes de base de données
db.sqlite3                 # Base de données SQLite
manage.py                  # Script de gestion Django
```

## Test de fonctionnement

Le projet a été testé avec succès :
- ✅ `python manage.py check` - Aucune erreur détectée
- ✅ Configuration Django valide
- ✅ Tous les imports fonctionnent correctement

## Note importante

Le nom du projet utilise un underscore (`le_planiculteur`) au lieu d'un tiret (`le-planiculteur`) car Python ne peut pas importer des modules contenant des tirets dans leur nom.

## Commandes utiles

```bash
# Vérifier la configuration
python manage.py check

# Démarrer le serveur de développement
python manage.py runserver

# Réinitialiser la base de données
python reset_db.py

# Restaurer la dernière sauvegarde
python restore_latest_backup.py
```
