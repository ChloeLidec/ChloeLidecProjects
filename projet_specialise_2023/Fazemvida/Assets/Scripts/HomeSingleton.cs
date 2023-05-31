using System.Collections;
using System.Collections.Generic;
using UnityEngine;


public class HomeSingleton 
{
    private static HomeSingleton instance;
    private PlayerSingleton player = PlayerSingleton.Instance();
    private bool inHome;
    public string tempHouse;
    public Material buildingsToBuyHalo;
    public Material buildingsHalo;
    private string house;

    private HomeSingleton()
    {
       this.inHome = false;
    }

    public static HomeSingleton Instance()
    {
        {
            if (instance == null)
            {
                instance = new HomeSingleton();
            }
            return instance;
        }
    }

    public bool IsHouseOfPlayer(string house)
    {
        if (house == player.GetHouseName())
        {
            return true;
        }
        else
        {
            return false;
        }
    }
    public void SetInHome(bool inHome)
    {
        this.inHome = inHome;
    }

    public bool GetInHome()
    {
        return inHome;
    }

    public void SetHouse(string newHouse)
    {
        this.house = newHouse;
    }

    public string GetHouse()
    {
        return house;
    }

    public void DeleteInstance()
    {
        instance = null;
    }
}
