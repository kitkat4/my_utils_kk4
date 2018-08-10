# coding: utf-8

import sys

import time




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

