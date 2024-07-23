from django.test import TestCase
from django.core.exceptions import ValidationError
from .models import Sondage, RepSondage
from GestionSoutien.models import Eleve, Semaine


class SondageModelTest(TestCase):
    def setUp(self):
        # Création d'une instance Semaine nécessaire pour les tests
        self.semaine = Semaine.objects.create(
            id_periode=None, date_debut="2024-01-01", date_fin="2024-01-08")

    def test_sondage_creation(self):
        # Test de la création d'un objet Sondage
        sondage = Sondage.objects.create(id_semaine=self.semaine)
        # Vérification du nombre d'objets Sondage
        self.assertEqual(Sondage.objects.count(), 1)
        # Vérification de la représentation textuelle de l'objet
        self.assertEqual(
            str(sondage), f"Sondage({sondage.id_sond}, {self.semaine})")


class RepSondageModelTest(TestCase):
    def setUp(self):
        # Création d'instances nécessaires pour les tests
        self.semaine = Semaine.objects.create(
            id_periode=None, date_debut="2024-01-01", date_fin="2024-01-08")
        self.eleve = Eleve.objects.create(
            num_etu="12345", nom="Doe", prenom="John", groupe="A")
        self.sondage = Sondage.objects.create(id_semaine=self.semaine)

    def test_repsondage_creation(self):
        # Test de la création d'un objet RepSondage
        rep_sondage = RepSondage.objects.create(
            id_sondage=self.sondage, num_etu=self.eleve, matiere_voulue="Mathematics", volontaire="Oui", commentaire="Test commentaire")
        # Vérification du nombre d'objets RepSondage
        self.assertEqual(RepSondage.objects.count(), 1)
        # Vérification de la représentation textuelle de l'objet
        self.assertEqual(
            str(rep_sondage), f"RepSondage(Oui, {self.sondage}, {self.eleve}, Mathematics, Test commentaire)")

    def test_repsondage_invalid_volontaire(self):
        # Test de création d'un RepSondage avec une valeur de volontaire invalide, cela devrait lever une ValidationError
        with self.assertRaises(ValidationError):
            RepSondage.objects.create(
                id_sondage=self.sondage, num_etu=self.eleve, matiere_voulue="Mathematics", volontaire="Invalid", commentaire="Test commentaire")

    def test_repsondage_empty_commentaire(self):
        # Test de la création d'un RepSondage avec un commentaire vide
        rep_sondage = RepSondage.objects.create(
            id_sondage=self.sondage, num_etu=self.eleve, matiere_voulue="Mathematics", volontaire="Oui", commentaire="")
        # Vérification du nombre d'objets RepSondage
        self.assertEqual(RepSondage.objects.count(), 1)
        # Vérification de la représentation textuelle de l'objet avec un commentaire vide
        self.assertEqual(
            str(rep_sondage), f"RepSondage(Oui, {self.sondage}, {self.eleve}, Mathematics, )")
