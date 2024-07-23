from django.db import models
from GestionSoutien.models import Creneau

# Create your models here.


class ParamDef(models.Model):
    id_param = models.AutoField(primary_key=True)
    # Liste qui stocke les ids des profs
    profs_mails = models.CharField(max_length=500, default="")

    def validate_unique(self, exclude=None):
        from django.core.exceptions import ValidationError, NON_FIELD_ERRORS
        if ParamDef.objects.count() != 0:
            raise ValidationError(
                {NON_FIELD_ERRORS: ["Il ne peut y avoir qu'une seule entrée"]})

    def __str__(self):
        return f"ParamDef({self.id_param})"

    class Meta:
        db_table = 'params'


class CreneauDef(models.Model):
    id_creneau = models.ForeignKey(Creneau, on_delete=models.CASCADE)
    id_param = models.ForeignKey(ParamDef, on_delete=models.CASCADE)

    def validate_unique(self, exclude=None):
        from django.core.exceptions import ValidationError, NON_FIELD_ERRORS
        if CreneauDef.objects.count() != 0:
            raise ValidationError(
                {NON_FIELD_ERRORS: ["Il ne peut y avoir qu'une seule entrée"]})

    def __str__(self):
        return f"CreneauDef({self.id_creneau}, {self.id_param})"

    class Meta:
        db_table = 'creneaudef'
        unique_together = (('id_creneau', 'id_param'),)
