using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;
using System.IO;

public class MenuMissionTController : MonoBehaviour
{   
    [SerializeField] private ManageFazem mainScript = null;
    [Header("UI")]
    [SerializeField] private GameObject mainUI = null;
    
    [Header("Player")]
    [SerializeField] private GameObject human = null;
    [SerializeField] private PlayerSingleton playerSingleton = PlayerSingleton.Instance();



    public void ShowMenu(){      
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
        
        GameObject inGameUI = mainUI.transform.Find("InGameUI").gameObject;
        inGameUI.SetActive(false);
        GameObject menuUI = mainUI.transform.Find("StartMTUI").gameObject;
        menuUI.SetActive(true);

        //if the player is in the mission, launch again and change the text of the button
        if(mainScript.MissionStarted() == "Taxi"){
            GameObject button = menuUI.transform.Find("LaunchMission").gameObject;
            button.GetComponentInChildren<Text>().text = "Relancer la mission";
        }
    }

    public void HideMenu(){
        
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
        
        GameObject inGameUI = mainUI.transform.Find("InGameUI").gameObject;
        inGameUI.SetActive(true);
        GameObject menuUI = mainUI.transform.Find("StartMTUI").gameObject;
        menuUI.SetActive(false);
    }

    public void StartMission(){
        HideMenu();
        mainScript.StartMissionTaxi();
    }
}