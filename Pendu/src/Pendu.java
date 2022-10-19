import javafx.application.Application;
import javafx.geometry.Insets;
import javafx.scene.text.Font;
import javafx.scene.text.FontWeight;
import javafx.stage.FileChooser;
import javafx.stage.Stage;
import javafx.geometry.Pos;
import javafx.scene.Scene;
import javafx.scene.control.*;
import javafx.scene.image.Image;
import javafx.scene.image.ImageView;
import javafx.scene.layout.*;
import javafx.scene.paint.Color;
import javafx.scene.text.Text;

import java.util.List;
import java.util.HashSet;
import java.io.File;
import java.util.ArrayList;


/**
 * Vue du jeu du pendu
 */
public class Pendu extends Application {
    /**
     * banniere du titre
     **/
    private BorderPane banniere;
    /**
     * modèle du jeu
     **/
    private MotMystere modelePendu;
    /**
     * Liste qui contient les images du jeu
     */
    private ArrayList<Image> lesImages;
    /**
     * Liste qui contient les noms des niveaux
     */    
    public List<String> niveaux;

    // les différents contrôles qui seront mis à jour ou consultés pour l'affichage
    /**
     * le dessin du pendu
     */
    private ImageView dessin;
    /**
     * le mot à trouver avec les lettres déjà trouvé
     */
    private Text motCrypte;
    /**
     * la barre de progression qui indique le nombre de tentatives
     */
    private ProgressBar pg;
    /**
     * le clavier qui sera géré par une classe à implémenter
     */
    private Clavier clavier;
    /**
     * le text qui indique le niveau de difficulté
     */
    private Text leNiveau;
    /**
     * le chronomètre qui sera géré par une clasee à implémenter
     */
    private Chronometre chrono;
    /**
     * le panel Central qui pourra être modifié selon le mode (accueil ou jeu)
     */
    private BorderPane panelCentral;
    /**
     * le bouton Paramètre / Engrenage
     */
    private Button boutonParametres;
    /**
     * le bouton Accueil / Maison
     */    
    private Button boutonMaison;
    /**
     * le bouton qui permet de (lancer ou relancer une partie
     */ 
    private Button bJouer;
    /**
     * le bouton Info
     */ 
    private Button boutInfo;
    /**
     * le texte exemple
     */ 
    private Text ex;
    /**
     * le fichier source
     */ 
    private String fichierMot;
    /**
     * le nombre min de lettres des mots
     */ 
    private int miniLet;
    /**
     * le nombre max de lettres des mots
     */ 
    private int maxLet;
    /**
     * vrai ou faux en fonction de si la dernière page ouverte est les paramètres
     */ 
    private boolean dernEstPar;
    /**
     * color picker
     */ 
    private ColorPicker colorP;
    /**
     * textfield police
     */ 
    private TextField tfP;
    /**
     * textfield max let
     */ 
    private TextField tfMax;
    /**
     * textfield min let
     */ 
    private TextField tfMin;
    /**
     * taille du mot du niveau et de texte ex
     */
    private int taillePolice;
    
    /**
     * initialise les attributs (créer le modèle, charge les images, crée le chrono ...)
     */    
    @Override
    public void init() {
        //initialisation dans cet ordre car param et commun ont besoin du modèle pour les controleurs
        //idem pour le bouton jouer
        this.initJeu();
        this.initParam();
        this.initCommun();
        this.bJouer = new Button("Lancer une partie");
        this.bJouer.setOnAction(new ControleurLancerPartie(this.modelePendu,this));
        this.panelCentral = new BorderPane();         
    }

    /**
     * initialisation communes a tout ex banniere
     */
    private void initCommun(){
        ImageView home = new ImageView("home.png");
        home.setFitHeight(35);
        home.setPreserveRatio(true);
        this.boutonMaison = new Button("",home);
        this.boutonMaison.setOnAction(new RetourAccueil(this.modelePendu, this));
        Tooltip mais = new Tooltip("Retour au menu");
        this.boutonMaison.setTooltip(mais);
        ImageView par = new ImageView("parametres.png");
        par.setFitHeight(35);
        par.setPreserveRatio(true);
        this.boutonParametres = new Button("",par);
        this.boutonParametres.setOnAction(new ControleurParametres(this.modelePendu, this));
        Tooltip para = new Tooltip("Paramètres");
        this.boutonParametres.setTooltip(para);
        ImageView inf = new ImageView("info.png");
        inf.setFitHeight(35);
        inf.setPreserveRatio(true);
        this.boutInfo = new Button("",inf);
        this.boutInfo.setOnAction(new ControleurInfos(this));
        Tooltip info = new Tooltip("Règles du jeu");
        this.boutInfo.setTooltip(info);
    }

