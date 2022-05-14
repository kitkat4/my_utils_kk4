# coding: utf-8

import numpy as np
import sys
import time


default_style = "\033[0m"; 
bold    = "\033[1m";
italic  = "\033[3m";
underline = "\033[4m";

black   = "\033[30m"
red     = "\033[31m"
green   = "\033[32m"
yellow  = "\033[33m"
blue    = "\033[34m"
magenta = "\033[35m"
cyan    = "\033[36m"
white   = "\033[37m"
default_color  = "\033[39m"
black_b   = "\033[40m"
red_b     = "\033[41m"
green_b   = "\033[42m"
yellow_b  = "\033[43m"
blue_b    = "\033[44m"
magenta_b = "\033[45m"
cyan_b    = "\033[46m"
white_b   = "\033[47m"
default_color_b  = "\033[49m"

class TransformEstimatorFromMovedPoints:

    def __init__(self):
        self.tl_estimated = None
        self.rot_estimated = None
        self.org_samples = None
        self.moved_samples = None

    def set_samples(self, org_samples, moved_samples):

        if org_samples.shape != moved_samples.shape:
            raise RuntimeError('The sizes of original samples and moved samples does not match')
        
        self.org_samples = org_samples
        self.moved_samples = moved_samples

    def estimate(self, is_alibi):
        org_samples_center = np.mean(self.org_samples, axis=1).reshape((3, 1))
        moved_samples_center = np.mean(self.moved_samples, axis=1).reshape((3, 1))

        org_samples_offset = self.org_samples - org_samples_center
        moved_samples_offset = self.moved_samples - moved_samples_center

        sum_direct_product_org_org = np.dot(org_samples_offset, org_samples_offset.T)
        sum_direct_product_moved_org = np.dot(moved_samples_offset, org_samples_offset.T)

        rot_estimated = np.dot(sum_direct_product_moved_org,
                               np.linalg.inv(sum_direct_product_org_org))
        tl_estimated = moved_samples_center - np.dot(rot_estimated, org_samples_center)


        if not is_alibi:
            rot_estimated = rot_estimated.T
            tl_estimated = np.dot(rot_estimated, -tl_estimated)
            
        self.tl_estimated = tl_estimated
        self.rot_estimated = rot_estimated
            
        return (self.tl_estimated, self.rot_estimated)


class Fps:
    
    def __init__(self, update_interval = 1.0):

        self.no_events_yet = True
        self.events_num_after_last_update = 0
        self.elapsed_time_after_last_update = 0.0
        self.update_interval = update_interval
        self.fps = 0.0
        self.time_of_last_event = 0.0
        

    def trigger(self):

        if self.no_events_yet:
            self.no_events_yet = False
            self.time_of_last_event = time.time()
        else:
            now = time.time()
            self.elapsed_time_after_last_update += now - self.time_of_last_event
            self.time_of_last_event = now
            self.events_num_after_last_update += 1
            
        if self.elapsed_time_after_last_update > self.update_interval:
            self.fps = self.events_num_after_last_update / self.elapsed_time_after_last_update
            self.elapsed_time_after_last_update = 0.0
            self.events_num_after_last_update = 0

        return

    def get_fps(self):
        
        return self.fps


# Detect a header line in text files like CSV files.
# This function tries to convert fields in the first two lines to float.
# If the patterns of success and failure of conversion in the lines are uniform,
# this function assumes that the file does not have a header line and returns False,
# otherwise True.
# 
# fname: input text file, typically CSV.
# delimiter: character used to split the lines.
# return: True if a header line is detected, otherwise False.
def has_header(fname, delimiter=','):

    patterns = [[], []]
    
    with open(fname, 'r') as f:
        for i in range(2):
            line = f.readline()
            fields = line.split(delimiter)
            for x in fields:
                try:
                    dummy = float(x)
                    patterns[i].append(True)
                except ValueError:
                    patterns[i].append(False)

    for p0, p1 in zip(patterns[0], patterns[1]):
        if p0 != p1:
            return True

    return False
                    

# Extract the header line as the list of strings.
# If no header line is detected, returns None.
def get_header(fname, delimiter=','):

    patterns = [[], []]
    lines = []
    fields = []
    
    with open(fname, 'r') as f:
        for i in range(2):
            lines.append(f.readline())
            fields.append(lines[i].split(delimiter))
            for x in fields[i]:
                try:
                    dummy = float(x)
                    patterns[i].append(True)
                except ValueError:
                    patterns[i].append(False)

    for p0, p1 in zip(patterns[0], patterns[1]):
        if p0 != p1:

            header = fields[0]

            # remove new line character from the back of the last field
            nl = header[-1].rfind('\n')
            if nl != -1:
                header[-1] = header[-1][:-1]

            # remove spaces and tabs from the front and back of each field
            for i in range(len(header)):
                while header[i].find(' ') == 0 or header[i].find('\t') == 0:
                   header[i] = header[i][1:]
                while header[i].find(' ') == len(header[i])-1 or \
                      header[i].find('\t') == len(header[i])-1:
                    header[i] = header[i][:-1]
                
            return header

    return None


# progress bar with Naitou Horizon.
# progress: float, in [0.0, 1.0]
def prog_bar_nh(progress, first_call = False):

    if progress < 0.0:
        prog = 0.0
    elif progress > 1.0:
        prog = 1.0
    else:
        prog = progress

    nh = ["           ／⌒ヽ                  ",
          "⊂二二二（  ＾ω＾）二⊃           ",
          "                /             ﾌﾞｰﾝ ",
          "        （  ヽノ                   ",
          "         ﾉ>ノ                      ",
          "   三    レﾚ                       "]

    offset = " " * int(prog * 40)

    prog_per = int(prog * 100)

    if not first_call:
        sys.stdout.write("\033[6A\r")
    for i, l in enumerate(nh):
        sys.stdout.write("|" + offset + l)
        if i == 0:
            sys.stdout.write("\r\033[64C| " + str(prog_per) + " %          \n")
        else:
            sys.stdout.write("\r\033[64C|           \n")




if __name__ == "__main__":

    # test prog_bar_nh
    for i in range(101):
        time.sleep(0.1)
        if i == 0:
            prog_bar_nh(0.01 * i, True)
        else:
            prog_bar_nh(0.01 * i)

