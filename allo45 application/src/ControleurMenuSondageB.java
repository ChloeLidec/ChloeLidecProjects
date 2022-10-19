import javafx.event.ActionEvent;
import javafx.event.EventHandler;
//controleur menu analyste
public class ControleurMenuSondageB implements EventHandler<ActionEvent>{
    private FenetreAnalyste vue;



    public ControleurMenuSondageB(FenetreAnalyste vue){
        this.vue=vue;
    }

    @Override
    public void handle(ActionEvent actionEvent) {
        this.vue.popupNom();
        }
    }