    /**
     * initialisation param
     */
    private void initParam(){
        this.ex = new Text("exemple");
        this.ex.setFont(Font.font("Arial", this.taillePolice));
        this.dernEstPar=false;
        this.colorP= new ColorPicker();
        this.colorP.setOnAction(new ControleurBoutCoul(this));
        this.tfP = new TextField("20");
        this.tfMax= new TextField("10");
        this.tfMin= new TextField("3");
    }

    /**
     * initialisation jeu
     */
    private void initJeu(){
        this.taillePolice=20;
        this.miniLet=3;
        this.maxLet=10;
        this.fichierMot="/usr/share/dict/american-english";
        this.modelePendu = new MotMystere(this.fichierMot, this.miniLet, this.maxLet, MotMystere.FACILE, 10);
        this.lesImages = new ArrayList<Image>();
        this.chargerImages("/home/chloe1a/ihm-tp4/img");
        this.dessin= new ImageView(this.lesImages.get(0));
        this.pg = new ProgressBar();
        this.clavier = new Clavier("ABCDEFGHIJKLMNOPQRSTUVWXYZ", new ControleurLettres(this.modelePendu, this),5);
        this.chrono = new Chronometre();
        this.motCrypte = new Text(modelePendu.getMotCrypte());
        this.motCrypte.setFont(Font.font("Arial", FontWeight.BOLD,this.taillePolice));
        this.leNiveau = new Text("");
        this.leNiveau.setFont(Font.font("Arial", this.taillePolice));
    }


    /**
     * @return  vrai si la derniere fenetre est les parametres
     */
    public boolean getDernPar(){
        return this.dernEstPar;
    }
    
    /**
     * change police du mot du niveau et du texte exemple
     */
    public void changePolice(){
        try{
        this.taillePolice=Integer.parseInt(this.tfP.getText());
        this.ex.setFont(Font.font(this.taillePolice));
        this.motCrypte.setFont(Font.font(this.taillePolice));
        this.leNiveau.setFont(Font.font(this.taillePolice));}
        catch(Exception e){Alert alert = new Alert(Alert.AlertType.WARNING,"Entrez un nombre");
        alert.showAndWait();}
    }
    /**
     * change la couleur avec la couleur recup par le controleur
     * @param c
     */
    public void changeCoul(Color c){
        this.banniere.setBackground(new Background(new BackgroundFill(c, null, null)));
    }
    /**
     * change la longeur des mots choisis
     */
    public void changeLongeur(){
        try{
        this.maxLet=Integer.parseInt(this.tfMax.getText());
        this.miniLet=Integer.parseInt(this.tfMin.getText());
        this.modelePendu.setDicoLong(this.fichierMot, this.miniLet, this.maxLet);
        this.modelePendu.setMotATrouver();}
        catch(Exception e){Alert alert = new Alert(Alert.AlertType.WARNING,"Entrez des nombres");
        alert.showAndWait();}
    }
    /**
     * 
     * premiere version du selectionneur de fichier
    public void changeFicSource(){
        try{
        this.fichierMot=this.tfFic.getText();
        FileReader tmp = new FileReader(this.fichierMot);        
        System.out.println(this.fichierMot);
        this.modelePendu.setDicoLong(this.fichierMot, this.miniLet, this.maxLet);}
        catch(Exception e){Alert alert = new Alert(Alert.AlertType.WARNING,"Fichier non existant");
        alert.showAndWait();}
    }*/
    /**
     * change le fichier grace au filechooser
     */
    public void changeFicSource2(){
        FileChooser fileChooser = new FileChooser();
        File selectedFile = fileChooser.showOpenDialog(null);
        this.fichierMot=selectedFile.getPath();
        this.modelePendu.setDicoLong(this.fichierMot, this.miniLet, this.maxLet);}
    
    /**
     * @return  le graphe de scène de la vue à partir de methodes précédantes
     */
    private Scene laScene(){
        BorderPane fenetre = new BorderPane();
        fenetre.setTop(this.titre());
        fenetre.setCenter(this.panelCentral);
        return new Scene(fenetre, 800, 1000);
    }

