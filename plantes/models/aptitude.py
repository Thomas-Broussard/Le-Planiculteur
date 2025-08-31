from django.db import models

class CategorieAptitude(models.Model):
    nom = models.CharField(max_length=200)
    description = models.TextField()

class AptitudePointFort(models.Model):
    description = models.TextField()
    categorie = models.ForeignKey(CategorieAptitude, on_delete=models.CASCADE)

class AptitudePointFaible(models.Model):
    description = models.TextField()
    categorie = models.ForeignKey(CategorieAptitude, on_delete=models.CASCADE)