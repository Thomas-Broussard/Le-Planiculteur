from django.contrib import admin
from plantes_configuration.models import *

class BaseNomDescriptionAdmin(admin.ModelAdmin):
    list_display = ('nom', 'description')
    search_fields = ('nom',)
    list_per_page = 10

admin.site.register(FamillePlante, BaseNomDescriptionAdmin)
admin.site.register(CategoriePlante, BaseNomDescriptionAdmin)
admin.site.register(BesoinSoleil, BaseNomDescriptionAdmin)
admin.site.register(BesoinArrosage, BaseNomDescriptionAdmin)