    /**
     * @return le panel contenant le titre du jeu
     */
    private Pane titre(){
        // A implementer          
        Text titre = new Text("Jeu du pendu");
        titre.setFont(Font.font("Arial", 50));
        this.banniere = new BorderPane();
        HBox bouts = new HBox();
        bouts.getChildren().addAll(this.boutonMaison,this.boutonParametres,this.boutInfo);
        this.banniere.setLeft(titre);
        this.banniere.setRight(bouts);
        this.banniere.setBackground(new Background(new BackgroundFill(Color.LAVENDER,null, null)));
        this.banniere.setPadding(new Insets(20,20,20,20));
        return this.banniere;
    }

    /**
    * @return le panel du chronomètre
    */
     private TitledPane leChrono(){
        TitledPane res = new TitledPane("Chronomètre",this.chrono);
        res.setDisable(true);
        res.setPrefSize(300, 75);
        res.setCollapsible(false);
        return res;
     }

     /**
      * @return la fenêtre de paramètres
      */
      private Pane fenetrePar(){
        
        VBox res = new VBox(20);
        Button boutP = new Button("Changer la police");
        boutP.setOnAction(new ControleurBoutPol(this));
        Button boutLettres = new Button("Changer les bornes");
        boutLettres.setOnAction(new ControleurMaxMin(this));
        Button boutFic = new Button("Changer le fichier source");
        boutFic.setOnAction(new ControleurFic(this));
        Label max = new Label("maxi");
        Label min = new Label("mini");
        res.getChildren().addAll(this.colorP,this.tfP,this.ex,boutP,max,this.tfMax,min,this.tfMin,boutLettres,boutFic);
        return res;
    }

     /**
      * @return la fenêtre de jeu avec le mot crypté, l'image, la barre
      *         de progression et le clavier
      */
     private Pane fenetreJeu(){
        
        BorderPane res = new BorderPane();
        VBox centre = new VBox(20);
        Button nvmot = new Button("Nouveau Mot");
        nvmot.setOnAction(new ControleurLancerPartie(this.modelePendu, this));
        centre.getChildren().addAll(this.motCrypte,this.dessin,this.pg,this.clavier);
        VBox droite = new VBox(20);
        nvmot.setAlignment(Pos.BASELINE_LEFT);
        droite.getChildren().addAll(this.leNiveau,this.leChrono(),nvmot);
        centre.setAlignment(Pos.CENTER);
        res.setCenter(centre);
        res.setRight(droite);
        res.setPadding(new Insets(20));
        return res;
    }

     /**
     // * @return la fenêtre d'accueil sur laquelle on peut choisir les paramètres de jeu
     // */
     private Pane fenetreAccueil(){
        Pane res = new VBox();
        ToggleGroup group = new ToggleGroup();
        RadioButton nivf = new RadioButton("Facile");
        RadioButton nivm = new RadioButton("Moyen");
        RadioButton nivd = new RadioButton("Difficile");
        RadioButton nive = new RadioButton("Expert");
        nivf.setOnAction(new ControleurNiveau(this.modelePendu));
        nivf.setSelected(true);
        nivm.setOnAction(new ControleurNiveau(this.modelePendu));
        nivd.setOnAction(new ControleurNiveau(this.modelePendu));
        nive.setOnAction(new ControleurNiveau(this.modelePendu));
        nivf.setToggleGroup(group);
        nivd.setToggleGroup(group);
        nivm.setToggleGroup(group);
        nive.setToggleGroup(group);
        VBox niveau = new VBox(10);
        niveau.getChildren().addAll(nivf,nivm,nivd,nive);
        TitledPane niv = new TitledPane("Niveau de difficulté",niveau);
        niv.setPadding(new Insets(10,0,0,0));
        niveau.setBackground(new Background(new BackgroundFill(Color.LIGHTGRAY,null, null)));
        niv.setCollapsible(false);
        res.getChildren().addAll(this.bJouer,niv);
        return res;
     }

    /**
     * pour changer le mot crypté en découvert à la fin
     * @param mot le mot refcup dans controlleur
     */
    public void majMotCrypte(String mot){
        this.motCrypte.setText(mot);
    }

    /**
     * charge les images à afficher en fonction des erreurs
     * @param repertoire répertoire où se trouvent les images
     */
    private void chargerImages(String repertoire){
        for (int i=0; i<this.modelePendu.getNbErreursMax()+1; i++){
            File file = new File(repertoire+"/pendu"+i+".png");
            System.out.println(file.toURI().toString());
            this.lesImages.add(new Image(file.toURI().toString()));
        }
    }

