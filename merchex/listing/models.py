from django.db import models

# Creation du modele groupe
class Groupe(models.Model):
    nom = models.CharField(max_length=100)


# Creation du modele listing
class Listing(models.Model):
    title = models.CharField(max_length=100)
