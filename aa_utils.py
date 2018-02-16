# coding: utf-8

import sys

import time

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
    margin = " " * (40 - int(prog * 40))

    prog_per = int(prog * 100)

    # print "a\n\n \033[1A\rb"

    if not first_call:
        sys.stdout.write("\033[6A\r")
    for i, l in enumerate(nh):
        sys.stdout.write("|" + offset + l + margin)
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
        print l


if __name__ == "__main__":

    # test prog_bar_nh
    for i in range(101):
        time.sleep(0.1)
        if i == 0:
            prog_bar_nh(0.01 * i, True)
        else:
            prog_bar_nh(0.01 * i)

