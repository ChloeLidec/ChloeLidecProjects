import java.util.ArrayList;
import java.util.List;

public class Case{
    /**
     * si la case est une bombe
     */
    private boolean bombe;
    /**
     * etat de la bombe
     */
    private String etat;
    /**
     * liste de voisins
     */
    private List<Case> voisins;
    /**
     * constructeur
     */
    public Case(){
        this.bombe = false;
        this.etat = " ";
        this.voisins = new ArrayList<>();
    }

    /**
     * indique si la case est une bombe
     * @return si la case est une bombe
     */
    public boolean estBombe(){return  this.bombe;}

    /**
     * indique si la case est revélé
     * @return si la case est revélé
     */
    public boolean estRevelee(){return  (!(this.etat.equals(" ")) && !(this.etat.equals("?")));}

    /**
     * indique si la case est marquée
     * @return si la case est marquée
     */
    public boolean estMarquee(){return  this.etat.equals("?");}

    /**
     *  la case devient une bombe
     */
    public void ajouteBombe(){this.bombe = true;}

    /**
     * mets l'état soit sur bombe soit sur le nb de bombes voisines
     * revele les cases voisines dans le cas ou la case est à 0 bombes voisines
     * @return le nombres de marques retirées
     */
    public int reveler()throws CaseReveleeException{
        int cpt=0;
        if (this.estRevelee()){throw new CaseReveleeException("La case est déja révélée");}
        if (this.bombe){this.etat = "@";}
        else {
            int nbbombesvois = this.getNbBombesVoisines();
            this.etat = "" + nbbombesvois;//on met le nb de case voisines en affichage
            if(nbbombesvois == 0){//si zero cases vois on revele les voisins
                for(Case casevois: this.voisins){
                    if(!casevois.estRevelee()){
                        if (casevois.estMarquee()){cpt++;}//si la case est marquee on ajoute 1 au compteur
                        cpt+=casevois.reveler();//on revele la case en récursif
                        
                    }
                }
                this.etat = "0";//on met l'état à 0
            }
        }
        return cpt;
    }
    
    /**
     * l'état devient marqué ou demarqué si c'est déjà marqué
     */
    public void marquer()throws CaseReveleeException{
        if (this.estRevelee()){throw new CaseReveleeException("La case est déja révélée");}
        else if (this.estMarquee()){this.etat = " ";}
        else{this.etat = "?";}
    }

    /**
     * indique la liste de cases voisines
     * @return la liste de cases voisines
     */
    public List<Case> getCasesVoisines(){return this.voisins;}

    /**
     * ajoute la case aux cases voisines
     */
    public void ajouteCaseVoisine(Case uneCase){voisins.add(uneCase);}

    /**
     * Parcours les cases voisines et le nombre de bombe
     * @return le nombre de bombe
     */

    public int getNbBombesVoisines(){
        int nbBombe = 0;
        for (Case uneCase : this.voisins){
            if (uneCase.estBombe()){nbBombe += 1;}
        }
        return nbBombe;
    }
    
    /**
     * affiche l'etat de la bombe
     * @return l'etat de la bombe
     */
    public String getAffichage(){return this.etat;}
}
