from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class Adresse(models.Model):
    id=models.AutoField(primary_key=True)
    ville=models.CharField(max_length=20)
    region=models.CharField(max_length=20)
    quartier=models.CharField(max_length=20)
    codePostal=models.IntegerField()
    rue=models.CharField(max_length=50)


    def __str__(self):
        return 'Ville :{} ,Région: {},Quartier : {},Code Postal : {},Rue : {} .'.format(self.ville,self.region,self.quartier,self.codePostal,self.rue)



class Ecole(models.Model):
    NIVEAU=(('Maternelle','Maternelle'),('Primaire','Primaire'),('College','Collège'),('Lycee','Lycée'))
    id=models.AutoField(primary_key=True)
    niveau=models.CharField(max_length=10,choices=NIVEAU,default='')
    nom=models.CharField(max_length=30,unique=True)
    adresse=models.ForeignKey(Adresse,on_delete=models.CASCADE,default='')

    def __str__(self):
        return '{}'.format(self.nom)


class Etudiant(models.Model):

    id=models.AutoField(primary_key=True)
    nom=models.CharField(max_length=20)
    prenom=models.CharField(max_length=20)
    email=models.EmailField()
    tel=models.CharField(max_length=10)
    adresse=models.ForeignKey(Adresse,on_delete=models.CASCADE,default='')
    ecole=models.ForeignKey(Ecole,on_delete=models.CASCADE,default='')
    
    def __str__(self):
        return 'Nom : {} , Prénom : {}'.format(self.nom,self.prenom)


class Parent(models.Model):
    id=models.AutoField(primary_key=True)
    nom=models.CharField(max_length=20)
    prenom=models.CharField(max_length=20)
    email=models.EmailField()
    tel=models.CharField(max_length=10)
    etudiant=models.ForeignKey(Etudiant,on_delete=models.CASCADE,default='')

    def __str__(self):
        return 'Nom : {} , Prénom : {}'.format(self.nom,self.prenom)

class Bus(models.Model):

    id=models.AutoField(primary_key=True)
    matricule=models.CharField(max_length=10,unique=True)
    nbrePlaces=models.IntegerField()
    ecole=models.ForeignKey(Ecole,on_delete=models.CASCADE,default='')
    
    
    def __str__(self):
        return 'matricule {} : '.format(self.matricule)


class Chauffeur(models.Model):

    id=models.AutoField(primary_key=True)
    nom=models.CharField(max_length=20)
    prenom=models.CharField(max_length=20)
    tel=models.CharField(max_length=10)
    bus=models.ForeignKey(Bus,on_delete=models.CASCADE,default='')
    ecole=models.ForeignKey(Ecole,on_delete=models.CASCADE,default='')

    def __str__(self):
        return 'Nom : {} , Prénom : {}'.format(self.nom,self.prenom)





class Notification(models.Model):
    id=models.AutoField(primary_key=True)
    message=models.CharField(max_length=200)



