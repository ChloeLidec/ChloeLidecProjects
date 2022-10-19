import javafx.event.EventHandler; 
import javafx.scene.input.MouseEvent; 
import javafx.scene.input.MouseButton;
import javafx.scene.control.Alert;
import javafx.scene.control.ButtonType;
import java.util.Optional;

public class ControleurBouton implements EventHandler<MouseEvent>{
    /**
     * bouton à connecter
     */
    private Bouton bouton;
    /**
     * case à connecter
     */
    private Case laCase;
    /**
     * application
     */
    private DemineurGraphique demineur;
    /**
     * modèle
     */
    private Grille lePlateau;
    /**
     * constructeur
     * @param bouton
     * @param laCase
     * @param demineur
     * @param lePlateau
     */
    public ControleurBouton(Bouton bouton, Case laCase, DemineurGraphique demineur, Grille lePlateau){
        this.bouton = bouton;
        this.laCase = laCase;
        this.demineur = demineur;
        this.lePlateau = lePlateau;
    }
    /**
     * override du handle 
     */
    @Override
    public void handle(MouseEvent e){
        if (e.getButton() == MouseButton.PRIMARY){//clic gauche on decouvre
            int pos = this.lePlateau.posCase(this.laCase);
            this.lePlateau.decouvrirCase((int)pos/this.lePlateau.getNombreDeColonnes(), (int)pos%this.lePlateau.getNombreDeColonnes());
            this.bouton.setDisable(true);
        }
        if(e.getButton() == MouseButton.SECONDARY){// clic droit on marque ou demarque
                int pos = this.lePlateau.posCase(this.laCase);
                this.lePlateau.marqueCase((int)pos/this.lePlateau.getNombreDeColonnes(), (int)pos%this.lePlateau.getNombreDeColonnes());
            }
        //mise a jour de l app
        this.demineur.maj_des_infos();
        this.demineur.maj_de_la_grille();
        
        if (this.lePlateau.estPerdue()){// on verif si la partie est perdue
            Alert alert = new Alert(Alert.AlertType.CONFIRMATION,"Vous avez perdu !\nVoulez-vous rejouer ?",ButtonType.YES, ButtonType.NO);
            alert.setTitle("Attention");
            Optional<ButtonType> rep = alert.showAndWait();
            
            if (rep.isPresent() && rep.get()==ButtonType.YES){// dans le cas où on recomence on réinitialise tout
                this.lePlateau.init();
                this.demineur.reinitGrille();
                this.demineur.maj_de_la_grille();
                this.demineur.maj_des_infos();
            }
            else{//sinon on désactive tout
                this.demineur.desactiver();
            }            
        }
        else if(this.lePlateau.estGagnee()){//partie gagnée
            Alert alert = new Alert(Alert.AlertType.CONFIRMATION,"Vous avez gagnée !\nVoulez-vous rejouer ?",ButtonType.YES, ButtonType.NO);
            alert.setTitle("Attention");
            Optional<ButtonType> rep = alert.showAndWait();
            
            if (rep.isPresent() && rep.get()==ButtonType.YES){// dans le cas où on recomence on réinitialise tout
                this.lePlateau.init();
                this.demineur.reinitGrille();
                this.demineur.maj_de_la_grille();
                this.demineur.maj_des_infos();
            }
            else{//sinon on désactive tout
                this.demineur.desactiver();
            }
        }
    }
}
