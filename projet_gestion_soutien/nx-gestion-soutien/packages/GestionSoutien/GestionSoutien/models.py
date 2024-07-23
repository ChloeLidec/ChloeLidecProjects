from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.core.exceptions import ValidationError

class Periode(models.Model):
    id_periode = models.AutoField(primary_key=True)
    date_debut = models.DateField()
    date_fin = models.DateField()

    def validate_quadruplet(self, exclude=None):
        from django.core.exceptions import ValidationError, NON_FIELD_ERRORS
        if Periode.objects.count() >= 4:
            raise ValidationError(
                {NON_FIELD_ERRORS: ["Il ne peut y avoir que 4 périodes"]})
            
    def clean(self) -> None:
        if self.date_debut and self.date_fin and self.date_debut >self.date_fin:
            raise ValidationError(
                {"date_debut": "La date de début doit être inférieure à la date de fin"})


    def __str__(self):
        return f"Periode({self.id_periode}, {self.date_debut}, {self.date_fin})"

    class Meta:
        db_table = "periode"


class Semaine(models.Model):
    id_semaine = models.AutoField(primary_key=True)
    id_periode = models.ForeignKey(Periode, on_delete=models.CASCADE)
    date_debut = models.DateField()
    date_fin = models.DateField()

    def __str__(self):
        return f"Semaine({self.id_semaine}, {self.id_periode}, {self.date_debut}, {self.date_fin})"

    class Meta:
        db_table = "semaine"


class Creneau(models.Model):
    id_creneau = models.AutoField(primary_key=True)
    jour = models.IntegerField(default=2, validators=[
                               MaxValueValidator(5), MinValueValidator(1)])
    heure_debut = models.TimeField(
        validators=[MaxValueValidator("18:00"), MinValueValidator("08:00")])

    def __str__(self):
        return f"Creneau({self.id_creneau}, {self.jour}, {self.heure_debut})"

    class Meta:
        db_table = "creneau"
        unique_together = (("jour", "heure_debut"),)


class Eleve(models.Model):
    num_etu = models.CharField(primary_key=True, max_length=50)
    nom = models.CharField(max_length=50)
    prenom = models.CharField(max_length=50)
    groupe = models.CharField(max_length=50)

    def __str__(self):
        return f"Eleve({self.num_etu}, {self.nom}, {self.prenom}, {self.groupe})"

    class Meta:
        db_table = "eleve"


class Matiere(models.Model):
    id_matiere = models.AutoField(primary_key=True)
    nom_matiere = models.CharField(max_length=50)

    def __str__(self):
        return f"Matiere({self.id_matiere}, {self.nom_matiere})"

    class Meta:
        db_table = "matiere"


class Professeur(models.Model):
    id_prof = models.CharField(max_length=50, primary_key=True)
    nom_prof = models.CharField(max_length=50)
    prenom_prof = models.CharField(max_length=50)
    email_prof = models.CharField(max_length=500)
    mdp_provisoire_prof = models.CharField(max_length=50, default="")

    def __str__(self):
        return f"Professeur({self.id_prof}, {self.nom_prof}, {self.prenom_prof}, {self.email_prof})"

    class Meta:
        db_table = "professeur"


class EnseigneMatiere(models.Model):
    id_prof = models.ForeignKey(Professeur, on_delete=models.CASCADE)
    id_matiere = models.ForeignKey(Matiere, on_delete=models.CASCADE)
    id_periode = models.ForeignKey(Periode, on_delete=models.CASCADE)

    def __str__(self):
        return f"EnseigneMatiere({self.id_prof}, {self.id_matiere}, {self.id_periode})"

    class Meta:
        db_table = "enseigne_matiere"
        unique_together = (("id_prof", "id_matiere", "id_periode"),)

class Soutien(models.Model):
    id_soutien = models.AutoField(primary_key=True)
    id_semaine = models.ForeignKey(Semaine, on_delete=models.CASCADE)
    id_matiere = models.ForeignKey(Matiere, on_delete=models.CASCADE,null=True)
    id_creneau = models.ForeignKey(Creneau, on_delete=models.CASCADE,null=True)

    def __str__(self):
        return f"Soutien({self.id_soutien}, {self.id_semaine}, {self.id_matiere}, {self.id_creneau})"

    class Meta:
        db_table = "soutien"


class ParticiperSoutienEleve(models.Model):
    id_soutien = models.ForeignKey(Soutien, on_delete=models.CASCADE)
    num_etu = models.ForeignKey(Eleve, on_delete=models.CASCADE)
    commentaire = models.CharField(max_length=800)

    def __str__(self):
        return f"ParticiperSoutienEleve({self.id_soutien}, {self.num_etu}, {self.commentaire})"

    class Meta:
        db_table = "participersoutieneleve"


class ParticiperSoutienProfesseur(models.Model):
    id_soutien = models.ForeignKey(Soutien, on_delete=models.CASCADE)
    num_prof = models.ForeignKey(Professeur, on_delete=models.CASCADE)
    disponibilite = models.BooleanField(default=False)
    organise = models.BooleanField(default=False)

    def __str__(self):
        return f"ParticiperSoutienProfesseur({self.id_soutien}, {self.num_prof}, {self.disponibilite}, {self.organise})"

    class Meta:
        db_table = "participersoutienprofesseur"
