#!/usr/bin/env python

import cv2
import subprocess

import sys

def main():

    if len(sys.argv) != 2:
        sys.stdout.write("Usage: movie_to_imgs.py <movie file>\n")
        sys.exit()
    

    movie_file_path = sys.argv[1]

    if movie_file_path.rfind('.') == -1:
        sys.stdout.write("[ERROR] Invalid data type\n")
        sys.exit()
    else:
        dir_to_create = movie_file_path[ : movie_file_path.rfind('.')]

    subprocess.call("mkdir " + dir_to_create, shell=True)

    vc = cv2.VideoCapture(movie_file_path)

    cnt = 0
    while(True):
        ret, frame = vc.read()
        if not ret:
            break
        out_img_path = dir_to_create + "/{:08d}.png".format(cnt)
        sys.stdout.write("\r[ INFO] Writing image to " + out_img_path)
        sys.stdout.flush()
        cv2.imwrite(out_img_path, frame)
        cnt += 1

    sys.stdout.write("\n[ INFO] Writing images: done\n")

if __name__ == "__main__":
    main()

