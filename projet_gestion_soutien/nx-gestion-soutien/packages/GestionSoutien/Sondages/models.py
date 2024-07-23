from django.db import models
from GestionSoutien.models import Eleve, Semaine
# Create your models here.


class Sondage(models.Model):
    id_sond = models.AutoField(primary_key=True)
    id_semaine = models.ForeignKey(Semaine, on_delete=models.CASCADE)

    def __str__(self):
        return f"Sondage({self.id_sond}, {self.id_semaine})"

    class Meta:
        db_table = "sondage"


class RepSondage(models.Model):
    id_sondage = models.ForeignKey(Sondage, on_delete=models.CASCADE)
    num_etu = models.ForeignKey(Eleve, on_delete=models.CASCADE)
    matiere_voulue = models.CharField(max_length=100)
    volontaire = models.CharField(max_length=50)
    commentaire = models.CharField(max_length=800)

    def __str__(self):
        return f"RepSondage({self.volontaire}, {self.id_sondage}, {self.num_etu}, {self.matiere_voulue}, {self.commentaire})"

    class Meta:
        db_table = "repsondage"
