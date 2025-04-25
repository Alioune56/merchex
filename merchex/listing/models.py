from django.db import models
# Validators
from django.core.validators import MinValueValidator,MaxValueValidator

# Creation du modele groupe
class Groupe(models.Model):

    class Genre(models.TextChoices):
        HIP_HOP = 'HH'
        SYNTH_POP = 'SP'
        ALTERNATIVE_ROCK = 'AR'

    nom = models.CharField(max_length=100)
    genre = models.CharField(max_length=5,choices=Genre.choices)
    biography = models.CharField(max_length=100)
    year_formed = models.IntegerField(
        validators=[MinValueValidator(1960),MaxValueValidator(2025)]
    )
    active = models.BooleanField(default=True)
    official_home_page = models.URLField(blank=True,null=True)

    def __str__(self):
        return self.nom

# Creation du modele listing
class Listing(models.Model):

    class Type(models.TextChoices):
        records = 'Disques'
        clothing = 'Vetements'
        posters = 'Affiches'
        miscellaenous = 'Divers'

    title = models.CharField(max_length=100)
    description = models.TextField()
    sold = models.BooleanField(default=False)
    year = models.IntegerField(
        validators=[MinValueValidator(1950),MaxValueValidator(2025)]
    )
    type = models.CharField(choices=Type.choices,max_length=50)
    groupe = models.ForeignKey(Groupe,null=True,on_delete=models.SET_NULL)