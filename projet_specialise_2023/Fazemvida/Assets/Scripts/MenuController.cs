using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;
using System.IO;

public class MenuController : MonoBehaviour
{   
    
    [SerializeField]
        private ManageFazem mainScript;
    [Header("UI")]
    [SerializeField] private GameObject mainUI = null;
    [SerializeField] private GameObject menuUI = null;
    [Header("Inventory")]
    [SerializeField] private GameObject inventoryUI = null;

    [Header("Map")]
    [SerializeField] private GameObject mapUI = null;

    [Header("Missions")]
    [SerializeField] private GameObject missionUI = null;
    [SerializeField] private StopWatch stopwatch = null;
    
    [Header("Player")]
    [SerializeField] private GameObject human = null;
    [SerializeField] private PlayerSingleton playerSingleton = PlayerSingleton.Instance();
    private Vector3 playerPosition;

    [Header("Vehicles")]
    [SerializeField] private InOutVehicles inOutVehicles = null;
    private GameObject vehicle = null;

    public void ShowMenu(){
        //save player position and rotation
        playerPosition = human.transform.Find("PlayerCapsule").gameObject.transform.position;
        //deactive the active vehicle if there is one and hide its UI
        
        if (inOutVehicles != null)
        {
            vehicle = inOutVehicles.activeVehicle;
        }
        else if (mainScript.taxi.activeSelf){
            vehicle = mainScript.taxi;
        }
        else
        {
            vehicle = null;
        }
        
        if (vehicle != null)
        {
            //save player positon as next to the vehicle
            playerPosition = vehicle.transform.position + vehicle.transform.TransformDirection(Vector3.left * 2);
            mainUI.transform.Find("VehicleUI").gameObject.SetActive(false);
            vehicle.SetActive(false);
            vehicle.transform.Find("Vehicle Camera").gameObject.GetComponent<Camera>().enabled = false;
            vehicle.GetComponent<PrometeoCarController>().StopCar();
            vehicle.GetComponent<PrometeoCarController>().enabled = false;
        }
        //deactive all human UIs and components
        else{
            GameObject move = mainUI.transform.Find("UI_Virtual_Joystick_Move").gameObject;
            GameObject look = mainUI.transform.Find("UI_Virtual_Joystick_Look").gameObject;
            GameObject sprint = mainUI.transform.Find("UI_Virtual_Button_Sprint").gameObject;
            GameObject jump = mainUI.transform.Find("UI_Virtual_Button_Jump").gameObject;
            move.SetActive(false);
            look.SetActive(false);
            sprint.SetActive(false);
            jump.SetActive(false);

            GameObject playerCapsule = human.transform.Find("PlayerCapsule").gameObject;
            GameObject MainCamera = human.transform.Find("MainCamera").gameObject;
            GameObject playerFollow = human.transform.Find("PlayerFollowCamera").gameObject;
            MainCamera.SetActive(false);
            playerFollow.SetActive(false);
            playerCapsule.SetActive(false);
        }
        stopwatch.Pause();
        string mission = mainScript.MissionStarted();
        if (mission == "GB"){
            MissionGBSingleton missionGBSingleton = MissionGBSingleton.Instance();
            missionGBSingleton.paused = true;
        }
        else if (mission == "Taxi"){
            MissionTaxiSingleton missionTaxiSingleton = MissionTaxiSingleton.Instance();
            missionTaxiSingleton.paused = true;
            mainUI.transform.Find("VehicleUI").gameObject.SetActive(false);
        }
        else if (mission == "Farm"){
            MissionFarmSingleton missionFarmSingleton = MissionFarmSingleton.Instance();
            missionFarmSingleton.paused = true;
        }
        GameObject inGameUI = mainUI.transform.Find("InGameUI").gameObject;
        inGameUI.SetActive(false);
        mainUI.transform.Find("CheckpointsGB").gameObject.SetActive(false);
        mainUI.transform.Find("FarmMissionUI").gameObject.SetActive(false);
        mainUI.transform.Find("StopWatch").gameObject.SetActive(false);
        menuUI.SetActive(true);
        ShowInventory();
    }

