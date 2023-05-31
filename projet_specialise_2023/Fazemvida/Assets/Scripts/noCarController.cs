using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class noCarController : MonoBehaviour
{
    public InOutVehicles inOutVehicles;
    public void OnTriggerEnter(Collider other)
    {
        if (other.gameObject.tag == "Vehicle" || other.gameObject.tag == "Boat")
        {
            inOutVehicles.EnterExitVehicle();
        }
    }
}
