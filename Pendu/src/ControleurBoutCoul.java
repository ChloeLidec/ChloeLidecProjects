import javafx.event.ActionEvent;
import javafx.event.EventHandler;
import javafx.scene.control.ColorPicker;

public class ControleurBoutCoul implements EventHandler<ActionEvent>{
    
    private Pendu appli;
    public ControleurBoutCoul(Pendu appli){
        this.appli = appli;
    }

    @Override
    public void handle(ActionEvent event) {
        ColorPicker cp= (ColorPicker)event.getSource();
        this.appli.changeCoul(cp.getValue());
    }
}