    public void HideMenu(){
        if (vehicle != null)
        {
            mainUI.transform.Find("VehicleUI").gameObject.SetActive(true);
            vehicle.SetActive(true);
            vehicle.transform.Find("Vehicle Camera").gameObject.GetComponent<Camera>().enabled = true;
            vehicle.GetComponent<PrometeoCarController>().enabled = true;
        }
        //active all human UIs and components
        else{
            GameObject move = mainUI.transform.Find("UI_Virtual_Joystick_Move").gameObject;
            GameObject look = mainUI.transform.Find("UI_Virtual_Joystick_Look").gameObject;
            GameObject sprint = mainUI.transform.Find("UI_Virtual_Button_Sprint").gameObject;
            GameObject jump = mainUI.transform.Find("UI_Virtual_Button_Jump").gameObject;
            move.SetActive(true);
            look.SetActive(true);
            sprint.SetActive(true);
            jump.SetActive(true);

            GameObject playerCapsule = human.transform.Find("PlayerCapsule").gameObject;
            GameObject MainCamera = human.transform.Find("MainCamera").gameObject;
            GameObject playerFollow = human.transform.Find("PlayerFollowCamera").gameObject;
            MainCamera.SetActive(true);
            playerFollow.SetActive(true);
            playerCapsule.SetActive(true);
        }
        GameObject inGameUI = mainUI.transform.Find("InGameUI").gameObject;
        inGameUI.SetActive(true);
        menuUI.SetActive(false);
        stopwatch.Resume();
        string mission = mainScript.MissionStarted();
        if (mission == "GB"){
            MissionGBSingleton missionGBSingleton = MissionGBSingleton.Instance();
            missionGBSingleton.paused = false;
            mainUI.transform.Find("CheckpointsGB").gameObject.SetActive(true);
            mainUI.transform.Find("StopWatch").gameObject.SetActive(true);
        }
        else if (mission == "Taxi"){
            MissionTaxiSingleton missionTaxiSingleton = MissionTaxiSingleton.Instance();
            missionTaxiSingleton.paused = false;
            mainUI.transform.Find("StopWatch").gameObject.SetActive(true);
            mainUI.transform.Find("VehicleUI").gameObject.SetActive(true);
            GameObject move = mainUI.transform.Find("UI_Virtual_Joystick_Move").gameObject;
            GameObject look = mainUI.transform.Find("UI_Virtual_Joystick_Look").gameObject;
            GameObject sprint = mainUI.transform.Find("UI_Virtual_Button_Sprint").gameObject;
            GameObject jump = mainUI.transform.Find("UI_Virtual_Button_Jump").gameObject;
            move.SetActive(false);
            look.SetActive(false);
            sprint.SetActive(false);
            jump.SetActive(false);

            GameObject playerCapsule = human.transform.Find("PlayerCapsule").gameObject;
            GameObject MainCamera = human.transform.Find("MainCamera").gameObject;
            GameObject playerFollow = human.transform.Find("PlayerFollowCamera").gameObject;
            MainCamera.SetActive(true);
            playerFollow.SetActive(true);
            playerCapsule.SetActive(true);
        }
        else if (mission == "Farm"){
            MissionFarmSingleton missionFarmSingleton = MissionFarmSingleton.Instance();
            missionFarmSingleton.paused = false;
            mainUI.transform.Find("FarmMissionUI").gameObject.SetActive(true);
            mainUI.transform.Find("StopWatch").gameObject.SetActive(true);
        }
    }

    public void Save(){
        //save player position and rotation
        playerSingleton.SetPosition(playerPosition);
        string json = JsonUtility.ToJson(playerSingleton);
        //overwrite the file with the new data
        File.WriteAllText(Application.persistentDataPath + "" + playerSingleton.playerName + ".json", json);
    }

    public void ShowInventory(){
        if (menuUI.activeSelf)
        {
            if (!inventoryUI.activeSelf)
            {
                inventoryUI.SetActive(true);
                //left part
                Text cornAmount = inventoryUI.transform.Find("Corn").gameObject.transform.Find("CornAmount").gameObject.GetComponent<Text>();
                Text coinAmount = inventoryUI.transform.Find("Coin").gameObject.transform.Find("AmountText").gameObject.GetComponent<Text>();
                cornAmount.text = playerSingleton.corn.ToString();
                coinAmount.text = playerSingleton.playerMoney.ToString();
                inventoryUI.transform.Find("House").gameObject.SetActive(true);
                Text houseName = inventoryUI.transform.Find("House").gameObject.transform.Find("Name").gameObject.GetComponent<Text>();
                if (playerSingleton.house != ""){
                    houseName.text = playerSingleton.house;
                }
                else{
                    houseName.text = "Vous n'avez pas de maison";
                }

                //right part
                if (playerSingleton.animals.Count > 0)
                {
                    List<string> animals = playerSingleton.GetAnimals();
                    List<string> animalTypes = new List<string>();
                    List<string> animalNames = new List<string>();
                    foreach (string animal in animals)
                    {
                        string[] animalSplit = animal.Split(' ');
                        animalTypes.Add(animalSplit[0]);
                        animalNames.Add(animalSplit[1]);
                    }
                    foreach (Transform child in inventoryUI.transform.Find("Animals").gameObject.transform)
                    {
                        if (animalTypes.Contains(child.gameObject.name))
                            {
                                child.gameObject.SetActive(true);
                                child.gameObject.transform.Find("Name").gameObject.GetComponent<Text>().text = animalNames[animalTypes.IndexOf(child.gameObject.name)];
                            }
                            else
                            {
                                child.gameObject.SetActive(false);
                            }
                    }
                }
            //now we deactivate the other UIs and show the right bg image for buttons
            mapUI.SetActive(false);
            missionUI.SetActive(false);
            menuUI.transform.Find("FBtn_Active").gameObject.SetActive(true);
            menuUI.transform.Find("FBtn_NActive").gameObject.SetActive(false);
            menuUI.transform.Find("SBtn_Active").gameObject.SetActive(false);
            menuUI.transform.Find("SBtn_NActive").gameObject.SetActive(true);
            menuUI.transform.Find("TBtn_Active").gameObject.SetActive(false);
            menuUI.transform.Find("TBtn_NActive").gameObject.SetActive(true);
            }
        }
    }

