using System.Collections;
using System.Collections.Generic;
using UnityEngine;

using UnityEngine;

public class CarCamera : MonoBehaviour
{
    [SerializeField]
    Transform character;
    public float smoothing = 1.5f;

    Vector2 velocity;
    Vector2 frameVelocity;


    void Reset()
    {
        character = GetComponentInParent<PrometeoCarController>().transform;
    }

    void Start()
    {
        // Lock the mouse cursor to the game screen.
        Cursor.lockState = CursorLockMode.Locked;
    }

    void Update()
    {
        // Get smooth velocity.
        Vector2 mouseDelta = new Vector2(Input.GetAxisRaw("Mouse X"), Input.GetAxisRaw("Mouse Y"));
        velocity += frameVelocity;
        velocity.y = Mathf.Clamp(velocity.y, -90, 90);

    }
}
