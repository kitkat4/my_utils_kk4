using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class ImageEditingSample : MonoBehaviour
{
    public RenderTexture rt;
    private Texture2D tx;
 
    // Start is called before the first frame update
    void Start()
    {
        rt = new RenderTexture(Screen.width, Screen.height, 24);
        tx = new Texture2D(Screen.width, Screen.height, TextureFormat.RGB24, false);
    }

    // Update is called once per frame
    void Update()
    {
        
    }

    void OnPreRender()
    {
        RenderTexture.active = rt;
    }

    void OnPostRender() 
    { 
    //    cam.Render();

        tx.ReadPixels(new Rect(0, 0, Screen.width, Screen.height), 0, 0);

        tx.SetPixel(10, 10, Color.red);
        tx.Apply();
    }

    void OnRenderImage(RenderTexture src, RenderTexture dst)
    {
        Graphics.Blit(tx, (RenderTexture)null);
    }
}
