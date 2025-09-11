from django.contrib import admin
from plantes.models.association import AssociationPlante

@admin.register(AssociationPlante)
class AssociationPlanteAdmin(admin.ModelAdmin):
    list_display = ('plantes_str', 'type')
    list_filter = ('type',)
    search_fields = ('plantes__nom_commun',)
    list_per_page = 10
    filter_horizontal = ('plantes',)

    def plantes_str(self, obj):
        return ", ".join([plante.nom_commun for plante in obj.plantes.all()])

    plantes_str.short_description = "Plantes"

