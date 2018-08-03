#include "my_utils_kk.hpp"

#include <thread>



int main(){


    my_utils_kk::Fps fps;

    for(int i = 0; i < 100000; i++){

        fps.informEvent();

        std::this_thread::sleep_for(std::chrono::milliseconds(100));
        
        std::cout << "[" << i << "] " << fps.getFps() << std::endl;
    }


    return 0;

}

