using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.SceneManagement;
using UnityEngine.UI;
using System.IO;

public class ConnectPlayer : MonoBehaviour
{   
    private PlayerSingleton playerSingleton;
    private string jsonFile;
    [SerializeField]
    public InputField playerNameInput;
    public Text textInfo;
    // Start is called before the first frame update
    public void StartPlayer(){
        string playerName = playerNameInput.text;
        bool correct = CheckPlayerName(playerName);
        if (correct)
        {
            playerSingleton = PlayerSingleton.Instance();
            playerSingleton.SetName(playerName);
            HandleJSON();
            SceneManager.LoadScene("Fazem");
        }
        else
        {
            textInfo.text = "Nom invalide. Entrez un nom sans caractères spéciaux autres que - et _";
            playerNameInput.text = "Entrez un nom...";
        }
    }

    private bool CheckPlayerName(string playerName)
    {
        //check that the player name is not empty, that it doesn't contain any special characters, and that it doesn't contain any spaces
        string acceptedCharacters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_-";
        if (playerName.Length == 0)
        {
            return false;
        }
        foreach (char c in playerName)
        {
            if (!acceptedCharacters.Contains(c.ToString()))
            {
                return false;
            }
        }
        return true;
    }
    private void HandleJSON()
    {
        // look for a file called "[playername].json" in the Resources folder check with Resources.Load<TextAsset>(playername)
        bool fileExists = File.Exists(Application.persistentDataPath + "" + playerSingleton.playerName + ".json");
        if (fileExists)
        {
            jsonFile = File.ReadAllText(Application.persistentDataPath + "" + playerSingleton.playerName + ".json");
            // if it exists, load it
            //get the money from the json file
            Player player = JsonUtility.FromJson<Player>(jsonFile);
            int money = player.GetMoney();
            playerSingleton.SetMoney(10000);
            //if the player has no position, set it to the default position
            if (player.GetPosition() == Vector3.zero)
            {
                playerSingleton.SetPosition(new Vector3(566.11f, 60.114f, 7.25f));
            }
            else
            {
                playerSingleton.SetPosition(player.GetPosition());
            }
            if (player.GetHouse() == "")
            {
                playerSingleton.SetHouseName("");
            }
            else
            {
                playerSingleton.SetHouseName(player.GetHouse());
            }
            if (player.GetAnimals() == null || player.GetAnimals().Count == 0)
            {
                playerSingleton.SetAnimals(new List<string>());
            }
            else
            {
                playerSingleton.SetAnimals(player.GetAnimals());
            }
            playerSingleton.corn = player.corn;
            if (player.GetFurniture() == null || player.GetFurniture().Count == 0)
            {
                playerSingleton.SetFurniture(new List<string>());
            }
            else
            {
                playerSingleton.SetFurniture(player.GetFurniture());
            }
            
        }
        else
        {
            // if it doesn't exist, create it
            playerSingleton.SetMoney(0);
            playerSingleton.SetPosition(new Vector3(566.11f, 60.114f, 7.25f));
            string json = JsonUtility.ToJson(playerSingleton);
            //get the path to the file for android
            string path = Application.persistentDataPath + "" + playerSingleton.playerName + ".json";
            //create the file and directory if it doesn't exist
            File.WriteAllText(path, json);
        }

    }
}
        
     
        
