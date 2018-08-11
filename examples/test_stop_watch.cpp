#include "my_utils_kk4.hpp"

#include <string>
#include <iostream>


int main(){

    my_utils_kk4::StopWatch sw;

    while(true){

        std::string buf;

        std::cout << "1: start  2: stop  3: lap  4: reset  5: break" << std::endl;

        std::cin >> buf;

        if(buf == "1"){
            sw.start();
            std::cout << "start" << std::endl;
        }else if(buf == "2"){
            std::cout << "stop: " << sw.stop() << std::endl;
        }else if(buf == "3"){
            std::cout << "lap: " << sw.lap() << std::endl;
        }else if(buf == "4"){
            sw.reset();
            std::cout << "reset" << std::endl;
        }else if(buf == "5"){
            std::cout << "break" << std::endl;
            break;
        }else{
            std::cerr << "[ERROR] unknown command:" << buf << std::endl;
        }

        std::cin.clear();

    }

    return 0;
}

