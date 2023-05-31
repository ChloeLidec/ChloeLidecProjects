using UnityEngine;

public class ShowHideMFarmButton : MonoBehaviour
    {

        [Header("Button")]
        public GameObject missionButton;

        [Header("Objects")]
        public GameObject staringMissionFarmer;
        public GameObject player;
        [SerializeField]
        private GameObject menuUI;
        [SerializeField]
        private GameObject menuMissionUI;
        [SerializeField]
        private ManageFazem mainScript;

        public void Start(){
            //hide the button
            missionButton.SetActive(false);
        }
        
        public void Update(){
            //if the player is close to th pole
            if (IsPlayerCloseToPole() && !menuUI.activeSelf && !menuMissionUI.activeSelf && (mainScript.MissionStarted()=="Farm" || mainScript.MissionStarted()=="none")){
                //show the button
                missionButton.SetActive(true);
            }
            else{
                //hide the button
                missionButton.SetActive(false);
            }
        }

        public bool IsPlayerCloseToPole(){
            GameObject playerCapsule = player.transform.Find("PlayerCapsule").gameObject;
            if (Vector3.Distance(staringMissionFarmer.transform.position, playerCapsule.transform.position) < 2){
                    return true;
                }
            return false;
        }
}


