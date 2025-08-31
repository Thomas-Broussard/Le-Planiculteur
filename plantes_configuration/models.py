from django.db import models
from plantes_configuration.models import *

class BaseNomDescription(models.Model):
    nom = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)

    class Meta:
        abstract = True

    def __str__(self):
        return self.nom

class FamillePlante(BaseNomDescription):
    class Meta:
        verbose_name = "Famille de plante"
        verbose_name_plural = "Familles de plantes"

class CategoriePlante(BaseNomDescription):
    class Meta:
        verbose_name = "Catégorie de plante"
        verbose_name_plural = "Catégories de plantes"

class BesoinSoleil(BaseNomDescription):
    class Meta:
        verbose_name = "Besoin en soleil"
        verbose_name_plural = "Besoins en soleil"

class BesoinArrosage(BaseNomDescription):
    class Meta:
        verbose_name = "Besoin en arrosage"
        verbose_name_plural = "Besoins en arrosage"

class TypeSol(BaseNomDescription):
    class Meta:
        verbose_name = "Type de sol"
        verbose_name_plural = "Types de sol"