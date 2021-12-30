#include "my_utils_kk4.hpp"

#include <iostream>
#include <cmath>

// Example: solve x^2 - 2 = 0 for x.

int main(int argc, char** argv){

    const size_t max_iteration_num = 10;
    size_t iteration_num = 0;
    bool converged = false;

    

    const double answer = my_utils_kk4::newtonRaphsonMethod([](const double x){return x * x - 2.0;},
                                                            [](const double x){return 2 * x;},
                                                            0.001,
                                                            max_iteration_num,
                                                            1.0,
                                                            &iteration_num,
                                                            &converged);

    std::cout << "Solved x^2 - 2 = 0 for x using Newton-Raphson method." << std::endl
              << "Result: " << answer << std::endl
              << "True value: " << std::sqrt(2.0) << std::endl
              << "Error: " << answer - std::sqrt(2.0) << std::endl
              << "Iteration num: " << iteration_num << "/" << max_iteration_num << std::endl
              << "Converged: " << converged << std::endl;
}

