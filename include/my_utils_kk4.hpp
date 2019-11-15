#pragma once

#include <chrono>
#include <time.h>
#include <string>
#include <iostream>

namespace my_utils_kk4{


static const std::string default_style = "\033[0m"; 
static const std::string bold    = "\033[1m";
static const std::string italic  = "\033[3m";
static const std::string underline = "\033[4m";

static const std::string black   = "\033[30m";
static const std::string red     = "\033[31m";
static const std::string green   = "\033[32m";
static const std::string yellow  = "\033[33m";
static const std::string blue    = "\033[34m";
static const std::string magenta = "\033[35m";
static const std::string cyan    = "\033[36m";
static const std::string white   = "\033[37m";
static const std::string default_color  = "\033[39m";
static const std::string black_b   = "\033[40m";
static const std::string red_b     = "\033[41m";
static const std::string green_b   = "\033[42m";
static const std::string yellow_b  = "\033[43m";
static const std::string blue_b    = "\033[44m";
static const std::string magenta_b = "\033[45m";
static const std::string cyan_b    = "\033[46m";
static const std::string white_b   = "\033[47m";
static const std::string default_color_b  = "\033[49m";



void progBarNh(const double progress, const bool first_call);


class Fps{
public:
    Fps(double update_interval = 1);
    ~Fps();
    void trigger();
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


class StopWatch{
public:

    typedef enum{
        LINUX_CLOCK_GETTIME,
        CHRONO_HIGH_RESOLUTION_CLOCK,
        CHRONO_STEADY_CLOCK
    }Mode;
    
    StopWatch(const bool verbose = false);
    ~StopWatch();
    
    void start();
    
    double stop();
    timespec stopTimespec();
    
    void reset();
    
    double lap();
    timespec lapTimespec();
    
    double interval();
    timespec intervalTimespec();
    
