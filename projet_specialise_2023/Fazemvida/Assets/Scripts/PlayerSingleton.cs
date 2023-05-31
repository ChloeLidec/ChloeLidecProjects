using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class PlayerSingleton 
{
    private static PlayerSingleton instance;

    public string playerName;
    public int playerMoney;
    public Vector3 playerPosition;
    public string house = "";
    public List<string> animals = new List<string>();
    public bool leftHouse = false;
    public int corn = 0;
    public List<string> furniture = new List<string>();

    private PlayerSingleton()
    {
        playerName = "";
        playerMoney = 0;
    }
    public static PlayerSingleton Instance()
    {
        {
            if (instance == null)
            {
                instance = new PlayerSingleton();
            }
            return instance;
        }
    }

    public void AddMoney(int amount)
    {
        playerMoney += amount;
    }

    public void RemoveMoney(int amount)
    {
        playerMoney -= amount;
    }

    public void SetMoney(int amount)
    {
        playerMoney = amount;
    }
    public void SetName(string name)
    {
        playerName = name;
    }

    public void SetPosition(Vector3 position)
    {
        playerPosition = position;
    }

    public void SetHouseName(string houseName)
    {
        house = houseName;
    }

    public string GetHouseName()
    {
        return house;
    }

    public List<string> GetAnimals()
    {
        return animals;
    }

    public void AddAnimal(string animal)
    {
        animals.Add(animal + " " + animal);
    }

    public void SetAnimals(List<string> animals)
    {
        this.animals = animals;
    }

    public void RenameAnimal(string animal, string newName)
    {
        List<string> animals = GetAnimals();
        List<string> animalTypes = new List<string>();
        foreach (string a in animals)
        {
            string[] animalSplit = a.Split(' ');
            animalTypes.Add(animalSplit[0]);
        }
        int index = animalTypes.IndexOf(animal);
        animals[index] = animal + " " + newName;
    }
    public int GetCorn()
    {
        return corn;
    }
    public void SetCorn(int amount)
    {
        corn = amount;
    }
    public void AddCorn(int amount)
    {
        corn += amount;
    }
    public void RemoveCorn(int amount)
    {
        corn -= amount;
    }
    public void SetFurniture(List<string> furniture)
    {
        this.furniture = furniture;
    }
    public List<string> GetFurniture()
    {
        return furniture;
    }
    public void AddFurniture(string furniture)
    {
        this.furniture.Add(furniture);
    }
    
}
