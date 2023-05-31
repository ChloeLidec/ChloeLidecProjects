using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.SceneManagement;
using UnityEngine.UI;
using StarterAssets;

public class ManageHouse : MonoBehaviour
{
    PlayerSingleton playerSingleton;
    HomeSingleton homeSingleton;
    
    [Header("Human")]
    public GameObject human;

    [Header("UI")]
    public GameObject mainUI;

    [Header("Animals")]
    public GameObject animalsContainer;
    public GameObject menuRename;
    public GameObject renameButton;

    [Header("Furniture")]
    public GameObject furnitureContainer;

    public StarterAssetsInputs starterAssetsInputs;
    // Start is called before the first frame update
    void Start()
    {
        playerSingleton = PlayerSingleton.Instance();
        homeSingleton = HomeSingleton.Instance();
        GameObject capsule = human.transform.Find("PlayerCapsule").gameObject;
        capsule.transform.position = new Vector3(4.83f, -0.74f, 15.26f);

        List<string> animals = playerSingleton.GetAnimals();
        //get just the animal types ie. "cat", "dog", "bird" by spliting the string
        List<string> animalTypes = new List<string>();
        List<string> animalNames = new List<string>();
        foreach (string animal in animals)
        {
            string[] animalSplit = animal.Split(' ');
            animalTypes.Add(animalSplit[0]);
            animalNames.Add(animalSplit[1]);
        }
        foreach (Transform child in animalsContainer.transform)
        {
            
                if (animalTypes.Contains(child.gameObject.name))
                {
                    child.gameObject.SetActive(true);
                    child.gameObject.transform.Find("Name").gameObject.GetComponent<TextMesh>().text = animalNames[animalTypes.IndexOf(child.gameObject.name)];
                }
                else
                {
                    child.gameObject.SetActive(false);
                }
            
        }
        foreach (Transform child in furnitureContainer.transform)
        {
            if (playerSingleton.GetFurniture().Contains(child.gameObject.name))
            {
                child.gameObject.SetActive(true);
            }
            else
            {
                child.gameObject.SetActive(false);
            }
        }
    }

    // Update is called once per frame
    void Update()
    {
        //check if the player is close to a pet
        GameObject capsule = human.transform.Find("PlayerCapsule").gameObject;
        List<string> animals = playerSingleton.GetAnimals();
        //get just the animal types ie. "cat", "dog", "bird" by spliting the string
        List<string> animalTypes = new List<string>();
        List<string> animalNames = new List<string>();
        foreach (string animal in animals)
        {
            string[] animalSplit = animal.Split(' ');
            animalTypes.Add(animalSplit[0]);
            animalNames.Add(animalSplit[1]);
        }
        foreach (Transform child in animalsContainer.transform)
        {
            if (child.gameObject.activeSelf)
            {
               child.gameObject.transform.Find("Name").gameObject.GetComponent<TextMesh>().text = animalNames[animalTypes.IndexOf(child.gameObject.name)];
               if (Vector3.Distance(child.position, capsule.transform.position) < 2.5f && !menuRename.activeSelf)
                {
                    renameButton.SetActive(true);
                    break;
                }
                else
                {
                    renameButton.SetActive(false);
                }
            }
        }
    }

    public void ShowRenamePet(){
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
        menuRename.SetActive(true);
        GameObject inputField = menuRename.transform.Find("InputField").gameObject;
        GameObject text = inputField.transform.Find("Text").gameObject;
        text.GetComponent<UnityEngine.UI.Text>().text = "";
        GameObject capsule = human.transform.Find("PlayerCapsule").gameObject;
        //get animal that was clicked
        foreach (Transform child in animalsContainer.transform)
        {
            if (child.gameObject.activeSelf)
            {
               if (Vector3.Distance(child.position, capsule.transform.position) < 2.5f)
                {
                    menuRename.transform.Find("Title").gameObject.GetComponent<UnityEngine.UI.Text>().text = child.gameObject.name;
                    break;
                }
            }
        }
    }

    public void HideRenamePet(){
        menuRename.SetActive(false);
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
        playerCapsule.transform.position = playerCapsule.transform.position - playerCapsule.transform.forward * 2;
    }

    public void RenamePet(){
        GameObject inputField = menuRename.transform.Find("InputField").gameObject;
        GameObject text = inputField.transform.Find("Text").gameObject;
        string newName = text.GetComponent<UnityEngine.UI.Text>().text;
        string animal = menuRename.transform.Find("Title").gameObject.GetComponent<UnityEngine.UI.Text>().text;
        playerSingleton.RenameAnimal(animal, newName);
        HideRenamePet();
    }
}
