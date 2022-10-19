public class Article{
    
    private int reference;
    private String libelle;
    private double prix;

    public Article(int reference, String libelle, double prix){
        this.reference = reference;
        this.libelle = libelle;
        this.prix = prix;
    }

    public int getReference(){
        return this.reference;
    }

    public String getLibelle(){
        return this.libelle;
    }

    public double getPrix(){
        return this.prix;
    }

    public String toString(){
        return "Article [reference=" + reference + ", libelle=" + libelle + ", prix=" + prix + "]";
    }
}