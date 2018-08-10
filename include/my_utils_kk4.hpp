#pragma once

#include <chrono>
#include <string>
#include <iostream>

namespace my_utils_kk4{


std::string black   = "\033[30m";
std::string red     = "\033[31m";
std::string green   = "\033[32m";
std::string yellow  = "\033[33m";
std::string blue    = "\033[34m";
std::string magenta = "\033[35m";
std::string cyan    = "\033[36m";
std::string white   = "\033[37m";
std::string default_color  = "\033[39m";
std::string black_b   = "\033[40m";
std::string red_b     = "\033[41m";
std::string green_b   = "\033[42m";
std::string yellow_b  = "\033[43m";
std::string blue_b    = "\033[44m";
std::string magenta_b = "\033[45m";
std::string cyan_b    = "\033[46m";
std::string white_b   = "\033[47m";
std::string default_color_b  = "\033[49m";



void progBarNh(const double progress, const bool first_call);


class Fps{
public:
    Fps(double update_interval = 1);
    ~Fps();
    void informEvent();
    double getFps()const{
        return fps;
    }
private:
    std::chrono::system_clock::time_point time_of_last_event;
    std::chrono::microseconds elapsed_time_after_last_update;
    int events_num_after_last_update;
    bool no_events_yet;
    int update_interval;
    double fps;
};

}







// sources
namespace my_utils_kk4{

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

    int prog_per = (int)(prog * 100);

    if(! first_call){
        std::cout << "\033[6A\r";
    }

    for(int i = 0; i < 6; i++){
        std::cout << "|" << offset << nh[i];
        if(i == 0){
            std::cout << "\r\033[64C| " << prog_per << " %          \n";
        }else{
            std::cout << "\r\033[64C|           \n";
        }
    }

    std::cout << std::flush;
    return;
}

// Constructor
Fps::Fps(double update_interval)
    : no_events_yet(true),
      events_num_after_last_update(0),
      elapsed_time_after_last_update(std::chrono::microseconds(0)),
      update_interval((int)(update_interval * 1000000)),
      fps(0.0){
}

// Destructor
Fps::~Fps(){
}


void Fps::informEvent(){

    
    if(no_events_yet){          // fist call
        no_events_yet = false;
        time_of_last_event = std::chrono::system_clock::now();
    }else{                      // calls after the second
        std::chrono::system_clock::time_point now = std::chrono::system_clock::now();

        elapsed_time_after_last_update +=
            std::chrono::duration_cast<std::chrono::microseconds>(now - time_of_last_event);

        time_of_last_event = now;

        events_num_after_last_update++;
    }

    if(elapsed_time_after_last_update.count() > update_interval){
        fps = 1000000 * (double) events_num_after_last_update / elapsed_time_after_last_update.count();
        elapsed_time_after_last_update = std::chrono::microseconds(0);
        events_num_after_last_update = 0;
    }
    
    return;
}


}

