set(MODULE_NAME Lua)
file(GLOB_RECURSE FILES
"${CMAKE_CURRENT_SOURCE_DIR}/src/*.c" 
"${CMAKE_CURRENT_SOURCE_DIR}/src/*.h"
)

add_library(${MODULE_NAME} STATIC ${FILES})

target_include_directories(${MODULE_NAME} PUBLIC 
    $<BUILD_INTERFACE:${CMAKE_CURRENT_SOURCE_DIR}/src>
    $<INSTALL_INTERFACE:${MODULE_NAME}/include>
)

#==================install config=========================
install(TARGETS ${MODULE_NAME}
    EXPORT ${MODULE_NAME}Targets
    ARCHIVE DESTINATION ${MODULE_NAME}/lib
    LIBRARY DESTINATION ${MODULE_NAME}/lib
    RUNTIME DESTINATION ${MODULE_NAME}/bin
)

include(CMakePackageConfigHelpers)
# install时拷贝头文件
install(DIRECTORY "${CMAKE_CURRENT_SOURCE_DIR}/src/"
    DESTINATION ${MODULE_NAME}/include
    FILES_MATCHING PATTERN "*.h"
)
# 2. 配置并生成 Config 文件
configure_package_config_file(
    "${CMAKE_CURRENT_SOURCE_DIR}/CMake/${MODULE_NAME}Config.cmake.in"  # 需要你自己写
    "${CMAKE_CURRENT_BINARY_DIR}/${MODULE_NAME}Config.cmake"
    INSTALL_DESTINATION ${MODULE_NAME}/
)

# 3. 安装 Config  文件
install(FILES
    "${CMAKE_CURRENT_BINARY_DIR}/${MODULE_NAME}Config.cmake"
    DESTINATION ${MODULE_NAME}/
)

# 4. 安装导出 Targets
install(EXPORT ${MODULE_NAME}Targets
    FILE ${MODULE_NAME}Targets.cmake
    DESTINATION ${MODULE_NAME}
)

