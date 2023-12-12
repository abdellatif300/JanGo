from django.db import models

# Create your models here.

class Utilisateur(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    email = models.EmailField()

class Cours(models.Model):
    nom_cours = models.CharField(max_length=100)
    description = models.TextField()

class Salle(models.Model):
    nom_salle = models.CharField(max_length=100)
    capacite = models.IntegerField()

class EmploiDuTemps(models.Model):
    jour_semaine = models.CharField(max_length=100)
    heure_debut = models.CharField(max_length=100)
    heure_fin = models.CharField(max_length=100)
    cours = models.ForeignKey(Cours, on_delete=models.CASCADE)
    utilisateur = models.ForeignKey(Utilisateur, on_delete=models.CASCADE)
    salle = models.ForeignKey(Salle, on_delete=models.CASCADE)

