from django.db import models
from plantes.models.plante import ModelePlante

class TypeAssociation(models.TextChoices):
    COMPAGNONNAGE = "COMPAGNONNAGE"
    INCOMPATIBILITE = "INCOMPATIBILITE"


class AssociationPlante(models.Model):
    plantes = models.ManyToManyField(
        ModelePlante,
        related_name="associations",
        help_text="Plantes associées dans cette association"
    )
    type = models.CharField(max_length=200, choices=TypeAssociation.choices)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        plantes_str = ", ".join([plante.nom_commun for plante in self.plantes.all()])
        return f"{plantes_str}"

    class Meta:
        verbose_name = "Association de plante"
        verbose_name_plural = "Associations de plantes"
        ordering = ["type"]
