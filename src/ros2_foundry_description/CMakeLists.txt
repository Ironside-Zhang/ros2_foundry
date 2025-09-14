cmake_minimum_required(VERSION 3.8)
project(ros2_foundry_description)

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

find_package(ament_cmake REQUIRED)
find_package(rosidl_default_generators REQUIRED)
find_package(urdf REQUIRED)
find_package(xacro REQUIRED)

# Install directories
install(DIRECTORY launch
  DESTINATION share/${PROJECT_NAME})
install(DIRECTORY urdf
  DESTINATION share/${PROJECT_NAME})
install(DIRECTORY rviz
  DESTINATION share/${PROJECT_NAME})
install(DIRECTORY config
  DESTINATION share/${PROJECT_NAME})

# ==================================================== #
# == FINAL FIX: Added this line to install SDF files  == #
# ==================================================== #
install(DIRECTORY sdf
  DESTINATION share/${PROJECT_NAME})
# ==================================================== #

install(DIRECTORY meshes
  DESTINATION share/${PROJECT_NAME}
  OPTIONAL)

ament_package()