import java.sql.*;
import java.util.ArrayList;
import java.util.List;

public class EntrepotBD {
    private ConnexionMySQL connexion;
    private Statement st;
    public EntrepotBD(ConnexionMySQL connexion){
        this.connexion = connexion;
    }
   
    //    Ecrire une fonction pour obtenir le plus grand num ́ero utilis ́e pour identifier un article.
    public int maxCodeArticle(){
        int max = 0;
        try {
            st = connexion.getConnexion().createStatement();
            ResultSet rs = st.executeQuery("SELECT MAX(reference) FROM ARTICLE");
            rs.next();
            max = rs.getInt(1);
            st.close();}
        catch (SQLException e) {
            System.out.println("Erreur SQL");
            System.out.println(e.getMessage());
        }
        return max;
    }
    // 2. Ecrire une fonction qui prend en param`etre un num ́ero et retourne l’article de la base
    // de donn ́ees qui a ce num ́ero.
    public Article getArticle(int reference){
        Article art=null;
        try {
            st = connexion.getConnexion().createStatement();
            ResultSet rs = st.executeQuery("SELECT * FROM ARTICLE WHERE reference = " + reference);
            rs.next();
            art = new Article(rs.getInt(1), rs.getString(2), rs.getDouble(3));
            st.close();
        } catch (SQLException e) {
            System.out.println("Erreur SQL");
            System.out.println(e.getMessage());
        }
        return art;
    }
    // 3. Ecrire une fonction pour obtenir l’article qui a le plus grand identifiant.
    public Article getArticleMax(){
        Article art = null;
        try {
            st = connexion.getConnexion().createStatement();
            ResultSet rs = st.executeQuery("SELECT * FROM ARTICLE WHERE reference = (SELECT MAX(reference) FROM ARTICLE)");
            rs.next();
            art = new Article(rs.getInt(1), rs.getString(2), rs.getDouble(3));
            st.close();
        } catch (SQLException e) {
            System.out.println("Erreur SQL");
            System.out.println(e.getMessage());
        }
        return art;
    }
    // 4. Ecrire une fonction qui retourne la liste des articles.
    public List<Article> getArticles(){
        List<Article> articles = new ArrayList<>();
        try {
            st = connexion.getConnexion().createStatement();
            ResultSet rs = st.executeQuery("SELECT * FROM ARTICLE");
            while (rs.next()){
                articles.add(new Article(rs.getInt(1), rs.getString(2), rs.getDouble(3)));
            }
            st.close();
        } catch (SQLException e) {
            System.out.println("Erreur SQL");
            System.out.println(e.getMessage());
        }
        return articles;
    }   
    // 5. Ecrire une proc ́edure pour afficher tous les entrepˆots tri ́es par d ́epartement avec pour
    // chaque d ́epartement, le nombre d’entrepˆots qu’a le d ́epartement.
    public String afficheEntrepots(){
        String deptprec ="";
        int cpt_ent=0;
        String res ="";
        try {
            st = connexion.getConnexion().createStatement();
            ResultSet rs = st.executeQuery("SELECT * FROM ENTREPOT ORDER BY departement");
            while (rs.next()){
                if (deptprec.equals("")){
                    deptprec=rs.getString(3);
                }
                if (!rs.getString(3).equals(deptprec)){
                    res+="Departement " + deptprec + " a :"+cpt_ent+" entrepots \n";
                    cpt_ent=0;
                }
                deptprec=rs.getString(3);
                res+=rs.getInt(1) + " " + rs.getString(2) + " " + rs.getString(3)+"\n";
                cpt_ent++;
            }
            res+="Departement " + deptprec + " a :"+cpt_ent+" entrepots \n";
            st.close();
        } catch (SQLException e) {
            System.out.println("Erreur SQL");
            System.out.println(e.getMessage());
        }
        return res;
    }
    // 6. Ecrire une proc ́edure qui pour un num ́ero d’article, affiche la liste des entrepˆot dispo-
    // sant de cet article avec leur quantit ́e disponible.
    public String afficheEntrepotsArticle(int reference){
        String res ="";
        try {
            st = connexion.getConnexion().createStatement();
            ResultSet rs = st.executeQuery("SELECT * FROM STOCKER WHERE reference = " + reference);
            while (rs.next()){
                ResultSet rsent = st.executeQuery("SELECT * FROM ENTREPOT WHERE code = " + rs.getInt(2));
                rsent.next();
                Entrepot ent = new Entrepot(rsent.getInt(1), rsent.getString(2), rsent.getString(3));
                // ResultSet rsart = st.executeQuery("SELECT * FROM ARTICLE WHERE reference = " + rs.getInt(1));
                // rsart.next();
                // Article art = new Article(rsart.getInt(1), rsart.getString(2), rsart.getInt(3));
                res+= ent.toString() + " a l'article demandé en " + rs.getInt(3) + " exemplaires\n";
            }
            st.close();
        } catch (SQLException e) {
            System.out.println("Erreur SQL");
            System.out.println(e.getMessage());
        }
        return res;
    }
    // 7. Ecrire une proc ́edure qui pour un num ́ero d’entrepˆot, affiche la liste des articles (avec
    // leur quantit ́e) disponibles dans l’entrepˆot.
    public String afficheArticlesEntrepot(int code){
        String res ="Dans l'entrepot " + code + " il y a :\n";
        try {
            st = connexion.getConnexion().createStatement();
            ResultSet rs = st.executeQuery("SELECT * FROM STOCKER WHERE code = " + code);
            while (rs.next()){
                ResultSet rsart = st.executeQuery("SELECT * FROM ARTICLE WHERE reference = " + rs.getInt(1));
                rsart.next();
                Article art = new Article(rsart.getInt(1), rsart.getString(2), rsart.getDouble(3));
                res+= art.toString() + " est disponible en " + rs.getInt(3) + " exemplaires\n";
            }
            st.close();
        } catch (SQLException e) {
            System.out.println("Erreur SQL");
            System.out.println(e.getMessage());
        }
        return res;
    }
    // 8. Ecrire une fonction qui retourne la valeur contenue dans un entrepˆot donn ́e
    public int valeurEntrepot(int code){
        int res = 0;
        try {
            st = connexion.getConnexion().createStatement();
            ResultSet rs = st.executeQuery("SELECT * FROM STOCKER WHERE code = " + code);
            while (rs.next()){
                ResultSet rsart = st.executeQuery("SELECT * FROM ARTICLE WHERE reference = " + rs.getInt(1));
                rsart.next();
                Article art = new Article(rsart.getInt(1), rsart.getString(2), rsart.getDouble(3));
                res+= art.getPrix() * rs.getInt(3);
            }
            st.close();
        } catch (SQLException e) {
            System.out.println("Erreur SQL");
            System.out.println(e.getMessage());
        }
        return res;
    }
    //     1. Ecrire une fonction qui permet de stocker un nouvel article dans la table article ou
    // de modifier le prix d’un article d ́ej`a existant. Par exemple si l’article est a=(123,
    // "tuile17x27", 3.55) alors majArticle(a) modifiera le prix de l’article 123 s’il
    // existe et qu’il correspond `a ’tuile 17x27’, si ne nom n’est pas ’tuile17x27’ afficher
    // un message d’erreur, si l’article 123 n’est pas dans la base ajouter un nouvel article
    // en prenant comme r ́ef ́erence la plus grande des r ́ef ́erences pr ́esentes dans la base plus
    // 1 `a la place de 123. La fonction retournera la r ́ef ́erence de l’article cr ́e ́e ou modifi ́e (-1
    // si erreur).
    public int majArticle(Article art){
        int res = -1;
        try {
            st = connexion.getConnexion().createStatement();
            ResultSet rs = st.executeQuery("SELECT * FROM ARTICLE WHERE reference = " + art.getReference()+" AND libelle = '"+art.getLibelle()+"'");
            if (rs.next()){
                st.executeUpdate("UPDATE ARTICLE SET prix = " + art.getPrix() + " WHERE reference = " + art.getReference());
                res = art.getReference();
            } else {
                ResultSet rs2 = st.executeQuery("SELECT MAX(reference) FROM ARTICLE");
                rs2.next();
                int ref = rs2.getInt(1) + 1;
                st.executeUpdate("INSERT INTO ARTICLE VALUES (" + ref + ", '" + art.getLibelle() + "', " + art.getPrix() + ")");
                res = ref;
            }
            st.close();
        } catch (SQLException e) {
            System.out.println("Erreur SQL");
            System.out.println(e.getMessage());
        }
        return res;
    }
    // 2. Ecrire une fonction qui ajoute un entrepˆot dans la base de donn ́ees. La fonction
    // retournera l’identifiant de l’entrepˆot ajout ́e, -1 si erreur. Attention aux contrainte :
    // on ne veut pas avoir plusieurs entrepˆots avec le mˆeme nom dans le mˆeme d ́epartement,
    // et on ne veut pas plus de trois entrepˆots dans un mˆeme d ́epartement.
    public int ajouteEntrepot(Entrepot ent){
        int res = -1;
        try {
            st = connexion.getConnexion().createStatement();
                    ResultSet rs3 = st.executeQuery("SELECT MAX(code) FROM ENTREPOT");
                    rs3.next();
                    int code = rs3.getInt(1) + 1;
                    st.executeUpdate("INSERT INTO ENTREPOT VALUES (" + code + ", '" + ent.getNom() + "', '" + ent.getDepartement() + "')");
                    res = code;
                
            
            st.close();}
            catch (SQLException e) {
                System.out.println("Erreur SQL");
                System.out.println(e.getMessage());
        }
        return res;
    }