    public void modeAccueil(){
       this.panelCentral.setPadding(new Insets(10,10,10,10));
       this.boutonMaison.setDisable(true);
       this.boutonParametres.setDisable(false);
       this.boutInfo.setDisable(false);
       this.panelCentral.setCenter(this.fenetreAccueil());
       this.dernEstPar=false;
    }
    
    public void modeJeu(){
       this.panelCentral.setPadding(new Insets(10,10,10,10));
       this.boutonMaison.setDisable(false);
       this.boutonParametres.setDisable(true);
       this.boutInfo.setDisable(false);
       this.panelCentral.setCenter(this.fenetreJeu());
       this.dernEstPar=false;
    }
    
    public void modeParametres(){
        this.panelCentral.setPadding(new Insets(10,10,10,10));
        this.boutonMaison.setDisable(false);
        this.boutonParametres.setDisable(true);
        this.boutInfo.setDisable(true);
        this.panelCentral.setCenter(this.fenetrePar());
        this.dernEstPar=true;
    }

    /** lance une partie */
    public void lancePartie(){
        if (this.modelePendu.getNiveau()==0){
            this.leNiveau.setText("Niveau Facile");
        }
        if (this.modelePendu.getNiveau()==1){
            this.leNiveau.setText("Niveau Medium");
        }
        if (this.modelePendu.getNiveau()==2){
            this.leNiveau.setText("Niveau Difficile");
        }
        if (this.modelePendu.getNiveau()==3){
            this.leNiveau.setText("Niveau Expert");
        }
        this.clavier.desactiveTouches(new HashSet<String>());
        this.chrono.resetTime();
        this.chrono.start();
    }

    /**
     * raffraichit l'affichage selon les données du modèle
     */
    public void majAffichage(){
        this.motCrypte.setText(this.modelePendu.getMotCrypte());
        this.clavier.desactiveTouches(this.modelePendu.getLettresEssayees());
        this.dessin.setImage(this.lesImages.get(this.lesImages.size()-this.modelePendu.getNbErreursRestants()-1));
        this.pg.setProgress(1-(double) this.modelePendu.getNbErreursRestants()/this.modelePendu.getNbErreursMax());
    }

    /**
     * accesseur du chronomètre (pour les controleur du jeu)
     * @return le chronomètre du jeu
     */
    public Chronometre getChrono(){
        // A implémenter
        return this.chrono; // A enlever
    }

    public Alert popUpPartieEnCours(){
        Alert alert = new Alert(Alert.AlertType.CONFIRMATION,"La partie est en cours!\n Etes-vous sûr de l'interrompre ?", ButtonType.YES, ButtonType.NO);
        alert.setTitle("Attention");
        return alert;
    }
        
    public Alert popUpReglesDuJeu(){
        // A implementer
        Alert alert = new Alert(Alert.AlertType.INFORMATION,"Jeu du pendu:\n Cliquez sur les lettres jusqu'à découvrir\n le mot mystère. \n 4 modes de jeu changent la difficulté.");
        return alert;
    }
    
    public Alert popUpMessageGagne(){
        // A implementer
        Alert alert = new Alert(Alert.AlertType.INFORMATION,"Partie gagnée bravo");       
        alert.setTitle("Bravo"); 
        return alert;
    }
    
    public Alert popUpMessagePerdu(){
        // A implementer    
        Alert alert = new Alert(Alert.AlertType.INFORMATION,"C'est perdu");
        alert.setTitle("Réessayez"); 
        return alert;
    }
    public Alert popUpRetourPartie() {
        Alert alert = new Alert(Alert.AlertType.INFORMATION,"Fermez cette fenêtre pour revenir au jeu");
        alert.setTitle("Revenez au jeu"); 
        return alert;
    } 

    /**
     * créer le graphe de scène et lance le jeu
     * @param stage la fenêtre principale
     */
    @Override
    public void start(Stage stage) {
        stage.setTitle("IUTEAM'S - La plateforme de jeux de l'IUTO");
        stage.setScene(this.laScene());
        this.modeAccueil();
        stage.show();
    }

    /**
     * Programme principal
     * @param args inutilisé
     */
    public static void main(String[] args) {
        launch(args);
    }

       
}
