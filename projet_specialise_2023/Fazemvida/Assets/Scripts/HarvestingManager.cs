using UnityEngine;
using UnityEngine.UI;
using System.Collections;


public class HarvestingManager : MonoBehaviour
    {

        [Header("Mission")]
        public GameObject haloFinish;
        public MissionFarmSingleton missionFarm = MissionFarmSingleton.Instance();
        [Header("UI")]
        public GameObject textCornAmount;
        public ManageFazem mainScript;
        public GameObject sliderHarvesting;
        [Header("Player")]
        public GameObject human;
        

        public void Start(){
            haloFinish.SetActive(false);
            textCornAmount.SetActive(true);
            sliderHarvesting.SetActive(false);
        }
        
        public void Update(){
            if (!missionFarm.stopped && !missionFarm.paused){
                textCornAmount.GetComponent<Text>().text = missionFarm.corn.ToString();
                if (missionFarm.corn >= 50){
                    haloFinish.SetActive(true);
                }
                if (Input.touchCount > 0 && Input.GetTouch(0).phase == TouchPhase.Began){
                    Ray ray = Camera.main.ScreenPointToRay(Input.GetTouch(0).position);
                    RaycastHit hit;
                    if (Physics.Raycast(ray, out hit)){
                        bool cornNearPlayer = Vector3.Distance(hit.transform.gameObject.transform.position, human.transform.Find("PlayerCapsule").transform.position) < 2;
                        if (hit.transform.gameObject.tag == "Corn" && !missionFarm.isHarvesting && cornNearPlayer){
                            StartCoroutine(Harvesting(hit.transform.gameObject));
                        }
                    }
                }
            }
        }

        public IEnumerator Harvesting(GameObject corn){
            missionFarm.isHarvesting = true;
            sliderHarvesting.SetActive(true);
            HoeMovement hoeslidermvt = sliderHarvesting.GetComponent<HoeMovement>();
            hoeslidermvt.Hoe(1f);
            yield return new WaitForSeconds(1);
            sliderHarvesting.SetActive(false);
            corn.SetActive(false);
            missionFarm.isHarvesting = false;
            missionFarm.HarvestCorn(1);
        }
}


