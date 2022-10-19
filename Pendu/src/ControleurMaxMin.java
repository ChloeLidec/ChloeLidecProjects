import javafx.event.ActionEvent;
import javafx.event.EventHandler;

public class ControleurMaxMin implements EventHandler<ActionEvent>{
    
    private Pendu appli;
    public ControleurMaxMin(Pendu appli){
        this.appli = appli;
    }

    @Override
    public void handle(ActionEvent event){
        this.appli.changeLongeur();
    }
}