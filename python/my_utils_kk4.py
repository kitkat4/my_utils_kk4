# coding: utf-8

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
                    
        


# progress bar with Naitou Horizon.
# progress: float, in [0.0, 1.0]
def prog_bar_nh(progress, first_call = False):

    if progress < 0.0:
        prog = 0.0
    elif progress > 1.0:
        prog = 1.0
    else:
        prog = progress

    # nh_small = "ﾌﾞｰﾝ ⊂二二二（　＾ω＾）二⊃"

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



        


def yaruo_kiri(statement):

    yaruo = ["                 ＿＿＿_",
             "             ／ ＼    ／＼  ｷﾘｯ",
             "           ／  （ー）   （ー）＼        ＜「" + statement + "」",
             "        ／     ⌒（__人__）⌒ ＼",
             "        |           |r┬-|        |",
             "         ＼         `ー’´     ／",
             "        ノ                       ＼",
             "   ／´                             ヽ",
             "  |        ｌ                            ＼",
             "  ヽ       -一””””~~｀`’ー–､      -一”””’ー-､.",
             "    ヽ ＿＿＿＿(⌒)(⌒)⌒)  )    (⌒＿(⌒)⌒)⌒))",
             "",
             "                  ＿＿＿_",
             "               ／_ノ   ヽ､_＼",
             "  ﾐ  ﾐ  ﾐ    oﾟ(（●）) (（●）)ﾟo            ﾐ  ﾐ  ﾐ      ＜だっておｗｗｗ",
             "/⌒)⌒)⌒. ::::::⌒（__人__）⌒:::＼      /⌒)⌒)⌒)     ",
             "|  /  /  /          |r┬-|        |  (⌒)/  / / /／              ",
             "|  :::::::::::(⌒)        |  |   |     ／   ゝ    :::::::::::/            ",
             "|          ノ         |  |   |     ＼    /    ）    /",
             "ヽ        /          `ー’´         ヽ /        ／",
             "  |        |     l||l  从人 l||l          l||l 从人 l||l    バンバン",
             "  ヽ       -一””””~~｀`’ー–､      -一”””’ー-､",
             "    ヽ ＿＿＿＿(⌒)(⌒)⌒)  )    (⌒＿(⌒)⌒)⌒))"]

    for i, l in enumerate(yaruo):
        sys.stdout.write(l + '\n')




if __name__ == "__main__":

    # test prog_bar_nh
    for i in range(101):
        time.sleep(0.1)
        if i == 0:
            prog_bar_nh(0.01 * i, True)
        else:
            prog_bar_nh(0.01 * i)

