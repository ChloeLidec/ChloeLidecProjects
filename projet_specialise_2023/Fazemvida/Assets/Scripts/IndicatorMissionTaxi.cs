using System.Collections;
using System.Collections.Generic;
using UnityEngine;

using UnityEngine;

public class IndicatorMissionTaxi : MonoBehaviour
{
    [SerializeField]
    GameObject indicator;
    [SerializeField]
    GameObject taxi;
    MissionTaxiSingleton missionTaxi = MissionTaxiSingleton.Instance();
    private GameObject destination;

    void Start()
    {
        
    }

    void Update()
    {
        destination = missionTaxi.destination;
        if (destination != null)
        {
            Vector3 destinationPos = destination.transform.position;
            Vector3 taxiPos = taxi.transform.position;
            Vector3 direction = destinationPos - taxiPos;
            this.transform.position = taxiPos + direction.normalized * 2;
            this.transform.LookAt(destinationPos);
        }

    }
}
