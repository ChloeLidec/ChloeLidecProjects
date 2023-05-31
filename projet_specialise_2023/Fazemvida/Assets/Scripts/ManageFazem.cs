using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.SceneManagement;
using UnityEngine.UI;

public class ManageFazem : MonoBehaviour
{
    PlayerSingleton playerSingleton;
    MissionGBSingleton missionGBSingleton;
    MissionTaxiSingleton missionTaxiSingleton;
    MissionFarmSingleton missionFarmSingleton;
    
    [Header("Player")]
    public GameObject human;
    public GameObject car;
    public GameObject[] parkingSigns;

    [Header("UI")]
    public GameObject coinUI;
    public GameObject mainUI;
    public GameObject vehicleUI;

    [Header("MissionGB")]
    public Text checkpointText;
    public GameObject[] checkpoints;

    [Header("MissionTaxi")]
    public GameObject taxi;
    public GameObject[] possibleDestinations;

    [Header("MissionFarm")]
    public GameObject farmerHalo;
    public GameObject finishHarvestHalo;
    public GameObject cropsContainer;
    [Header("Houses")]
    public GameObject housesHaloContainer;
    public Material buildingsToBuyHalo;
    public Material buildingsHalo;

    [Header("Stopwatch")]
    public StopWatch stopWatch;
    public GameObject stopwatchUI;
    // Start is called before the first frame update
    void Start()
    {
        playerSingleton = PlayerSingleton.Instance();
        GameObject textCA = coinUI.transform.Find("CoinAmount").gameObject;
        textCA.GetComponent<UnityEngine.UI.Text>().text = playerSingleton.playerMoney.ToString();
        GameObject capsule = human.transform.Find("PlayerCapsule").gameObject;
        capsule.transform.position = new Vector3(playerSingleton.playerPosition[0], playerSingleton.playerPosition[1], playerSingleton.playerPosition[2]);

        foreach (Transform child in housesHaloContainer.transform)
        {
            if (playerSingleton.GetHouseName() == child.gameObject.name){
                MeshRenderer meshRenderer = child.gameObject.GetComponent<MeshRenderer>();
                meshRenderer.material = buildingsToBuyHalo;
            }
            else
            {
                MeshRenderer meshRenderer = child.gameObject.GetComponent<MeshRenderer>();
                meshRenderer.material = buildingsHalo;
            }
        }
        if (playerSingleton.leftHouse){
        GameObject playerCapsule = human.transform.Find("PlayerCapsule").gameObject;
        string houseName = playerSingleton.GetHouseName();
        foreach (Transform child in housesHaloContainer.transform)
        {
            if (child.name == houseName)
            {
                playerCapsule.transform.position = child.transform.position;
                playerCapsule.transform.position = new Vector3(playerCapsule.transform.position.x, 60, playerCapsule.transform.position.z + 2);
            }
        }
        playerSingleton.leftHouse = false;
        }
    }

    // Update is called once per frame
    void Update()
    {
        GameObject textCA = coinUI.transform.Find("CoinAmount").gameObject;
        textCA.GetComponent<UnityEngine.UI.Text>().text = playerSingleton.playerMoney.ToString();
    }

    public string MissionStarted(){
        if (missionGBSingleton!=null && !missionGBSingleton.stopped){
            return "GB";
        }
        else if (missionTaxiSingleton!=null && !missionTaxiSingleton.stopped){
            return "Taxi";
        }
        else if (missionFarmSingleton!=null && !missionFarmSingleton.stopped){
            return "Farm";
        }
        else{
            return "none";
        }
    }

    public void StartMissionGB()
    {
        //reset mission
        missionGBSingleton = MissionGBSingleton.Instance();
        missionGBSingleton.ResetMission();
        missionGBSingleton.SetMissionStartTime();
        foreach (GameObject checkpoint in checkpoints)
        {
            checkpoint.SetActive(true);
        }
        stopWatch.StartSW();
        checkpointText.gameObject.SetActive(true);
        checkpointText.text = "Checkpoints 0/7";
    }

    public void StartMissionTaxi(){
        missionTaxiSingleton = MissionTaxiSingleton.Instance();
        missionTaxiSingleton.ResetMission();
        int randomIndex = Random.Range(0, possibleDestinations.Length);
        Debug.Log(randomIndex);
        GameObject destination = possibleDestinations[randomIndex];
        Debug.Log(destination);
        missionTaxiSingleton.SetDestination(destination);
        destination.SetActive(true);
        GameObject move = mainUI.transform.Find("UI_Virtual_Joystick_Move").gameObject;
        GameObject look = mainUI.transform.Find("UI_Virtual_Joystick_Look").gameObject;
        GameObject sprint = mainUI.transform.Find("UI_Virtual_Button_Sprint").gameObject;
        GameObject jump = mainUI.transform.Find("UI_Virtual_Button_Jump").gameObject;
        move.SetActive(false);
        look.SetActive(false);
        sprint.SetActive(false);
        jump.SetActive(false);
        GameObject playerCapsule = human.transform.Find("PlayerCapsule").gameObject;
        GameObject mainCamera = human.transform.Find("MainCamera").gameObject;
        GameObject playerFollow = human.transform.Find("PlayerFollowCamera").gameObject;
        mainCamera.SetActive(false);
        playerFollow.SetActive(false);
        playerCapsule.SetActive(false);
        GameObject inGameUI = mainUI.transform.Find("InGameUI").gameObject;
        inGameUI.SetActive(false);
        taxi.SetActive(true);
        vehicleUI.SetActive(true);
        PrometeoCarController  prometeoCarController = taxi.GetComponent<PrometeoCarController>();
        prometeoCarController.enabled = true;
        taxi.transform.Find("Vehicle Camera").gameObject.GetComponent<Camera>().enabled = true;
        taxi.transform.position = new Vector3(482.20f, 60.10f, -104.10f);
        taxi.transform.rotation = Quaternion.Euler(0, 0, 0);
        missionTaxiSingleton.SetMissionStartTime();
        stopWatch.StartSW();
    }

    public void StartMissionFarm(){
        foreach (Transform child in cropsContainer.transform)
        {
            child.gameObject.SetActive(true);
        }
        GameObject missionUI = mainUI.transform.Find("FarmMissionUI").gameObject;
        missionUI.SetActive(true);
        farmerHalo.SetActive(false);
        finishHarvestHalo.SetActive(false);
        missionFarmSingleton = MissionFarmSingleton.Instance();
        missionFarmSingleton.ResetMission();
        missionFarmSingleton.SetMissionStartTime();
        stopWatch.StartSW();
    }

    public void TPCarToParking(){
        foreach (GameObject parkingSign in parkingSigns)
        {
            if (Vector3.Distance(parkingSign.transform.position, human.transform.Find("PlayerCapsule").gameObject.transform.position) < 2){
                car.transform.position = parkingSign.transform.position - parkingSign.transform.forward * 10;
            }
        }
    }
}
