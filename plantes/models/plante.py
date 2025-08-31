from django.db import models
from plantes.models.aptitude import AptitudePointFort, AptitudePointFaible
from plantes_configuration.models import *
from le_planiculteur.common.choices import MOIS

# Create your models here.
class ModelePlante(models.Model):
    class Meta:
        verbose_name = "plante"
        verbose_name_plural = "plantes"
        ordering = ["nom_commun"]

    # Identité de base
    nom_commun = models.CharField(max_length=200)
    nom_latin = models.CharField(max_length=200, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='plantes/', blank=True, null=True)

    categorie = models.ForeignKey(CategoriePlante, on_delete=models.SET_NULL, null=True)
    famille = models.ForeignKey(FamillePlante, on_delete=models.SET_NULL, null=True)

    # Besoins de la plante
    type_sol = models.ForeignKey(TypeSol, on_delete=models.SET_NULL, null=True)
    besoin_soleil = models.ForeignKey(BesoinSoleil, on_delete=models.SET_NULL, null=True)
    besoin_arrosage = models.ForeignKey(BesoinArrosage, on_delete=models.SET_NULL, null=True)

    # Cycle Semis / Recolte
    debut_semis = models.PositiveSmallIntegerField(choices=MOIS, blank=True, null=True)
    fin_semis = models.PositiveSmallIntegerField(choices=MOIS, blank=True, null=True)

    debut_recolte = models.PositiveSmallIntegerField(choices=MOIS, blank=True, null=True)
    fin_recolte = models.PositiveSmallIntegerField(choices=MOIS, blank=True, null=True)

    # Espacements
    espacement_plants = models.FloatField(help_text="Distance entre deux plants (cm)", blank=True, null=True)
    espacement_lignes = models.FloatField(help_text="Distance entre deux lignes (cm)", blank=True, null=True)

    # Points forts / faibles
    points_forts = models.ManyToManyField(AptitudePointFort)
    points_faibles = models.ManyToManyField(AptitudePointFaible)


    # -----------------------------------
    # Fonctions
    # -----------------------------------
    def __str__(self):
        return self.nom_commun
