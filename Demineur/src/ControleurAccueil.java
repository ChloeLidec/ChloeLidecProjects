import javafx.event.ActionEvent;
import javafx.event.EventHandler;
import javafx.scene.control.TextField;

public class ControleurAccueil implements EventHandler<ActionEvent> {
    private DemineurGraphique vue;

    /**
     * Permet l'initialisation du Controleur
     * @param vue la vue sur laquelle intéragir
     */
    public ControleurAccueil(DemineurGraphique vue){
        this.vue = vue;
    }

    /**
     * Les actions à effectuer lorsqu'il est activer
     */
    @Override
    public void handle(ActionEvent actionEvent) {
        boolean bon = true;
        TextField texthauteur = this.vue.getHauteur();
        TextField textlargeur = this.vue.getLargeur();
        TextField nbbombe = this.vue.getNbBombes();
        int hauteur=0, largeur=0, nbBombes=0;
        try{
            hauteur = Integer.parseInt(texthauteur.getText());
            if(hauteur<0){
                texthauteur.setStyle("-fx-border-color: red; -fx-border-width: 2px;");
                bon = false;
            }else{
                texthauteur.setStyle(null);
            }
        }catch(NumberFormatException se){
            texthauteur.setStyle("-fx-border-color: red; -fx-border-width: 2px;");
            bon = false;
        }try{
            largeur = Integer.parseInt(textlargeur.getText());
            if(largeur<0){
                textlargeur.setStyle("-fx-border-color: red; -fx-border-width: 2px;");
                bon = false;
            }else{
                textlargeur.setStyle(null);
            }
        }catch(NumberFormatException se){
            textlargeur.setStyle("-fx-border-color: red; -fx-border-width: 2px;");
            bon = false;
        }
        try{
            nbBombes = Integer.parseInt(nbbombe.getText());
            if(nbBombes<0 || nbBombes>= hauteur*largeur){
                nbbombe.setStyle("-fx-border-color: red; -fx-border-width: 2px;");
                bon = false;
            }else{
                nbbombe.setStyle(null);
            }
        }catch(NumberFormatException se){
            nbbombe.setStyle("-fx-border-color: red; -fx-border-width: 2px;");
            bon = false;
        }
        if(bon){
            this.vue.setGrille(new Grille(hauteur, largeur, nbBombes));
            this.vue.modeJeux();
        }
    }
}
