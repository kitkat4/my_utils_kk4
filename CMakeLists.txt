cmake_minimum_required(VERSION 2.8)

project(my_utils_kk)

# 次の行を追加するとDebug, MinSizeRel, RelWithDebInfoの選択肢を生成することが抑制できます。
set(CMAKE_CONFIGURATION_TYPES "Release" CACHE STRING "limited configs" FORCE)
set(CMAKE_SUPPRESS_REGENERATION)
set(CMAKE_CXX_STANDARD 11)
set(CMAKE_CXX_FLAGS "-Wall")
include_directories(include)

add_executable(test_fps examples/test_fps.cpp)
add_executable(test_color examples/test_color.cpp)
add_executable(test_stop_watch examples/test_stop_watch.cpp)
add_executable(test_split examples/test_split.cpp)


