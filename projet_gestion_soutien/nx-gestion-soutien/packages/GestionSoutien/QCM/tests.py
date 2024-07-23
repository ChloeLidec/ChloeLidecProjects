from django.test import TestCase
from django.core.exceptions import ValidationError
from .models import QCM, ResultatQCM
from GestionSoutien.models import Eleve, Matiere, Semaine


class QCMModelTest(TestCase):
    def setUp(self):
        # Création d'instances nécessaires pour les tests
        self.matiere = Matiere.objects.create(nom_matiere="Mathematics")
        self.semaine = Semaine.objects.create(
            id_periode=None, date_debut="2024-01-01", date_fin="2024-01-08")

    def test_qcm_creation(self):
        # Test de la création d'un objet QCM
        qcm = QCM.objects.create(
            nom_qcm="Test QCM", id_matiere=self.matiere, id_semaine=self.semaine)
        # Vérification du nombre d'objets QCM
        self.assertEqual(QCM.objects.count(), 1)
        # Vérification de la représentation textuelle de l'objet
        self.assertEqual(
            str(qcm), f"QCM({qcm.id_qcm}, Test QCM, {self.matiere}, {self.semaine})")


class ResultatQCMModelTest(TestCase):
    def setUp(self):
        # Création d'instances nécessaires pour les tests
        self.matiere = Matiere.objects.create(nom_matiere="Mathematics")
        self.semaine = Semaine.objects.create(
            id_periode=None, date_debut="2024-01-01", date_fin="2024-01-08")
        self.eleve = Eleve.objects.create(
            num_etu="12345", nom="Doe", prenom="John", groupe="A")

        self.qcm = QCM.objects.create(
            nom_qcm="Test QCM", id_matiere=self.matiere, id_semaine=self.semaine)

    def test_resultat_qcm_creation(self):
        # Test de la création d'un objet ResultatQCM
        resultat_qcm = ResultatQCM.objects.create(
            id_qcm=self.qcm, num_etu=self.eleve, note=13)
        # Vérification du nombre d'objets ResultatQCM
        self.assertEqual(ResultatQCM.objects.count(), 1)
        # Vérification de la représentation textuelle de l'objet
        self.assertEqual(
            str(resultat_qcm), f"ResultatQCM({self.qcm}, {self.eleve}, 13)")

    def test_resultat_qcm_invalid_note(self):
        # Test de création d'un ResultatQCM avec une note invalide, cela devrait lever une ValidationError
        with self.assertRaises(ValidationError):
            ResultatQCM.objects.create(
                id_qcm=self.qcm, num_etu=self.eleve, note=-10)

    def test_resultat_qcm_note_out_of_range(self):
        # Test de création d'un ResultatQCM avec une note hors de la plage valide, cela devrait lever une ValidationError
        with self.assertRaises(ValidationError):
            ResultatQCM.objects.create(
                id_qcm=self.qcm, num_etu=self.eleve, note=110)
