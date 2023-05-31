using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Player 
{
    [SerializeField]
    public string playerName;
    [SerializeField]
    public int playerMoney;
    public Vector3 playerPosition;
    public string house;
    public List<string> animals;
    public bool leftHouse;
    public int corn;
    public List<string> furniture;
    
    public Player(string name, int money)
    {
        playerName = name;
        playerMoney = money;
    }

    public string GetName()
    {
        return playerName;
    }

    public int GetMoney()
    {
        return playerMoney;
    }

    public Vector3 GetPosition()
    {
        return playerPosition;
    }

    public string GetHouse()
    {
        return house;
    }
    public List<string> GetAnimals()
    {
        return animals;
    }
    public int GetCorn()
    {
        return corn;
    }
    public List<string> GetFurniture()
    {
        return furniture;
    }
}
