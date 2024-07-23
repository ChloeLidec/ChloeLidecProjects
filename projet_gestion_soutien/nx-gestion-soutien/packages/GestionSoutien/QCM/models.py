from django.db import models

from GestionSoutien.models import Eleve, Matiere, Semaine
# Create your models here.


class QCM(models.Model):
    id_qcm = models.AutoField(primary_key=True)
    nom_qcm = models.CharField(max_length=50)
    id_matiere = models.ForeignKey(Matiere, on_delete=models.CASCADE)
    id_semaine = models.ForeignKey(Semaine, on_delete=models.CASCADE)

    def __str__(self):
        return f"QCM({self.id_qcm}, {self.nom_qcm}, {self.id_matiere}, {self.id_semaine})"

    class Meta:
        db_table = "qcm"


class ResultatQCM(models.Model):
    id_qcm = models.ForeignKey(QCM, on_delete=models.CASCADE)
    num_etu = models.ForeignKey(Eleve, on_delete=models.CASCADE)
    note = models.IntegerField()

    def __str__(self):
        return f"ResultatQCM({self.id_qcm}, {self.num_etu}, {self.note})"

    class Meta:
        db_table = "resultatqcm"
