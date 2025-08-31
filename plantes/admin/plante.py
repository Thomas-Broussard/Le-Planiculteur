from django.contrib import admin
from plantes.models import *

@admin.register(ModelePlante)
class PlanteAdmin(admin.ModelAdmin):
    list_display = (
        'nom_commun',
        'nom_latin',
        'categorie',
        'famille',
        'type_sol',
        'besoin_soleil',
        'besoin_arrosage',
        'debut_semis',
        'fin_semis',
        'debut_recolte',
        'fin_recolte',
        'espacement_plants',
        'espacement_lignes',
    )
    list_filter = (
        'categorie',
        'famille',
    )
    search_fields = (
        'nom_commun',
        'nom_latin',
    )
    list_per_page = 10