#!/usr/bin/env python
import os
import sys
import glob
import datetime

# Configure Django environment
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "le_planiculteur.settings")

import django
django.setup()

from django.core.management import call_command

def backup_database():
    """
    Sauvegarde toutes les données existantes dans un fichier JSON horodaté.
    """
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_file = f"backups/backup_{timestamp}.json"
    print(f"💾 Sauvegarde de la base dans {backup_file} ...")
    call_command("dumpdata", "--natural-foreign", "--natural-primary", "--exclude", "contenttypes", "--exclude", "auth.permission", output=backup_file)
    return backup_file

def reset_database():
    """
    Réinitialise la base de données et charge toutes les fixtures.
    """
    backup_file = backup_database()

    print("🔹 Suppression de la base de données (flush)...")
    call_command("flush", "--noinput")

    # Suppression du fichier db.sqlite3 s'il existe
    try:
        if os.path.exists("db.sqlite3"):
                print("🔹 Suppression du fichier db.sqlite3...")
                os.remove("db.sqlite3")
    except Exception as e:
        print(f"  - Erreur lors de la suppression du fichier db.sqlite3: {e}")

    # Suppression de tous les fichiers de migration (sauf __init__.py)
    print("🔹 Suppression des fichiers de migration...")
    # Parcourir tous les dossiers à la racine du projet
    racine_projet = os.path.dirname(os.path.abspath(__file__))
    dossiers_racine = [
        nom for nom in os.listdir(racine_projet)
        if os.path.isdir(os.path.join(racine_projet, nom))
    ]
    for dossier in dossiers_racine:
        for root, dirs, files in os.walk(dossier):
            if root.endswith("migrations"):
                for file in files:
                    if file != "__init__.py" and file.endswith(".py"):
                        chemin_fichier = os.path.join(root, file)
                        print(f"  - Suppression de {chemin_fichier}")
                        os.remove(chemin_fichier)
                    elif file.endswith(".pyc"):
                        chemin_fichier = os.path.join(root, file)
                        print(f"  - Suppression de {chemin_fichier}")
                        os.remove(chemin_fichier)

    print("🔹 Appliquer les migrations...")
    call_command("makemigrations")
    call_command("migrate")

    print("🔹 Création d'un superutilisateur par défaut (thomas/thomas)...")
    from django.contrib.auth import get_user_model
    User = get_user_model()
    if not User.objects.filter(username="thomas").exists():
        User.objects.create_superuser("thomas", "thomas@example.com", "thomas")
        print("  - Superutilisateur 'thomas' créé avec succès.")
    else:
        print("  - Le superutilisateur 'thomas' existe déjà.")

    print("🔹 Chargement des fixtures...")

    fixtures = [
        f for f in glob.glob("plantes_configuration/fixtures/*.json")
    ]

    for fixture in fixtures:
        print(f"  - Chargement de {fixture} ...")
        call_command("loaddata", fixture)

    print("✅ Base de données réinitialisée et fixtures chargées !")
    print(f"💾 Les anciennes données ont été sauvegardées dans : {backup_file}")


if __name__ == "__main__":
    reset_database()
