using System.Collections;
using System.Collections.Generic;
using UnityEngine;
public class InOutVehicles : MonoBehaviour
{   
    [Header("UI")]
    [SerializeField] private GameObject mainUI = null;
    [Header("Human")]
    [SerializeField] private GameObject human = null;

    [Header("Vehicles")]
    [SerializeField] private GameObject[] vehicles = null;

    [Header("Active Vehicle")]
    [SerializeField] public GameObject activeVehicle = null;
    [SerializeField] private PrometeoCarController prometeoCarController = null;

    public void EnterExitVehicle()
    {
        if (activeVehicle == null)
        {
            EnterVehicle();
        }
        else
        {
            ExitVehicle();
        }
    }

    private void ExitVehicle()
    {
        
        mainUI.transform.Find("VehicleUI").gameObject.SetActive(false);
        human.transform.Find("MainCamera").gameObject.SetActive(true);
        human.transform.Find("PlayerFollowCamera").gameObject.SetActive(true);
        mainUI.transform.Find("UI_Virtual_Joystick_Move").gameObject.SetActive(true);
        mainUI.transform.Find("UI_Virtual_Joystick_Look").gameObject.SetActive(true);
        mainUI.transform.Find("UI_Virtual_Button_Sprint").gameObject.SetActive(true);
        mainUI.transform.Find("UI_Virtual_Button_Jump").gameObject.SetActive(true);
        GameObject inGameUI = mainUI.transform.Find("InGameUI").gameObject;
        GameObject inGameUI2 = inGameUI.transform.Find("MenuBtn").gameObject;
        inGameUI2.SetActive(true);
        activeVehicle.GetComponent<PrometeoCarController>().StopCar();       
        activeVehicle.transform.Find("Vehicle Camera").gameObject.GetComponent<Camera>().enabled = false;
        activeVehicle.GetComponent<PrometeoCarController>().enabled = false;
        prometeoCarController = null;
        GameObject vehicleBody = activeVehicle.transform.Find("Body").gameObject;
        GameObject playerCapsule = human.transform.Find("PlayerCapsule").gameObject;
        playerCapsule.SetActive(true);
        playerCapsule.transform.position = vehicleBody.transform.position + new Vector3(2, 0, 0);
        activeVehicle = null;
    }

    private void EnterVehicle()
    {
        foreach (GameObject vehicle in vehicles)
        {
            //get the PlayerCapsule of the human
            GameObject playerCapsule = human.transform.Find("PlayerCapsule").gameObject;
            int distance = 2;
            if(vehicle.tag=="Boat"){distance = 15;}
            if (Vector3.Distance(vehicle.transform.position, playerCapsule.transform.position) < distance)
            {
                //active the vehicle UI
                mainUI.transform.Find("VehicleUI").gameObject.SetActive(true);
                //disable the human UI
                GameObject move = mainUI.transform.Find("UI_Virtual_Joystick_Move").gameObject;
                GameObject look = mainUI.transform.Find("UI_Virtual_Joystick_Look").gameObject;
                GameObject sprint = mainUI.transform.Find("UI_Virtual_Button_Sprint").gameObject;
                GameObject jump = mainUI.transform.Find("UI_Virtual_Button_Jump").gameObject;
                GameObject inGameUI = mainUI.transform.Find("InGameUI").gameObject;
                GameObject inGameUI2 = inGameUI.transform.Find("MenuBtn").gameObject;
                inGameUI2.SetActive(false);
                move.SetActive(false);
                look.SetActive(false);
                sprint.SetActive(false);
                jump.SetActive(false);

                //set the active vehicle
                activeVehicle = vehicle;
                prometeoCarController = activeVehicle.GetComponent<PrometeoCarController>();
                prometeoCarController.enabled = true;
                activeVehicle.transform.Find("Vehicle Camera").gameObject.GetComponent<Camera>().enabled = true;
                GameObject MainCamera = human.transform.Find("MainCamera").gameObject;
                GameObject playerFollow = human.transform.Find("PlayerFollowCamera").gameObject;

                //disable the human's components that are not needed
                MainCamera.SetActive(false);
                playerFollow.SetActive(false);
                playerCapsule.SetActive(false);
                break;
            }
        }
    }

}
