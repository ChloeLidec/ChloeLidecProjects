using UnityEngine;

public class ShowHideMGBButton : MonoBehaviour
    {

        [Header("Button")]
        public GameObject missionButton;

        [Header("Objects")]
        public GameObject staringMissionPole;
        public GameObject player;
        [SerializeField]
        private GameObject menuUI;
        [SerializeField]
        private GameObject menuMissionUI;
        [SerializeField]
        private ManageFazem mainScript = null;
        public void Start(){
            //hide the button
            missionButton.SetActive(false);
        }
        
        public void Update(){
            //if the player is close to th pole
            if (IsPlayerCloseToPole() && !menuUI.activeSelf && !menuMissionUI.activeSelf && (mainScript.MissionStarted()=="GB" || mainScript.MissionStarted()=="none")){
                //show the button
                missionButton.SetActive(true);
            }
            else{
                //hide the button
                missionButton.SetActive(false);
            }
        }

        //check if the player is close to the pole
        public bool IsPlayerCloseToPole(){
            GameObject playerCapsule = player.transform.Find("PlayerCapsule").gameObject;
            if (Vector3.Distance(staringMissionPole.transform.position, playerCapsule.transform.position) < 2){
                    //return true
                    return true;
                }
            //return false
            return false;
        }
}


