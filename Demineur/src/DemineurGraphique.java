import javafx.application.Application;
import javafx.scene.Scene;
import javafx.stage.Stage;
import javafx.scene.layout.Pane;
import javafx.scene.layout.BorderPane;
import javafx.scene.layout.GridPane;
import javafx.scene.layout.VBox;
import javafx.scene.control.Label;
import javafx.scene.control.Alert;
import javafx.scene.layout.HBox;
import javafx.geometry.Pos;
import javafx.scene.control.TextField;
import javafx.scene.control.Button;

import javafx.scene.Node;
public class DemineurGraphique extends Application {
    /**
     * modele
     */
    private Grille lePlateau;
    /**
     * pane d'infos changeables donc en attributs
     */
    private Pane infos;
    /**
     * grille mise à jour donc attribut
     */
    private GridPane grille;

    private BorderPane centre;

    private TextField textFieldHauteur;

    private TextField textFieldLargeur;

    private TextField textFieldNbBombes;
    
    private Button bouttonJeu;

    @Override
    public void init(){
        this.centre = new BorderPane();
        this.centre.setPrefSize(350, 350);
        this.textFieldHauteur = new TextField("5");
        this.textFieldLargeur = new TextField("5");
        this.textFieldNbBombes = new TextField("4");
        this.bouttonJeu = new Button("Lancer une partie");
        this.bouttonJeu.setOnAction(new ControleurAccueil(this));
        this.bouttonJeu.setAlignment(Pos.CENTER);
    }

    @Override
    public void start(Stage stage){
        this.centre.setCenter(this.accueil());
        Scene scene = new Scene(centre);
        stage.setTitle("Demineur");
        stage.setScene(scene);
        stage.show();
    }

    public VBox jeu(){
        VBox vbox = new VBox(20);
        //vbox.setAlignment(Pos.TOP_CENTER);
        this.grille = new GridPane();
        this.grille.setHgap(1);
        this.grille.setVgap(1);     
        for (int i = 0; i<this.lePlateau.getNombreDeLignes(); i++){
            for (int j=0; j<this.lePlateau.getNombreDeColonnes(); j++){
                try{
                Case laCase = this.lePlateau.getCase(i, j);
                Bouton b = new Bouton(laCase);
                b.setOnMouseClicked(new ControleurBouton(b, laCase, this, this.lePlateau));
                grille.add(b, j, i);}
                catch(IndLigneMauvException ex){
                    System.out.println(i);
                    System.out.println("1");
                    System.out.println(this.lePlateau.getNombreDeLignes());
                    Alert alert = new Alert(Alert.AlertType.INFORMATION,"Num ligne invalide");
                    alert.setTitle("Attention");
                    alert.showAndWait();}
                catch(IndColMauvException ex){
                    System.out.println(j);
                    System.out.println("2");
                    System.out.println(this.lePlateau.getNombreDeColonnes());
                    Alert alert = new Alert(Alert.AlertType.INFORMATION,"Num ligne invalide");
                    alert.setTitle("Attention");
                    alert.showAndWait();}
            }
        }
        this.infos = new VBox(); 
        vbox.getChildren().addAll(grille, infos);
        this.maj_des_infos();
        return vbox;
    }
    /**
     * reinitialisation grille en cas de relance
     */
    public void reinitGrille(){
        this.grille.getChildren().clear();
        for (int i = 0; i<this.lePlateau.getNombreDeLignes(); i++){
            for (int j=0; j<this.lePlateau.getNombreDeColonnes(); j++){
                try{
                Case laCase = this.lePlateau.getCase(i, j);
                Bouton b = new Bouton(laCase);
                b.setOnMouseClicked(new ControleurBouton(b, laCase, this, this.lePlateau));
                
                this.grille.add(b, j, i);}
                catch(IndLigneMauvException ex){
                    Alert alert = new Alert(Alert.AlertType.INFORMATION,"Num ligne invalide");
                    alert.setTitle("Attention");
                    alert.showAndWait();}
                catch(IndColMauvException ex){
                    Alert alert = new Alert(Alert.AlertType.INFORMATION,"Num ligne invalide");
                    alert.setTitle("Attention");
                    alert.showAndWait();}
            }
        }
    }
    /**
     * maj grille 
     */
    public void maj_de_la_grille(){
        for (Node b : this.grille.getChildren()){
            Bouton bb = (Bouton) b;
            bb.maj();
        }
    }
    /**
     * desactive la grille quand partie non relancée
     */
    public void desactiver(){
        for (Node b : this.grille.getChildren()){
            b.setDisable(true);
        }
    }
    /**
     * maj infos dans le pane d'infos
     */
    public void maj_des_infos(){
        this.infos.getChildren().clear();
        Label label1 = new Label("Nombres de bombes : " + this.lePlateau.getNombreDeBombes());
        Label label2 = new Label("Nombres de cases marquées : " + this.lePlateau.getNombreDeMarques() +"/"+this.lePlateau.getNombreDeBombes());
        Label label3 = new Label("Nombres de cases découvertes : " + this.lePlateau.getNombreDeCasesRevelees());
        this.infos.getChildren().addAll(label1, label2, label3);
    }
    /**
     * creer l'interface pour l'accueil
     * @return interface de l'accueil
     */
    public VBox accueil(){
        VBox accueil = new VBox(10);
        HBox hauteur = new HBox(10);
        HBox largeur = new HBox(10);
        HBox nbBombes = new HBox(10);
        HBox bouton = new HBox();
        hauteur.getChildren().addAll(new Label("nombre de ligne: "),this.textFieldHauteur);
        largeur.getChildren().addAll(new Label("nombre de colonne: "),this.textFieldLargeur);
        nbBombes.getChildren().addAll(new Label("nombre de bombes: "),this.textFieldNbBombes);
        hauteur.setAlignment(Pos.CENTER);
        largeur.setAlignment(Pos.CENTER);
        nbBombes.setAlignment(Pos.CENTER);
        bouton.getChildren().add(this.bouttonJeu);
        bouton.setAlignment(Pos.CENTER);
        accueil.getChildren().addAll(hauteur, largeur, nbBombes, bouton);
        return accueil;
    }
    /**
     * Retourne le TextField pour la hauteur
     * @return TextField de la hauteur
     */
    public TextField getHauteur(){return this.textFieldHauteur;}
    /**
     * Retourne le TextField pour la largeur
     * @return TextField de la largeur
     */
    public TextField getLargeur(){return this.textFieldLargeur;}
    /**
     * Retourne le TextField pour le nombre de bombes
     * @return TextField du nombre de bombe
     */
    public TextField getNbBombes(){return this.textFieldNbBombes;}
    /**
     * Permet de définir quel grille utilisé
     * @param grille
     */
    public void setGrille(Grille grille){this.lePlateau = grille;}
    /**
     * Permet de passer dans le mode jeux
     */
    public void modeJeux(){
        this.centre.setCenter(this.jeu());
    }
    public static void main(String args[]){
        Application.launch(args);
    }
}
