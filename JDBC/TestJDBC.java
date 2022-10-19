import java.util.List;

public class TestJDBC {
    private ConnexionMySQL connexion;
    public TestJDBC(){
        connexion = new ConnexionMySQL("servinfo-mariadb", "DBlidec", "lidec", "lidec");
    }
    public void affiche(){
        if (connexion.getConnecte()){
            System.out.println("Connecte");
        } else {
            System.out.println("Non connecte");
        }
    }

    public void maxCodeArticle(){
        EntrepotBD entrepotBD = new EntrepotBD(connexion);
        System.out.println("Max code article: " + entrepotBD.maxCodeArticle());
    }
    public void getArticle(int code){
        EntrepotBD entrepotBD = new EntrepotBD(connexion);
        Article art = entrepotBD.getArticle(code);
        System.out.println("Article " + code + ": " + art);
    }
    public void getArticleMax(){
        EntrepotBD entrepotBD = new EntrepotBD(connexion);
        Article art = entrepotBD.getArticleMax();
        System.out.println("Article max: " + art);
    }   
    public void getArticles(){
        EntrepotBD entrepotBD = new EntrepotBD(connexion);
        List<Article> articles = entrepotBD.getArticles();
        System.out.println("Articles: " + articles);
    }
    public void afficheEntrepots(){
        EntrepotBD entrepotBD = new EntrepotBD(connexion);
        System.out.println(entrepotBD.afficheEntrepots());
    }
    public void afficheEntrepotsArt(int code){
        EntrepotBD entrepotBD = new EntrepotBD(connexion);
        System.out.println(entrepotBD.afficheEntrepotsArticle(code));
    }
    public void afficheArticlesEntrepot(int code){
        EntrepotBD entrepotBD = new EntrepotBD(connexion);
        System.out.println(entrepotBD.afficheArticlesEntrepot(code));
    }
    public void valeurEntrepot(int code){
        EntrepotBD entrepotBD = new EntrepotBD(connexion);
        System.out.println(entrepotBD.valeurEntrepot(code));
    }
    public void majArticle(Article art){
        EntrepotBD entrepotBD = new EntrepotBD(connexion);
        System.out.println("ref art:"+entrepotBD.majArticle(art));
        this.getArticles();
    }
    public void ajouteEntrepot(Entrepot ent){
        EntrepotBD entrepotBD = new EntrepotBD(connexion);
        System.out.println("id ent: "+entrepotBD.ajouteEntrepot(ent));
        this.afficheEntrepots();
    }
    public void entrerStock(int refA, int codeEnt, int qte){
        EntrepotBD entrepotBD = new EntrepotBD(connexion);
        this.afficheEntrepotsArt(refA);
        System.out.println("qte entrée: "+entrepotBD.entrerStock(refA, codeEnt, qte));
        this.afficheEntrepotsArt(refA);
    }
    public void sortirStock(int refA, int codeEnt, int qte){
        EntrepotBD entrepotBD = new EntrepotBD(connexion);
        this.afficheEntrepotsArt(refA);
        System.out.println("qte sortie: "+entrepotBD.sortirStock(refA, codeEnt, qte));
        this.afficheEntrepotsArt(refA);
    }
    public static void main(String[] args) {
        TestJDBC test = new TestJDBC();
        if (test.connexion.getConnecte()){
            // test.maxCodeArticle();
            // test.getArticle(1);
            // test.getArticleMax();
            // test.getArticles();
            // test.afficheEntrepots();
            // test.afficheEntrepotsArt(1);
            // test.afficheArticlesEntrepot(1);
            // test.valeurEntrepot(1);
            // Article art = new Article(126, "testbis", 1.5);
            // test.majArticle(art);
            // Article artcgt = new Article(126, "test", 150);
            // test.majArticle(artcgt);
            Entrepot ent = new Entrepot(5, "testent","Cher");
            Entrepot entref = new Entrepot(1, "testref","Cher");
            Entrepot entrefdep = new Entrepot(6, "testdep","Loiret");
            test.ajouteEntrepot(ent);
            test.ajouteEntrepot(entref);
            test.ajouteEntrepot(entrefdep);
            Entrepot entb = new Entrepot(7, "testent","Cher");
            Entrepot entrefb = new Entrepot(1, "testdep","Loiret");
            Entrepot entrefdepb = new Entrepot(6, "testnom","Loiret");
            test.ajouteEntrepot(entb);
            test.ajouteEntrepot(entrefb);
            test.ajouteEntrepot(entrefdepb);
            // test.entrerStock(1, 4, 10);
            // test.entrerStock(1, 1, -5);
            // test.entrerStock(8, 2, 50);
            // test.entrerStock(1, 10, 100);
            // test.sortirStock(1, 4, 25);
            // test.sortirStock(1, 1, 15);
            // test.sortirStock(8, 2, 50);
            // test.sortirStock(1, 3, 100);

        } else {
            System.out.println("Non connecte");
        }
    }
}