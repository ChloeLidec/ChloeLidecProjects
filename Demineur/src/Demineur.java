import java.util.Scanner;

public class Demineur{
    /**
     * executable
     * @param Args
     */
    public static void main(String [] Args){
        Scanner scan = new Scanner(System.in);
        int hauteur = -1;
        int largeur = -1;
        int nbbombe = -1;
        while(hauteur<0){
        try{//demande de lignes
            Scanner scan2 = new Scanner(System.in);
            System.out.println("Entrez le nombre de lignes");
            hauteur = scan2.nextInt();
            if(hauteur < 0){
                System.out.println("Indiquer un nombre supérieur à 0");
            }
        }catch(Exception IME){
            System.out.println("Entrez un nombre");
        }}
        while(largeur<0){
        try{//demande de colonnes
            Scanner scan2 = new Scanner(System.in);
            System.out.println("Entrez le nombre de colonnes");
            largeur = scan2.nextInt();
            if(largeur < 0){
                System.out.println("Indiquer un nombre supérieur à 0");
            }
        }catch(Exception IME){
            System.out.println("Entrez un nombre");
        }}
        while(nbbombe<0){
        try{//demande nb bombes
            System.out.println("Entrez le nombre de bombes");
            Scanner scan2 = new Scanner(System.in);
            nbbombe = scan2.nextInt();
            if(nbbombe < 0){
                System.out.println("Indiquer un nombre supérieur à 0");
            }else if( nbbombe >= largeur * hauteur){
                nbbombe = -1;
                System.out.println("Indiquer un nombre inférieur à : "+ (largeur * hauteur));
            }
        }catch(Exception IME){
            System.out.println("Entrez un nombre");
        }}
        Grille jeu = new Grille(hauteur,largeur,nbbombe);
        jeu.affiche();
        while(!(jeu.estPerdue()) && !(jeu.estGagnee())){//demande d instructions en boucle
            int ligne = -1;
            int colonne = -1;
            String action = "";
            boolean estvalide = true;
            boolean estfini = false;
            while(!estfini){
            System.out.println("Entrez une instruction de la forme R 3 2 ou M 3 2 pour réveler/marquer une case à la ligne 3 et la colonne 2");
            int i = 2;
            String car = scan.nextLine();
            car += " ";
            if(!(car.charAt(0) == 'M' || car.charAt(0) == 'R')){
                estvalide = false;
                System.out.println("Les instructions disponibles sont R pour révéler et M pour marquer");
            }else{
                action = car;
            }
            try{
                String chaine = "";
                while(!(car.charAt(i)==' ')){
                    chaine+= car.charAt(i);
                    ++i;
                }
                ++i;
                ligne = Integer.parseInt(chaine);
            }catch(NumberFormatException exce){
                estvalide = false;
                System.out.println("Veuillez entrer un nombre en deuxième paramètre");
            }
            catch(IndexOutOfBoundsException exce){
                estvalide = false;
                System.out.println("Veuillez rentrer une instruction au format R 3 2 ou M 3 2");
            }
            try{
                String chaine = "";
                while(!(car.charAt(i)==' ') && i<car.length()){
                    chaine+= car.charAt(i);
                    ++i;
                }
                colonne = Integer.parseInt(chaine);
            }catch(NumberFormatException exce){
                estvalide = false;
                System.out.println("Veuillez rentrez un nombre en troisième paramètre");
            }
            catch(IndexOutOfBoundsException exce){
                estvalide = false;
                System.out.println("Veuillez entrer une instruction au format R 3 2 ou M 3 2");
            }
            if(estvalide){
                if(action.charAt(0) == 'M'){
                    jeu.marqueCase(ligne, colonne);
                }
                else{
                    jeu.decouvrirCase(ligne, colonne);
                }
                jeu.affiche();
                estfini = true;
            }
            estvalide=true;
            }
        }
        scan.close();
        if(jeu.estPerdue()){
            System.out.println("Vous avez perdu la partie");
        }else{
            System.out.println("Vous avez gagné la partie");
        }
    }
}
