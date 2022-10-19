import javafx.event.ActionEvent;
import javafx.event.EventHandler;

public class ControleurParametres implements EventHandler<ActionEvent> {
    /**
     * modèle du jeu
     */
    private MotMystere modelePendu;
    /**
     * vue du jeu
     **/
    private Pendu vuePendu;

    /**
     * @param modelePendu modèle du jeu
     * @param vuePendu vue du jeu
     */
    public ControleurParametres(MotMystere modelePendu, Pendu vuePendu) {
        this.modelePendu=modelePendu;
        this.vuePendu=vuePendu;
    }


    /**
     * L'action consiste à retourner sur la page d'accueil. Il faut vérifier qu'il n'y avait pas une partie en cours
     * @param actionEvent l'événement action
     */
    @Override
    public void handle(ActionEvent actionEvent) {
        this.vuePendu.modeParametres();
    }
}
