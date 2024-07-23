from django.test import TestCase
from django.core.exceptions import ValidationError
from .models import Periode, Semaine, Creneau, Eleve, Matiere, Professeur, EnseigneMatiere


class PeriodeModelTest(TestCase):
    def test_periode_creation(self):
        # Test de la création d'une instance de Periode
        periode = Periode.objects.create(
            date_debut="2024-01-01", date_fin="2024-01-15")
        # Vérification du nombre d'instances de Periode
        self.assertEqual(Periode.objects.count(), 1)
        # Vérification de la représentation textuelle de l'instance
        self.assertEqual(
            str(periode), f"Periode({periode.id_periode}, 2024-01-01, 2024-01-15)")


class SemaineModelTest(TestCase):
    def test_semaine_creation(self):
        # Création d'une instance de Periode pour les tests
        periode = Periode.objects.create(
            date_debut="2024-01-01", date_fin="2024-01-15")
        # Test de la création d'une instance de Semaine
        semaine = Semaine.objects.create(
            id_periode=periode, date_debut="2024-01-01", date_fin="2024-01-08")
        # Vérification du nombre d'instances de Semaine
        self.assertEqual(Semaine.objects.count(), 1)
        # Vérification de la représentation textuelle de l'instance
        self.assertEqual(
            str(semaine), f"Semaine({semaine.id_semaine}, {periode}, 2024-01-01, 2024-01-08)")


class CreneauModelTest(TestCase):
    def test_creneau_creation(self):
        # Test de la création d'une instance de Creneau
        creneau = Creneau.objects.create(jour=1, heure_debut="08:30")
        # Vérification du nombre d'instances de Creneau
        self.assertEqual(Creneau.objects.count(), 1)
        # Vérification de la représentation textuelle de l'instance
        self.assertEqual(
            str(creneau), f"Creneau({creneau.id_creneau}, 1, 08:30)")


class EleveModelTest(TestCase):
    def test_eleve_creation(self):
        # Test de la création d'une instance de Eleve
        eleve = Eleve.objects.create(
            num_etu="12345", nom="Doe", prenom="John", groupe="A")
        # Vérification du nombre d'instances de Eleve
        self.assertEqual(Eleve.objects.count(), 1)
        # Vérification de la représentation textuelle de l'instance
        self.assertEqual(str(eleve), f"Eleve(12345, Doe, John, A)")


class MatiereModelTest(TestCase):
    def test_matiere_creation(self):
        # Test de la création d'une instance de Matiere
        matiere = Matiere.objects.create(nom_matiere="Mathematics")
        # Vérification du nombre d'instances de Matiere
        self.assertEqual(Matiere.objects.count(), 1)
        # Vérification de la représentation textuelle de l'instance
        self.assertEqual(
            str(matiere), f"Matiere({matiere.id_matiere}, Mathematics)")


class ProfesseurModelTest(TestCase):
    def test_professeur_creation(self):
        # Test de la création d'une instance de Professeur
        professeur = Professeur.objects.create(
            id_prof="123", nom_prof="Smith", prenom_prof="Jane", email_prof="jane@example.com")
        # Vérification du nombre d'instances de Professeur
        self.assertEqual(Professeur.objects.count(), 1)
        # Vérification de la représentation textuelle de l'instance
        self.assertEqual(
            str(professeur), f"Professeur(123, Smith, Jane, jane@example.com)")


class EnseigneMatiereModelTest(TestCase):
    def test_enseigne_matiere_creation(self):
        # Création d'instances nécessaires pour les tests
        professeur = Professeur.objects.create(
            id_prof="123", nom_prof="Smith", prenom_prof="Jane", email_prof="jane@example.com")
        matiere = Matiere.objects.create(nom_matiere="Mathematics")
        periode = Periode.objects.create(
            date_debut="2024-01-01", date_fin="2024-01-15")

        # Test de la création d'une instance de EnseigneMatiere
        enseigne_matiere = EnseigneMatiere.objects.create(
            id_prof=professeur, id_matiere=matiere, id_periode=periode)
        # Vérification du nombre d'instances de EnseigneMatiere
        self.assertEqual(EnseigneMatiere.objects.count(), 1)
        # Vérification de la représentation textuelle de l'instance
        self.assertEqual(
            str(enseigne_matiere), f"EnseigneMatiere({professeur}, {matiere}, {periode})")
