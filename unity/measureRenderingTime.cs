using System;
using System.Collections;
using System.Collections.Generic;
using System.IO;
using System.Diagnostics;
using UnityEngine;
using UnityEngine.SceneManagement;

public class measureRenderingTime : MonoBehaviour
{

    private StreamWriter fout;

    private ulong imageCount;

    private String filename;

    private Stopwatch simulationStopWatch;
    private Stopwatch renderingStopWatch;
    
    // Start is called before the first frame update
    void Start()
    {
        filename = "time_" + SceneManager.GetActiveScene().name + "_" + DateTime.Now.ToString("yyyy_MM_dd_HH_mm_ss") + ".csv";
        fout = new StreamWriter(filename, false);
        fout.WriteLine("seq,elapsed_time[s],time[ms]");
        UnityEngine.Debug.Log("Opened " + filename);
        
        simulationStopWatch = new Stopwatch();
        renderingStopWatch = new Stopwatch();
        simulationStopWatch.Start();
        
        imageCount = 0;
    }

    void LateUpdate()
    {
        imageCount += 1;
        StartCoroutine(StopMeasuring());
        renderingStopWatch.Start();
    }

    void OnDestroy(){
        fout.Close();
        UnityEngine.Debug.Log("Closed " + filename);
    }

 
   IEnumerator StopMeasuring()
    {
        yield return new WaitForEndOfFrame();

        renderingStopWatch.Stop();
        
        fout.WriteLine(imageCount + "," + simulationStopWatch.Elapsed.TotalSeconds + "," + renderingStopWatch.Elapsed.TotalMilliseconds);

        renderingStopWatch.Reset();
        
        yield return null;
    }
    
}
