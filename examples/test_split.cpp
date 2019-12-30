#include <my_utils_kk4.hpp>

#include <string>
#include <iostream>


int main(){

    std::string buf_str, buf_delim;

    std::cout << "Enter string:" << std::endl
              << ">" << std::flush;

    std::cin >> buf_str;

    while(true){
        std::cout << "Enter deliminater:" << std::endl
                  << ">" << std::flush;
        std::cin >> buf_delim;
        
        if(buf_delim.size() != 1){
            std::cerr << "[ERROR] Delimiter must be one character. Please enter a delimiter again" << std::endl;
        }else{
            break;
        }
    }

    std::vector<std::string> result = my_utils_kk4::split(buf_str, buf_delim[0]);

    std::cout << "Result: " << std::endl;
    for(size_t i = 0; i < result.size(); i++){

        std::cout << "    \"" << result[i] << "\"" << std::endl;
    }
    std::cout << "    ... " << result.size() << " elements" << std::endl;

    return 0;
}

