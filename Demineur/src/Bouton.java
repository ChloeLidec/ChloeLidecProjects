import javafx.scene.control.Button; 
import javafx.scene.image.ImageView;
import javafx.scene.paint.Color;
import javafx.scene.image.Image;
import javafx.scene.control.Label;

public class Bouton extends Button{
    /**
     * la case associée au bouton
     */
    private Case laCase;
    /**
     * constructeur du bouton
     * @param laCase case à connecter
     */
    public Bouton(Case laCase){
        super();
        this.setPrefWidth(50);
        this.setPrefHeight(50);
        this.laCase = laCase;
        if (laCase.estRevelee() && laCase.estBombe())
            ajouteImage("bombe.png");
        else if (laCase.estRevelee() && laCase.estBombe())
            ajouteImage("bombe.png");
        
    }
    /**
     * ajoute une image sur le bouton en fonction du fichierImage
     * @param fichierImage
     */
    private void ajouteImage(String fichierImage){
        try{
                Image image = new Image(fichierImage);
                ImageView iv = new ImageView();
                iv.setImage(image);
                iv.setFitWidth(20);
                iv.setPreserveRatio(true);
                this.setGraphic(iv);
            }
        catch(Exception e){
            this.setText(laCase.getAffichage());
        }
    }

    /**
     * mise à jour de l'affichage des boutons 
     */
    public void maj(){
        if (this.laCase.estRevelee()){//case revelee on reinitialise l affichage et desactive
            this.setDisable(true);
            this.setGraphic(new Label(""));}
        else{
            this.setDisable(false);}//sinon on active
        if (this.laCase.getAffichage().equals("?")){//si case marquee on met drapeau
            this.ajouteImage("drapeau.png");
        }
        else if (this.laCase.getAffichage().equals("@")){//si bombe on met bombe
            this.ajouteImage("bombe.png");
        }
        /* cas de nb de bombes voisines on enleve les eventuelles images
         * on met le nb de bombes voisines et on set la couleur
         */
        else if (this.laCase.getAffichage().equals("0")){
            this.setGraphic(new Label(""));
            this.setText(this.laCase.getAffichage());
            this.setTextFill(Color.CHARTREUSE);
        }
        else if (this.laCase.getAffichage().equals("1")){
            this.setGraphic(new Label(""));
            this.setText(this.laCase.getAffichage());
            this.setTextFill(Color.OLIVE);
        }
        else if (this.laCase.getAffichage().equals("2")){
            this.setGraphic(new Label(""));
            this.setText(this.laCase.getAffichage());
            this.setTextFill(Color.SANDYBROWN);
        }
        else if (this.laCase.getAffichage().equals("3")){
            this.setGraphic(new Label(""));
            this.setText(this.laCase.getAffichage());
            this.setTextFill(Color.ORANGERED);
        }
        else if (this.laCase.getAffichage().equals("4")){
            this.setGraphic(new Label(""));
            this.setText(this.laCase.getAffichage());
            this.setTextFill(Color.RED);
        }
        else if (this.laCase.getAffichage().equals("5")){
            this.setGraphic(new Label(""));
            this.setText(this.laCase.getAffichage());
            this.setTextFill(Color.CRIMSON);
        }
        else if (this.laCase.getAffichage().equals("6")){
            this.setGraphic(new Label(""));
            this.setText(this.laCase.getAffichage());
            this.setTextFill(Color.FIREBRICK);
        }
        else if (this.laCase.getAffichage().equals("7")){
            this.setGraphic(new Label(""));
            this.setText(this.laCase.getAffichage());
            this.setTextFill(Color.DARKRED);
        }
        else if (this.laCase.getAffichage().equals("8")){
            this.setGraphic(new Label(""));
            this.setText(this.laCase.getAffichage());
            this.setTextFill(Color.MAROON);
        }
        else{//cas ou enleve le drapeau 
            this.setText(this.laCase.getAffichage());
            this.setGraphic(new Label(""));}
    }
}
