using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;

public class CheckpointManager : MonoBehaviour
{
    public MissionGBSingleton missionGBSingleton = MissionGBSingleton.Instance();
    public Text checkpointUI;
    public void OnTriggerEnter(Collider other)
    {
        if (other.gameObject.tag == "Player" && !missionGBSingleton.stopped )
        {
            missionGBSingleton.PassCheckpoint();
            checkpointUI.text = "Checkpoints " + missionGBSingleton.nbOfCheckpointsPassed + "/7";
            //deactivate checkpoint
            gameObject.SetActive(false);
        }
    }
}
