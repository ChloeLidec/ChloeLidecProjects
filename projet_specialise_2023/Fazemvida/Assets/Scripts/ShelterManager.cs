using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.SceneManagement;
using UnityEngine.UI;
using StarterAssets;
using System;

public class ShelterManager : MonoBehaviour
{
    public HomeSingleton home = HomeSingleton.Instance();
    public PlayerSingleton player = PlayerSingleton.Instance();
    public GameObject shelterUI;
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
        shelterUI.SetActive(true);
        List<string> animals = player.GetAnimals();
        //get just the animal types ie. "cat", "dog", "bird" by spliting the string
        List<string> animalTypes = new List<string>();
        foreach (string animal in animals)
        {
            string[] animalSplit = animal.Split(' ');
            animalTypes.Add(animalSplit[0]);
        }
        foreach (Transform child in shelterUI.transform)
        {
            if (child.gameObject.tag == "Animal")
            {
                if (animalTypes.Contains(child.gameObject.name))
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
        foreach (Transform child in shelterUI.transform)
        {
            if (child.gameObject.tag == "Animal")
            {
                child.gameObject.SetActive(true);
            }
        }
        shelterUI.SetActive(false);
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
        playerCapsule.transform.position = new Vector3(519.32f, 60.09f, -163.40f);
        
        GameObject inGameUI = mainUI.transform.Find("InGameUI").gameObject;
        inGameUI.SetActive(true);
    }

    public void Adopt(){
        List<string> animals = player.GetAnimals();
        List<string> animalTypes = new List<string>();
        List<string> animalNames = new List<string>();
        foreach (string animal in animals)
        {
            string[] animalSplit = animal.Split(' ');
            animalTypes.Add(animalSplit[0]);
            animalNames.Add(animalSplit[1]);
        }
        if (player.playerMoney >= 300 && !animalTypes.Contains(this.gameObject.name))
        {
            player.RemoveMoney(300);
            string animalName = this.gameObject.name;
            player.AddAnimal(animalName);
            this.gameObject.SetActive(false);
        }
    }
}
