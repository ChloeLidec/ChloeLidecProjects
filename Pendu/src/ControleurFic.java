import javafx.event.ActionEvent;
import javafx.event.EventHandler;

public class ControleurFic implements EventHandler<ActionEvent>{
    
    private Pendu appli;
    public ControleurFic(Pendu appli){
        this.appli = appli;
    }

    @Override
    public void handle(ActionEvent event){
        this.appli.changeFicSource2();
    }
}