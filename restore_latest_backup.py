#!/usr/bin/env python
import os
import sys
import glob

# Configure Django environment
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "le_planiculteur.settings")

import django
django.setup()

from django.core.management import call_command

def get_latest_backup(folder="."):
    """
    Cherche le dernier fichier backup_YYYYMMDD_HHMMSS.json dans le dossier spécifié.
    """
    pattern = os.path.join(folder, "backup_*.json")
    backups = glob.glob(pattern)
    if not backups:
        return None
    # Trie par date, décroissant
    backups.sort(reverse=True)
    return backups[0]

def restore_latest_backup():
    backup_file = get_latest_backup("backups/")
    if not backup_file:
        print("❌ Aucun fichier de backup trouvé.")
        return

    print(f"🔹 Restauration depuis le dernier backup : {backup_file} ...")
    call_command("loaddata", backup_file)
    print("✅ Restauration terminée !")

if __name__ == "__main__":
    restore_latest_backup()
