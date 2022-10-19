import javafx.event.ActionEvent;
import javafx.event.EventHandler;

public class ControleurBoutPol implements EventHandler<ActionEvent>{
    
    private Pendu appli;
    public ControleurBoutPol(Pendu appli){
        this.appli = appli;
    }

    @Override
    public void handle(ActionEvent event){
        this.appli.changePolice();
    }
}