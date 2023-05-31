using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.SceneManagement;
using UnityEngine.UI;
using StarterAssets;
using System;

public class SupermarketManager : MonoBehaviour
{
    public HomeSingleton home = HomeSingleton.Instance();
    public PlayerSingleton player = PlayerSingleton.Instance();
    public GameObject supermarketUI;
    public GameObject mainUI;
    public GameObject human;
    public StarterAssetsInputs starterAssetsInputs;
    public void OnTriggerEnter(Collider other)
    {
        ShowMenu();
    }

    public void ShowMenu()
    {
        starterAssetsInputs.StopInput();
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
        supermarketUI.SetActive(true);
        List<string> furniture = player.GetFurniture();
        foreach (Transform child in supermarketUI.transform)
        {
            if (child.gameObject.tag == "Furniture")
            {
                if (furniture.Contains(child.gameObject.name))
                {
                    child.gameObject.SetActive(false);
                }
                else
                {
                    child.gameObject.SetActive(true);
                }
            }
        }
    }

    public void CloseMenu()
    {
        starterAssetsInputs.StopInput();
        foreach (Transform child in supermarketUI.transform)
        {
            if (child.gameObject.tag == "Furniture")
            {
                child.gameObject.SetActive(true);
            }
        }
        supermarketUI.SetActive(false);
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
        playerCapsule.transform.position = new Vector3(377.38f, 60.10f, -321.54f);
        
        GameObject inGameUI = mainUI.transform.Find("InGameUI").gameObject;
        inGameUI.SetActive(true);
    }

    public void BuyFurniture(){
        List<string> furniture = player.GetFurniture();
        if (player.playerMoney >= 800 && !furniture.Contains(this.gameObject.name))
        {
            player.RemoveMoney(800);
            player.AddFurniture(this.gameObject.name);
            this.gameObject.SetActive(false);
        }
    }
}