    public void ShowMap(){
        if (menuUI.activeSelf)
        {
            if (!mapUI.activeSelf)
            {
                mapUI.SetActive(true);
                inventoryUI.SetActive(false);
                missionUI.SetActive(false);
                menuUI.transform.Find("FBtn_Active").gameObject.SetActive(false);
                menuUI.transform.Find("FBtn_NActive").gameObject.SetActive(true);
                menuUI.transform.Find("SBtn_Active").gameObject.SetActive(true);
                menuUI.transform.Find("SBtn_NActive").gameObject.SetActive(false);
                menuUI.transform.Find("TBtn_Active").gameObject.SetActive(false);
                menuUI.transform.Find("TBtn_NActive").gameObject.SetActive(true);
            }
        }
    }

    public void ShowMissionRecap(){
    if (menuUI.activeSelf)
        {
            if (!missionUI.activeSelf)
            {
                missionUI.SetActive(true);
                if (mainScript.MissionStarted() == "none"){
                    missionUI.transform.Find("Title").gameObject.GetComponent<Text>().text = "Aucune mission en cours";
                    missionUI.transform.Find("Description").gameObject.GetComponent<Text>().text = "Vous pouvez effectuer des missions aux endroits marqués par des halos rouges et par des chats sur la carte";
                }
                else if (mainScript.MissionStarted() == "GB"){
                    missionUI.transform.Find("Title").gameObject.GetComponent<Text>().text = "Mission du Grand Bois";
                    missionUI.transform.Find("Description").gameObject.GetComponent<Text>().text = "Vous devez parcourir le grand bois sans indications autre que votre carte et passer par un maximum de checkpoints en un minimum de temps afin de pouvoir guider les touristes. Bonne chance !";
                }
                else if (mainScript.MissionStarted() == "Taxi"){
                    missionUI.transform.Find("Title").gameObject.GetComponent<Text>().text = "Mission Taxi";
                    missionUI.transform.Find("Description").gameObject.GetComponent<Text>().text = "Vous devez vous rendre à la destination indiquée par un halo jaune en suivant la flèche rouge près de vous en un minimum de temps afin de pouvoir réussir votre mission. Il est de votre choix de suivre les routes ;). Bonne route !";
                }
                else if (mainScript.MissionStarted() == "Farm"){
                    missionUI.transform.Find("Title").gameObject.GetComponent<Text>().text = "Mission de Récolte";
                    missionUI.transform.Find("Description").gameObject.GetComponent<Text>().text = "Vous devez aider le fermier à récolter 50 maïs en un minimum de temps afin de pouvoir réussir votre mission. Il vous suffit pour cela de cliquer sur les maïs pour les récolter. À savoir que les maïs supplémentaires pourront vous être utiles pour d'autres tâches. Bonne récolte !";
                }
                
                inventoryUI.SetActive(false);
                mapUI.SetActive(false);
                menuUI.transform.Find("FBtn_Active").gameObject.SetActive(false);
                menuUI.transform.Find("FBtn_NActive").gameObject.SetActive(true);
                menuUI.transform.Find("SBtn_Active").gameObject.SetActive(false);
                menuUI.transform.Find("SBtn_NActive").gameObject.SetActive(true);
                menuUI.transform.Find("TBtn_Active").gameObject.SetActive(true);
                menuUI.transform.Find("TBtn_NActive").gameObject.SetActive(false);
            }
        }
    }

}