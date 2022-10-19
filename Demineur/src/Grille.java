import java.util.List;
import java.util.ArrayList;

public class Grille{
    /**
     * attributs pour la grille
     */
    private int hauteur, largeur, nbBombes, nbrevelees, nbmarques;
    /**
     * le plateau de cases
     */
    private List<Case> plateau;
    /**
     * 
     * @param hauteur
     * @param largeur
     * @param nbBombes
     */
    public Grille(int hauteur, int largeur, int nbBombes){
        this.hauteur = hauteur;
        this.largeur = largeur;
        this.nbBombes = nbBombes;
        this.nbrevelees = 0;
        this.nbmarques = 0;
        this.plateau = new ArrayList<>();
        for(int ind=0; ind < hauteur * largeur; ++ind){
            plateau.add(new Case());
        }
        for(int haut=0 ; haut < hauteur; haut++){
            for(int large=0 ; large < largeur; large++){
                Case caseActu = plateau.get(largeur * haut + large);
                if (haut == 0 && large == 0){
                    caseActu.ajouteCaseVoisine(plateau.get((largeur * (haut+1) + large)));
                    caseActu.ajouteCaseVoisine(plateau.get((largeur * (haut+1) + large+1)));
                    caseActu.ajouteCaseVoisine(plateau.get((largeur * haut + large)+1));
                }
                else if(haut == 0 && large == largeur - 1){
                    caseActu.ajouteCaseVoisine(plateau.get((largeur * haut + large)-1));
                    caseActu.ajouteCaseVoisine(plateau.get((largeur * (haut+1) + large)));
                    caseActu.ajouteCaseVoisine(plateau.get((largeur * (haut+1) + large-1)));
                }
                else if(haut == hauteur-1 && large == 0){
                    caseActu.ajouteCaseVoisine(plateau.get((largeur * (haut-1) + large)));
                    caseActu.ajouteCaseVoisine(plateau.get((largeur * (haut-1) + large+1)));
                    caseActu.ajouteCaseVoisine(plateau.get((largeur * haut + large)+1));
                }
                else if(haut == hauteur-1 && large == largeur - 1){
                    caseActu.ajouteCaseVoisine(plateau.get((largeur * haut + large)-1));
                    caseActu.ajouteCaseVoisine(plateau.get((largeur * (haut-1) + large-1)));
                    caseActu.ajouteCaseVoisine(plateau.get((largeur * (haut-1) + large)));
                }
                else if (haut == 0){
                    caseActu.ajouteCaseVoisine(plateau.get((largeur * haut + large)-1));
                    caseActu.ajouteCaseVoisine(plateau.get((largeur * haut + large)+1));
                    caseActu.ajouteCaseVoisine(plateau.get((largeur * (haut+1) + large)));
                    caseActu.ajouteCaseVoisine(plateau.get((largeur * (haut+1) + large+1)));
                    caseActu.ajouteCaseVoisine(plateau.get((largeur * (haut+1) + large-1)));
                }
                else if (haut == hauteur - 1){
                    caseActu.ajouteCaseVoisine(plateau.get((largeur * haut + large)-1));
                    caseActu.ajouteCaseVoisine(plateau.get((largeur * haut + large)+1));
                    caseActu.ajouteCaseVoisine(plateau.get((largeur * (haut-1) + large)));
                    caseActu.ajouteCaseVoisine(plateau.get((largeur * (haut-1) + large+1)));
                    caseActu.ajouteCaseVoisine(plateau.get((largeur * (haut-1) + large-1)));
                }
                else if (large == 0){
                    caseActu.ajouteCaseVoisine(plateau.get((largeur * (haut+1) + large)));
                    caseActu.ajouteCaseVoisine(plateau.get((largeur * (haut+1) + large+1)));
                    caseActu.ajouteCaseVoisine(plateau.get((largeur * haut + large)+1));
                    caseActu.ajouteCaseVoisine(plateau.get((largeur * (haut-1) + large)));
                    caseActu.ajouteCaseVoisine(plateau.get((largeur * (haut-1) + large+1)));
                }
                else if (large == largeur - 1){
                    caseActu.ajouteCaseVoisine(plateau.get((largeur * haut + large)-1));
                    caseActu.ajouteCaseVoisine(plateau.get((largeur * (haut-1) + large)));
                    caseActu.ajouteCaseVoisine(plateau.get((largeur * (haut-1) + large-1)));
                    caseActu.ajouteCaseVoisine(plateau.get((largeur * (haut+1) + large)));
                    caseActu.ajouteCaseVoisine(plateau.get((largeur * (haut+1) + large-1)));
                }
                else{
                    caseActu.ajouteCaseVoisine(plateau.get((largeur * haut + large)-1));
                    caseActu.ajouteCaseVoisine(plateau.get((largeur * haut + large)+1));
                    caseActu.ajouteCaseVoisine(plateau.get((largeur * (haut-1) + large)));
                    caseActu.ajouteCaseVoisine(plateau.get((largeur * (haut-1) + large+1)));
                    caseActu.ajouteCaseVoisine(plateau.get((largeur * (haut-1) + large-1)));
                    caseActu.ajouteCaseVoisine(plateau.get((largeur * (haut+1) + large)));
                    caseActu.ajouteCaseVoisine(plateau.get((largeur * (haut+1) + large+1)));
                    caseActu.ajouteCaseVoisine(plateau.get((largeur * (haut+1) + large-1)));
                }
            }
        }
    }
    /**
     * initialisation de la grille sans creer une nouvelle grille
     */
    public void init(){
        this.nbrevelees = 0;
        this.nbmarques = 0;
        this.plateau = new ArrayList<>();
        for(int ind=0; ind < this.hauteur * this.largeur; ++ind){
            this.plateau.add(new Case());
        }
        for(int haut=0 ; haut < this.hauteur; haut++){
            for(int large=0 ; large < this.largeur; large++){
                Case caseActu = this.plateau.get(this.largeur * haut + large);
                if (haut == 0 && large == 0){
                    caseActu.ajouteCaseVoisine(plateau.get((this.largeur * (haut+1) + large)));
                    caseActu.ajouteCaseVoisine(plateau.get((this.largeur * (haut+1) + large+1)));
                    caseActu.ajouteCaseVoisine(plateau.get((this.largeur * haut + large)+1));
                }
                else if(haut == 0 && large == this.largeur - 1){
                    caseActu.ajouteCaseVoisine(plateau.get((this.largeur * haut + large)-1));
                    caseActu.ajouteCaseVoisine(plateau.get((this.largeur * (haut+1) + large)));
                    caseActu.ajouteCaseVoisine(plateau.get((this.largeur * (haut+1) + large-1)));
                }
                else if(haut == this.hauteur-1 && large == 0){
                    caseActu.ajouteCaseVoisine(plateau.get((this.largeur * (haut-1) + large)));
                    caseActu.ajouteCaseVoisine(plateau.get((this.largeur * (haut-1) + large+1)));
                    caseActu.ajouteCaseVoisine(plateau.get((this.largeur * haut + large)+1));
                }
                else if(haut == this.hauteur-1 && large == this.largeur - 1){
                    caseActu.ajouteCaseVoisine(plateau.get((this.largeur * haut + large)-1));
                    caseActu.ajouteCaseVoisine(plateau.get((this.largeur * (haut-1) + large-1)));
                    caseActu.ajouteCaseVoisine(plateau.get((this.largeur * (haut-1) + large)));
                }
                else if (haut == 0){
                    caseActu.ajouteCaseVoisine(plateau.get((this.largeur * haut + large)-1));
                    caseActu.ajouteCaseVoisine(plateau.get((this.largeur * haut + large)+1));
                    caseActu.ajouteCaseVoisine(plateau.get((this.largeur * (haut+1) + large)));
                    caseActu.ajouteCaseVoisine(plateau.get((this.largeur * (haut+1) + large+1)));
                    caseActu.ajouteCaseVoisine(plateau.get((this.largeur * (haut+1) + large-1)));
                }
                else if (haut == this.hauteur - 1){
                    caseActu.ajouteCaseVoisine(plateau.get((this.largeur * haut + large)-1));
                    caseActu.ajouteCaseVoisine(plateau.get((this.largeur * haut + large)+1));
                    caseActu.ajouteCaseVoisine(plateau.get((this.largeur * (haut-1) + large)));
                    caseActu.ajouteCaseVoisine(plateau.get((this.largeur * (haut-1) + large+1)));
                    caseActu.ajouteCaseVoisine(plateau.get((this.largeur * (haut-1) + large-1)));
                }
                else if (large == 0){
                    caseActu.ajouteCaseVoisine(plateau.get((this.largeur * (haut+1) + large)));
                    caseActu.ajouteCaseVoisine(plateau.get((this.largeur * (haut+1) + large+1)));
                    caseActu.ajouteCaseVoisine(plateau.get((this.largeur * haut + large)+1));
                    caseActu.ajouteCaseVoisine(plateau.get((this.largeur * (haut-1) + large)));
                    caseActu.ajouteCaseVoisine(plateau.get((this.largeur * (haut-1) + large+1)));
                }
                else if (large == this.largeur - 1){
                    caseActu.ajouteCaseVoisine(plateau.get((this.largeur * haut + large)-1));
                    caseActu.ajouteCaseVoisine(plateau.get((this.largeur * (haut-1) + large)));
                    caseActu.ajouteCaseVoisine(plateau.get((this.largeur * (haut-1) + large-1)));
                    caseActu.ajouteCaseVoisine(plateau.get((this.largeur * (haut+1) + large)));
                    caseActu.ajouteCaseVoisine(plateau.get((this.largeur * (haut+1) + large-1)));
                }
                else{
                    caseActu.ajouteCaseVoisine(plateau.get((this.largeur * haut + large)-1));
                    caseActu.ajouteCaseVoisine(plateau.get((this.largeur * haut + large)+1));
                    caseActu.ajouteCaseVoisine(plateau.get((this.largeur * (haut-1) + large)));
                    caseActu.ajouteCaseVoisine(plateau.get((this.largeur * (haut-1) + large+1)));
                    caseActu.ajouteCaseVoisine(plateau.get((this.largeur * (haut-1) + large-1)));
                    caseActu.ajouteCaseVoisine(plateau.get((this.largeur * (haut+1) + large)));
                    caseActu.ajouteCaseVoisine(plateau.get((this.largeur * (haut+1) + large+1)));
                    caseActu.ajouteCaseVoisine(plateau.get((this.largeur * (haut+1) + large-1)));
                }
            }
        }
    }
    /**
     * retourne le nombre de ligne
     * @return le nombre de ligne
     */
    public int getNombreDeLignes(){return this.hauteur;}
    /**
     * retourne le nombre de colonne
     * @return le nombre colonne
     */
    public int getNombreDeColonnes(){return this.largeur;}
    /**
     * retourne le nombre de bombes sur le plateau
     * @return le nombre de bombes
     */
    public int getNombreDeBombes(){return this.nbBombes;}
    /**
     * retourne le nombre de marques sur le plateau
     * @return le nombre de marques
     */
    public int getNombreDeMarques(){return this.nbmarques;}
    /**
     * retourne le nombre de case decouvertes sur le plateau
     * @return le nombre de case decouvertes
     */
    public int getNombreDeCasesRevelees(){return this.nbrevelees;}
    /**
     * retourne la case à la position (i,j)
     * lève deux exceptions en cas de nombre invalide
     * @param i le numéro de la ligne
     * @param j le numéro de colonne
     * @return la case aux cordonnées (i,j)
     */
    public Case getCase(int i, int j)throws IndLigneMauvException,IndColMauvException{
        if(i<0 || i > this.hauteur-1){throw new IndLigneMauvException("Veuillez entrer un nombre entre "+0+" et "+(this.largeur-1));}
        else if(j<0 || j > this.largeur-1){throw new IndColMauvException("Veuillez entrer un nombre entre "+0+" et "+(this.hauteur-1));}
        else{return this.plateau.get(this.largeur * i + j);}}
    /**
     * indique si la partie est perdue
     * * @return si la partie est perdue
     */
    public boolean estPerdue(){
        boolean res = false;
        for(Case caseactuel: plateau){
            if(caseactuel.estBombe() && caseactuel.estRevelee()){
                res = true;
            }
        }
        return res;
    }
    /**
     * indique si la partie est gagnée
     * @return si la partie est gagnée
     */
    public boolean estGagnee(){
        return !(this.estPerdue()) && this.nbmarques == nbBombes && this.nbrevelees == (this.largeur * this.hauteur - this.nbBombes);
    }
    /**
     * marque la case en x y ou la demarque si elle est deja marquee
     * @param x ligne
     * @param y colonne
     */
    public void marqueCase(int x, int y){
        try{
            if(this.getCase(x, y).estMarquee()){
                this.getCase(x, y).marquer();
                this.nbmarques--;
            }
            else if (!(this.getNombreDeMarques()+1 > this.getNombreDeBombes())){
                this.getCase(x, y).marquer();
                this.nbmarques++;
            }}
    
            
            
        catch(CaseReveleeException e){System.out.println(e.getMessage());}
        catch(IndLigneMauvException e){System.out.println(e.getMessage());}
        catch(IndColMauvException e){System.out.println(e.getMessage());}
    }
    /**
     * revele la case en x y
     * enleve la marque si elle est deja marquee
     * @param x ligne
     * @param y colonne
     */
    public void decouvrirCase(int x, int y){
        try{
            if(this.nbrevelees==0){//si c'est la 1ere case révélée on init les bombes
                this.initBombes(x, y);
            }
            if(this.getCase(x, y).estMarquee()){//on enleve l'éventuelle marque
                this.getCase(x, y).marquer();
                this.nbmarques--;
            }
            int marques = this.getCase(x, y).reveler();
            int nbrev=0;
            for(Case caseplat: this.plateau){
                if(caseplat.estRevelee()){
                    nbrev++;
                }
            }
            this.nbmarques-= marques;
            this.nbrevelees = nbrev;
        }
        catch(CaseReveleeException e){System.out.println(e.getMessage());}
        catch(IndLigneMauvException e){System.out.println(e.getMessage());}
        catch(IndColMauvException e){System.out.println(e.getMessage());}
    }
    /**
     *affiche le jeu
     */
    public void affiche(){
        System.out.println("JEU DU DEMINEUR\n");
        String plateau = "   ";
        for(int c=0 ; c<this.getNombreDeColonnes(); c++){
            plateau += "  " +c+" ";
        }
        plateau += "\n  |";
        for(int i=0; i<this.getNombreDeColonnes();i++){
            plateau+= "‾‾‾|";
        }
        for(int l=0 ; l<this.getNombreDeLignes(); l++){
            if(l !=0){
                plateau += "  |";
                for(int i=0; i<this.getNombreDeColonnes();i++){
                    plateau+= "   |";
            }}
            plateau +=" \n"+ l+" |"; 
            for (int c=0 ; c<this.getNombreDeColonnes(); c++){
                try{
                Case caseActu = this.getCase(l, c);
                if (caseActu.estRevelee()){
                    if (caseActu.estBombe()){
                        plateau += " @ |";
                    }
                    else {plateau += " "+caseActu.getNbBombesVoisines()+" |";}
                }
                else if (caseActu.estMarquee()){
                    plateau += " ? |";
                }else{ plateau += "   |";}
                
            }
            catch(IndLigneMauvException e){System.out.println(e.getMessage());}
            catch(IndColMauvException e){System.out.println(e.getMessage());}
          
            }
            plateau += " \n  |";
            for(int i=0; i<this.getNombreDeColonnes();i++){
                plateau+= "___|";
            }
            plateau+= "\n";
        }
        plateau += "\nNombres de bombes : "+this.nbBombes;
        plateau += "\nNombres de cases marquées : "+this.nbmarques;
        plateau += "\nNombres de cases découvertes : "+this.nbrevelees;


        System.out.println(plateau);

        
    }
    /**
     * ajoutee
     *initialise les bombes
     */
    public void initBombes(int x, int y){
        int pos = x * this.largeur + y;
        int indbombe = 0;
        while (indbombe<this.getNombreDeBombes()){
            int ind =(int)(Math.random()* this.plateau.size());
            if(!(pos == ind)){
                if(!(this.plateau.get(ind).estBombe())){
                    this.plateau.get(ind).ajouteBombe();
                    indbombe++;
                }
            }
        }
    }
    /**
     * ajoutee
     * @param case1
     * @return la position dans la liste de la case
     */
    public int posCase(Case case1){
        return this.plateau.indexOf(case1);
    }
}