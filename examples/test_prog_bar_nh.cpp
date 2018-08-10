#include "my_utils_kk4.hpp"


int main(){

    for(int i = 0; i < 101; i++){
        for(int j = 0; j < 50000000; j++){
            // do nothing
        }
        if(i == 0){
            my_utils_kk4::progBarNh(0.01 * i, true);
        }else{
            my_utils_kk4::progBarNh(0.01 * i, false);
        }
    }
}    