    // 3. Ecrire une fonction entrerStock(refA int, codeE int, qte int) qui augmente
    // le stock de l’article refA dans l’entrepˆot codeE de qte. Retourne la nouvelle quantit ́e
    // de l’article (-1) quand l’article ou l’entrepˆot n’existe pas.
    public int entrerStock(int refA, int codeE, int qte){
        int res = -1;
        try {
            st = connexion.getConnexion().createStatement();
            ResultSet rs = st.executeQuery("SELECT * FROM ARTICLE WHERE reference = " + refA);
            if (rs.next()){
                ResultSet rs2 = st.executeQuery("SELECT * FROM ENTREPOT WHERE code = " + codeE);
                if (rs2.next()){
                    ResultSet rs3 = st.executeQuery("SELECT * FROM STOCKER WHERE reference = " + refA + " AND code = " + codeE);
                    if (rs3.next()){
                        st.executeUpdate("UPDATE STOCKER SET quantite = " + (rs3.getInt(3) + qte) + " WHERE reference = " + refA + " AND code = " + codeE);
                        res = rs3.getInt(3) + qte;
                    } else {
                        st.executeUpdate("INSERT INTO STOCKER VALUES (" + refA + ", " + codeE + ", " + qte + ")");
                        res = qte;
                    }
                } else {
                    System.out.println("Cet entrepot n'existe pas");
                }
            } else {
                System.out.println("Cet article n'existe pas");
            }
            st.close();
        } catch (SQLException e) {
            System.out.println("Erreur SQL");
            System.out.println(e.getMessage());
        }
        return res;
    }
    // 4. Ecrire une fonction sortirStock(refA int, codeE int, qte int) qui diminue le
    // stock de l’article refA dans l’entrepˆot codeE de qte. La quantit ́e `a sortir est limit ́ee
    // `a la quantit ́e pr ́esente. Retourne la quantit ́e r ́eellement sortie
    public int sortirStock(int refA, int codeE, int qte){
        int res = 0;
        try {
            st = connexion.getConnexion().createStatement();
            ResultSet rs = st.executeQuery("SELECT * FROM ARTICLE WHERE reference = " + refA);
            if (rs.next()){
                ResultSet rs2 = st.executeQuery("SELECT * FROM ENTREPOT WHERE code = " + codeE);
                if (rs2.next()){
                    ResultSet rs3 = st.executeQuery("SELECT * FROM STOCKER WHERE reference = " + refA + " AND code = " + codeE);
                    if (rs3.next()){
                        if (rs3.getInt(3) >= qte){
                            st.executeUpdate("UPDATE STOCKER SET quantite = " + (rs3.getInt(3) - qte) + " WHERE reference = " + refA + " AND code = " + codeE);
                            res = qte;
                        } else {
                            st.executeUpdate("UPDATE STOCKER SET quantite = " + 0 + " WHERE reference = " + refA + " AND code = " + codeE);
                            res = rs3.getInt(3);
                            System.out.println("Il n'y a pas assez de stock");
                        }
                    } else {
                        System.out.println("Cet entrepot ne contient pas cet article");
                    }
                } else {
                    System.out.println("Cet entrepot n'existe pas");
                }
            } else {
                System.out.println("Cet article n'existe pas");
            }
            st.close();
        } catch (SQLException e) {
            System.out.println("Erreur SQL");
            System.out.println(e.getMessage());
        }
        return res;
    }
}