    double getResult()const;
    timespec getResultTimespec()const;
    
private:
    static struct timespec sub(const struct timespec& a, const struct timespec& b);
    static struct timespec add(const struct timespec& a, const struct timespec& b);
    static double toSec(const struct timespec& t);
    
#if defined(linux) || defined(__linux) || defined(__linux__)
    struct timespec time_start;
    struct timespec offset;
#else
    std::chrono::high_resolution_clock::time_point time_start_high_res;
    std::chrono::steady_clock::time_point time_start;
    std::chrono::nanoseconds offset;
#endif
    bool measuring;
    struct timespec result;
    Mode mode;
};


// sources

inline void progBarNh(const double progress, const bool first_call){

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
inline Fps::Fps(double update_interval)
    : elapsed_time_after_last_update(std::chrono::microseconds(0)),
      events_num_after_last_update(0),
      no_events_yet(true),
      update_interval((int)(update_interval * 1000000)),
      fps(0.0){
}

// Destructor
inline Fps::~Fps(){
}


inline void Fps::trigger(){

    
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


inline StopWatch::StopWatch(const bool verbose)
    : measuring(false),
#if defined(linux) || defined(__linux) || defined(__linux__)
      offset({0,0})
#else
      offset(std::chrono::nanoseconds(0))
#endif
{

#if defined(linux) || defined(__linux) || defined(__linux__)
    mode = LINUX_CLOCK_GETTIME;
    if(verbose){
        std::cerr << "[ INFO] clock_gettime(CLOCK_MONOTONIC_RAW, ...) will be used" << std::endl;
    }
#else
    if(! std::chrono::high_resolution_clock::is_steady){
        mode = CHRONO_STEADY_CLOCK;
        if(verbose){
            std::cerr << yellow
                      << "[ WARN] std::chrono::high_resolution_clock "
                      << "is not steady. std::chrono::steady_clock will "
                      << "be used instead."
                      << default_style << std::endl;
        }
    }else{
        mode = CHRONO_HIGH_RESOLUTION_CLOCK;
    }
#endif
}

inline StopWatch::~StopWatch(){}


inline struct timespec StopWatch::sub(const struct timespec& a, const struct timespec& b){
    
    timespec ret;
    ret.tv_sec = a.tv_sec - b.tv_sec;
    ret.tv_nsec = a.tv_nsec - b.tv_nsec;
    if(ret.tv_nsec < 0){
        ret.tv_sec--;
        ret.tv_nsec += 1000000000;
    }
    return ret;
}

inline struct timespec StopWatch::add(const struct timespec& a, const struct timespec& b){
    
    timespec ret;
    ret.tv_sec = a.tv_sec + b.tv_sec;
    ret.tv_nsec = a.tv_nsec + b.tv_nsec;
    if(ret.tv_nsec >= 1000000000){
        ret.tv_sec++;
        ret.tv_nsec -= 1000000000;
    }
    return ret;
}


inline double StopWatch::toSec(const struct timespec& t){

    return t.tv_sec + t.tv_nsec * 0.000000001;
}


inline void StopWatch::start(){

    if(measuring){
        std::cerr << red
                  << "[ERROR] " << __FILE__ << " (line " << __LINE__
                  << "): StopWatch::start() called while already running"
                  << default_style << std::endl;
    }
    
    measuring = true;
#if defined(linux) || defined(__linux) || defined(__linux__)
    clock_gettime(CLOCK_MONOTONIC_RAW, &time_start);
#else
    if(mode == CHRONO_HIGH_RESOLUTION_CLOCK){
        time_start_high_res = std::chrono::high_resolution_clock::now();
    }else{
        time_start = std::chrono::steady_clock::now();
    }
#endif
}


inline double StopWatch::stop(){

    return toSec(stopTimespec());
}

inline struct timespec StopWatch::stopTimespec(){

    if(! measuring){
        std::cerr << red
                  << "[ERROR] " << __FILE__ << " (line " << __LINE__
                  << "): StopWatch::stop() called while not running"
                  << default_style << std::endl;
        struct timespec ret = {0,0};
        return ret;
    }
#if defined(linux) || defined(__linux) || defined(__linux__)
    struct timespec now;
    clock_gettime(CLOCK_MONOTONIC_RAW, &now);
    offset = add(sub(now, time_start), offset);
    measuring = false;
    result = offset;
#else
    if(mode == CHRONO_HIGH_RESOLUTION_CLOCK){
        auto now = std::chrono::high_resolution_clock::now();
        offset = std::chrono::duration_cast<std::chrono::nanoseconds>(now - time_start_high_res) + offset;
    }else{
        auto now = std::chrono::steady_clock::now();
        offset = std::chrono::duration_cast<std::chrono::nanoseconds>(now - time_start) + offset;
    }
    measuring = false;
    result.tv_sec = static_cast<int>(offset.count() / 1000000000);
    result.tv_nsec = offset.count() % 1000000000;
#endif
    return result;
}



inline void StopWatch::reset(){

    if(measuring){
        std::cerr << red
                  << "[ERROR] " << __FILE__ << " (line " << __LINE__
                  << default_style << "): StopWatch::reset() called while running" << std::endl;
    }
#if defined(linux) || defined(__linux) || defined(__linux__)
    offset.tv_sec = 0;
    offset.tv_nsec = 0;
#else
    offset = std::chrono::nanoseconds(0);
#endif
}

inline double StopWatch::lap(){

    return toSec(lapTimespec());
}

inline struct timespec StopWatch::lapTimespec(){

    if(! measuring){
        std::cerr << red
                  << "[ERROR] " << __FILE__ << " (line " << __LINE__
                  << default_style << "): StopWatch::lap() called while not running" << std::endl;
        struct timespec ret = {0,0};
        return ret;
    }
#if defined(linux) || defined(__linux) || defined(__linux__)
    struct timespec now;
    clock_gettime(CLOCK_MONOTONIC_RAW, &now);
    result = add(sub(now, time_start), offset);
#else
    if(mode == CHRONO_HIGH_RESOLUTION_CLOCK){
        auto now = std::chrono::high_resolution_clock::now();
        auto tmp_result = std::chrono::duration_cast<std::chrono::nanoseconds>(now - time_start_high_res) + offset;
        result.tv_sec = static_cast<time_t>(tmp_result.count() / 1000000000);
        result.tv_nsec = tmp_result.count() % 1000000000;
    }else{
        auto now = std::chrono::steady_clock::now();
        auto tmp_result = std::chrono::duration_cast<std::chrono::nanoseconds>(now - time_start) + offset;
        result.tv_sec = static_cast<time_t>(tmp_result.count() / 1000000000);
        result.tv_nsec = tmp_result.count() % 1000000000;
    }
#endif
    return result;
}

inline double StopWatch::interval(){

    return toSec(intervalTimespec());
}

inline struct timespec StopWatch::intervalTimespec(){

    if(! measuring){
        std::cerr << red
                  << "[ERROR] " << __FILE__ << " (line " << __LINE__
                  << default_style << "): StopWatch::interval() called while not running" << std::endl;
        struct timespec ret = {0,0};
        return ret;
    }

    struct timespec ret = stopTimespec();
    reset();
    start();
    return ret;
}

inline struct timespec StopWatch::getResultTimespec()const{

    return result;
}

inline double StopWatch::getResult()const{

    return toSec(result);
}


}


