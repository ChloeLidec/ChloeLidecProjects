public class Stocker{
    
    private Entrepot entrepot;
    private Article article;
    private int quantite;

    public Stocker(Entrepot entrepot, Article article, int quantite){
        this.entrepot = entrepot;
        this.article = article;
        this.quantite = quantite;
    }

    public Entrepot getEntrepot(){
        return this.entrepot;
    }   

    public Article getArticle(){
        return this.article;
    }

    public int getQuantite(){
        return this.quantite;
    }

    public String toString(){
        return "Stocker [entrepot=" + entrepot + ", article=" + article + ", quantite=" + quantite + "]";
    }
}