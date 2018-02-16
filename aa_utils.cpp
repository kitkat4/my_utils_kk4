#include <iostream>
#include <string>


void progBarNh(const double progress, const bool first_call){

    double prog;
    if(progress < 0.0){
        prog = 0.0;
    }else if(progress > 1.0){
        prog = 1.0;
    }else{
        prog = progress;
    }

    const char * nh[] = {"           ／⌒ヽ                  ",
                         "⊂二二二（  ＾ω＾）二⊃           ",
                         "                /             ﾌﾞｰﾝ ",
                         "        （  ヽノ                   ",
                         "         ﾉ>ノ                      ",
                         "   三    レﾚ                       "};

    
    std::string offset((int)(prog * 40), ' ');
    std::string margin(40 - (int)(prog * 40), ' ');

    int prog_per = (int)(prog * 100);

    if(! first_call){
        std::cout << "\033[6A\r";
    }

    for(int i = 0; i < 6; i++){
        std::cout << "|" << offset << nh[i] << margin;
        if(i == 0){
            std::cout << "\r\033[64C| " << prog_per << " %          \n";
        }else{
            std::cout << "\r\033[64C|           \n";
        }
    }

    std::cout << std::flush;
    return;
}

