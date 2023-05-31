using UnityEngine;

namespace StarterAssets
{
    public class UICanvasControllerInput : MonoBehaviour
    {

        [Header("Output")]
        public StarterAssetsInputs starterAssetsInputs;
        public InOutVehicles inOutVehicles;
        public MenuController menuController;
        public MenuMissionGBController menuMissionGBController;
        public MenuMissionTController menuMissionTController;
        public MenuMissionFController menuMissionFController;
        public PrometeoCarController prometeoCarController;
        public ManageFazem manageFazem;
        public void VirtualMoveInput(Vector2 virtualMoveDirection)
        {
            starterAssetsInputs.MoveInput(virtualMoveDirection);
        }

        public void VirtualLookInput(Vector2 virtualLookDirection)
        {
            starterAssetsInputs.LookInput(virtualLookDirection);
        }

        public void VirtualJumpInput(bool virtualJumpState)
        {
            starterAssetsInputs.JumpInput(virtualJumpState);
        }

        public void VirtualSprintInput(bool virtualSprintState)
        {
            starterAssetsInputs.SprintInput(virtualSprintState);
        }
        public void VirtualEnterExitVehicleInput()
        {
            starterAssetsInputs.StopInput();
            inOutVehicles.EnterExitVehicle();
        }

        public void VirtualShowMenuInput()
        {
            starterAssetsInputs.StopInput();
            if (inOutVehicles.activeVehicle != null){
                inOutVehicles.activeVehicle.GetComponent<PrometeoCarController>().StopCar();
            }
            menuController.ShowMenu();
        }

        public void VirtualHideMenuInput()
        {
            menuController.HideMenu();
        }

        public void VirtualSaveInput()
        {
            menuController.Save();
        }

        public void VirtualStartMissionGBInput()
        {
            starterAssetsInputs.StopInput();
            menuMissionGBController.StartMission();
        }

        public void VirtualStartMissionTaxiInput()
        {
            starterAssetsInputs.StopInput();
            menuMissionTController.StartMission();
        }

        public void VirtualStartMissionFarmInput()
        {
            starterAssetsInputs.StopInput();
            menuMissionFController.StartMission();
        }
        public void VirtualTPToParkingInput(){
            starterAssetsInputs.StopInput();
            manageFazem.TPCarToParking();
        }
    }

}
