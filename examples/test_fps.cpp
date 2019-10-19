#include "my_utils_kk4.hpp"

#include <thread>



int main(){


    my_utils_kk4::Fps fps;

    for(int i = 0; i < 100000; i++){

        fps.trigger();

        std::this_thread::sleep_for(std::chrono::milliseconds(100));
        
        std::cout << "[" << i << "] " << fps.getFps() << std::endl;
    }


    return 0;

}

