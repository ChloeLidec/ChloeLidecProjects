using UnityEngine;

public class ShowHideVehicleButton : MonoBehaviour
    {

        [Header("Button")]
        //the input button for entering car
        [SerializeField]
        private GameObject vehicleButton;

        [Header("Scripts")]
        [SerializeField]
        InOutVehicles inOutVehicles;
        [Header("Objects")]
        [SerializeField]
        private GameObject[] vehicles;
        [SerializeField]
        private GameObject player;
        [SerializeField]
        private GameObject menuUI;

        public void Start(){
            //hide the button
            vehicleButton.SetActive(false);
        }
        
        public void Update(){
            //if the player is close to a vehicle
            if (IsPlayerCloseToVehicle() && !menuUI.activeSelf){
                //show the button
                vehicleButton.SetActive(true);
            }
            else{
                //hide the button
                vehicleButton.SetActive(false);
            }
        }

        //check if the player is close to a vehicle
        public bool IsPlayerCloseToVehicle(){
            if (inOutVehicles.activeVehicle != null){
                    return true;
                }
            foreach (GameObject vehicle in vehicles){
            //if the player is close to the vehicle
            GameObject playerCapsule = player.transform.Find("PlayerCapsule").gameObject;
            //si le nom est Prometheus 1
            int distance = 2;
            if(vehicle.tag=="Boat"){distance = 15;}
            if (Vector3.Distance(vehicle.transform.position, playerCapsule.transform.position) < distance){
                    return true;
                }
            }
            //return false
            return false;
        }
}


