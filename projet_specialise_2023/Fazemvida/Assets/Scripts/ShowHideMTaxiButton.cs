using UnityEngine;

public class ShowHideMTaxiButton : MonoBehaviour
    {

        [Header("Button")]
        public GameObject missionButton;

        [Header("Objects")]
        public GameObject staringMissionPole;
        public GameObject player;
        public GameObject taxi;
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
            if (IsPlayerCloseToPole() && !menuUI.activeSelf && !menuMissionUI.activeSelf && (mainScript.MissionStarted()=="Taxi" || mainScript.MissionStarted()=="none")){
                //show the button
                missionButton.SetActive(true);
            }
            else{
                //hide the button
                missionButton.SetActive(false);
            }
        }

        public bool IsPlayerCloseToPole(){
            if (taxi.activeSelf){
                if (Vector3.Distance(staringMissionPole.transform.position, taxi.transform.position) < 4){
                    return true;
                }
            }
            else{
            GameObject playerCapsule = player.transform.Find("PlayerCapsule").gameObject;
            if (Vector3.Distance(staringMissionPole.transform.position, playerCapsule.transform.position) < 2){
                    return true;
                }}
            return false;
        }
}


