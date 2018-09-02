#!/usr/bin/env python
#coding: utf-8

import my_utils_kk4

import time
import sys

if __name__ == "__main__":

    fps = my_utils_kk4.Fps()

    for i in range(1000000):
        
        fps.inform_event()

        time.sleep(0.1)

        sys.stdout.write("[" + str(i) + "] " + str(fps.get_fps()) + "\n")
        
