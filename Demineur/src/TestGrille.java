import org.junit.*;
import static org.junit.Assert.assertEquals;
import static org.junit.Assert.assertTrue;
import static org.junit.Assert.assertFalse;

public class TestGrille {
    
    private Grille grille1;
    private Grille grille2;
    private Grille grille3;
    private Grille grille4;
    /**
     * init des grilles
     */
    @Before
    public void initialisationGrille(){
        this.grille1 = new Grille(5, 5, 4);
        this.grille2 = new Grille(7, 6, 8);
        this.grille3 = new Grille(3, 5, 3);
        this.grille4 = new Grille(4, 4, 2);
    }

    /**
     * test initialisation grilles et get nblignes
     */
    @Test
    public void testInitNbGetLignes(){
        assertEquals(grille1.getNombreDeLignes(),5);
        assertEquals(grille2.getNombreDeLignes(),7);
        assertEquals(grille3.getNombreDeLignes(),3);
        assertEquals(grille4.getNombreDeLignes(),4);
    }

    /**
     *test initialisation grilles et get nbcolonnes
     */
    @Test
    public void testInitGetNbColonnes(){
        assertEquals(grille1.getNombreDeColonnes(),5);
        assertEquals(grille2.getNombreDeColonnes(),6);
        assertEquals(grille3.getNombreDeColonnes(),5);
        assertEquals(grille4.getNombreDeColonnes(),4);
    }

    /**
     * test initialisation grilles et get nbbombes
     */
    @Test
    public void testInitGetNbBombes(){
        assertEquals(grille1.getNombreDeBombes(),4);
        assertEquals(grille2.getNombreDeBombes(),8);
        assertEquals(grille3.getNombreDeBombes(),3);
        assertEquals(grille4.getNombreDeBombes(),2);
    }

    /**
     * test du marquage de case
     */
    @Test
    public void testMarquage(){
        assertEquals(grille1.getNombreDeMarques(),0);
        grille1.marqueCase(2, 3);
        grille1.marqueCase(0, 4);
        grille1.marqueCase(4, 3);
        grille1.marqueCase(2, 4);
        assertEquals(grille1.getNombreDeMarques(),4);
    }

    /**
     * test de exceptions de getCase()
     */
    @Test
    public void testExceptionGetCase(){
        boolean exLigne = false;
        boolean exCol = false;
        try { // exception ind ligne trop petit ou trop grand
            grille1.getCase(5,3);        } 
        catch(IndLigneMauvException e) {
            exLigne = (e.getMessage().equals("Veuillez entrer un nombre entre 0 et 4"));
        }
        catch (IndColMauvException e) {// on est obligé de mettre ce catch pour la compilation
            exCol = (e.getMessage().equals("Veuillez entrer un nombre entre 0 et 4"));
        }
        try {// exception ind col
            grille1.getCase(2,6);
        } 
        catch (IndColMauvException e) {
            exCol = (e.getMessage().equals("Veuillez entrer un nombre entre 0 et 4"));
        }
        catch(IndLigneMauvException e) {
            exLigne = (e.getMessage().equals("Veuillez entrer un nombre entre 0 et 4"));
        }
        assertTrue(exLigne);
        assertTrue(exCol);
    }

    /**
     * test revelages de cases
     */
    @Test
    public void testReveler(){
        assertEquals(grille1.getNombreDeCasesRevelees(),0);
        grille1.decouvrirCase(2, 3);
        grille1.decouvrirCase(0, 4);
        grille1.decouvrirCase(4, 3);
        grille1.decouvrirCase(2, 4);
        assertEquals(grille1.getNombreDeCasesRevelees(),4);
    }
    /**
     * test de perdre une partie
     */
    @Test
    public void testPerdu(){
        assertFalse(grille1.estPerdue());
        for(int haut=0 ; haut < grille1.getNombreDeLignes(); haut++){
            for(int large=0 ; large < grille1.getNombreDeColonnes(); large++){
                grille1.decouvrirCase(haut,large);
            }
        }
        assertTrue(grille1.estPerdue());
    }
    //on ne peut pas tester directement la victoire car le posage de bombes est aléatoire
}
