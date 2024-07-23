from django.test import TestCase
from django.core.exceptions import ValidationError
from .models import ParamDef, CreneauDef
from GestionSoutien.models import Creneau


class ParamDefModelTest(TestCase):
    def test_unique_constraint(self):
        ParamDef.objects.create()

        # Tentative de créer une deuxième entrée, cela devrait lever une ValidationError
        with self.assertRaises(ValidationError):
            param_def = ParamDef()
            param_def.full_clean()
            param_def.save()

    def test_str_representation(self):
        param_def = ParamDef.objects.create()
        self.assertEqual(str(param_def), f"ParamDef({param_def.id_param})")


class CreneauDefModelTest(TestCase):
    def test_unique_constraint(self):
        # Créer un nouveau ParamDef pour chaque test
        param_def = ParamDef.objects.create()

        # Créer un nouveau Creneau pour chaque test
        creneau = Creneau.objects.create(jour=1, heure_debut="08:00")

        CreneauDef.objects.create(id_creneau=creneau, id_param=param_def)

        # Tentative de créer une deuxième entrée avec les mêmes clés étrangères, cela devrait lever une ValidationError
        with self.assertRaises(ValidationError):
            creneau_def = CreneauDef(id_creneau=creneau, id_param=param_def)
            creneau_def.save()

    def test_unique_together_constraint(self):
        # Créer un nouveau ParamDef pour chaque test
        param_def1 = ParamDef.objects.create()
        param_def2 = ParamDef.objects.create()

        creneau1 = Creneau.objects.create(jour=1, heure_debut="08:00")

        # Créer une entrée initiale avec les clés étrangères
        creneau_def1 = CreneauDef.objects.create(
            id_creneau=creneau1, id_param=param_def1)

        # Tentative de créer une deuxième entrée avec les mêmes clés étrangères, cela devrait lever une ValidationError
        with self.assertRaises(ValidationError):
            CreneauDef.objects.create(
                id_creneau=creneau1, id_param=param_def1)

        # Créer une entrée avec une autre combinaison de clés étrangères, cela devrait fonctionner
        creneau2 = Creneau.objects.create(jour=2, heure_debut="10:00")
        creneau_def2 = CreneauDef.objects.create(
            id_creneau=creneau2, id_param=param_def2)

        # Vous pouvez également tester si la création de la deuxième entrée est réussie
        self.assertIsNotNone(creneau_def2)
