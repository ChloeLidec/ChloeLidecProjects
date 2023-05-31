using System.Collections;
using System.Collections.Generic;
using UnityEngine;


public class MissionFarmSingleton 
{
    private static MissionFarmSingleton instance;
    public float missionStartTime;
    public bool stopped = true;
    public float missionTime;
    public int corn;
    public bool isHarvesting = false;
    public bool paused = false;

    private MissionFarmSingleton()
    {
        missionStartTime = 0;
        corn = 0;
    }

    public static MissionFarmSingleton Instance()
    {
        {
            if (instance == null)
            {
                instance = new MissionFarmSingleton();
            }
            return instance;
        }
    }

    public void SetMissionStartTime()
    {
        missionStartTime = Time.deltaTime;
    }

    public void ResetMission()
    {
        missionStartTime = 0;
        stopped = false;
        corn = 0;
    }

    public void HarvestCorn(int amount)
    {
        corn += amount;
    }

    public void FinishMission()
    {
        stopped = true;
    }

    public void DeleteInstance()
    {
        instance = null;
    }
}
