using UnityEngine;

public class ShowHideCarTPButton : MonoBehaviour
    {

        [Header("Button")]
        //the input button for entering car
        [SerializeField]
        private GameObject vehicleTPButton;

        [Header("Scripts")]
        [SerializeField]
        InOutVehicles inOutVehicles;
        [Header("Objects")]
        [SerializeField]
        private GameObject[] parkingSigns;
        [SerializeField]
        private GameObject player;
        [SerializeField]
        private GameObject menuUI;
        [SerializeField]
        private GameObject car;

        public void Start(){
            //hide the button
            vehicleTPButton.SetActive(false);
        }
        
        public void Update(){
            //if the player is close to a vehicle
            if (IsPlayerCloseToSign() && !menuUI.activeSelf && inOutVehicles.activeVehicle == null){
                //show the button
                vehicleTPButton.SetActive(true);
            }
            else{
                //hide the button
                vehicleTPButton.SetActive(false);
            }
        }

        public bool IsPlayerCloseToSign(){
            foreach (GameObject sign in parkingSigns){
            GameObject playerCapsule = player.transform.Find("PlayerCapsule").gameObject;
            if (Vector3.Distance(sign.transform.position, playerCapsule.transform.position) < 2){
                    return true;
                }
            if (inOutVehicles.activeVehicle != null){
                    
                    return false;
                }
            }
            return false;
        }
}


