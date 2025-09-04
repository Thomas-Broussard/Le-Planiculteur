from django.contrib import admin
from plantes.models import *

@admin.register(ModelePlante)
class PlanteAdmin(admin.ModelAdmin):
    fieldsets = (
        ("Identité de la plante", {
            'fields': (
                'nom_commun',
                'nom_latin',
                'description',
                'image',
            )
        }),
        ("Catégorisation", {
            'fields': (
                'categorie',
                'famille',
            )
        }),
        ("Besoins de la plante", {
            'fields': (
                'type_sol',
                'besoin_soleil',
                'besoin_arrosage',
            )
        }),
        ("Cycle Semis / Récolte", {
            'fields': (
                ('debut_semis', 'fin_semis'),
                ('debut_recolte', 'fin_recolte'),
            )
        }),
        ("Espacements", {
            'fields': (
                'espacement_plants',
                'espacement_lignes',
            )
        }),
        ("Points forts et faibles", {
            'fields': (
                'points_forts',
                'points_faibles',
            )
        }),
    )
    list_display = (
        'nom_commun',
        'categorie',
        'famille',
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