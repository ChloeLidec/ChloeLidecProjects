import java.util.ArrayList;
import java.util.Arrays;
import org.junit.*;
import static org.junit.Assert.assertEquals;
import static org.junit.Assert.assertTrue;
import static org.junit.Assert.assertFalse;

public class TestCase {

    private Case case1;
    private Case case2;
    private Case case3;
    private Case case4;

    /**
     * initialisation des cases
     */
    @Before
    public void initialisationCase(){
        this.case1 = new Case();
        case1.ajouteBombe();
        this.case2 = new Case();
        try{
        case2.marquer();}
        catch(CaseReveleeException e){System.err.println(e.getMessage());}
        this.case3 = new Case();
        this.case4 = new Case();
        case3.ajouteCaseVoisine(case1);
        case3.ajouteCaseVoisine(case4);
        
    }

    /**
     *verif que les cases s'initialisent bien 
     */
    @Test
    public void testInitCases(){
        //verif case cachées
        assertFalse(case1.estRevelee());
        assertFalse(case2.estRevelee());
        assertFalse(case3.estRevelee());
        assertFalse(case4.estRevelee());
        //verif bombes et marques
        assertTrue(case1.estBombe());
        assertTrue(case2.estMarquee());
        //verif voisins
        assertEquals(case3.getCasesVoisines(), Arrays.asList(case1,case4));
        assertEquals(case1.getCasesVoisines(), new ArrayList<>());
    }

    /**
     *verif que les bombes s'ajoutent correctement
     */
    @Test
    public void testAjouteBombe(){
        assertFalse(case2.estBombe());
        case2.ajouteBombe();
        assertTrue(case2.estBombe());
    }

    /**
     *test revelation de case
     * @throws CaseReveleeException
     */
    @Test
    public void testReveler() throws CaseReveleeException{
        case1.reveler();
        assertTrue(case1.estRevelee());
        assertEquals(case1.getAffichage(),"@");
        case2.reveler();
        assertTrue(case2.estRevelee());
        assertEquals(case2.getAffichage(),"0");
        case3.reveler();
        assertTrue(case3.estRevelee());
        assertEquals(case3.getAffichage(),"1");
    }

    /**
     * test si l excpetion est bien gérée et le message est le bon
     * @throws CaseReveleeException
     */
    @Test
    public void testCaseReveleeException() throws CaseReveleeException {
        case4.reveler();
        boolean thrown = false;
        boolean messOk = false;
        try {
            case4.marquer();;
        } 
        catch (CaseReveleeException e) {
            thrown = true;
            messOk = (e.getMessage().equals("La case est déja révélée"));
        }

        assertTrue(thrown);
        assertTrue(messOk);
    }
    /**
     * test marquage de case
     */
    @Test
    public void testMarquer(){
        assertEquals(case4.getAffichage()," ");
        try{
        case4.marquer();
        assertEquals(case4.getAffichage(),"?");
        assertFalse(case4.estRevelee());
        assertTrue(case4.estMarquee());}
        catch(CaseReveleeException e){System.err.println(e.getMessage());} 
    }

    /**
     *test nb de bombes voisines
     */
    @Test
    public void testBombesVois(){
        assertEquals(case4.getNbBombesVoisines(),0);
        assertEquals(case3.getNbBombesVoisines(),1);
    }
}