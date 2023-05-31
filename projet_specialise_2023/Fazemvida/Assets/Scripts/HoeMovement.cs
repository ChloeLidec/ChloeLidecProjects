using UnityEngine;
using UnityEngine.UI;

public class HoeMovement : MonoBehaviour
{
    [SerializeField]
    public GameObject handle;
    public Slider slider;
    private float startTime;
    private float duration;

    public void Update()
    {
        float progress = (Time.time - startTime) / duration;
        slider.value = progress;
        handle.transform.Rotate(0, 0, (Time.time % 1 < 0.5 ? 1 : -1) * Time.deltaTime * 80);
    }

    public void Hoe(float time)
    {
        startTime = Time.time;
        duration = time;

    }

}
